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
    elif scene[0] == 2:
        return doFieldPromotion(scene, battle)
    elif scene[0] == 3:
        return doOvertime(scene, battle)
    elif scene[0] == 4:
        return doTesting(scene, battle)

def doNothing(scene, battle):
    return ("InsertSuitTrack", "InsertCamTrack")

def doProtocall(scene, battle):
    suit = battle.findSuit(scene[1])
    return ("InsertSuitTrack", "InsertCamTrack")

def getPartTrack(particleEffect, startDelay, durationDelay, partExtraArgs):
    particleEffect = partExtraArgs[0]
    parent = partExtraArgs[1]
    if len(partExtraArgs) > 2:
        worldRelative = partExtraArgs[2]
    else:
        worldRelative = 1
    return Sequence(Wait(startDelay), ParticleInterval(particleEffect, parent, worldRelative, duration=durationDelay, cleanup=True))

def doTesting(scene, battle):
    foreman = battle.findSuit(scene[1])
    suits = []
    try:
        lucky_suit1 = battle.findSuit(scene[3][0])
        suits.append(lucky_suit1)
    except:
        pass
    try:
        lucky_suit2 = battle.findSuit(scene[3][1])
        suits.append(lucky_suit2)
    except:
        pass

    movie = Parallel()

    for suit in suits:
        movie.append(ActorInterval(suit, 'squirt-small-react'))
    cameraTrack = suitGroupShot(foreman, movie.duration)
    return (movie, cameraTrack)


def doFieldPromotion(scene, battle):
    foreman = battle.findSuit(scene[1])
    lucky_suit = battle.findSuit(scene[3][0])
    
    foremanPos = foreman.getPos()
    foremanHpr = foreman.getHpr()
    
    promotion_movie = payRaiseMovie(lucky_suit, battle)
    
    movie = Sequence()
    
    promotion_sfx = loader.loadSfx("phase_4/audio/sfx/ttr_s_ene_cgb_sellbotForeman_firedUp.ogg")
    
    movie.append(Func(foreman.headsUp, lucky_suit))
    
    promotionalGiven = Parallel(ActorInterval(foreman, 'chop-chop'), Func(promotion_sfx.play), Sequence(Wait(2)), promotion_movie)
    
    movie.append(promotionalGiven)
    
    movie.append(Func(foreman.setHpr, foremanHpr))
    
    cameraTrack = suitGroupShot(foreman, movie.duration)
    
    return (movie, cameraTrack)

def doFireEffect(lucky_suit):
    baseFlameEffect = BattleParticles.createParticleEffect(file='firedBaseFlame')
    flameEffect = BattleParticles.createParticleEffect('FiredFlame')
    flecksEffect = BattleParticles.createParticleEffect('SpriteFiredFlecks')
    
    baseFlameTrack = getPartTrack(baseFlameEffect, 0.1, 900, [baseFlameEffect, lucky_suit, 0])
    flameTrack = getPartTrack(flameEffect, 0.05, 900, [flameEffect, lucky_suit, 0])
    flecksTrack = getPartTrack(flecksEffect, 0.0, 900, [flecksEffect, lucky_suit, 0])
    
    particalTrackFull = Parallel(baseFlameTrack, flameTrack, flecksTrack)
    particalTrackFull.loop()

def doOvertime(scene, battle):    
    foreman = battle.findSuit(scene[1])
    
    """
    
    foremanPos = foreman.getPos()
    foremanHpr = foreman.getHpr()
    
    fire_sfx = loader.loadSfx("phase_5/audio/sfx/SA_hot_air.ogg")
    
    promotion_movie = Parallel(Sequence(Wait(1), Parallel(Func(fire_sfx.play), ActorInterval(lucky_suit, 'powered-up'), Func(doFireEffect, lucky_suit), Func(lucky_suit.getGeomNode().setColorScale, Vec4(0.9, 0.65, 0.65, 1.0))), Func(lucky_suit.loop, 'neutral'), Func(lucky_suit.getGeomNode().setColorScale, Vec4(1.0, 1.0, 1.0, 1.0))))
    
    -2.20, 7.73, 3.70

    192.09, 18.43, 0

    -0.26, 11.39, 6.08

    182.71, 0, 0
    
    """
    cog_sfx = loader.loadSfx("phase_4/audio/sfx/ttr_s_ene_cgb_sellbotForeman_overtime.ogg")
    headModelPath = 'phase_3.5/models/char/ttr_r_ene_cgb_heads'
    
    foremanMusicNew = base.loader.loadMusic('phase_9/audio/bgm/ttr_s_ara_shq_facilityBossOvertime.ogg')
    foremanMusicNew.setLoop(1)
    
    movie = Parallel(Func(foremanMusicNew.play), Sequence(Func(foreman.setChatAbsolute, "You..have all failed my...", CFSpeech | CFTimeout), Wait(1.4), Func(foreman.setChatAbsolute, "QOUTA!", CFSpeech | CFTimeout)), Func(camera.reparentTo, foreman), ActorInterval(foreman, 'livid'), Func(cog_sfx.play), Sequence(Wait(2.5), Func(doFireEffect, foreman), Func(doHeadSwap, foreman, headModelPath), Wait(4), Func(camera.reparentTo, battle)))
    #camera.place()
    """
    promotion_sfx = loader.loadSfx("phase_4/audio/sfx/ttr_s_ene_cgb_sellbotForeman_firedUp.ogg")
    
    promotionalGiven = Parallel(ActorInterval(foreman, 'chop-chop'), Func(promotion_sfx.play), promotion_movie)
    
    movie.append(promotionalGiven)
    
    movie.append(Func(foreman.setHpr, foremanHpr))
    
    """
    
    #cameraTrack = allGroupHighShot(foreman, movie.duration)
    cameraTrack = Sequence(Func(camera.setPosHpr, Point3(-0.26, 11.39, 6.08), Vec3(182.71, 0, 0)), Wait(1.4), Func(camera.setPosHpr, Point3(-2.20, 7.73, 3.70), Vec3(192.09, 18.43, 0)), Wait(3.0))
    
    return (movie, cameraTrack)

def doHeadSwap(foreman, headModelPath):
    headModel = loader.loadModel(headModelPath).find('**/factoryforemanangry')
    for headPart in foreman.headParts:
        headPart.stash()
    headModel.reparentTo(foreman.find('**/def_M_head_01'))
    foreman.headParts.append(headModel)