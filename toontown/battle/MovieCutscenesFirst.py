from toontown.toonbase.ToontownBattleGlobals import *
from toontown.battle.BattleBase import *
from direct.interval.IntervalGlobal import *
from direct.showbase import DirectObject
from . import MovieCamera, MovieUtil
from .BattleBase import *
from .BattleProps import *
from .BattleSounds import *
from .MovieUtil import *
from .MovieCamera import *
from . import BattleParticles
from toontown.toon.ToonDNA import *
from toontown.suit.SuitDNA import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toon import TTEmote
from panda3d.core import *
import random
from libotp import *
from . import PlayByPlayText
from toontown.effects import DustCloud

def doScene(scene, battle):
    #how this works:
    if scene[0] == 1:
        return doNothing(scene, battle)
    if scene[0] == 2:
        return doForemanIntro(scene, battle)

def doNothing(scene, battle):
    return ("InsertSuitTrack", "InsertCamTrack")

def foremanNeeds(foreman):
    camera.reparentTo(foreman)
    camera.setPos(6, -0.60, 1.43)
    camera.setHpr(0, 0, 0)
    base.camLens.setFov(90)
    silence = loader.loadMusic("phase_3/audio/bgm/none.ogg")
    silence.play()

def doForemanIntro(scene, battle):
    foreman = battle.findSuit(scene[1])
    
    # camera 1 (rep. foreman) --> pos: x 6, -0.60, 1.43 hpr 0, 0, 0
    # camera 2 (rep. foreman) --> pos: x 6, -0.60, 6.14 hpr 0.00, 352.87, 0.00
    # camera 3 --> pos: x 5.07, 9.39, 6.16 hpr 169.45, 348.31, 0.00
    # camera 4 (rep. foreman) --> pos: x 5.99, 0, 2.18 hpr 0, 52.13, 0
    
    cameraLerp1 = LerpPosHprInterval(camera, 6, Point3(6, -0.60, 6.14), Point3(0.00, 352.87, 0.00), blendType='easeOut', other=battle, name='poshprCamera')
    
    promotion_sfx = loader.loadSfx("phase_4/audio/sfx/ttr_s_ene_cgb_sellbotForeman_firedUp.ogg")
    foremanMusic = base.loader.loadMusic('phase_9/audio/bgm/ttr_s_ara_shq_facilityBoss.ogg')
    
    movie = Sequence(Func(foremanNeeds, foreman), Parallel(cameraLerp1, Sequence(Wait(2.4), Func(foreman.setChatAbsolute, "It seems my quata was not clear...", CFSpeech | CFTimeout))), Func(camera.reparentTo, battle), Func(camera.setPos, Point3(5.07, 9.39, 6.16)), Func(camera.setHpr, Vec3(169.45, 348.31, 0.00)), Wait(1), Func(foreman.setChatAbsolute, "If you all want to maintain your positions.", CFSpeech | CFTimeout), Wait(4), Func(camera.reparentTo, foreman), Func(camera.setPos, Point3(5.99, 0, 2.18)), Func(camera.setHpr, Vec3(0, 52.13, 0)), Func(foreman.setChatAbsolute, "Then I would suggest to start matching it with these animals.", CFSpeech | CFTimeout), Func(foremanMusic.play), Wait(2), Parallel(Func(promotion_sfx.play), ActorInterval(foreman, 'chop-chop'), Func(base.camLens.setFov, BattleCamDefaultFov)))
    
    cameraTrack = Sequence(Wait(movie.duration))
    
    return (movie, cameraTrack)
