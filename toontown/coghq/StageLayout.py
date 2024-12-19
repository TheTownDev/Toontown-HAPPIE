from direct.directnotify import DirectNotifyGlobal
from direct.showbase.PythonUtil import invertDictLossless
from toontown.coghq import StageRoomSpecs
from toontown.toonbase import ToontownGlobals
from direct.showbase.PythonUtil import normalDistrib, lerp
import random


def printAllCashbotInfo():
    print('roomId: roomName')
    for roomId, roomName in list(StageRoomSpecs.LawbotStageRoomId2RoomName.items()):
        print('%s: %s' % (roomId, roomName))

    print('\nroomId: numBattles')
    for roomId, numBattles in list(StageRoomSpecs.roomId2numBattles.items()):
        print('%s: %s' % (roomId, numBattles))

    print('\nstageId floor roomIds')
    printStageRoomIds()
    print('\nstageId floor numRooms')
    printNumRooms()
    print('\nstageId floor numForcedBattles')
    printNumBattles()


def iterateLawbotStages(func):
    from toontown.toonbase import ToontownGlobals
    for layoutId in range(len(stageLayouts)):
        for floorNum in range(getNumFloors(layoutId)):
            func(StageLayout(0, floorNum, layoutId))


def printStageInfo():
    def func(sl):
        print(sl)

    iterateLawbotStages(func)


def printRoomUsage():
    usage = {}

    def func(sl):
        for roomId in sl.getRoomIds():
            usage.setdefault(roomId, 0)
            usage[roomId] += 1

    iterateLawbotStages(func)
    roomIds = list(usage.keys())
    roomIds.sort()
    for roomId in roomIds:
        print('%s: %s' % (roomId, usage[roomId]))


def printRoomInfo():
    roomIds = list(StageRoomSpecs.roomId2numCogs.keys())
    roomIds.sort()
    for roomId in roomIds:
        print('room %s: %s cogs, %s cogLevels, %s merit cogLevels' % (roomId,
                                                                      StageRoomSpecs.roomId2numCogs[roomId],
                                                                      StageRoomSpecs.roomId2numCogLevels[roomId],
                                                                      StageRoomSpecs.roomId2numMeritCogLevels[roomId]))


def printStageRoomIds():
    def func(ml):
        print(ml.getStageId(), ml.getFloorNum(), ml.getRoomIds())

    iterateCashbotStages(func)


def printStageRoomNames():
    def func(ml):
        print(ml.getStageId(), ml.getFloorNum(), ml.getRoomNames())

    iterateCashbotStages(func)


def printNumRooms():
    def func(ml):
        print(ml.getStageId(), ml.getFloorNum(), ml.getNumRooms())

    iterateCashbotStages(func)


def printNumBattles():
    def func(ml):
        print(ml.getStageId(), ml.getFloorNum(), ml.getNumBattles())

    iterateCashbotStages(func)


DefaultLayout1 = (
    {
        0: (0, 1, 2, 3, 1, 2, 4),
        1: (0, 1, 2, 3, 1, 2, 4),
        2: (0, 1, 2, 3, 1, 2, 4),
        3: (0, 1, 2, 3, 1, 2, 4),
        4: (0, 1, 2, 3, 1, 2, 4),
        5: (0, 1, 2, 3, 1, 2, 4),
        6: (0, 1, 2, 3, 1, 2, 4),
        7: (0, 1, 2, 3, 1, 2, 4),
        8: (0, 1, 2, 3, 1, 2, 4),
        9: (0, 1, 2, 3, 1, 2, 4),
        10: (0, 1, 2, 3, 1, 2, 4),
        11: (0, 1, 2, 3, 1, 2, 4),
        12: (0, 1, 2, 3, 1, 2, 4),
        13: (0, 1, 2, 3, 1, 2, 4),
        14: (0, 1, 2, 3, 1, 2, 4),
        15: (0, 1, 2, 3, 1, 2, 4),
        16: (0, 1, 2, 3, 1, 2, 4),
        17: (0, 1, 2, 3, 1, 2, 4),
        18: (0, 1, 2, 3, 1, 2, 4),
        19: (0, 1, 2, 3, 1, 2, 4)
    },
)

DefaultLayout = [
    (0, 5, 2, 3, 5, 2, 1),
    (0, 5, 2, 3, 5, 2, 1),
    (0, 5, 2, 3, 5, 2, 1),
    (0, 5, 2, 3, 5, 2, 1),
    (0, 5, 2, 3, 5, 2, 1),
    (0, 5, 2, 3, 5, 2, 1),
    (0, 5, 2, 3, 5, 2, 1),
    (0, 5, 2, 3, 5, 2, 1),
    (0, 5, 2, 3, 5, 2, 1),
    (0, 5, 2, 3, 5, 2, 1),
    (0, 5, 2, 3, 5, 2, 1)
]

testLayout = [
    (0, 3, 8, 105, 1),
    (0, 7, 8, 105, 2)
]

