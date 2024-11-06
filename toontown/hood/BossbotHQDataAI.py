from panda3d.core import Point3
from direct.directnotify import DirectNotifyGlobal
from . import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedCogHQDoorAI
from toontown.building import DistributedDoorAI
from toontown.building import DoorTypes
from toontown.coghq import LobbyManagerAI
from toontown.building import DistributedBossElevatorAI
from toontown.suit import DistributedBossbotBossAI
from toontown.building import DistributedBBElevatorAI
from toontown.building import DistributedBoardingPartyAI
from toontown.building import FADoorCodes
from toontown.coghq import DistributedCogKartAI
from toontown.safezone import ArchipelagoTreasurePlannerAI
from toontown.safezone import DistributedArchiTreasureAI
from toontown.suit.DistributedExecutiveCogHQGoonAI import DistributedExecutiveCogHQGoonAI

class BossbotHQDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('BossbotHQDataAI')

    def __init__(self, air, zoneId=None):
        self.notify.debug('__init__: zoneId:%s' % zoneId)
        hoodId = ToontownGlobals.BossbotHQ
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        self.cogKarts = []
        self.goons = []
        return

    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)

        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, DistributedBossbotBossAI.DistributedBossbotBossAI)
        self.lobbyMgr.generateWithRequired(ToontownGlobals.BossbotLobby)
        self.addDistObj(self.lobbyMgr)
        self.lobbyElevator = DistributedBBElevatorAI.DistributedBBElevatorAI(self.air, self.lobbyMgr, ToontownGlobals.BossbotLobby, antiShuffle=1)
        self.lobbyElevator.generateWithRequired(ToontownGlobals.BossbotLobby)
        self.addDistObj(self.lobbyElevator)
        self.treasurePlanner = [ArchipelagoTreasurePlannerAI.ArchipelagoTreasurePlannerAI(self.zoneId, DistributedArchiTreasureAI.DistributedArchiTreasureAI, 0),
                                ]
        for planner in self.treasurePlanner:
            planner.start()
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.boardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, [self.lobbyElevator.doId], 8)
            self.boardingParty.generateWithRequired(ToontownGlobals.BossbotLobby)

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

        makeDoor(ToontownGlobals.BossbotLobby, 0, 0, FADoorCodes.BB_DISGUISE_INCOMPLETE)
        makeDoor(ToontownGlobals.BossbotLobby, 1, 1, FADoorCodes.UNKNOWN_COG_AREA)
        
        kartIdList = self.createCogKarts()
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.courseBoardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, kartIdList, 4)
            self.courseBoardingParty.generateWithRequired(self.zoneId)
        
        newGoon = DistributedExecutiveCogHQGoonAI(self.air)
        self.goons.append(newGoon)
        newGoon.setHFov(8)
        newGoon.setVelocity(8)
        newGoon.generateWithRequired(self.zoneId)
        newGoon.d_setPosHpr(-432.7,
            188,
            3.92, 180, 0, 0)
        newGoon.b_setStrength(42)
        newGoon.d_setPath(
            -432.2,
            287.35,
            3.97,
            -432.7,
            188,
            3.92,
            )
        newGoon.d_setPathDuration(6)
        newGoon.d_setScale(9)
        newGoon.d_setReverseTheta(True)
        
        newGoon1 = DistributedExecutiveCogHQGoonAI(self.air)
        self.goons.append(newGoon1)
        newGoon1.setHFov(8)
        newGoon1.setVelocity(8)
        newGoon1.generateWithRequired(self.zoneId)
        newGoon1.d_setPosHpr(-548.86,
            431.85,
            3.92, 180, 0, 0)
        newGoon1.b_setStrength(42)
        newGoon1.d_setPath(
            -548.46,
            383.85,
            3.92,
            -548.96,
            432.15,
            3.92,
            )
        newGoon1.d_setPathDuration(6)
        newGoon1.d_setScale(9)
        newGoon1.d_setReverseTheta(True)
        
        newGoon2 = DistributedExecutiveCogHQGoonAI(self.air)
        self.goons.append(newGoon2)
        newGoon2.setHFov(8)
        newGoon2.setVelocity(8)
        newGoon2.generateWithRequired(self.zoneId)
        newGoon2.d_setPosHpr(-437.19,
            224.73,
            3.92, 0, 0, 0)
        newGoon2.b_setStrength(42)
        newGoon2.d_setPath(
            -437.19,
            295.73,
            3.92,
            -437.79,
            224.83,
            3.92,
            )
        newGoon2.d_setPathDuration(6)
        newGoon2.d_setScale(9)
        newGoon2.d_setReverseTheta(True)
        
        for goon in self.goons:
            goon.startGoon()
            goon.d_showObstacle()

    def createCogKarts(self):
        posList = ((-26.5658, 237.459, 0), (-28.725, -235.706, 0))
        hprList = ((-159, 0, 0), (-21, 0, 0))
        lockList = (FADoorCodes.FRONT_THREE_ACCESS_MISSING, FADoorCodes.BACK_NINE_ACCESS_MISSING)
        kartIdList = []
        for cogCourse in range(len(posList)):
            pos = posList[cogCourse]
            hpr = hprList[cogCourse]
            cogKart = DistributedCogKartAI.DistributedCogKartAI(self.air, cogCourse, pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2], self.air.countryClubMgr, minLaff=0)
            cogKart.generateWithRequired(self.zoneId)
            self.cogKarts.append(cogKart)
            kartIdList.append(cogKart.doId)

        return kartIdList
