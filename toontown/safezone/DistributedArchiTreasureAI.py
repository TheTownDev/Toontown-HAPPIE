from . import DistributedSZTreasureAI
from toontown.toonbase import ToontownGlobals
from toontown.quest import Quests
from toontown.hood import ZoneUtil
import math

class DistributedArchiTreasureAI(DistributedSZTreasureAI.DistributedSZTreasureAI):

    def __init__(self, air, treasurePlanner, x, y, z):
        DistributedSZTreasureAI.DistributedSZTreasureAI.__init__(self, air, treasurePlanner, x, y, z)
        self.healAmount = 0.15
        self.packageId = 5

    def getLocationFromCode(self, archiCode, index):
        return ToontownGlobals.ARCHI_CODE_TO_LOCATION[archiCode][index]
    
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
                        if quest.getPackageId() and self.packageId == quest.getPackageId():
                            return 1
        return 0

    def validAvatar(self, av, archiCode):
        if av:
            if self.doesToonHaveTreasureQuest(av):
                return 1
        

    def isValidHp(self, av):
        return (av.hp > 0 and av.hp < av.maxHp)

    def d_setGrab(self, avId, archiCode):
        self.notify.debug('d_setGrab %s' % avId)
        self.sendUpdate('setGrab', [avId])
        av = self.air.doId2do[avId]
        if av:
            for index, quest in enumerate(self.air.questManager.toonQuestsList2Quests(av.quests)):
                if isinstance(quest, Quests.TreasureQuest):
                    if quest.getCompletionStatus(av, av.quests[index]) != Quests.COMPLETE:
                        self.air.questManager.incrementQuestProgressCustom(av.quests[index], av, self.zoneId)
