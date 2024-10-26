from . import DistributedSZTreasure
from panda3d.core import *
from direct.interval.IntervalGlobal import *

from typing import Union


class DistributedArchiTreasure(DistributedSZTreasure.DistributedSZTreasure):
    def __init__(self, cr):
        DistributedSZTreasure.DistributedSZTreasure.__init__(self, cr)
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.ogg'
        self.billboard = False
        self.animateTrack = None
        self.zOffset = 1.25
    
    def delete(self):
        if self.animateTrack:
            self.animateTrack.finish()
            self.animateTrack = None
        DistributedSZTreasure.DistributedSZTreasure.delete(self)

    def prepareModel(self, modelPath, modelFindString):
        model = loader.loadModel('phase_4/models/props/ttr_r_prp_qst_package')
        model.setScale(3)
        self.makeDoSpinInterval(model)
        return model
    
    def makeDoSpinInterval(self, model):
        spinTrack = LerpHprInterval(model, 8, (0, 0, 0), (360, 0, 0))
        startPos = model.getPos()
        endPos = startPos + Point3(0, 0, 1)
        floatTrack = Sequence(LerpPosInterval(model, 4, endPos, startPos=startPos, blendType='easeInOut'), LerpPosInterval(model, 4, startPos, endPos, blendType='easeInOut'))
        self.animateTrack = Parallel(spinTrack, floatTrack)
        self.animateTrack.loop()
