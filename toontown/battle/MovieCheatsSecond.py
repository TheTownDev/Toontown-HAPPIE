from toontown.toonbase.ToontownBattleGlobals import *
from toontown.battle.BattleBase import *
from direct.interval.IntervalGlobal import *
from direct.showbase import DirectObject
from . import MovieCamera, MovieUtil
from .BattleBase import *
from .BattleProps import *
from .BattleSounds import *
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
        return doBookSmart(scene, battle)
    elif scene[0] == 4:
        return doScold(scene, battle)

def doNothing(scene, battle):
    return ("InsertSuitTrack", "InsertCamTrack")

def getPartTrack(particleEffect, startDelay, durationDelay, partExtraArgs):
    particleEffect = partExtraArgs[0]
    parent = partExtraArgs[1]
    if len(partExtraArgs) > 2:
        worldRelative = partExtraArgs[2]
    else:
        worldRelative = 1
    return Sequence(Wait(startDelay), ParticleInterval(particleEffect, parent, worldRelative, duration=durationDelay, cleanup=True))

def doFireEffect(lucky_suit):
    baseFlameEffect = BattleParticles.createParticleEffect(file='firedBaseFlame')
    flameEffect = BattleParticles.createParticleEffect('FiredFlame')
    flecksEffect = BattleParticles.createParticleEffect('SpriteFiredFlecks')
    
    baseFlameTrack = getPartTrack(baseFlameEffect, 0.1, 900, [baseFlameEffect, lucky_suit, 0])
    flameTrack = getPartTrack(flameEffect, 0.05, 900, [flameEffect, lucky_suit, 0])
    flecksTrack = getPartTrack(flecksEffect, 0.0, 900, [flecksEffect, lucky_suit, 0])
    
    particalTrackFull = Parallel(baseFlameTrack, flameTrack, flecksTrack)
    particalTrackFull.loop()

def doFieldPromotion(scene, battle):    
    foreman = battle.findSuit(scene[1])
    lucky_suit = battle.findSuit(scene[3][0])
    
    foremanPos = foreman.getPos()
    foremanHpr = foreman.getHpr()
    
    fire_sfx = loader.loadSfx("phase_5/audio/sfx/SA_hot_air.ogg")
    
    promotion_movie = Parallel(Sequence(Wait(1), Parallel(Func(fire_sfx.play), ActorInterval(lucky_suit, 'powered-up'), Func(doFireEffect, lucky_suit), Func(lucky_suit.getGeomNode().setColorScale, Vec4(0.9, 0.65, 0.65, 1.0))), Func(lucky_suit.loop, 'neutral'), Func(lucky_suit.getGeomNode().setColorScale, Vec4(1.0, 1.0, 1.0, 1.0))))
    
    movie = Sequence()
    
    promotion_sfx = loader.loadSfx("phase_4/audio/sfx/ttr_s_ene_cgb_sellbotForeman_firedUp.ogg")
    
    promotionalGiven = Parallel(ActorInterval(foreman, 'chop-chop'), Func(promotion_sfx.play), promotion_movie)
    
    movie.append(promotionalGiven)
    
    movie.append(Func(foreman.setHpr, foremanHpr))
    
    cameraTrack = allGroupHighShot(foreman, movie.duration)
    
    return (movie, cameraTrack)

def doScold(scene, battle):    
    foreman = battle.findSuit(scene[1])
    lucky_suit = battle.findSuit(scene[3][0])
    
    foremanPos = foreman.getPos()
    foremanHpr = foreman.getHpr()
    
    fire_sfx = loader.loadSfx("phase_5/audio/sfx/SA_hot_air.ogg")
    
    promotion_movie = Parallel(Sequence(Wait(1), Parallel(Func(fire_sfx.play), ActorInterval(lucky_suit, 'powered-up'), Func(doFireEffect, lucky_suit), Func(lucky_suit.getGeomNode().setColorScale, Vec4(0.9, 0.65, 0.65, 1.0))), Func(lucky_suit.loop, 'neutral'), Func(lucky_suit.getGeomNode().setColorScale, Vec4(1.0, 1.0, 1.0, 1.0))))
    
    movie = Sequence()
    
    promotion_sfx = loader.loadSfx("phase_4/audio/sfx/ttr_s_ene_cgb_sellbotForeman_firedUp.ogg")
    
    promotionalGiven = Parallel(ActorInterval(foreman, 'chop-chop'), Func(promotion_sfx.play), promotion_movie)
    
    movie.append(promotionalGiven)
    
    movie.append(Func(foreman.setHpr, foremanHpr))
    
    cameraTrack = allGroupHighShot(foreman, movie.duration)
    
    return (movie, cameraTrack)

def doBookSmart(scene, battle):
    foreman = battle.findSuit(scene[1])
    lucky_suit = battle.findSuit(scene[3][0])
    
    baseFlameEffect = BattleParticles.createParticleEffect(file='firedBaseFlame')
    flameEffect = BattleParticles.createParticleEffect('FiredFlame')
    flecksEffect = BattleParticles.createParticleEffect('SpriteFiredFlecks')
    
    baseFlameTrack = getPartTrack(baseFlameEffect, 0.3, 3.2, [baseFlameEffect, lucky_suit, 0])
    flameTrack = getPartTrack(flameEffect, 0.3, 3.1, [flameEffect, lucky_suit, 0])
    flecksTrack = getPartTrack(flecksEffect, 0.3, 3, [flecksEffect, lucky_suit, 0])
    
    particalTrackFull = Parallel(baseFlameTrack, flameTrack, flecksTrack)
    
    foremanPos = foreman.getPos()
    foremanHpr = foreman.getHpr()
    
    fire_sfx = loader.loadSfx("phase_5/audio/sfx/SA_hot_air.ogg")
    
    promotion_movie = Parallel(Sequence(Wait(2.4), Parallel(Func(fire_sfx.play), ActorInterval(lucky_suit, 'powered-up'), particalTrackFull, Func(lucky_suit.getGeomNode().setColorScale, Vec4(0.9, 0.65, 0.65, 1.0))), Func(lucky_suit.loop, 'neutral'), Func(lucky_suit.getGeomNode().setColorScale, Vec4(1.0, 1.0, 1.0, 1.0))))
    
    movie = Sequence()
    
    promotion_sfx = loader.loadSfx("phase_4/audio/sfx/ttr_s_ene_cgb_sellbotForeman_firedUp.ogg")
    
    promotionalGiven = Parallel(ActorInterval(foreman, 'chop-chop'), Func(promotion_sfx.play), promotion_movie)
    
    movie.append(promotionalGiven)
    
    movie.append(Func(foreman.setHpr, foremanHpr))
    
    cameraTrack = allGroupHighShot(foreman, movie.duration)
    
    return (movie, cameraTrack)