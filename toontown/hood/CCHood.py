from panda3d.core import *
from . import ToonHood
from toontown.town import CCTownLoader
from toontown.safezone import CCSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *

class CCHood(ToonHood.ToonHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ClearCoasts
        self.townLoaderClass = CCTownLoader.CCTownLoader
        self.safeZoneLoaderClass = CCSafeZoneLoader.CCSafeZoneLoader
        self.storageDNAFile = 'phase_6/dna/storage_CC.dna'
        self.holidayStorageDNADict = {WINTER_DECORATIONS: ['phase_6/dna/winter_storage_CC.dna'],
         WACKY_WINTER_DECORATIONS: ['phase_6/dna/winter_storage_CC.dna'],
         HALLOWEEN_PROPS: ['phase_6/dna/halloween_props_storage_CC.dna'],
         SPOOKY_PROPS: ['phase_6/dna/halloween_props_storage_CC.dna']}
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.titleColor = (0.8, 0.6, 0.5, 1.0)
        self.whiteFogColor = Vec4(0.32, 0.32, 0.32, 1)
        self.underwaterFogColor = Vec4(0.32, 0.32, 0.32, 1.0)
        self.spookySkyFile = 'phase_3.5/models/props/BR_sky'

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('CCHood').addChild(self.fsm)
        self.fog = Fog('CCFog')

    def unload(self):
        self.parentFSM.getStateNamed('CCHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)
        self.fog = None
        return

    def enter(self, *args):
        ToonHood.ToonHood.enter(self, *args)

    def exit(self):
        ToonHood.ToonHood.exit(self)

    def setUnderwaterFog(self):
        if base.wantFog:
            self.fog.setColor(self.underwaterFogColor)
            self.fog.setLinearRange(0.1, 100.0)
            render.setFog(self.fog)
            self.sky.setFog(self.fog)

    def setWhiteFog(self):
        if base.wantFog:
            self.fog.setColor(self.whiteFogColor)
            self.fog.setLinearRange(0.0, 400.0)
            
    def setNoFog(self):
        if base.wantFog:
            render.clearFog()
            self.sky.clearFog()
