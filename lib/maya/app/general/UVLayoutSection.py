import sys
from . import UVGenericSection as _UVGenericSection
import maya.cmds as cmds
import os
import maya.mel as mel
import re

from PySide.QtCore import *
from PySide.QtGui import *

from maya.app.general.UVGenericSection import UVGenericSection
from random import randint

class UVLayoutSection(UVGenericSection):
    def __init__(self):
        pass
    
    
    def arrangeCmd(self):
        pass
    
    
    def createLayout(self):
        pass
    
    
    def createPlacement(self):
        pass
    
    
    def createScaleRotate(self):
        pass
    
    
    def createSpacing(self):
        pass
    
    
    def placementSettingsCmd(self):
        pass
    
    
    staticMetaObject = None



CHECKBOX_STYLE = 'QCheckBox{\n                }'


