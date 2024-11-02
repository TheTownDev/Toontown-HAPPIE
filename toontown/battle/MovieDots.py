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
    if scene[0] == 2:
        return doDOTDamage(scene, battle)

def doNothing(scene, battle):
    return ("InsertSuitTrack", "InsertCamTrack")

def doDOTDamage(scene, battle):
    suit = battle.findSuit(scene[1])
    #lucky_suit = battle.findSuit(scene[3][0])
    
    hp = scene[2][0]
    died = scene[4]
    showDamage = Func(suit.showHpText, -hp, openEnded=0)
    updateHealthBar = Func(suit.updateHealthBar, hp)
    
    movie = Sequence(Parallel(ActorInterval(suit, 'squirt-small-react'), updateHealthBar, showDamage))
    
    if died:
        extraMovie = MovieUtil.createSuitDeathTrack(suit, battle.activeToons[0], battle)
        movie.append(extraMovie)
    
    cameraTrack = heldRelativeShot(suit, 3, 8, suit.getHeight() * 0.66, 159, 3.6, 0, movie.duration, 'avatarCloseUpDOTShot')
    
    return (movie, cameraTrack)