from direct.directnotify import DirectNotifyGlobal
from toontown.coghq.resourcebot import BoardOfficeRoomSpecs
from toontown.toonbase import ToontownGlobals
from direct.showbase.PythonUtil import invertDictLossless
import random

def printAllBoardbotInfo():
    pass


def iterateBoardOffices(func):
    from toontown.toonbase import ToontownGlobals
    for boardofficeId in [ToontownGlobals.ResourcebotGeneralField, ToontownGlobals.ResourcebotSpecialistField]:
        for floorNum in range(ToontownGlobals.BoardOfficeNumFloors[boardofficeId]):
            func(BoardOfficeLayout(boardofficeId, floorNum))


def printBoardOfficeInfo():

    def func(ml):
        print(ml)

    iterateBoardOffices(func)


def printBoardOfficeRoomIds():

    def func(ml):
        print(ml.getBoardOfficeId(), ml.getFloorNum(), ml.getRoomIds())

    iterateBoardOffices(func)


def printBoardOfficeRoomNames():

    def func(ml):
        print(ml.getBoardOfficeId(), ml.getFloorNum(), ml.getRoomNames())

    iterateBoardOffices(func)


def printNumRooms():

    def func(ml):
        print(ml.getBoardOfficeId(), ml.getFloorNum(), ml.getNumRooms())

    iterateBoardOffices(func)


def printNumBattles():

    def func(ml):
        print(ml.getBoardOfficeId(), ml.getFloorNum(), ml.getNumBattles())

    iterateBoardOffices(func)


BakedFloorLayouts = {14500: {0: (0,
             101,
             100,
             19),
         1: (0,
             101,
             101,
             100,
             19),
         2: (0,
             101,
             100,
             19),
         3: (0,
             101,
             100,
             19),
         4: (0,
             101,
             100,
             19),
         5: (0,
             101,
             100,
             19),
         6: (0,
             101,
             100,
             19),
         7: (0,
             101,
             100,
             19),
         8: (0,
             101,
             100,
             19),
         9: (0,
             101,
             100,
             19),
         10: (0,
             101,
             100,
             19),
         11: (0,
             101,
             100,
             19),
         12: (0,
             101,
             100,
             19),
         13: (0,
             101,
             100,
             19),
         14: (0,
             101,
             100,
             19),
         15: (0,
             101,
             100,
             19),
         16: (0,
             101,
             100,
             19),
         17: (0,
             101,
             100,
             19),
         18: (0,
             101,
             100,
             19),
         19: (0,
              101,
             100,
             19)},
                     14600: {0: (0,
                                  100,
                                  19),
                             1: (0,
                                  100,
                                  19),
                             2: (0,
                                  100,
                                  19),
                             3: (0,
                                  100,
                                  19),
                             4: (0,
                                  100,
                                  19),
                             5: (0,
                                  100,
                                  19),
                             6: (0,
                                  100,
                                  19),
                             7: (0,
                                  100,
                                  19),
                             8: (0,
                                  100,
                                  19),
                             9: (0,
                                  100,
                                  19),
                             10: (0,
                                  100,
                                  19),
                             11: (0,
                                  100,
                                  19),
                             12: (0,
                                  100,
                                  19),
                             13: (0,
                                  100,
                                  19),
                             14: (0,
                                  100,
                                  19),
                             15: (0,
                                  100,
                                  19),
                             16: (0,
                                  100,
                                  19),
                             17: (0,
                                  100,
                                  19),
                             18: (0,
                                  100,
                                  19),
                             19: (0,
                                  100,
                                  19)}
                     }