"""
LawbotStageSpecModules = {
    0: LawbotOfficeEntrance_Action00,
    1: LawbotOfficeOilRoom_Battle00,
    2: LawbotOfficeOilRoom_Battle01,
    3: LawbotOfficeBoilerRoom_Security00,
    4: LawbotOfficeBoilerRoom_Battle00,
    5: LawbotOfficeGearRoom_Action00,
    6: LawbotOfficeLobby_Action00,
    7: LawbotOfficeGearRoom_Security00,
    8: LawbotOfficeLobby_Trap00,
    9: LawbotOfficeDiamondRoom_Security00,
    10: LawbotOfficeDiamondRoom_Trap00,
    11: LawbotOfficeGearRoom_Platform00,
    12: LawbotOfficeLobby_Lights00,
    100: LawbotOfficeBoilerRoom_Action01,
    101: LawbotOfficeDiamondRoom_Action00,
    102: LawbotOfficeDiamondRoom_Action01,
    103: LawbotOfficeLobby_Action01,
    104: LawbotOfficeDiamondRoom_Battle00,
    105: LawbotOfficeGearRoom_Battle00,
    106: LawbotOfficeDiamondRoom_Battle01,
    107: LawbotOfficeBoilerRoom_Battle01,
    108: LawbotOfficeLavaRoomFoyer_Battle00
}
"""

JUNIOR_BOOK_ROOM = 200 # tt_f_ara_dbr_action00
JUNIOR_EVIDENCE_GOON_ROOM = 201 # tt_f_ara_der_action00
JUNIOR_EVIDENCE_DOOM_ROOM = 202 # tt_f_ara_der_action01
JUNIOR_EVIDENCE_SINGLE_ROOM = 203 # tt_f_ara_der_action02
JUNIOR_DIAMOND_STOMPER_ROOM = 204 # tt_f_ara_ddr_action00
JUNIOR_DIAMOND_GOON_ROOM = 205 # tt_f_ara_ddr_action01
JUNIOR_DIAMOND_SINGLE_ROOM = 206 # tt_f_ara_ddr_action02
JUNIOR_DIAMOND_DOOM_ROOM = 207 # tt_f_ara_ddr_action04
JUNIOR_ENTRANCE_ROOM = 208 # tt_f_ara_delr_action00
JUNIOR_TRAP_LOBBY_ROOM = 209 # tt_f_ara_dtr_action00
JUNIOR_TRAP_DIAMOND_ROOM = 210 # tt_f_ara_dtr_action01
JUNIOR_LOBBY_COGS = 211 # tt_f_ara_dlr_action00
JUNIOR_LOBBY_CAMERAS = 212 # tt_f_ara_dlr_action01
JUNIOR_BOX_GOON_ROOM = 213 # tt_f_ara_dgr_action00
JUNIOR_BOX_PLATFORM_ROOM = 214 # tt_f_ara_dgr_action01
JUNIOR_BOX_SECURITY_ROOM = 215 # tt_f_ara_dgr_action02
JUNIOR_BOX_SINGLE_ROOM = 216 # tt_f_ara_dgr_action04
JUNIOR_BOX_DOOM_ROOM = 217 # tt_f_ara_dgr_action05
JUNIOR_LEGAL_ROOM = 218 # tt_f_ara_dler_action00

LawOfficeLayout2_0 = [
    (JUNIOR_ENTRANCE_ROOM, JUNIOR_LEGAL_ROOM, JUNIOR_DIAMOND_SINGLE_ROOM, JUNIOR_DIAMOND_GOON_ROOM, 1),
    (JUNIOR_ENTRANCE_ROOM, JUNIOR_LEGAL_ROOM, JUNIOR_EVIDENCE_DOOM_ROOM, JUNIOR_TRAP_DIAMOND_ROOM, JUNIOR_BOOK_ROOM, 2)
]

LawOfficeLayout2_1 = [
    (JUNIOR_ENTRANCE_ROOM, JUNIOR_LEGAL_ROOM, JUNIOR_DIAMOND_STOMPER_ROOM, JUNIOR_EVIDENCE_GOON_ROOM, JUNIOR_EVIDENCE_DOOM_ROOM, 1),
    (JUNIOR_ENTRANCE_ROOM, JUNIOR_LEGAL_ROOM, JUNIOR_TRAP_LOBBY_ROOM, JUNIOR_DIAMOND_SINGLE_ROOM, JUNIOR_EVIDENCE_SINGLE_ROOM, 2)
]

LawOfficeLayout2_2 = [
    (JUNIOR_ENTRANCE_ROOM, JUNIOR_LEGAL_ROOM, JUNIOR_TRAP_DIAMOND_ROOM, JUNIOR_DIAMOND_DOOM_ROOM, JUNIOR_EVIDENCE_GOON_ROOM, JUNIOR_DIAMOND_STOMPER_ROOM, 1),
    (JUNIOR_ENTRANCE_ROOM, JUNIOR_LEGAL_ROOM, JUNIOR_DIAMOND_STOMPER_ROOM, JUNIOR_BOOK_ROOM, 2)
]

