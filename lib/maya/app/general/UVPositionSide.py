import sys
import maya.cmds as cmds
import os
import maya.mel as mel
import re
from . import UVSubSideBar as _UVSubSideBar

from PySide.QtCore import *
from PySide.QtGui import *

from maya.app.general.UVCoordSpaceSection import UVCoordSpaceSection
from maya.app.general.UVSubSideBar import UVSubSideBar
from maya.app.general.UVPositionSection import UVPositionSection
from random import randint

class UVPositionSide(UVSubSideBar):
    def __init__(self):
        pass
    
    
    def updateLayout(self):
        pass
    
    
    staticMetaObject = None



