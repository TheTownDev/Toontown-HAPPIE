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

def doNothing(scene, battle):
    return ("InsertSuitTrack", "InsertCamTrack")

def doProtocall(scene, battle):
    suit = battle.findSuit(scene[1])
    return ("InsertSuitTrack", "InsertCamTrack")

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

