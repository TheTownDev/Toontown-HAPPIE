from panda3d.core import *
from direct.showbase.DirectObject import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals, ToontownBattleGlobals
from libotp import *


IVAL_TIME = 0.3


class ButtonContainer(DirectObject):
    """
    Houses multiple buttons in a visual "list" on screen.
    Can be either vertical or horizontal.
    TODO: Horizontal container
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('ButtonContainer')
    CONTAINER_ID = 0

    def __init__(self):
        DirectObject.__init__(self)
        self.containerNode = aspect2d.attachNewNode('buttonContainerNode-%s' % self.CONTAINER_ID)
        self.CONTAINER_ID += 1
        self.buttonList = []
        self.readjustIval = None

    @property
    def buttonSpacing(self):
        return 0.2

    def addButton(self, buttonClass, extraArgs=None):
        button = buttonClass(self, extraArgs)
        button.setColorScale(1, 1, 1, 0)
        button.reparentTo(self.containerNode)
        self.buttonList.append(button)
        button.setPos(0, 0, self.buttonList.index(button)*self.buttonSpacing)
        self.doReadjustIval()

    def buttonDismissed(self, button):
        if button not in self.buttonList:
            self.notify.debug('button clicked that was not in list.')
            return

        self.buttonList.remove(button)
        self.doReadjustIval()

    def cleanupReadjustIval(self):
        if self.readjustIval:
            self.readjustIval.pause()
            self.readjustIval = None

    def doReadjustIval(self):
        # Pause and delete the existing ival before creating the new one.
        self.cleanupReadjustIval()
        self.readjustIval = Parallel()
        for i, button in enumerate(self.buttonList):
            buttonTrack = Parallel(
                LerpPosInterval(button, IVAL_TIME, (0, 0, i*self.buttonSpacing), blendType='easeIn'),
                # Include this color scale in case this adjust ival was previously interrupted.
                # Also helps in the case of a button appearing for the first time.
                LerpColorScaleInterval(button, IVAL_TIME, (1, 1, 1, 1), blendType='easeIn')
            )
            self.readjustIval.append(buttonTrack)

        self.readjustIval.start()

    def cleanup(self):
        self.cleanupReadjustIval()

        for button in self.buttonList:
            button.cleanup()
        self.buttonList = []
        self.containerNode.removeNode()


class ButtonContainerButton(DirectButton):
    """
    Button used in ButtonContainer instances.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('ButtonContainerButton')

    BUTTON_TEXT = 'omg it is so happie'

    def __init__(self, container, extraArgs, **kwargs):
        DirectButton.__init__(self,
                              parent=container.containerNode,
                              relief=None,
                              command=self.handleClicked,
                              **kwargs)
        self.initialiseoptions(self.__class__)
        self.container = container
        # Data passed through for child button classes.
        self.extraArgs = extraArgs or []
        self.hoverObj = None
        self['state'] = DGG.NORMAL
        self.bind(DGG.WITHIN, self.hover)
        self.bind(DGG.WITHOUT, self.cleanupHover)
        self.dismissIval = None
        self.dismissed = False
        self.speech3d = ChatBalloon(loader.loadModel('phase_3/models/props/chatbox').node())
        self.newBubble = self.speech3d.generate(self.BUTTON_TEXT, ToontownGlobals.getInterfaceFont(), 10, Vec4(0, 0, 0, 1), Vec4(1, 1, 1, 1), 0, 0, 0, NodePath(), 0, 0, NodePath())
        self.newBubbleNP = self.attachNewNode(self.newBubble)
        self.newBubbleNP.setScale(0.05)
        self.newBubbleNP.hide()
        self.bind(DGG.WITHOUT, self.hover_command, [False])
        self.bind(DGG.WITHIN, self.hover_command, [True])

    def hover_command(self, hover, frame):
        if hover:
            self.newBubbleNP.show()
        else:
            self.newBubbleNP.hide()

    def handleClicked(self):

        if self.dismissed:
            return

        self.dismissed = True
        self.dismissIval = Sequence(
            LerpColorScaleInterval(self, IVAL_TIME, (1, 1, 1, 0), blendType='easeIn'),
            Func(self.cleanup)
        )
        self.container.buttonDismissed(self)
        self.dismissIval.start()

    def hover(self, _):
        raise NotImplementedError('ButtonContainerButton hover()')  # Must subclass

    def cleanupHover(self, _):
        raise NotImplementedError('ButtonContainerButton cleanupHover()')  # Must subclass

    def cleanup(self):
        self.unbind(DGG.WITHIN)
        self.unbind(DGG.WITHOUT)
        if self.dismissIval:
            self.dismissIval.finish()
            del self.dismissIval

        del self.container
        del self.extraArgs
        if self.hoverObj:
            self.hoverObj.cleanup()
        del self.hoverObj

        if self.speech3d:
            self.newBubbleNP.removeNode()
            del self.speech3d

        DirectButton.destroy(self)


