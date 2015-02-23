import pymel as _pymel
import pymel.api.plugins as _plugins
import pymel.internal.pmcmds as _pmcmds
import pymel.internal.cmdcache as _cmdcache
import pymel.versions as _versions
from . import uitypes as ui
from . import uitypes
from . import runtime
import pymel.internal.factories as _factories
from . import nodetypes
from . import nodetypes as nt
import maya.cmds as cmds
from . import datatypes as dt
import pymel.internal as _internal
import pymel.internal.startup as _startup
import pymel.api as _api
import pymel.api as api

from pymel.core.other import *
from pymel.core.general import *
from pymel.core.rendering import *
from pymel.core.system import *
from pymel.core.language import *
from pymel.core.windows import *
from pymel.core.effects import *
from pymel.core.modeling import *
from pymel.core.context import *
from pymel.core.animation import *

def _addPluginCommand(pluginName, funcName):
    pass


def _removePluginCommand(pluginName, command):
    pass


def _removePluginNode(pluginName, node):
    pass


def _addPluginNode(pluginName, mayaType):
    pass


def _pluginLoaded(*args):
    pass


def _pluginUnloaded(*args):
    pass


def _installCallbacks():
    """
    install the callbacks that trigger new nodes and commands to be added to pymel when a
    plugin loads.  This is called from pymel.__init__
    """

    pass



_pluginLoadedCB = True

_pluginData = {}

_logger = None


