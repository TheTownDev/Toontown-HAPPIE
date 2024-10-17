from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toonbase.ToontownGlobals import *

class EventManagerAI(DistributedObjectAI):
    
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.events = []
    
    def addEvent(self, classString):
        self.events.append(classString)