class GagExpButton(ButtonContainerButton):
    """
    Button used for Gag Exp info in the reward panel.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('GagExpButton')

    BUTTON_TEXT = 'omg it is so happie'

    def __init__(self, container, extraArgs):
        model = loader.loadModel('phase_3.5/models/gui/ttr_m_gui_bat_statusEffect')
        circle = model.find('**/ttr_t_gui_bat_statusEffect_cog')
        invIcons = loader.loadModel('phase_3.5/models/gui/inventory_icons')
        pieIcon = invIcons.find('**/inventory_tart')
        pieIcon.setScale(4)
        pieIcon.setPos(-0.01, 0, 0.01)
        pieIcon.reparentTo(circle)
        model.removeNode()
        invIcons.removeNode()
        circle.setColor(tuple(list(ToontownBattleGlobals.TrackColors[ToontownBattleGlobals.THROW_TRACK]) + [1]))
        pieIcon.setColor(1, 1, 1, 1)
        self.BUTTON_TEXT = 'omg it is so happie'
        ButtonContainerButton.__init__(self,
                                       container,
                                       extraArgs,
                                       image=circle,
                                       image_scale=0.04)

    def hover(self, _):
        pass

    def cleanupHover(self, _):
        pass


class MeritButton(ButtonContainerButton):
    """
    Button used for Merit info in the reward panel.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('DisguisePartButton')
    SWITCH_TIME = 1.0

    BUTTON_TEXT = 'omg it is so happie'

    def __init__(self, container, extraArgs):
        self.index = 0
        self.BUTTON_TEXT = 'omg it is so happie'
        image = self.makeImage()
        ButtonContainerButton.__init__(self,
                                       container,
                                       extraArgs,
                                       image=image,
                                       image_scale=0.04)
        self.switchTaskName = self.uniqueName('merit-button-swap-icons')
        taskMgr.doMethodLater(self.SWITCH_TIME, self.updateImage, self.switchTaskName)

    def makeImage(self):
        # Backwards so that it starts with sellbot
        cogTypes = ['**/SalesIcon', '**/MoneyIcon', '**/LegalIcon', '**/CorpIcon']
        model = loader.loadModel('phase_3.5/models/gui/ttr_m_gui_bat_statusEffect')
        circle = model.find('**/ttr_t_gui_bat_statusEffect_cog')
        cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
        cogIcon = cogIcons.find(cogTypes[self.index])
        cogIcon.setScale(4.0)
        cogIcon.setPos(-0.006, 0, 0.01)
        cogIcon.reparentTo(circle)
        plusText = TextNode('plus')
        plusText.setFont(ToontownGlobals.getSignFont())
        plusText.setTextColor(0, 1, 0, 1)
        plusText.setTextScale(0.15)
        plusText.setText('+')
        plusNode = circle.attachNewNode(plusText)
        plusNode.setPos(-0.08, 0, -0.05)
        model.removeNode()
        cogIcons.removeNode()
        circle.setColor(tuple(list(ToontownBattleGlobals.TrackColors[ToontownBattleGlobals.DROP_TRACK]) + [1]))
        cogIcon.setColor(1, 1, 1, 1)
        return circle

    def updateImage(self, task=None):
        self.index += 1
        if self.index == 4:
            self.index = 0

        image = self.makeImage()
        self['image'] = image
        return task.again

    def hover(self, _):
        pass

    def cleanupHover(self, _):
        pass

    def cleanup(self):
        taskMgr.remove(self.switchTaskName)
        del self.switchTaskName
        ButtonContainerButton.cleanup(self)


class DisguisePartButton(ButtonContainerButton):
    """
    Button used for Disguise Part info in the reward panel.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('DisguisePartButton')

    BUTTON_TEXT = 'omg it is so happie'

    def __init__(self, container, extraArgs):
        model = loader.loadModel('phase_3.5/models/gui/ttr_m_gui_bat_statusEffect')
        circle = model.find('**/ttr_t_gui_bat_statusEffect_cog')
        bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
        cogArm = bookModel.find('**/CogArmIcon2')
        cogArm.setScale(4.0)
        cogArm.setPos(-0.01, 0, 0.01)
        cogArm.reparentTo(circle)
        model.removeNode()
        bookModel.removeNode()
        circle.setColor(tuple(list(ToontownBattleGlobals.TrackColors[ToontownBattleGlobals.LURE_TRACK]) + [1]))
        cogArm.setColor(1, 1, 1, 1)
        self.BUTTON_TEXT = 'omg it is so happie'
        ButtonContainerButton.__init__(self,
                                       container,
                                       extraArgs,
                                       image=circle,
                                       image_scale=0.04)

    def hover(self, _):
        pass

    def cleanupHover(self, _):
        pass

class JellybeansGainButton(ButtonContainerButton):
    """
    Button used for Disguise Part info in the reward panel.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('DisguisePartButton')

    BUTTON_TEXT = 'omg it is so happie'

    def __init__(self, container, extraArgs):
        model = loader.loadModel('phase_3.5/models/gui/ttr_m_gui_bat_statusEffect')
        circle = model.find('**/ttr_t_gui_bat_statusEffect_cog')
        bookModel = loader.loadModel('phase_3.5/models/gui/jar_gui')
        cogArm = bookModel
        cogArm.setScale(4.0)
        cogArm.setPos(-0.01, 0, 0.01)
        cogArm.reparentTo(circle)
        model.removeNode()
        circle.setColor(tuple(list(ToontownBattleGlobals.TrackColors[ToontownBattleGlobals.LURE_TRACK]) + [1]))
        cogArm.setColor(1, 1, 1, 1)
        self.BUTTON_TEXT = extraArgs[0]
        ButtonContainerButton.__init__(self,
                                       container,
                                       extraArgs,
                                       image=circle,
                                       image_scale=0.04)

    def hover(self, _):
        pass

    def cleanupHover(self, _):
        pass


