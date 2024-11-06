from direct.directnotify import DirectNotifyGlobal
from . import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedMintElevatorExtAI
from toontown.coghq import DistributedCogHQDoorAI
from toontown.building import DoorTypes
from toontown.coghq import LobbyManagerAI
from toontown.building import DistributedCFOElevatorAI
from toontown.suit import DistributedCashbotBossAI
from toontown.building import FADoorCodes
from toontown.building import DistributedBoardingPartyAI
from toontown.safezone import ArchipelagoTreasurePlannerAI
from toontown.safezone import DistributedArchiTreasureAI
from toontown.suit.DistributedCogHQGoonAI import DistributedCogHQGoonAI

class CashbotHQDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('CashbotHqDataAI')

    def __init__(self, air, zoneId=None):
        hoodId = ToontownGlobals.CashbotHQ
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        self.goons = []
        return

    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)
        mins = ToontownGlobals.FactoryLaffMinimums[1]
        self.testElev0 = DistributedMintElevatorExtAI.DistributedMintElevatorExtAI(self.air, self.air.mintMgr, ToontownGlobals.CashbotMintIntA, antiShuffle=0, minLaff=mins[0])
        self.testElev0.generateWithRequired(ToontownGlobals.CashbotHQ)
        self.addDistObj(self.testElev0)
        self.testElev2 = DistributedMintElevatorExtAI.DistributedMintElevatorExtAI(self.air, self.air.mintMgr, ToontownGlobals.CashbotMintIntC, antiShuffle=0, minLaff=mins[2])
        self.testElev2.generateWithRequired(ToontownGlobals.CashbotHQ)
        self.addDistObj(self.testElev2)
        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, DistributedCashbotBossAI.DistributedCashbotBossAI)
        self.lobbyMgr.generateWithRequired(ToontownGlobals.CashbotLobby)
        self.addDistObj(self.lobbyMgr)
        self.lobbyElevator = DistributedCFOElevatorAI.DistributedCFOElevatorAI(self.air, self.lobbyMgr, ToontownGlobals.CashbotLobby, antiShuffle=1)
        self.lobbyElevator.generateWithRequired(ToontownGlobals.CashbotLobby)
        self.addDistObj(self.lobbyElevator)
        self.treasurePlanner = [ArchipelagoTreasurePlannerAI.ArchipelagoTreasurePlannerAI(self.zoneId, DistributedArchiTreasureAI.DistributedArchiTreasureAI, 0, treasureCount=5),
                                ]
        newGoon = DistributedCogHQGoonAI(self.air)
        self.goons.append(newGoon)
        newGoon.setHFov(8)
        newGoon.setVelocity(8)
        newGoon.generateWithRequired(self.zoneId)
        newGoon.d_setPosHpr(-56.60, -397.97, -23.44, 180, 0, 0)
        newGoon.b_setStrength(20)
        newGoon.d_setPath(
            -56.80,
            -460.82,
            -23.44,
            -56.60,
            -397.97,
            -23.44
            )
        newGoon.d_setPathDuration(9)
        newGoon.d_setScale(1.7)
        
        newGoon1 = DistributedCogHQGoonAI(self.air)
        self.goons.append(newGoon1)
        newGoon1.setHFov(8)
        newGoon1.setVelocity(8)
        newGoon1.generateWithRequired(self.zoneId)
        newGoon1.d_setPosHpr(-113.13, -87.44, -23.44, 0, 0, 0)
        newGoon1.b_setStrength(18)
        newGoon1.d_setPath(
            -113.43,
            34.86,
            -23.44,
            -113.13,
            87.44,
            -23.44
            )
        newGoon1.d_setPathDuration(9)
        newGoon1.d_setScale(1.4)
        
        newGoon2 = DistributedCogHQGoonAI(self.air)
        self.goons.append(newGoon2)
        newGoon2.setHFov(8)
        newGoon2.setVelocity(8)
        newGoon2.generateWithRequired(self.zoneId)
        newGoon2.d_setPosHpr(-90.24, 35.89, -23.44, 0, 0, 0)
        newGoon2.b_setStrength(8)
        newGoon2.d_setPath(
            -90.44,
            66.57,
            -23.44,
            -90.24,
            35.89,
            -23.44,
            )
        newGoon2.d_setPathDuration(9)
        newGoon2.d_setScale(0.6)
        
        
        for goon in self.goons:
            goon.startGoon()
            goon.d_showObstacle()
        
        for planner in self.treasurePlanner:
            planner.start()
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.boardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, [self.lobbyElevator.doId], 8)
            self.boardingParty.generateWithRequired(ToontownGlobals.CashbotLobby)
        destinationZone = ToontownGlobals.CashbotLobby
        extDoor0 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.EXT_COGHQ, destinationZone, doorIndex=0, lockValue=FADoorCodes.CB_DISGUISE_INCOMPLETE)
        extDoorList = [
         extDoor0]
        intDoor0 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.INT_COGHQ, ToontownGlobals.CashbotHQ, doorIndex=0)
        intDoor0.setOtherDoor(extDoor0)
        intDoor0.zoneId = ToontownGlobals.CashbotLobby
        mintIdList = [
         self.testElev0.doId, self.testElev2.doId]
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.mintBoardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, mintIdList, 4)
            self.mintBoardingParty.generateWithRequired(self.zoneId)
        for extDoor in extDoorList:
            extDoor.setOtherDoor(intDoor0)
            extDoor.zoneId = ToontownGlobals.CashbotHQ
            extDoor.generateWithRequired(ToontownGlobals.CashbotHQ)
            extDoor.sendUpdate('setDoorIndex', [extDoor.getDoorIndex()])
            self.addDistObj(extDoor)

        intDoor0.generateWithRequired(ToontownGlobals.CashbotLobby)
        intDoor0.sendUpdate('setDoorIndex', [intDoor0.getDoorIndex()])
        self.addDistObj(intDoor0)
