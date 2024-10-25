import math
from . import DistributedTreasureAI
from toontown.toonbase import ToontownGlobals
from toontown.quest import Quests
from toontown.hood import ZoneUtil

class DistributedSZTreasureAI(DistributedTreasureAI.DistributedTreasureAI):

    def __init__(self, air, treasurePlanner, x, y, z):
        DistributedTreasureAI.DistributedTreasureAI.__init__(self, air, treasurePlanner, x, y, z)
        if hasattr(treasurePlanner, 'healAmount'):
            self.healAmount = treasurePlanner.healAmount
        else:
            self.healAmount = 0.10
    
    def isLocationMatch(self, zoneId):
        loc = self.getLocation()
        if loc is Quests.Anywhere:
            return 1
        if ZoneUtil.isPlayground(loc):
            if loc == ZoneUtil.getCanonicalHoodId(zoneId):
                return 1
            else:
                return 0
        elif loc == ZoneUtil.getCanonicalBranchZone(zoneId):
            return 1
        elif loc == zoneId:
            return 1
        else:
            return 0
    
    def doesToonHaveTreasureQuest(self, av):
        for index, quest in enumerate(self.air.questManager.toonQuestsList2Quests(av.quests)):
            if isinstance(quest, Quests.TreasureQuest):
                if quest.getCompletionStatus(av, av.quests[index]) != Quests.COMPLETE:
                    if quest.isLocationMatch(self.zoneId):
                        return 1
        return 0

    def validAvatar(self, av):
        if self.doesToonHaveTreasureQuest(av):
            return 1
        if av.hp > 0 and av.hp < av.maxHp:
            return 1
    
    def d_setGrab(self, avId):
        DistributedTreasureAI.DistributedTreasureAI.d_setGrab(self, avId)
        if avId in self.air.doId2do:
            av = self.air.doId2do[avId]
            av.toonUp(math.ceil(av.maxHp * self.healAmount))
            for index, quest in enumerate(self.air.questManager.toonQuestsList2Quests(av.quests)):
                if isinstance(quest, Quests.TreasureQuest):
                    if quest.getCompletionStatus(av, av.quests[index]) != Quests.COMPLETE:
                        self.air.questManager.incrementQuestProgressCustom(av.quests[index], av, self.zoneId)
