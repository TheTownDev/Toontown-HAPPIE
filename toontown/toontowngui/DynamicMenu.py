from panda3d.core import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.directnotify.DirectNotifyGlobal import directNotify

from . import DynamicMenuGlobals


class DynamicMenu:
    """
    Container class for dynamic menu instances.
    """
    notify = directNotify.newCategory('DynamicMenu')

    def __init__(self, menuType=0):
        self.menuType = menuType
        self.menuData = DynamicMenuGlobals.MenuData[menuType]
        self.menuObjects = {}
        self.currCategory = -1
        self.inTransition = False
        self.activeSeq = None
        self.buildFromData()
        self.switchCategories(0, forceSmooth=False)

    def buildFromData(self):
        for objKw, objData in list(self.menuData.items()):
            # Some others, such as categories, will be included but aren't necessarily object IDs, or ints.
            if not isinstance(objKw, int):
                continue

            # Ignore duplicate object IDs.
            if objKw in self.menuObjects:
                self.notify.warning('duplicate ID for menu object: %s.' % objKw)
                continue

            # Grab what kind of object it is. Panel, button, etc.
            objType = objData['type']
            if objType not in Object2Class:
                self.notify.warning('invalid menu object type: %s.' % objType)
                continue

            # Grab the actual class representing this object.
            objClass = Object2Class[objType]
            # Create the optiondefs for this object based on the definition.
            optiondefs = tuple((keyword, value, None) for keyword, value in list(objData.items()) if keyword not in DynamicMenuGlobals.SpecialArgs)
            menuObj = objClass(self, objKw, objType, objData, optiondefs)

            # Store it
            self.menuObjects[objKw] = menuObj

        # All objects require this.
        for obj in list(self.menuObjects.values()):
            obj.initialiseoptions(obj.__class__)
            obj.handleSpecialArgs()

    def switchCategories(self, category, forceSmooth=None):
        categoryKw = 'menu_category_%s' % category
        # Validate this menu category.
        if categoryKw not in self.menuData:
            self.notify.warning('invalid menu category specified: %s' % category)
            return
        # No need to change to a category we're already in.
        if category == self.currCategory:
            self.notify.debug('ignoring category request: %s. already in category.' % category)
            return
        # Can't change categories while actively changing to another one already.
        if self.inTransition:
            self.notify.debug("ignoring category request: %s. we're moving to another one." % category)
            return

        # Clean up the active movement sequence if there is one.
        self.cleanupActiveSeq()

        categoryData = self.menuData[categoryKw]
        self.currCategory = category
        self.inTransition = True
        self.activeSeq = Parallel()
        for objId in categoryData:
            obj = self.menuObjects[objId]
            objSeq = Parallel()
            objData = categoryData[objId]
            # Check if we need smoothing.
            # If 'smooth' is not included in the definition, smooth by default.
            wantSmooth = ('smooth' not in objData or (objData['smooth'])) and not (forceSmooth is not None and not forceSmooth)
            # Update pos of objects.
            if 'pos' in objData:
                smoothSeq = LerpPosInterval(obj, DynamicMenuGlobals.SmoothTime, objData['pos']) if wantSmooth else Func(obj.setPos, objData['pos'])
                objSeq.append(smoothSeq)
            # Update scale of objects.
            if 'scale' in objData:
                smoothSeq = LerpScaleInterval(obj, DynamicMenuGlobals.SmoothTime, objData['scale']) if wantSmooth else Func(obj.setScale, objData['scale'])
                objSeq.append(smoothSeq)
            # Hide/Show objects.
            if 'wantShow' in objData:
                if objData['wantShow']:
                    smoothSeq = LerpColorScaleInterval(obj, DynamicMenuGlobals.SmoothTime, (1, 1, 1, 1)) if wantSmooth else Sequence()
                    objSeq = Sequence(Func(obj.show), Parallel(smoothSeq, objSeq))
                else:
                    smoothSeq = LerpColorScaleInterval(obj, DynamicMenuGlobals.SmoothTime, (1, 1, 1, 0)) if wantSmooth else Sequence()
                    objSeq = Sequence(Parallel(objSeq, smoothSeq), Func(obj.hide))

            # Finally, add this object sequence to the parallel housing all object sequences.
            self.activeSeq.append(objSeq)
        self.activeSeq = Sequence(self.activeSeq, Func(self.setInTransition, False))
        self.activeSeq.start()

    def setInTransition(self, inTransition):
        self.inTransition = inTransition

    def cleanupActiveSeq(self):
        if self.activeSeq:
            self.activeSeq.finish()
            self.activeSeq = None

    def destroy(self):
        self.cleanupActiveSeq()
        for obj in list(self.menuObjects.values()):
            obj.destroy()

        del self.menuType
        del self.menuData
        del self.menuObjects