class QuestProgressButton(ButtonContainerButton):
    """
    Button used for quest progress info in the reward panel.
    """
    BUTTON_TEXT = 'omg it is so happie'

    notify = DirectNotifyGlobal.directNotify.newCategory('QuestProgressButton')

    def __init__(self, container, extraArgs):
        model = loader.loadModel('phase_3.5/models/gui/ttr_m_gui_bat_statusEffect')
        circle = model.find('**/ttr_t_gui_bat_statusEffect_cog')
        bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
        questCard = bookModel.find('**/package')
        questCard.setScale(0.1)
        questCard.setPos(-0.01, 0, 0.01)
        questCard.reparentTo(circle)
        model.removeNode()
        bookModel.removeNode()
        circle.setColor(tuple(list(ToontownBattleGlobals.TrackColors[ToontownBattleGlobals.TRAP_TRACK]) + [1]))
        questCard.setColor(1, 1, 1, 1)
        ButtonContainerButton.__init__(self,
                                       container,
                                       extraArgs,
                                       image=circle,
                                       image_scale=0.04)

    def hover(self, _):
        pass

    def cleanupHover(self, _):
        pass

class GoldSkelecogButton(ButtonContainerButton):
    """
    Button used for gold skelecog info in the battle gui.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('GoldSkelecogButton')
    SWITCH_TIME = 1.0

    BUTTON_TEXT = 'This cog\'s HP is equal to a cog two levels above.'

    def __init__(self, container, extraArgs):
        self.index = 0
        image = self.makeImage()
        ButtonContainerButton.__init__(self,
                                       container,
                                       extraArgs,
                                       image=image,
                                       image_scale=0.04)
        self.switchTaskName = self.uniqueName('merit-button-swap-icons')
        taskMgr.doMethodLater(self.SWITCH_TIME, self.updateImage, self.switchTaskName)

    def makeImage(self):
        cogTypes = '**/MoneyIcon'
        model = loader.loadModel('phase_3.5/models/gui/ttr_m_gui_bat_statusEffect')
        circle = model.find('**/ttr_t_gui_bat_statusEffect_cog')
        cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
        cogIcon = cogIcons.find(cogTypes)
        cogIcon.setScale(4.0)
        cogIcon.setPos(-0.006, 0, 0.01)
        cogIcon.reparentTo(circle)
        plusText = TextNode('plus')
        plusText.setFont(ToontownGlobals.getSignFont())
        plusText.setTextColor(0, 1, 0, 1)
        plusText.setTextScale(0.15)
        plusText.setText('+')
        plusNode = circle.attachNewNode(plusText)
        plusNode.setPos(-0.08, 0, -0.05)
        model.removeNode()
        cogIcons.removeNode()
        circle.setColor(tuple(list(ToontownBattleGlobals.TrackColors[ToontownBattleGlobals.DROP_TRACK]) + [1]))
        cogIcon.setColor(1, 1, 1, 1)
        return circle

    def updateImage(self, task=None):
        self.index += 1
        if self.index == 4:
            self.index = 0

        image = self.makeImage()
        self['image'] = image
        return task.again

    def hover(self, _):
        pass

    def cleanupHover(self, _):
        pass

    def cleanup(self):
        taskMgr.remove(self.switchTaskName)
        del self.switchTaskName
        ButtonContainerButton.cleanup(self)

class LureStatusButton(ButtonContainerButton):
    """
    Button used for Lure Gag info in the Battle GUI.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('LureStatusButton')

    BUTTON_TEXT = 'omg it is so happie'

    def __init__(self, container, extraArgs):
        model = loader.loadModel('phase_3.5/models/gui/ttr_m_gui_bat_statusEffect')
        circle = model.find('**/ttr_t_gui_bat_statusEffect_cog')
        invIcons = loader.loadModel('phase_3.5/models/gui/inventory_icons')
        pieIcon = invIcons.find('**/inventory_big_magnet')
        pieIcon.setScale(4)
        pieIcon.setPos(-0.01, 0, 0.01)
        pieIcon.reparentTo(circle)
        model.removeNode()
        invIcons.removeNode()
        circle.setColor(tuple(list(ToontownBattleGlobals.TrackColors[ToontownBattleGlobals.THROW_TRACK]) + [1]))
        pieIcon.setColor(1, 1, 1, 1)
        self.BUTTON_TEXT = extraArgs[0]
        ButtonContainerButton.__init__(self,
                                       container,
                                       extraArgs,
                                       image=circle,
                                       image_scale=0.04)

    def hover(self, _):
        pass

    def cleanupHover(self, _):
        pass