LawOfficeLayout2_3 = [
    (JUNIOR_ENTRANCE_ROOM, JUNIOR_LEGAL_ROOM, JUNIOR_DIAMOND_GOON_ROOM, JUNIOR_EVIDENCE_GOON_ROOM, JUNIOR_BOOK_ROOM, JUNIOR_EVIDENCE_DOOM_ROOM, 1),
    (JUNIOR_ENTRANCE_ROOM, JUNIOR_LEGAL_ROOM, JUNIOR_DIAMOND_STOMPER_ROOM, JUNIOR_LOBBY_COGS, 2)
]

LawOfficeLayout5_0 = [
    (0, 110, 4, 3, 1),
    (0, 12, 10, 105, 2)
]

LawOfficeLayout5_1 = [
    (0, 110, 3, 104, 1),
    (0, 106, 8, 108, 2)
]

LawOfficeLayout5_2 = [
    (0, 7, 9, 107, 1),
    (0, 4, 10, 2)
]

LawOfficeLayout5_3 = [
    (0, 4, 3, 1),
    (0, 105, 8, 2)
]

stageLayouts = {
    ToontownGlobals.LawbotStageIntA: [LawOfficeLayout2_0,
    LawOfficeLayout2_1,
    LawOfficeLayout2_2,
    LawOfficeLayout2_3],
    ToontownGlobals.LawbotStageIntD: [LawOfficeLayout5_0,
    LawOfficeLayout5_1,
    LawOfficeLayout5_2,
    LawOfficeLayout5_3],

 ToontownGlobals.LawbotStageIntB: [LawOfficeLayout2_0,
    LawOfficeLayout2_1,
    LawOfficeLayout2_2,
    LawOfficeLayout2_3],
    ToontownGlobals.LawbotStageIntC: [LawOfficeLayout5_0,
    LawOfficeLayout5_1,
    LawOfficeLayout5_2,
    LawOfficeLayout5_3]
}

stageLayouts1 = [
    testLayout,
    testLayout,
    testLayout,
    testLayout,
    testLayout,
    testLayout,
    testLayout,
    testLayout,
    testLayout,
    testLayout,
    testLayout,
    testLayout
]


def getNumFloors(layoutIndex):
    return len(stageLayouts[layoutIndex])


class StageLayout:
    notify = DirectNotifyGlobal.directNotify.newCategory('StageLayout')

    def __init__(self, stageId, floorNum, stageLayout=0):
        self.stageId = stageId
        self.floorNum = floorNum
        self.roomIds = []
        self.hallways = []
        self.layoutId = stageLayout
        self.roomIds = stageLayouts[stageId][stageLayout][floorNum]
        self.numRooms = 1 + len(self.roomIds)
        self.numHallways = self.numRooms - 1
        hallwayRng = self.getRng()
        connectorRoomNames = StageRoomSpecs.CashbotStageConnectorRooms
        for i in range(self.numHallways):
            self.hallways.append(hallwayRng.choice(connectorRoomNames))

    def getNumRooms(self):
        return len(self.roomIds)

    def getRoomId(self, n):
        return self.roomIds[n]

    def getRoomIds(self):
        return self.roomIds[:]

    def getRoomNames(self):
        names = []
        for roomId in self.roomIds:
            names.append(StageRoomSpecs.LawbotStageRoomId2RoomName[roomId])

        return names

    def getNumHallways(self):
        return len(self.hallways)

    def getHallwayModel(self, n):
        return self.hallways[n]

    def getNumBattles(self):
        numBattles = 0
        for roomId in self.getRoomIds():
            numBattles += StageRoomSpecs.roomId2numBattles[roomId]

        return numBattles

    def getNumCogs(self):
        numCogs = 0
        for roomId in self.getRoomIds():
            numCogs += StageRoomSpecs.roomId2numCogs[roomId]

        return numCogs

    def getNumCogLevels(self):
        numLevels = 0
        for roomId in self.getRoomIds():
            numLevels += StageRoomSpecs.roomId2numCogLevels[roomId]

        return numLevels

    def getNumMeritCogLevels(self):
        numLevels = 0
        for roomId in self.getRoomIds():
            numLevels += StageRoomSpecs.roomId2numMeritCogLevels[roomId]

        return numLevels

    def getStageId(self):
        return self.stageId

    def getFloorNum(self):
        return self.floorNum

    def getNumFloors(self):
        return len(stageLayouts[stageId][self.layoutId])

    def getRng(self):
        return random.Random(self.stageId * self.floorNum)

    def __str__(self):
        return 'StageLayout: id=%s, layout=%s, floor=%s, meritCogLevels=%s, numRooms=%s, numBattles=%s, numCogs=%s' % (
        self.stageId,
        self.layoutId,
        self.floorNum,
        self.getNumMeritCogLevels(),
        self.getNumRooms(),
        self.getNumBattles(),
        self.getNumCogs())

    def __repr__(self):
        return str(self)
