from direct.particles.ParticleEffect import *
import os
from direct.directnotify import DirectNotifyGlobal
notify = DirectNotifyGlobal.directNotify.newCategory('BattleParticles')
TutorialParticleEffects = ('gearExplosionBig.ptf', 'gearExplosionSmall.ptf', 'gearExplosion.ptf')
ParticleNames = ('audit-div', 'audit-five', 'audit-four', 'audit-minus', 'audit-mult', 'audit-one', 'audit-plus', 'audit-six', 'audit-three', 'audit-two', 'blah', 'brainstorm-box', 'brainstorm-env', 'brainstorm-track', 'buzzwords-crash', 'buzzwords-inc', 'buzzwords-main', 'buzzwords-over', 'buzzwords-syn', 'confetti', 'doubletalk-double', 'doubletalk-dup', 'doubletalk-good', 'filibuster-cut', 'filibuster-fiscal', 'filibuster-impeach', 'filibuster-inc', 'jargon-brow', 'jargon-deep', 'jargon-hoop', 'jargon-ipo', 'legalese-hc', 'legalese-qpq', 'legalese-vd', 'mumbojumbo-boiler', 'mumbojumbo-creative', 'mumbojumbo-deben', 'mumbojumbo-high', 'mumbojumbo-iron', 'poundsign', 'schmooze-genius', 'schmooze-instant', 'schmooze-master', 'schmooze-viz', 'roll-o-dex', 'rollodex-card', 'dagger', 'fire', 'snow-particle', 'raindrop', 'gear', 'checkmark', 'dollar-sign', 'spark')
particleModel = None
particleSearchPath = None

def loadParticles():
    global particleModel
    if particleModel == None:
        particleModel = loader.loadModel('phase_3.5/models/props/suit-particles')
    return


def unloadParticles():
    global particleModel
    if particleModel != None:
        particleModel.removeNode()
    del particleModel
    particleModel = None
    return


def getParticle(name):
    if name in ParticleNames:
        particle = particleModel.find('**/' + str(name))
        return particle
    else:
        notify.warning('getParticle() - no name: %s' % name)
        return None
    return None


def loadParticleFile(name):
    global particleSearchPath
    if particleSearchPath == None:
        particleSearchPath = DSearchPath()
        particleSearchPath.appendDirectory(Filename('/phase_3.5/etc'))
        particleSearchPath.appendDirectory(Filename('/phase_4/etc'))
        particleSearchPath.appendDirectory(Filename('/phase_5/etc'))
        particleSearchPath.appendDirectory(Filename('/phase_8/etc'))
        particleSearchPath.appendDirectory(Filename('/phase_9/etc'))

    pfile = Filename(name)
    found = vfs.resolveFilename(pfile, particleSearchPath)
    if not found:
        notify.warning('loadParticleFile() - no path: %s' % name)
        return
    notify.debug('Loading particle file: %s' % pfile)
    effect = ParticleEffect()
    effect.loadConfig(pfile)
    return effect


def createParticleEffect(name = None, file = None, numParticles = None, color = None):
    if not name:
        fileName = file + '.ptf'
        return loadParticleFile(fileName)
    if name == 'GearExplosion':
        return __makeGearExplosion(numParticles)
    elif name == 'BigGearExplosion':
        return __makeGearExplosion(numParticles, 'Big')
    elif name == 'WideGearExplosion':
        return __makeGearExplosion(numParticles, 'Wide')
    elif name == 'BrainStorm':
        return loadParticleFile('brainStorm.ptf')
    elif name == 'BuzzWord':
        return loadParticleFile('buzzWord.ptf')
    elif name == 'Calculate':
        return loadParticleFile('calculate.ptf')
    elif name == 'Confetti':
        return loadParticleFile('confetti.ptf')
    elif name == 'DemotionFreeze':
        return loadParticleFile('demotionFreeze.ptf')
    elif name == 'DemotionSpray':
        return loadParticleFile('demotionSpray.ptf')
    elif name == 'DoubleTalkLeft':
        return loadParticleFile('doubleTalkLeft.ptf')
    elif name == 'DoubleTalkRight':
        return loadParticleFile('doubleTalkRight.ptf')
    elif name == 'FingerWag':
        return loadParticleFile('fingerwag.ptf')
    elif name == 'FiredFlame':
        return loadParticleFile('firedFlame.ptf')
    elif name == 'FreezeAssets':
        return loadParticleFile('freezeAssets.ptf')
    elif name == 'GlowerPower':
        return loadParticleFile('glowerPowerKnives.ptf')
    elif name == 'HotAir':
        return loadParticleFile('hotAirSpray.ptf')
    elif name == 'PoundKey':
        return loadParticleFile('poundkey.ptf')
    elif name == 'ShiftSpray':
        return loadParticleFile('shiftSpray.ptf')
    elif name == 'ShiftLift':
        return __makeShiftLift()
    elif name == 'Shred':
        return loadParticleFile('shred.ptf')
    elif name == 'Smile':
        return loadParticleFile('smile.ptf')
    elif name == 'SpriteFiredFlecks':
        return loadParticleFile('spriteFiredFlecks.ptf')
    elif name == 'Synergy':
        return loadParticleFile('synergy.ptf')
    elif name == 'Waterfall':
        return loadParticleFile('waterfall.ptf')
    elif name == 'FloodSynergy':
        return loadParticleFile('flood_synergy.ptf')
    elif name == 'FloodWaterfall':
        return loadParticleFile('flood_synergyWaterfall.ptf')
    elif name == 'PoundKey':
        return loadParticleFile('poundkey.ptf')
    elif name == 'RubOut':
        return __makeRubOut(color)
    elif name == 'SplashLines':
        return loadParticleFile('splashlines.ptf')
    elif name == 'Withdrawal':
        return loadParticleFile('withdrawal.ptf')
    else:
        notify.warning('createParticleEffect() - no name: %s' % name)
    return None


