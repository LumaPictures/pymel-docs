"""
Bookmarks are saved using the special node nodeGraphEditorBookmarkInfo.

Each Node Editor Bookmark is represented by a nodeGraphEditorBookmarkInfo which stores the bookmark info, i.e. the view state and the graph state, including the state of each individual node in the scene.
"""

import maya.cmds as cmds
import maya
import re

from functools import partial

class NodeEditorBookmarksWindow(object):
    """
    Tracks the state of the Bookmarks window UI
    """
    
    
    
    def __init__(self, ned):
        pass
    
    
    def reset(self):
        pass
    
    
    def selectLastLoadedInfo(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None



def _deleteBookmarks(infos):
    pass


def _getBookmarkInfos():
    pass


def _getDescriptionForInfo(bookmarkInfo):
    pass


def _renameBookmark(info, name):
    pass


def addCallback(ned):
    """
    called when a panel is added
    """

    pass


def createBookmark(ned, *args):
    """
    create a new bookmark
    """

    pass


def _getBookmarkName(name):
    pass


def _getNextBookmark(ned, incr):
    pass


def _getInstance():
    pass


def showWindow(ned, *args):
    """
    Show the Bookmarks window.  If it already exists, re-build it
    """

    pass


def buildToolbar(ned):
    """
    builds the bookmarking toolbar elmenets for the given editor
    """

    pass


def loadPreviousBookmark(ned):
    """
    load the previous bookmark, based on alphabetical ordering of bookmarks
    """

    pass


def loadNextBookmark(ned):
    """
    load the next bookmark, based on alphabetical ordering of bookmarks
    """

    pass


def renameBookmark(ned, oldname, info, *args):
    """
    Rename the supplied bookmark, given the old name
    """

    pass


def loadBookmark(ned, info, *args):
    """
    apply the supplied bookmark
    """

    pass


def buildMenu(ned):
    """
    builds the Bookmarks menu for the panel menuBar
    """

    pass


def removeCallback(ned=None):
    """
    called when the owning panel is removed, and on file-new
    """

    pass


def _naturalKey(str_):
    pass


def _refreshWindow():
    pass



_instance = None

windowName = 'nodeEditorBookmarksWindow'

_panelInfos = {}


