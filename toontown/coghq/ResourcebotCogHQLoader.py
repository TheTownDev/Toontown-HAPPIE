from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from . import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
from .resourcebot import BoardOfficeInterior
from . import ResourcebotHQExterior
from . import ResourcebotHQBossBattle
from . import ResourcebotOfficeExterior
from panda3d.core import Fog, VirtualFileSystem
from .LawbotOfficeExterior_Action00 import GlobalEntities
from toontown.content_pack import MusicManagerGlobals
import json
aspectSF = 0.7227

class ResourcebotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('ResourcebotCogHQLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('boardofficeInterior', self.enterboardofficeInterior, self.exitboardofficeInterior, ['quietZone', 'cogHQExterior']))
        self.fsm.addState(State.State('factoryExterior', self.enterFactoryExterior, self.exitFactoryExterior, ['quietZone', 'cogHQExterior']))
        for stateName in ['start', 'cogHQExterior', 'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('boardofficeInterior')

        for stateName in ['quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryExterior')

        fileSystem = VirtualFileSystem.getGlobalPtr()
        self.musicJson = json.loads(fileSystem.readFile(ToontownGlobals.musicJsonFilePath, True))
        self.cogHQExteriorModelPath = 'phase_15/models/resourcebotHQ/ttr_m_ara_rhq_bourgeoisieParisCenter'
        self.factoryExteriorModelPath = 'phase_11/models/lawbotHQ/ttr_m_ara_lhq_daLobby.egg'
        self.cogHQLobbyModelPath = 'phase_11/models/lawbotHQ/LB_CH_Lobby'
        self.officeExtModels = []
        self.room = GlobalEntities
        self.geom = None
        return

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()

    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)
        return

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        self.notify.debug('zoneId = %d ToontownGlobals.ResourcebotHQ=%d' % (zoneId, ToontownGlobals.ResourcebotHQ))
        if zoneId == ToontownGlobals.ResourcebotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            self.geom.setY(0)
            self.geom.setX(0)

            self.musicCode = MusicManagerGlobals.GLOBALS[zoneId]['music']
            self.battleMusicCode = MusicManagerGlobals.GLOBALS[zoneId]['battleMusic']

            ug = self.geom.find('**/underground')
            ug.setBin('ground', -10)
            brLinkTunnel = self.geom.find('**/TunnelEntrance1')
            brLinkTunnel.setName('linktunnel_br_3326_DNARoot')
            for prop in self.officeExtModels:
                prop.removeNode()
        elif zoneId == ToontownGlobals.ResourcebotFieldCenter:
            self.geom = loader.loadModel(self.factoryExteriorModelPath)
            self.geom.setY(0)
            self.geom.setX(0)

            self.musicCode = MusicManagerGlobals.GLOBALS[zoneId]['music']
            self.battleMusicCode = MusicManagerGlobals.GLOBALS[zoneId]['battleMusic']

            ug = self.geom.find('**/underground')
            ug.setBin('ground', -10)
            self.makeOfficeProps()
        elif zoneId == ToontownGlobals.ResourcebotCapitalLobby:
            if base.config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit ResourcebotLobby')
            self.notify.debug('cogHQLobbyModelPath = %s' % self.cogHQLobbyModelPath)
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
            self.geom.setY(0)
            self.geom.setX(0)

            self.musicCode = MusicManagerGlobals.GLOBALS[zoneId]['music']
            self.battleMusicCode = MusicManagerGlobals.GLOBALS[zoneId]['battleMusic']

            ug = self.geom.find('**/underground')
            ug.setBin('ground', -10)
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadSellbotHQAnims()
    
    def makeOfficeProps(self):
        for entity in self.room:
            if self.room[entity]['type'] == 'model':
                modelName = self.room[entity]['modelPath']

                if 'modelPart' in self.room[entity]:
                    model = loader.loadModel(modelName).find(self.room[entity]['modelPart'])
                else:
                    model = loader.loadModel(modelName)
                model.reparentTo(render)
                model.setPos(self.room[entity]['pos'])
                model.setHpr(self.room[entity]['hpr'])
                model.setScale(self.room[entity]['scale'])
                self.officeExtModels.append(model)

    def enterboardofficeInterior(self, requestStatus):
        self.placeClass = BoardOfficeInterior.BoardOfficeInterior
        self.boardofficeId = requestStatus['boardofficeId']
        self.enterPlace(requestStatus)

    def exitboardofficeInterior(self):
        self.exitPlace()
        self.placeClass = None
        return

    def getExteriorPlaceClass(self):
        self.notify.debug('getExteriorPlaceClass')
        return ResourcebotHQExterior.ResourcebotHQExterior

    def getBossPlaceClass(self):
        self.notify.debug('getBossPlaceClass')
        return ResourcebotHQBossBattle.ResourcebotHQBossBattle

    def enterFactoryExterior(self, requestStatus):
        self.placeClass = ResourcebotOfficeExterior.ResourcebotOfficeExterior
        self.enterPlace(requestStatus)
        self.hood.spawnTitleText(requestStatus['zoneId'])

    def exitFactoryExterior(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None
        return

    def enterCogHQBossBattle(self, requestStatus):
        self.notify.debug('ResourcebotCogHQLoader.enterCogHQBossBattle')
        CogHQLoader.CogHQLoader.enterCogHQBossBattle(self, requestStatus)
        base.cr.forbidCheesyEffects(1)

    def exitCogHQBossBattle(self):
        self.notify.debug('ResourcebotCogHQLoader.exitCogHQBossBattle')
        CogHQLoader.CogHQLoader.exitCogHQBossBattle(self)
        base.cr.forbidCheesyEffects(0)
