from direct.directnotify import DirectNotifyGlobal

from .DistributedCogHQEntityAI import DistributedCogHQEntityAI


class DistributedCogHQBarrelBaseAI(DistributedCogHQEntityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCogHQBarrelBaseAI')

    def __init__(self, air):
        DistributedCogHQEntityAI.__init__(self, air)
        self.usedAvIds = []

    def requestGrab(self):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('requestGrab %s' % avId)
        if avId not in self.usedAvIds:
            self.usedAvIds.append(avId)
            self.d_setGrab(avId)
        else:
            self.sendUpdate('setReject')

    def d_setGrab(self, avId):
        self.sendUpdate('setGrab', [avId])