def setEffectTexture(effect, name, color = None):
    particles = effect.getParticlesNamed('particles-1')
    np = getParticle(name)
    if color:
        particles.renderer.setColor(color)
    particles.renderer.setFromNode(np)


def __makeGearExplosion(numParticles = None, style = 'Normal'):
    if style == 'Normal':
        effect = loadParticleFile('gearExplosion.ptf')
    elif style == 'Big':
        effect = loadParticleFile('gearExplosionBig.ptf')
    elif style == 'Wide':
        effect = loadParticleFile('gearExplosionWide.ptf')
    if numParticles:
        particles = effect.getParticlesNamed('particles-1')
        particles.setPoolSize(numParticles)
    return effect


def __makeRubOut(color = None):
    effect = loadParticleFile('demotionUnFreeze.ptf')
    loadParticles()
    setEffectTexture(effect, 'snow-particle')
    particles = effect.getParticlesNamed('particles-1')
    particles.renderer.setInitialXScale(0.03)
    particles.renderer.setFinalXScale(0.0)
    particles.renderer.setInitialYScale(0.02)
    particles.renderer.setFinalYScale(0.0)
    if color:
        particles.renderer.setColor(color)
    else:
        particles.renderer.setColor(Vec4(0.54, 0.92, 0.32, 0.7))
    return effect


def __makeShiftLift():
    effect = loadParticleFile('pixieDrop.ptf')
    particles = effect.getParticlesNamed('particles-1')
    particles.renderer.setCenterColor(Vec4(1, 1, 0, 0.9))
    particles.renderer.setEdgeColor(Vec4(1, 1, 0, 0.6))
    particles.emitter.setRadius(0.01)
    effect.setHpr(0, 180, 0)
    effect.setPos(0, 0, 0)
    return effect

def raindisk(self):
    self.reset()
    self.setPos(0.0, 5.0, 50.0)
    self.setHpr(0.0, 0.0, 0.0)
    self.setScale(1.0, 1.0, 1.0)
    p0 = Particles.Particles('particles-1')
    p0.setFactory('PointParticleFactory')
    p0.setRenderer('LineParticleRenderer')
    p0.setEmitter('DiscEmitter')
    p0.setPoolSize(3072)
    p0.setBirthRate(0.02)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    p0.factory.setLifespanBase(1.0)
    p0.factory.setLifespanSpread(0.0)
    p0.factory.setMassBase(1.0)
    p0.factory.setMassSpread(0.0)
    p0.factory.setTerminalVelocityBase(400.0)
    p0.factory.setTerminalVelocitySpread(0.0)
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.0)
    p0.renderer.setHeadColor(Vec4(0.39, 0.39, 0.58, 0.49))
    p0.renderer.setTailColor(Vec4(0.39, 0.39, 0.39, 0.29))
    p0.renderer.setLineScaleFactor(1.7)
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.2)
    p0.emitter.setAmplitudeSpread(0.0)
    p0.emitter.setOffsetForce(Vec3(11.3, 0.0, -41.0))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
    p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
    p0.emitter.setRadius(100.0)
    self.addParticles(p0)