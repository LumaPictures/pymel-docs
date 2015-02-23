import sys
import maya.cmds as cmds
import os
import maya.mel as mel
import re
from . import UVSubSideBar as _UVSubSideBar

from PySide.QtCore import *
from PySide.QtGui import *

from random import randint
from maya.app.general.UVPinSection import UVPinSection
from maya.app.general.UVSubSideBar import UVSubSideBar
from maya.app.general.UVCutSection import UVCutSection
from maya.app.general.UVSewSection import UVSewSection

class UVSeamSide(UVSubSideBar):
    def __init__(self):
        pass
    
    
    staticMetaObject = None



