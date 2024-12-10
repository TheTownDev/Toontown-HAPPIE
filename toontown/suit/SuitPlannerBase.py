from panda3d.core import *
from panda3d.toontown import *
import random
import string
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
from toontown.hood import HoodUtil
from toontown.building import SuitBuildingGlobals

class SuitPlannerBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitPlannerBase')
    SuitHoodInfo = [#Toontown Central
                    [2100, 12, 20, 0, 99, 100, 3, (1, 5, 10, 40, 60, 80), (0, 0, 25, 65, 10), (1, 2, 3, 4), [], 4],
                    [2200, 12, 20, 0, 99, 100, 3, (1, 5, 10, 40, 60, 80), (0, 50, 50, 0, 0), (1, 2, 3, 4), [], 4],
                    [2300, 12, 20, 0, 99, 100, 3, (1, 5, 10, 40, 60, 80), (75, 25, 0, 0, 0), (1, 2, 3, 4), [], 4],
                    [2400, 12, 20, 0, 99, 100, 3, (1, 5, 10, 40, 60, 80), (40, 10, 10, 0, 40), (2, 3, 4, 5), [], 4],

                    #Donalds Dock
                    [1100, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (50, 0, 50, 0, 0), (3, 4, 5, 6, 7), [], 4],
                    [1200, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 0, 25, 50, 25), (3, 4, 5, 6, 7), [], 4],
                    [1300, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (25, 50, 0, 0, 25), (3, 4, 5, 6, 7), [], 4],

                    # Daisy Gardens
                    [5100, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 50, 40, 0, 10),  (4, 5, 6, 7, 8), [], 4],
                    [5200, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (50, 25, 25, 0, 0), (4, 5, 6, 7, 8), [], 4],
                    [5300, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 0, 0, 65, 35),  (4, 5, 6, 7, 8, 9), [], 4],

                    # Minnies Melodyland
                    [4100, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (50, 0, 0, 50, 0),  (4, 5, 6, 7, 8, 9, 10), [], 7],
                    [4200, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 70, 0, 0, 30),  (4, 5, 6, 7, 8, 9, 10), [], 7],
                    [4300, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (25, 0, 40, 25, 10), (6, 7, 8, 9, 10, 11), [], 8],

                    # The Brrrgh
                    [3100, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (70, 0, 0, 0, 30), (7, 8, 9, 10, 11, 12), [], 7],
                    [3200, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 0, 50, 50, 0), (7, 8, 9, 10, 11, 12), [], 7],
                    [3300, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 70, 0, 5, 25), (8, 9, 10, 11, 12, 13), [], 7],

                    #Donalds Dreamland
                    [9100, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (33, 34, 0, 33, 0), (8, 9, 10, 11, 12, 13), [], 7],
                    [9200, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 0, 75, 0, 25),  (8, 9, 10, 11, 12, 13), [], 7],
                    [9300, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (45, 20, 0, 20, 15),  (9, 10, 11, 12, 13, 14), [], 7],

                    #Clear Coasts
                    [7100, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 10, 10, 0, 80), (9, 10, 11, 12, 13, 14), [], 7],
                    [7200, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (10, 40, 50, 0, 0),  (9, 10, 11, 12, 13, 14), [], 7],
                    [7300, 1, 5, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (40, 20, 0, 20, 20),  (10, 11, 12, 13, 14, 15), [], 7],

                    # Sellbot Courtyard, Factory Exterior
                    [11000, 3, 15, 0, 0, 0, 4, (1, 5, 10, 40, 60, 80), (0, 0, 0, 100, 0),  (5, 6, 7, 8, 9), [], 7],
                    [11200, 10, 20, 0, 0, 0, 4, (1, 5, 10, 40, 60, 80), (0, 0, 0, 100, 0), (6, 7, 8, 9, 10, 11), [], 6],

                    # Cashbot Courtyard
                    [12000, 10, 20, 0, 0, 0, 4, (1, 5, 10, 40, 60, 80), (0, 0, 100, 0, 0), (8, 9, 10, 11, 12, 13), [], 7],

                    # Lawbot Courtyard, Office Lobby
                    [13000, 10, 20, 0, 0, 0, 4, (1, 5, 10, 40, 60, 80), (0, 100, 0, 0, 0), (9, 10, 11, 12, 13), [], 7],
                    [13200, 2, 6, 0, 0, 0, 4, (1, 5, 10, 40, 60, 80), (0, 100, 0, 0, 0), (10, 11, 12, 13, 14), [], 7],

                    # Bossbot Courtyard
                    [10000, 10, 20, 0, 0, 0, 4, (1, 5, 10, 40, 60, 80), (100, 0, 0, 0, 0), (9, 10, 11, 12, 13, 14, 15), [], 8]]
    SUIT_HOOD_INFO_ZONE = 0
    SUIT_HOOD_INFO_MIN = 1
    SUIT_HOOD_INFO_MAX = 2
    SUIT_HOOD_INFO_BMIN = 3
    SUIT_HOOD_INFO_BMAX = 4
    SUIT_HOOD_INFO_BWEIGHT = 5
    SUIT_HOOD_INFO_SMAX = 6
    SUIT_HOOD_INFO_JCHANCE = 7
    SUIT_HOOD_INFO_TRACK = 8
    SUIT_HOOD_INFO_LVL = 9
    SUIT_HOOD_INFO_HEIGHTS = 10
    TOTAL_BWEIGHT = 0
    TOTAL_BWEIGHT_PER_TRACK = [0,
     0,
     0,
     0,
     0]
    TOTAL_BWEIGHT_PER_HEIGHT = [0,
     0,
     0,
     0,
     0,
     0]
    for currHoodInfo in SuitHoodInfo:
        weight = currHoodInfo[SUIT_HOOD_INFO_BWEIGHT]
        tracks = currHoodInfo[SUIT_HOOD_INFO_TRACK]
        levels = currHoodInfo[SUIT_HOOD_INFO_LVL]
        heights = [
         0, 0, 0, 0, 0, 0]
        for level in levels:
            floorInfo = max(0, min(level - 1, (len(SuitBuildingGlobals.SuitBuildingInfo) - 1)))
            minFloors, maxFloors = SuitBuildingGlobals.SuitBuildingInfo[floorInfo][0]
            for i in range(minFloors - 1, maxFloors):
                heights[i] += 1

        currHoodInfo[SUIT_HOOD_INFO_HEIGHTS] = heights
        TOTAL_BWEIGHT += weight
        TOTAL_BWEIGHT_PER_TRACK[0] += weight * tracks[0]
        TOTAL_BWEIGHT_PER_TRACK[1] += weight * tracks[1]
        TOTAL_BWEIGHT_PER_TRACK[2] += weight * tracks[2]
        TOTAL_BWEIGHT_PER_TRACK[3] += weight * tracks[3]
        TOTAL_BWEIGHT_PER_TRACK[4] += weight * tracks[4]
        TOTAL_BWEIGHT_PER_HEIGHT[0] += weight * heights[0]
        TOTAL_BWEIGHT_PER_HEIGHT[1] += weight * heights[1]
        TOTAL_BWEIGHT_PER_HEIGHT[2] += weight * heights[2]
        TOTAL_BWEIGHT_PER_HEIGHT[3] += weight * heights[3]
        TOTAL_BWEIGHT_PER_HEIGHT[4] += weight * heights[4]
        TOTAL_BWEIGHT_PER_HEIGHT[5] += weight * heights[5]

    def __init__(self):
        self.suitWalkSpeed = ToontownGlobals.SuitWalkSpeed
        self.dnaStore = None
        self.pointIndexes = {}
        return

    def setupDNA(self):
        if self.dnaStore:
            return None
        self.dnaStore = DNAStorage()
        dnaFileName = self.genDNAFileName()
        try:
            simbase.air.loadDNAFileAI(self.dnaStore, dnaFileName)
        except:
            loader.loadDNAFileAI(self.dnaStore, dnaFileName)

        self.initDNAInfo()
        return None

    def genDNAFileName(self):
        try:
            return simbase.air.genDNAFileName(self.getZoneId())
        except:
            zoneId = ZoneUtil.getCanonicalZoneId(self.getZoneId())
            hoodId = ZoneUtil.getCanonicalHoodId(zoneId)
            hood = ToontownGlobals.dnaMap[hoodId]
            phase = ToontownGlobals.streetPhaseMap[hoodId]
            if hoodId == zoneId:
                zoneId = 'sz'
            return 'phase_%s/dna/%s_%s.dna' % (phase, hood, zoneId)

    def getZoneId(self):
        return self.zoneId

    def setZoneId(self, zoneId):
        self.notify.debug('setting zone id for suit planner')
        self.zoneId = zoneId
        self.setupDNA()

    def extractGroupName(self, groupFullName):
        return str(groupFullName).split(':', 1)[0]

    def initDNAInfo(self):
        numGraphs = self.dnaStore.discoverContinuity()
        if numGraphs != 1:
            self.notify.info('zone %s has %s disconnected suit paths.' % (self.zoneId, numGraphs))
        self.battlePosDict = {}
        self.cellToGagBonusDict = {}
        for i in range(self.dnaStore.getNumDNAVisGroupsAI()):
            vg = self.dnaStore.getDNAVisGroupAI(i)
            zoneId = int(self.extractGroupName(vg.getName()))
            if vg.getNumBattleCells() == 1:
                battleCell = vg.getBattleCell(0)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            elif vg.getNumBattleCells() > 1:
                self.notify.warning('multiple battle cells for zone: %d' % zoneId)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()

            for i in range(vg.getNumChildren()):
                childDnaGroup = vg.at(i)
                if isinstance(childDnaGroup, DNAInteractiveProp):
                    self.notify.debug('got interactive prop %s' % childDnaGroup)
                    battleCellId = childDnaGroup.getCellId()
                    if battleCellId == -1:
                        self.notify.warning('interactive prop %s  at %s not associated with a a battle' % (childDnaGroup, zoneId))
                    elif battleCellId == 0:
                        if zoneId in self.cellToGagBonusDict:
                            self.notify.error('FIXME battle cell at zone %s has two props %s %s linked to it' % (zoneId, self.cellToGagBonusDict[zoneId], childDnaGroup))
                        else:
                            name = childDnaGroup.getName()
                            propType = HoodUtil.calcPropType(name)
                            if propType in ToontownBattleGlobals.PropTypeToTrackBonus:
                                trackBonus = ToontownBattleGlobals.PropTypeToTrackBonus[propType]
                                self.cellToGagBonusDict[zoneId] = trackBonus

        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()
        self.streetPointList = []
        self.frontdoorPointList = []
        self.sidedoorPointList = []
        self.cogHQDoorPointList = []
        numPoints = self.dnaStore.getNumSuitPoints()
        for i in range(numPoints):
            point = self.dnaStore.getSuitPointAtIndex(i)
            if point.getPointType() == DNASuitPoint.FRONTDOORPOINT:
                self.frontdoorPointList.append(point)
            elif point.getPointType() == DNASuitPoint.SIDEDOORPOINT:
                self.sidedoorPointList.append(point)
            elif point.getPointType() == DNASuitPoint.COGHQINPOINT or point.getPointType() == DNASuitPoint.COGHQOUTPOINT:
                self.cogHQDoorPointList.append(point)
            else:
                self.streetPointList.append(point)
            self.pointIndexes[point.getIndex()] = point

        return None

    def performPathTest(self):
        if not self.notify.getDebug():
            return None
        startAndEnd = self.pickPath()
        if not startAndEnd:
            return None
        startPoint = startAndEnd[0]
        endPoint = startAndEnd[1]
        path = self.dnaStore.getSuitPath(startPoint, endPoint)
        numPathPoints = path.getNumPoints()
        for i in range(numPathPoints - 1):
            zone = self.dnaStore.getSuitEdgeZone(path.getPointIndex(i), path.getPointIndex(i + 1))
            travelTime = self.dnaStore.getSuitEdgeTravelTime(path.getPointIndex(i), path.getPointIndex(i + 1), self.suitWalkSpeed)
            self.notify.debug('edge from point ' + repr(i) + ' to point ' + repr((i + 1)) + ' is in zone: ' + repr(zone) + ' and will take ' + repr(travelTime) + ' seconds to walk.')

        return None

    def genPath(self, startPoint, endPoint, minPathLen, maxPathLen):
        return self.dnaStore.getSuitPath(startPoint, endPoint, minPathLen, maxPathLen)

    def getDnaStore(self):
        return self.dnaStore
