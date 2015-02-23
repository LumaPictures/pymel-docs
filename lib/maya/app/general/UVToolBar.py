import inspect
import PySide.QtGui as _QtGui

from maya.app.general.UVMoveSewBar import *

from maya.app.general.UVNudgeBar import UVNudgeBar
from maya.app.general.UVEditBar import UVEditBar
from maya.app.general.UVDisplay3Bar import UVDisplay3Bar
from maya.app.general.UVDisplay1Bar import UVDisplay1Bar
from maya.app.general.UVDisplay2Bar import UVDisplay2Bar
from maya.app.general.UVMiscBar import UVMiscBar
from maya.app.general.UVCopyPasteBar import UVCopyPasteBar
from maya.app.general.UVFlipRotateBar import UVFlipRotateBar
from maya.app.general.UVAlignBar import UVAlignBar
from maya.app.general.UVIsolateSelectBar import UVIsolateSelectBar

class UVToolBar(_QtGui.QToolBar):
    def __init__(self):
        pass
    
    
    def createNewSubBar(self):
        pass
    
    
    def onToolBarOrientationChange(self, orientation):
        """
        #Code to fix resize on orientation change
        if(orientation == Qt.Horizontal):
            self.setMinimumWidth(self.width)
            self.setMinimumHeight(self.height)
        else:
            self.setMinimumWidth(self.height)
            self.setMinimumHeight(self.width)
        """
    
        pass
    
    
    staticMetaObject = None



SEPARATOR_SHORT = 7

UI_SEPARATOR_CLOSE_HOR = '/Applications/Autodesk/maya2016/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python2.7/site-packages/maya/app/general/UIAssets/textureEditorCloseBarH.png'

UI_SEPARATOR_OPEN_VERT = '/Applications/Autodesk/maya2016/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python2.7/site-packages/maya/app/general/UIAssets/textureEditorOpenBarV.png'

UI_ICON_PATH = 'C:/t_cheus/clients/mainline/Maya/src/PolyUISlice/UI/bitmaps/'

SEPARATOR_LONG = 56

UI_SEPARATOR_OPEN_HOR = '/Applications/Autodesk/maya2016/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python2.7/site-packages/maya/app/general/UIAssets/textureEditorOpenBarH.png'

BUTTON_SYTLE = 'QToolButton{border: 0px solid black;};'

ICON_HEIGHT = 25

UI_SEPARATOR_CLOSE_VERT = '/Applications/Autodesk/maya2016/Maya.app/Contents/Frameworks/Python.framework/Versions/Current/lib/python2.7/site-packages/maya/app/general/UIAssets/textureEditorCloseBarV.png'


