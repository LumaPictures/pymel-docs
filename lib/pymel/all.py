import pymel.internal.plogging as plogging
import pymel as _pymel
from . import core
import pymel.core.effects as effects
from . import mayautils
import pymel.core.language as language
import pymel.core.windows as windows
import pymel.core.runtime as runtime
import pymel.core.rendering as rendering
import maya.cmds as cmds
import pymel.core.context as context
import pymel.core.animation as animation
import pymel.core.nodetypes as nodetypes
import pymel.core.nodetypes as nt
import pymel.core.datatypes as dt
import pymel.internal.factories as factories
from . import tools
import pymel.core.uitypes as ui
import pymel.core.uitypes as uitypes
import pymel.core.modeling as modeling
from . import api

from pymel.core.other import *
from pymel.core.general import *
from pymel.core.rendering import *
from pymel.core.nodetypes import *
from pymel.core.system import *
from pymel.core.language import *
from pymel.core.context import *
from pymel.core.uitypes import *
from pymel.core.effects import *
from pymel.core.windows import *
from pymel.core.modeling import *
from pymel.util.arrays import *
from pymel.core.animation import *

class LazyLoader(object):
    """
    A data descriptor that delays instantiation of an object
    until it is first accessed.
    """
    
    
    
    def __get__(self, obj, objtype):
        pass
    
    
    def __init__(self, name, creator, *creatorArgs, **creatorKwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



doFinalize = True


