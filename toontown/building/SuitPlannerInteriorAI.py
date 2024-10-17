import functools
import math
from typing import List, Dict, Tuple, Optional

from otp.ai.AIBaseGlobal import *
import random

from toontown.building import SuitBuildingGlobals
from toontown.suit import SuitDNA
from direct.directnotify import DirectNotifyGlobal
from toontown.suit import DistributedSuitAI

class SuitPlannerInteriorAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitPlannerInteriorAI')

    def __init__(self, numFloors: int, bldgLevel: int, bldgTrack: int, zone: int, respectInvasions: bool = True, numToons: Optional[int] = None, isBoss: bool = False):
        self.dbg_nSuits1stRound = config.GetBool('n-suits-1st-round', 0)
        self.dbg_4SuitsPerFloor = config.GetBool('4-suits-per-floor', 0)
        self.dbg_1SuitPerFloor = config.GetBool('1-suit-per-floor', 0)
        self.zoneId = zone
        self.numFloors = numFloors
        self.respectInvasions = respectInvasions
        self.numToons = numToons
        dbg_defaultSuitName = simbase.config.GetString('suit-type', 'random')
        if dbg_defaultSuitName == 'random':
            self.dbg_defaultSuitType = None
        else:
            self.dbg_defaultSuitType = SuitDNA.getSuitType(dbg_defaultSuitName)
        if isinstance(bldgLevel, bytes):
            self.notify.warning('bldgLevel is a string!')
            bldgLevel = int(bldgLevel)
        self._genSuitInfos(numFloors, bldgLevel, bldgTrack, numToons, isBoss)
        return

    def __genJoinChances(self, num: int) -> List[int]:
        """Generate a list of random numbers between 1 and 100, inclusive.
        
        Args:
            num: The number of random numbers to generate.
        
        Returns:
            A list of random numbers.
        """
        joinChances = []
        for currChance in range(num):
            joinChances.append(random.randint(1, 100))

        joinChances.sort(key=functools.cmp_to_key(cmp))
        return joinChances

    def _genSuitInfos(self, numFloors: int, bldgLevel: int, bldgTrack: int, numToons: Optional[int], isBoss: bool) -> None:
        """Generates a list of dictionaries describing the suit info for each floor.
        
        Args:
            numFloors: The number of floors in the building.
            bldgLevel: The level of the building.
            bldgTrack: The track of the building.
            numToons: The number of toons in the building.
            isBoss: Whether the building is a boss building.
        """
        self.suitInfos = []
        self.notify.debug('\n\ngenerating suitsInfos with numFloors (' + str(numFloors) + ') bldgLevel (' + str(bldgLevel) + '+1) and bldgTrack (' + str(bldgTrack) + ')')
        for currFloor in range(numFloors):
            infoDict = {}
            lvls = self.__genLevelList(bldgLevel, currFloor, numFloors, numToons, isBoss)
            activeDicts = []
            maxActive = min(4, len(lvls))
            if self.dbg_nSuits1stRound:
                numActive = min(self.dbg_nSuits1stRound, maxActive)
            else:
                numActive = random.randint(1, maxActive)
            if currFloor + 1 == numFloors and len(lvls) > 1:
                origBossSpot = len(lvls) - 1
                if numActive == 1:
                    newBossSpot = numActive - 1
                else:
                    newBossSpot = numActive - 2
                tmp = lvls[newBossSpot]
                lvls[newBossSpot] = lvls[origBossSpot]
                lvls[origBossSpot] = tmp
            if isBoss:
                bldgInfo = SuitBuildingGlobals.SuitBossInfo[bldgLevel]
            else:
                bldgInfo = SuitBuildingGlobals.SuitBuildingInfo[bldgLevel]
            if len(bldgInfo) > SuitBuildingGlobals.SUIT_BLDG_INFO_REVIVES:
                revives = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_REVIVES][0]
            else:
                revives = 0
            if len(bldgInfo) > SuitBuildingGlobals.SUIT_BLDG_INFO_IMMUNE:
                immune = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_IMMUNE][0]
            else:
                immune = 0
            for currActive in range(numActive - 1, -1, -1):
                level = lvls[currActive]
                type = self.__genNormalSuitType(level)
                activeDict = {}
                activeDict['type'] = type
                activeDict['track'] = bldgTrack
                activeDict['level'] = level
                activeDict['revives'] = revives
                activeDict['immune'] = immune
                activeDicts.append(activeDict)

            infoDict['activeSuits'] = activeDicts
            reserveDicts = []
            numReserve = len(lvls) - numActive
            joinChances = self.__genJoinChances(numReserve)
            for currReserve in range(numReserve):
                level = lvls[currReserve + numActive]
                type = self.__genNormalSuitType(level)
                reserveDict = {}
                reserveDict['type'] = type
                reserveDict['track'] = bldgTrack
                reserveDict['level'] = level
                reserveDict['revives'] = revives
                reserveDict['joinChance'] = joinChances[currReserve]
                reserveDicts.append(reserveDict)

            infoDict['reserveSuits'] = reserveDicts
            self.suitInfos.append(infoDict)

    def __genNormalSuitType(self, lvl: int) -> int:
        if self.dbg_defaultSuitType != None:
            return self.dbg_defaultSuitType
        return SuitDNA.getRandomSuitType(lvl)

    def __genLevelList(self, bldgLevel: int, currFloor: int, numFloors: int, numToons: Optional[int], isBoss: bool) -> List[int]:
        if isBoss:
            bldgInfo = SuitBuildingGlobals.SuitBossInfo[bldgLevel]
        else:
            bldgInfo = SuitBuildingGlobals.SuitBuildingInfo[bldgLevel]
        if self.dbg_1SuitPerFloor:
            return [1]
        else:
            if self.dbg_4SuitsPerFloor:
                return [5, 6, 7, 10]

        if numToons:
            levelPoolRangeList = []
            for levelPoolRange in bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_LVL_POOL]:
                newLevelPoolRange = math.ceil(levelPoolRange * SuitBuildingGlobals.NUM_TOONS_TO_COGS_RATIO[numToons])
                levelPoolRangeList.append(newLevelPoolRange)
            levelPoolRange = (levelPoolRangeList[0], levelPoolRangeList[1])
        else:
            levelPoolRange = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_LVL_POOL]

        maxFloors = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_FLOORS][1]
        levelPoolMults = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_LVL_POOL_MULTS]
        floorIdx = min(currFloor, maxFloors - 1)
        levelPoolMin = levelPoolRange[0] * levelPoolMults[floorIdx]
        levelPoolMax = levelPoolRange[1] * levelPoolMults[floorIdx]
        levelPool = random.randint(int(levelPoolMin), int(levelPoolMax))
        levelMin = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_SUIT_LVLS][0]
        levelMax = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_SUIT_LVLS][1]

        levelList = []
        while levelPool >= levelMin:
            newLevel = random.randint(levelMin, min(levelPool, levelMax))
            levelList.append(newLevel)
            levelPool -= newLevel

        if currFloor + 1 == numFloors:
            bossLevelRange = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_BOSS_LVLS]
            newLevel = random.randint(bossLevelRange[0], bossLevelRange[1])
            levelList.append(newLevel)

        levelList.sort(key=functools.cmp_to_key(cmp))
        return levelList

    def __setupSuitInfo(self, suit, bldgTrack, suitLevel, suitType):
        suitName, skeleton = simbase.air.suitInvasionManager.getInvadingCog()
        if suitName and self.respectInvasions:
            suitType = SuitDNA.getSuitType(suitName)
            bldgTrack = SuitDNA.getSuitDept(suitName)
            suitLevel = min(max(suitLevel, suitType), suitType + 4)
        dna = SuitDNA.SuitDNA()
        dna.newSuitRandom(suitType, bldgTrack)
        suit.dna = dna
        if suitLevel < suitType:
            suitLevel = suitType
        suit.setLevel(suitLevel)
        return skeleton

    def __genSuitObject(self, zoneId, suitType, bldgTrack, suitLevel, revives=0, immune=0):
        suit = DistributedSuitAI.DistributedSuitAI(simbase.air, None)
        skeleton = self.__setupSuitInfo(suit, bldgTrack, suitLevel, suitType)
        if skeleton:
            suit.setSkelecog(1)
        suit.setSkeleRevives(revives)
        suit.setImmuneStatus(immune)
        suit.generateWithRequired(zoneId)
        suit.node().setName('suit-%s' % suit.doId)
        return suit

    def genFloorSuits(self, floor):
        suitHandles = {}
        floorInfo = self.suitInfos[floor]
        activeSuits = []
        for activeSuitInfo in floorInfo['activeSuits']:
            suit = self.__genSuitObject(self.zoneId, activeSuitInfo['type'], activeSuitInfo['track'], activeSuitInfo['level'], activeSuitInfo['revives'])
            activeSuits.append(suit)

        suitHandles['activeSuits'] = activeSuits
        reserveSuits = []
        for reserveSuitInfo in floorInfo['reserveSuits']:
            suit = self.__genSuitObject(self.zoneId, reserveSuitInfo['type'], reserveSuitInfo['track'], reserveSuitInfo['level'], reserveSuitInfo['revives'])
            reserveSuits.append((suit, reserveSuitInfo['joinChance']))

        suitHandles['reserveSuits'] = reserveSuits
        return suitHandles

    def genSuits(self):
        suitHandles = []
        for floor in range(len(self.suitInfos)):
            floorSuitHandles = self.genFloorSuits(floor)
            suitHandles.append(floorSuitHandles)

        return suitHandles
