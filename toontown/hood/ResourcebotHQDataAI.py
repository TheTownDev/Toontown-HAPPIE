from direct.directnotify import DirectNotifyGlobal
from . import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq.resourcebot import DistributedBoardOfficeElevatorExtAI
from toontown.coghq import DistributedCogHQDoorAI
from toontown.coghq.LawbotOfficeExterior_Action00 import GlobalEntities
from toontown.building import DistributedDoorAI
from toontown.building import DoorTypes
from toontown.coghq import LobbyManagerAI
from toontown.building import DistributedBossElevatorAI
from toontown.suit import DistributedLawbotBossAI
from toontown.building import DistributedCJElevatorAI
from toontown.building import FADoorCodes
from toontown.building import DistributedBoardingPartyAI
from toontown.safezone import ArchipelagoTreasurePlannerAI
from toontown.safezone import DistributedArchiTreasureAI
from toontown.suit.DistributedCogHQHealBarrelAI import DistributedCogHQHealBarrelAI

class ResourcebotHQDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('ResourcebotHQDataAI')

    def __init__(self, air, zoneId=None):
        self.notify.debug('__init__: zoneId:%s' % zoneId)
        hoodId = ToontownGlobals.ResourcebotHQ
        if zoneId == None:
            zoneId = hoodId
        self.healBarrels = []
        self.room = GlobalEntities
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        return

    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)

        def makeOfficeElevator(index, antiShuffle=0, minLaff=0):
            destZone = (ToontownGlobals.ResourcebotGeneralField, ToontownGlobals.ResourcebotSpecialistField)[index]
            elev = DistributedBoardOfficeElevatorExtAI.DistributedBoardOfficeElevatorExtAI(self.air, self.air.boardofficeMgr, destZone, antiShuffle=0, minLaff=minLaff)
            elev.generateWithRequired(ToontownGlobals.ResourcebotFieldCenter)
            self.addDistObj(elev)
            return elev.doId

        mins = ToontownGlobals.FactoryLaffMinimums[2]
        officeId0 = makeOfficeElevator(0, 0, mins[0])
        officeId3 = makeOfficeElevator(1, 0, mins[0])
        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, DistributedLawbotBossAI.DistributedLawbotBossAI)
        self.lobbyMgr.generateWithRequired(ToontownGlobals.LawbotLobby)
        self.addDistObj(self.lobbyMgr)
        self.lobbyElevator = DistributedCJElevatorAI.DistributedCJElevatorAI(self.air, self.lobbyMgr, ToontownGlobals.LawbotLobby, antiShuffle=1)
        self.lobbyElevator.generateWithRequired(ToontownGlobals.LawbotLobby)
        self.addDistObj(self.lobbyElevator)
        #ArchipelagoTreasurePlannerAI.ArchipelagoTreasurePlannerAI(self.zoneId, DistributedArchiTreasureAI.DistributedArchiTreasureAI, 0, treasureCount=5)
        self.treasurePlanner = []
        for planner in self.treasurePlanner:
            planner.start()
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.boardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, [self.lobbyElevator.doId], 8)
            self.boardingParty.generateWithRequired(ToontownGlobals.LawbotLobby)

        def makeDoor(destinationZone, intDoorIndex, extDoorIndex, lock=0):
            intDoor = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.INT_COGHQ, self.canonicalHoodId, doorIndex=intDoorIndex, lockValue=lock)
            intDoor.zoneId = destinationZone
            extDoor = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.EXT_COGHQ, destinationZone, doorIndex=extDoorIndex, lockValue=lock)
            extDoor.setOtherDoor(intDoor)
            intDoor.setOtherDoor(extDoor)
            intDoor.generateWithRequired(destinationZone)
            intDoor.sendUpdate('setDoorIndex', [intDoor.getDoorIndex()])
            self.addDistObj(intDoor)
            extDoor.generateWithRequired(self.canonicalHoodId)
            extDoor.sendUpdate('setDoorIndex', [extDoor.getDoorIndex()])
            self.addDistObj(extDoor)

        makeDoor(ToontownGlobals.LawbotLobby, 0, 1, FADoorCodes.LB_DISGUISE_INCOMPLETE)
        makeDoor(ToontownGlobals.ResourcebotFieldCenter, 0, 0)

        for entity in self.room: # battleBlocker
            if self.room[entity]['type'] == 'healBarrel':
                self.addHealBarrel(self.room[entity]['pos'], self.room[entity]['hpr'])

        for healBarrel in self.healBarrels:
            healBarrel.d_showObstacle()
        officeIdList = [
         officeId0, officeId3]
        if simbase.config.GetBool('want-boarding-parties', 1):
            self.officeBoardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, officeIdList, 4)
            self.officeBoardingParty.generateWithRequired(ToontownGlobals.ResourcebotFieldCenter)

    def addHealBarrel(self, pos, hpr):
        newHealBarrel = DistributedCogHQHealBarrelAI(self.air)
        self.healBarrels.append(newHealBarrel)
        newHealBarrel.generateWithRequired(ToontownGlobals.ResourcebotFieldCenter)
        newHealBarrel.d_setPos(pos[0], pos[1], pos[2])
        newHealBarrel.d_setHpr(hpr[0], hpr[1], hpr[2])