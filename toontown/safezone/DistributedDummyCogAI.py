from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.fsm.FSM import FSM
import random
from otp.distributed.OtpDoGlobals import *
from direct.task import Task
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedDummyCogAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDummyTowerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'ToonfestCogFSM')
        self.position = (0, 0, 0)
        self.hpr = (0, 0, 0)
        self.cogid = 0
        self.state = 'Up'
        self.air = air

    def enterOff(self):
        self.requestDelete()

    def generate(self):
        self.toggleCogTask()

    def setProperties(self):
        self.setCogPosId(self.position[0], self.position[1], self.position[2], self.cogid)

    def toggleCogTask(self):
        taskMgr.doMethodLater(10, self.toggleCog, 'toggle-cog', extraArgs=[])

    def toggleCog(self):
        if self.state == 'Down':
            self.state = 'Up'
            self.enterUp()
        elif self.state == 'Up':
            self.state = 'Down'
            self.enterDown()
        taskMgr.doMethodLater(10, self.toggleCog, 'toggle-cog', extraArgs=[])

    def setCogPosId(self, x, y, z, cogid):
        self.sendUpdate('setCogPosId', [x, y, z, cogid])

    def setCogId(self, cogid):
        self.sendUpdate('setCogId', [cogid])

    def setCogPos(self, x, y, z):
        self.sendUpdate('setCogPos', [x, y, z])

    def d_setHpr(self, h, p, r):
        self.sendUpdate('setHpr', [h, p, r])

    def enterDown(self):
        self.cogDown = True
        self.sendUpdate('toggleCog', ['Down'])
        print('Cog has gone down.')

    def enterUp(self):
        self.cogUp = True
        self.sendUpdate('toggleCog', ['Up'])
        print('Cog has come up.')

    def updateTower(self, avName, avId, cogDoId):
        base = random.randint(50, 75)
        av = self.air.doId2do[avId]
        if cogDoId == self.doId:
            av.b_setMoney(av.getMoney() + base)
        print('%s has won %d beans from cog %d' % (avName, base, self.doId))
