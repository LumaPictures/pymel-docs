import inspect
import PySide.QtGui as _QtGui

from maya.app.general.UVGroupSide import *

from maya.app.general.UVToolsSide import UVToolsSide
from maya.app.general.UVLayoutSide import UVLayoutSide
from maya.app.general.UVSeamSide import UVSeamSide
from maya.app.general.UVSelectionSide import UVSelectionSide
from maya.app.general.UVTranslateSide import UVTranslateSide
from maya.app.general.UVPositionSide import UVPositionSide

class UVSideBar(_QtGui.QDockWidget):
    def __init__(self):
        pass
    
    
    def dragEnterEvent(self, event):
        pass
    
    
    def dragMoveEvent(self, event):
        pass
    
    
    def dragWidgetHorizontalLayout(self, event):
        pass
    
    
    def dragWidgetVerticalLayout(self, event):
        pass
    
    
    def dropEvent(self, event):
        pass
    
    
    def onDockLocationChange(self, area):
        pass
    
    
    def onSubSideBarReattach(self, sideBar):
        pass
    
    
    def onSubSideBarTearOff(self, sideBar):
        pass
    
    
    staticMetaObject = None



UI_ICON_PATH = 'C:/t_cheus/clients/mainline/Maya/src/PolyUISlice/UI/bitmaps/'

BUTTON_SYTLE = 'QToolButton   {\n                                    border: 0px solid black;\n                                    margin: 0px;\n                                };'

ICON_HEIGHT = 15

ICON_WIDTH = ICON_HEIGHT

