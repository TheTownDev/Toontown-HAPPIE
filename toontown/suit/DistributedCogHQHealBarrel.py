from direct.directnotify import DirectNotifyGlobal

from .DistributedCogHQBarrelBase import DistributedCogHQBarrelBase


class DistributedCogHQHealBarrel(DistributedCogHQBarrelBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCogHQHealBarrel')

    def __init__(self, cr):
        DistributedCogHQBarrelBase.__init__(self, cr)
        self.numGags = 0
        self.gagScale = 0.6

    def disable(self):
        DistributedCogHQBarrelBase.disable(self)
        self.ignoreAll()

    def delete(self):
        self.gagModel.removeNode()
        del self.gagModel
        DistributedCogHQBarrelBase.delete(self)

    def applyLabel(self):
        self.gagModel = loader.loadModel('phase_4/models/props/icecream')
        self.gagModel.reparentTo(self.gagNode)
        self.gagModel.find('**/p1_2').clearBillboard()
        self.gagModel.setScale(self.gagScale)
        self.gagModel.setPos(0, -0.1, -.1 - self.gagScale)

    def setGrab(self, avId):
        DistributedCogHQBarrelBase.setGrab(self, avId)
