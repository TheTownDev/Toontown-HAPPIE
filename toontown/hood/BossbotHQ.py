from . import CogHood
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.coghq import BossbotCogHQLoader
from toontown.hood import ZoneUtil
from panda3d.core import *
from direct.interval.LerpInterval import LerpHprInterval

class BossbotHQ(CogHood.CogHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        CogHood.CogHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ToontownGlobals.BossbotHQ
        self.cogHQLoaderClass = BossbotCogHQLoader.BossbotCogHQLoader
        self.storageDNAFile = None
        self.skyFile = 'phase_12/models/bossbotHQ/ttr_m_ara_bhq_extSkybox'
        self.titleColor = (0.78, 0.70, 0.67, 1.0)
        return

    def load(self):
        CogHood.CogHood.load(self)
        self.sky.setScale(3)
        self.parentFSM.getStateNamed('BossbotHQ').addChild(self.fsm)
        self.fog = Fog('BBHQ')

    def unload(self):
        self.parentFSM.getStateNamed('BossbotHQ').removeChild(self.fsm)
        del self.cogHQLoaderClass
        CogHood.CogHood.unload(self)

    def enter(self, *args):
        CogHood.CogHood.enter(self, *args)
        localAvatar.setCameraFov(ToontownGlobals.DefaultCameraFov)
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)

    def exit(self):
        localAvatar.setCameraFov(ToontownGlobals.DefaultCameraFov)
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        CogHood.CogHood.exit(self)

    def spawnTitleText(self, zoneId, countryClub=None, floorNum = None):
        if ZoneUtil.isMintInteriorZone(zoneId):
            text = '%s\n%s' % (ToontownGlobals.StreetNames[zoneId][-1], TTLocalizer.MintFloorTitle % (floorNum + 1))
            self.doSpawnTitleText(text)
        if ZoneUtil.isCGCInteriorZone(zoneId):
            text = '%s\n%s\n%s' % (ToontownGlobals.StreetNames[zoneId][-1], TTLocalizer.CountryFloorTitle % TTLocalizer.CountryClubLetters[countryClub], TTLocalizer.MintFloorTitle % (floorNum + 1))
            self.doSpawnTitleText(text)
        else:
            CogHood.CogHood.spawnTitleText(self, zoneId)

    def setFog(self):
        if base.wantFog:
            self.fog.setColor(0.15, 0.15, 0.15)
            self.fog.setLinearRange(30.0, 800.0)
            render.clearFog()
            render.setFog(self.fog)
            self.sky.clearFog()
            self.sky.setFog(self.fog)
    
    def startSky(self):
        CogHood.CogHood.startSky(self)
        self.sky.reparentTo(render)
        ce = CompassEffect.make(NodePath(), CompassEffect.PRot | CompassEffect.PZ)
        self.sky.node().setEffect(ce)
        self.sky.setBin('background', 0)
        self.sky.setZ(-500)
        #self.skyLerp = LerpHprInterval(self.sky.find('**/MiddleGroup'), 200, (0, 0, 0), (0, 0, 360))
        #self.skyLerp.loop()

    def stopSky(self):
        #self.skyLerp.finish()
        #self.skyLerp = None
        CogHood.CogHood.stopSky(self)

