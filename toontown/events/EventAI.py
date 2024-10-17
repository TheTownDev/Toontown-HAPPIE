from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toonbase.ToontownGlobals import *

class EventAI(DistributedObjectAI):
    
    OFF = 0
    ON = 1
    
    def __init__(self, air, eventId):
        DistributedObjectAI.__init__(self, air)
        self.eventId = eventId
        self.eventState = OFF
    
    def setState(self, state):
        self.eventState = state
        self.sendUpdate('setState', [state])