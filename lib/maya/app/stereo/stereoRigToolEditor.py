import maya.cmds as cmds
from . import stereoCameraErrors
import maya
import maya.mel as mel

def __buildCB(layout, func, control, param):
    pass


def __changeLang(layout, control, rig):
    pass


def __oneItem(layout, rig, definition, mode):
    """
    Build the UI for one rig
    """

    pass


def __buildCB2(layout, func, name, lang, create, cameraSet):
    pass


def __delete(layout, control, rig):
    pass


def __rebuildUI(layout):
    """
    Rebuild the complete UI after a tool was added or removed
    """

    pass


def buildMainToolUI():
    """
    Build the UI for this window
    """

    pass


def __changeCameraSetProcedure(layout, control, rig):
    pass


def __changeProcedure(layout, control, rig):
    pass


def customRigEditor():
    """
    Create the custom stereo rig editor window
    """

    pass


def __add(layout, nameBox, langMenu, createBox, createCamSet):
    pass


def rebuildUI(layout):
    """
    Rebuild the complete UI after a tool was added or removed. Using
    evalDeferred so that it can be attached to the UI controls.
    """

    pass



__mainWin = None


