import sys
import maya.cmds as cmds
import os
import maya.mel as mel
import re
from . import UVSubSideBar as _UVSubSideBar

from PySide.QtCore import *
from PySide.QtGui import *

from maya.app.general.UVSelectSection import UVSelectSection
from maya.app.general.UVSubSideBar import UVSubSideBar
from random import randint

class UVSelectionSide(UVSubSideBar):
    def __init__(self):
        pass
    
    
    staticMetaObject = None



