from panda3d.core import *
from . import SafeZoneLoader
from . import CCPlayground
from direct.fsm import State
from toontown.char import CharDNA
from toontown.char import Char
from toontown.toonbase import ToontownGlobals

class CCSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = CCPlayground.CCPlayground
        self.musicFile = 'phase_6/audio/bgm/ttr_m_ara_cc_clearCoastsPlayground.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/ttr_m_ara_cc_clearCoastsActivity.ogg'
        self.dnaFile = 'phase_6/dna/clear_coasts_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_CC_sz.dna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.seagullSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_Seagull.ogg')
        self.underwaterSound = base.loader.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loader.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loader.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')
        self.boat = self.geom.find('**/donalds_boat')
        self.dockSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_dockcreak.ogg')
        self.foghornSound = base.loader.loadSfx('phase_5/audio/sfx/SZ_DD_foghorn.ogg')
        self.bellSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_shipbell.ogg')
        self.waterSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_waterlap.ogg')

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.seagullSound
        del self.underwaterSound
        del self.swimSound
        del self.dockSound
        del self.foghornSound
        del self.bellSound
        del self.waterSound
        del self.submergeSound

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)