class DynamicMenuObjectBase:
    """
    A base object used in dynamic menu instances.
    Dynamic menu objects will inherit from this object.
    """
    notify = directNotify.newCategory('DynamicMenuObjectBase')

    def __init__(self, container, objId, objType, objData, optiondefs):
        self.container = container
        self.objId = objId
        self.objType = objType
        self.objData = objData
        # Bit janky, but it works
        self.dynMenuDefineOptions(optiondefs)

    def dynMenuDefineOptions(self, optiondefs):
        for keyword in list(self.kwOptions.keys()):
            # Don't care about these if they have been replaced in the definition.
            if keyword in self.objData:
                del self.kwOptions[keyword]
        self.defineoptions(self.kwOptions, optiondefs)

    def handleSpecialArgs(self):
        # Get the parent object from the menu object ID if it exists.
        if 'parent' in self.objData:
            if isinstance(self.objData['parent'], int):
                # Handle invalid parent object IDs.
                if self.objData['parent'] not in self.container.menuObjects:
                    self.notify.warning('invalid parent object ID: %s' % self.objData['parent'])
                    return

                # Grab the parent object and reparent our object to it.
                parentObj = self.container.menuObjects[self.objData['parent']]
            else:
                parentObj = self.objData['parent']
            self.reparentTo(parentObj)

    def __str__(self):
        return 'objId: %s | objType: %s' % (self.objId, self.objType)


class DynamicPanel(DirectFrame, DynamicMenuObjectBase):
    """
    A panel used in dynamic menu instances.
    """
    notify = directNotify.newCategory('DynamicPanel')

    def __init__(self, container, objId, objType, objData, optiondefs):
        self.kwOptions = {'relief': None,
                          'image': DGG.getDefaultDialogGeom()}
        DynamicMenuObjectBase.__init__(self, container, objId, objType, objData, optiondefs)
        DirectFrame.__init__(self, parent=aspect2d)


class DynamicButton(DirectButton, DynamicMenuObjectBase):
    """
    A button used in dynamic menu instances.
    """
    notify = directNotify.newCategory('DynamicButton')

    validCommands = ('category', 'exit', 'messenger')

    def __init__(self, container, objId, objType, objData, optiondefs):
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        self.kwOptions = {'relief': None,
                          'image': (guiButton.find('**/QuitBtn_UP'),
                                    guiButton.find('**/QuitBtn_DN'),
                                    guiButton.find('**/QuitBtn_RLVR')),
                          'image_scale': DynamicMenuGlobals.ButtonImageScale,
                          'text_scale': DynamicMenuGlobals.ButtonTextScale,
                          'text_pos': DynamicMenuGlobals.ButtonTextPos}
        guiButton.removeNode()
        DynamicMenuObjectBase.__init__(self, container, objId, objType, objData, optiondefs)
        DirectButton.__init__(self)

    def handleSpecialArgs(self):
        DynamicMenuObjectBase.handleSpecialArgs(self)
        # If the button was given a command, construct it here.
        # Make sure the command given was a valid one.
        if 'command' in self.objData and self.objData['command'][0] in self.validCommands:
            # Grab the command type
            comType = self.objData['command'][0]
            # All handled through lambdas, as they need to trigger when the button is pressed.
            if comType == 'category':
                # Find the category number and then switch categories.
                categoryNum = self.objData['command'][1]
                self['command'] = lambda: self.container.switchCategories(categoryNum)
            elif comType == 'exit':
                # Simple exit, just destroy all gui pieces.
                self['command'] = lambda: self.container.destroy()
            elif comType == 'messenger':
                # Split into message to send and its arguments.
                message = self.objData['command'][1][0]
                extraArgs = self.objData['command'][1][1]
                self['command'] = lambda: messenger.send(message, extraArgs)
            else:
                self.notify.warning('invalid button command type: %s' % comType)


class DynamicLabel(DirectLabel, DynamicMenuObjectBase):
    """
    A label used in dynamic menu instances.
    """
    notify = directNotify.newCategory('DynamicLabel')

    def __init__(self, container, objId, objType, objData, optiondefs):
        self.kwOptions = {'relief': None,
                          'text': 'No text',
                          'text_scale': 0.12}
        DynamicMenuObjectBase.__init__(self, container, objId, objType, objData, optiondefs)
        DirectLabel.__init__(self, parent=aspect2d)


Object2Class = {DynamicMenuGlobals.DM_OBJ_PANEL: DynamicPanel,
                DynamicMenuGlobals.DM_OBJ_BUTTON: DynamicButton,
                DynamicMenuGlobals.DM_OBJ_TEXT: DynamicLabel}