class BoardOfficeLayout:
    notify = DirectNotifyGlobal.directNotify.newCategory('BoardOfficeLayout')

    def __init__(self, boardofficeId, floorNum):
        self.boardofficeId = boardofficeId
        self.floorNum = floorNum
        self.roomIds = []
        self.hallways = []
        self.numRooms = 1 + ToontownGlobals.BoardOfficeNumRooms[self.boardofficeId][self.floorNum]
        self.numHallways = self.numRooms - 1
        if self.boardofficeId in BakedFloorLayouts and self.floorNum in BakedFloorLayouts[self.boardofficeId]:
            self.roomIds = list(BakedFloorLayouts[self.boardofficeId][self.floorNum])
        else:
            self.roomIds = self._genFloorLayout()
        hallwayRng = self.getRng()
        connectorRoomNames = BoardOfficeRoomSpecs.BoardOfficeConnectorRooms
        for i in range(self.numHallways):
            self.hallways.append(hallwayRng.choice(connectorRoomNames))

    def _genFloorLayout(self):
        rng = self.getRng()
        startingRoomIDs = BoardOfficeRoomSpecs.BoardOfficeEntranceIDs
        middleRoomIDs = BoardOfficeRoomSpecs.BoardOfficeMiddleRoomIDs
        finalRoomIDs = BoardOfficeRoomSpecs.BoardOfficeFinalRoomIDs

        numBattlesLeft = 20

        finalRoomId = rng.choice(finalRoomIDs)
        numBattlesLeft -= BoardOfficeRoomSpecs.getNumBattles(finalRoomId)

        middleRoomIds = []
        middleRoomsLeft = self.numRooms - 2

        numBattles2middleRoomIds = invertDictLossless(BoardOfficeRoomSpecs.middleRoomId2numBattles)

        allBattleRooms = []
        for num, roomIds in list(numBattles2middleRoomIds.items()):
            if num > 0:
                allBattleRooms.extend(roomIds)
        while 1:
            allBattleRoomIds = list(allBattleRooms)
            rng.shuffle(allBattleRoomIds)
            battleRoomIds = self._chooseBattleRooms(numBattlesLeft,
                                                    allBattleRoomIds)
            if battleRoomIds is not None:
                break

            MintLayout.notify.info('could not find a valid set of battle rooms, trying again')

        middleRoomIds.extend(battleRoomIds)
        middleRoomsLeft -= len(battleRoomIds)

        if middleRoomsLeft > 0:
            actionRoomIds = numBattles2middleRoomIds[0]
            for i in range(middleRoomsLeft):
                roomId = rng.choice(actionRoomIds)
                actionRoomIds.remove(roomId)
                middleRoomIds.append(roomId)

        roomIds = []

        roomIds.append(rng.choice(startingRoomIDs))

        rng.shuffle(middleRoomIds)
        roomIds.extend(middleRoomIds)

        roomIds.append(finalRoomId)

        return roomIds

    def getNumRooms(self):
        return len(self.roomIds)

    def getRoomId(self, n):
        return self.roomIds[n]

    def getRoomIds(self):
        return self.roomIds[:]

    def getRoomNames(self):
        names = []
        for roomId in self.roomIds:
            names.append(BoardOfficeRoomSpecs.BoardOfficeRoomId2RoomName[roomId])

        return names

    def getNumHallways(self):
        return len(self.hallways)

    def getHallwayModel(self, n):
        return self.hallways[n]

    def getNumBattles(self):
        numBattles = 0
        for roomId in self.getRoomIds():
            numBattles += BoardOfficeRoomSpecs.roomId2numBattles[roomId]

        return numBattles

    def getBoardOfficeId(self):
        return self.boardofficeId

    def getFloorNum(self):
        return self.floorNum

    def getRng(self):
        return random.Random(self.boardofficeId * self.floorNum)

    def _chooseBattleRooms(self, numBattlesLeft, allBattleRoomIds, baseIndex = 0, chosenBattleRooms = None):
        if chosenBattleRooms is None:
            chosenBattleRooms = []
        while baseIndex < len(allBattleRoomIds):
            nextRoomId = allBattleRoomIds[baseIndex]
            baseIndex += 1
            newNumBattlesLeft = numBattlesLeft - BoardOfficeRoomSpecs.middleRoomId2numBattles[nextRoomId]
            if newNumBattlesLeft < 0:
                self.notify.info('newNumBattlesLeft is less than 0!')
                return chosenBattleRooms
            elif newNumBattlesLeft == 0:
                chosenBattleRooms.append(nextRoomId)
                return chosenBattleRooms
            chosenBattleRooms.append(nextRoomId)
            result = self._chooseBattleRooms(newNumBattlesLeft, allBattleRoomIds, baseIndex, chosenBattleRooms)
            if result is not None:
                return result
            else:
                del chosenBattleRooms[-1:]
        else:
            return

    def __str__(self):
        return 'BoardOfficeLayout: id=%s, floor=%s, numRooms=%s, numBattles=%s' % (self.boardofficeId,
         self.floorNum,
         self.getNumRooms(),
         self.getNumBattles())

    def __repr__(self):
        return str(self)
