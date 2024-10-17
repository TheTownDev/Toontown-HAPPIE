from direct.distributed.DistributedObjectAI import DistributedObject
from toontown.toonbase.ToontownGlobals import *

class Event(DistributedObject):
    
    OFF = 0
    ON = 1

    def __init__(self, air):
        DistributedObject.__init__(self, air)
        self.eventId = 0
        self.eventState = self.OFF

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)

    def delete(self):
        self.eventMgr.removeEvent(self)