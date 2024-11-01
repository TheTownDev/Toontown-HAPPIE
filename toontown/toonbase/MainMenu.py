from panda3d.core import *
from libotp import *
from direct.interval.IntervalGlobal import *
from direct.task import Task
from direct.fsm import FSM
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta
from direct.showbase import PythonUtil
from toontown.suit import SuitCreationFunc

class MainMenu:
    
    def __init__(self, launcher):
        self.launcher = launcher
        self.mainMenuRoom = loader.loadModel('phase_5/models/cogdominium/ttr_m_ara_cbr_barrelRoom.bam')
        self.mainMenuRoom.reparentTo(render)
        self.accept('space', self.moveToPickAToon)