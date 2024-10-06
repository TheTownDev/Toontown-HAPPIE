from . import TownLoader
from . import CCStreet
from toontown.suit import Suit

class CCTownLoader(TownLoader.TownLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = CCStreet.CCStreet
        self.musicFile = 'phase_6/audio/bgm/ttr_m_ara_cc_clearCoastsStreetZone.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/ttr_m_ara_cc_clearCoastsActivity.ogg'
        self.townStorageDNAFile = 'phase_6/dna/storage_CC_town.dna'

    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        Suit.loadSuits(2)
        dnaFile = 'phase_6/dna/clear_coasts_' + str(self.canonicalBranchZone) + '.dna'
        self.createHood(dnaFile)

    def unload(self):
        Suit.unloadSuits(2)
        TownLoader.TownLoader.unload(self)

    def enter(self, requestStatus):
        TownLoader.TownLoader.enter(self, requestStatus)

    def exit(self):
        TownLoader.TownLoader.exit(self)
