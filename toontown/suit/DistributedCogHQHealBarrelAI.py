import random

from direct.directnotify import DirectNotifyGlobal

from .DistributedCogHQBarrelBaseAI import DistributedCogHQBarrelBaseAI


class DistributedCogHQHealBarrelAI(DistributedCogHQBarrelBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCogHQHealBarrelAI')

    def __init__(self, air):
        DistributedCogHQBarrelBaseAI.__init__(self, air)
        self.toonUpValues = [4, 8, 12, 16, 20]

    def d_setGrab(self, avId):
        self.notify.debug('d_setGrab %s' % avId)
        self.sendUpdate('setGrab', [avId])
        av = self.air.doId2do.get(avId)
        if av:
            av.toonUp(random.choice(self.toonUpValues))
