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
    if scene[0] == 3:
        return doAuditorCutscene(scene, battle)

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


def doAuditorCutscene(scene, battle):
    foreman = battle.findSuit(scene[1])

    camera.setPos(0, 0, 10)
    camera.setHpr(0, 0, 0)
    base.camLens.setFov(BattleCamDefaultFov - 17)


    mintAuditorCameraPos = Point3(6.57, -18.26, 6.44)
    mintAuditorCameraHpr = Vec3(20.56, 0, 0.00)

    regularCogs = []
    regularCogWalking = Parallel()
    for suit in battle.activeSuits:
        if suit != foreman:
            regularCogs.append(suit)
            destPos, destHpr = battle.getActorPosHpr(suit, battle.suits)
            suit.setH(suit.getH() + 180)
            cogHprLerp = LerpHprInterval(suit, 3, destHpr,
                                             blendType='easeOut',
                                             other=battle, name='hprCamera')
            cogWaling = Parallel(Wait(0.25), Func(suit.loop, 'walk'), cogHprLerp, Sequence(Wait(3.25), Func(suit.loop, 'neutral')))
            regularCogWalking.append(cogWaling)
        else:
            destPos, destHpr = battle.getActorPosHpr(suit, battle.suits)
            foreman.setY(destPos[1] + -0.1)

    cameraLerp1 = LerpPosHprInterval(camera, 6, Point3(0, -27.48, 7.88), Vec3(0, 0, 0.00), blendType='easeInOut',
                                     other=battle, name='poshprCamera')

    cameraTrack = Sequence(Func(camera.reparentTo, battle), Wait(1.0), cameraLerp1, Wait(2.0), Func(base.camLens.setFov, BattleCamDefaultFov),Func(camera.setPos, mintAuditorCameraPos),  Func(camera.setHpr, mintAuditorCameraHpr), Wait(14.5))

    auditorSpeaking = Sequence(Func(foreman.setChatAbsolute, "Excuse me, we have company...", CFSpeech | CFTimeout), Wait(5.2), Func(foreman.clearChat), Func(foreman.setChatAbsolute, "And it seems like the market will also have new company.", CFSpeech | CFTimeout), Wait(4.4), Func(foreman.clearChat), Func(foreman.setChatAbsolute, "Time is money. I'm expecting all of you to make your paychecks worth it.", CFSpeech | CFTimeout), Wait(8), Func(foreman.clearChat))

    promotion_sfx = loader.loadSfx("phase_4/audio/sfx/ttr_s_ene_cgc_cashbotAuditor_promoting.ogg")
    foremanMusic = base.loader.loadMusic('phase_10/audio/bgm/ttr_s_ara_chq_facilityBossBear.ogg')
    foremanIntroMusic = base.loader.loadMusic('phase_10/audio/bgm/ttr_s_ara_chq_facilityBossCutscene.ogg')

    auditorVisuals = Sequence(Wait(11.0), Parallel(ActorInterval(foreman, 'promoting'), Func(promotion_sfx.play)), Func(foreman.loop, 'neutral'))

    movie = Sequence(Parallel(Func(foremanIntroMusic.play), regularCogWalking, auditorSpeaking, auditorVisuals), Wait(7), Func(base.camLens.setFov, BattleCamDefaultFov), Func(foremanMusic.play))

    return (movie, cameraTrack)
