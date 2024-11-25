from typing import List

from direct.directnotify import DirectNotifyGlobal
from . import HoodDataAI, ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.safezone import DistributedTrolleyAI
from toontown.safezone import TTTreasurePlannerAI
from toontown.safezone import ArchipelagoTreasurePlannerAI
from toontown.safezone import DistributedArchiTreasureAI
from toontown.safezone import ButterflyGlobals
from toontown.safezone import DistributedBenchAI
from panda3d.core import *
from panda3d.toontown import *
from direct.task import Task

class TTHoodDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTHoodDataAI')

    def __init__(self, air, zoneId=None):
        hoodId = ToontownGlobals.ToontownCentral
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        return

    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)
        trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        trolley.generateWithRequired(self.zoneId)
        trolley.start()
        self.addDistObj(trolley)
        self.trolley = trolley                        
        self.treasurePlanner = [TTTreasurePlannerAI.TTTreasurePlannerAI(self.zoneId),
                                ArchipelagoTreasurePlannerAI.ArchipelagoTreasurePlannerAI(ToontownGlobals.SillyStreet + 1, DistributedArchiTreasureAI.DistributedArchiTreasureAI, 0, treasureCount=1)
                                ]
        for planner in self.treasurePlanner:
            planner.start()
        self.createButterflies(ButterflyGlobals.TTC)
        if simbase.blinkTrolley:
            taskMgr.doMethodLater(0.5, self._deleteTrolley, 'deleteTrolley')
        messenger.send('TTHoodSpawned', [self])
        self.createBenches()
    
    def findAndCreateBenches(self, dnaGroup, zoneId, area, overrideDNAZone = 0, type = 'bench'):
        picnicTables = []
        picnicTableGroups = []
        # if isinstance(dnaGroup, DNAGroup) and string.find(dnaGroup.getName(), type) >= 0:
        
        if isinstance(dnaGroup, DNAGroup) and dnaGroup.getName().find(type) >= 0:
            if type == 'bench':   
                pos = Point3(-45, -85, 0.53)
                hpr = Vec3(8.75, 0, 0)
                        
                picnicTable = DistributedBenchAI.DistributedBenchAI(self.air, 1, pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2])
                picnicTable.generateWithRequired(zoneId)
                picnicTables.append(picnicTable)
        else:
            if isinstance(dnaGroup, DNAVisGroup) and not overrideDNAZone:
                zoneId = ZoneUtil.getTrueZoneId(int(dnaGroup.getName().split(':')[0]), zoneId)
            for i in range(dnaGroup.getNumChildren()):
                childPicnicTables = self.findAndCreateBenches(dnaGroup.at(i), zoneId, area, overrideDNAZone, type)
                picnicTables += childPicnicTables

        return picnicTables
    
    def createBenches(self):
        self.benches = []
        for zone in self.air.zoneTable[self.canonicalHoodId]:
            zoneId = ZoneUtil.getTrueZoneId(zone[0], self.zoneId)
            dnaData = self.air.dnaDataMap.get(zone[0], None)
            if isinstance(dnaData, DNAData):
                area = ZoneUtil.getCanonicalZoneId(zoneId)
                foundTables = self.findAndCreateBenches(dnaData, zoneId, area, overrideDNAZone=True)
                self.benches += foundTables

        for bench in self.benches:
            bench.start()
            self.addDistObj(bench)

        return

    def shutdown(self):
        HoodDataAI.HoodDataAI.shutdown(self)
        messenger.send('TTHoodDestroyed', [self])

    def _deleteTrolley(self, task):
        self.trolley.requestDelete()
        taskMgr.doMethodLater(0.5, self._createTrolley, 'createTrolley')
        return Task.done

    def _createTrolley(self, task):
        trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        trolley.generateWithRequired(self.zoneId)
        trolley.start()
        self.trolley = trolley
        taskMgr.doMethodLater(0.5, self._deleteTrolley, 'deleteTrolley')
        return Task.done

    def getStreetClerkZoneIds(self) -> List[int]:
        return [2114, 2218, 2326]  # Silly, Loopy, Punchline
