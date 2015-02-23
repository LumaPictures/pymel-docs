"""
In particular, the system module contains the functionality of maya.cmds.file. The file command should not be imported into
the default namespace because it conflicts with python's builtin file class. Since the file command has so many flags,
we decided to kill two birds with one stone: by breaking the file command down into multiple functions -- one for each
primary flag -- the resulting functions are more readable and allow the file command's functionality to be used directly
within the pymel namespace.

for example, instead of this:

    >>> res = cmds.file( 'test.ma', exportAll=1, preserveReferences=1, type='mayaAscii', force=1 ) # doctest: +SKIP

you can do this:

    >>> expFile = exportAll( 'test.ma', preserveReferences=1, force=1)

some of the new commands were changed slightly from their flag name to avoid name clashes and to add to readability:

    >>> importFile( expFile )  # flag was called import, but that's a python keyword
    >>> ref = createReference( expFile )
    >>> ref # doctest: +ELLIPSIS
    FileReference(u'.../test.ma', refnode=u'testRN')

Notice that the 'type' flag is set automatically for you when your path includes a '.mb' or '.ma' extension.

Paths returned by these commands are either a `Path` or a `FileReference`, so you can use object-oriented path methods with
the results::

    >>> expFile.exists()
    True
    >>> expFile.remove() # doctest: +ELLIPSIS
    Path('.../test.ma')
"""

from . import general
import pymel.versions as versions
import pymel.internal.factories as _factories
import maya.OpenMaya as _OpenMaya
from . import other
import pymel.internal as _internal
import pymel.util as _util
import pymel.internal.pmcmds as cmds
import os
import maya.mel as _mel
import warnings
import sys

from pymel.util.path import path as pathClass
from pymel.util.decoration import decorator
from pymel.util.scanf import fscanf

class UndoChunk(object):
    """
    Context manager for encapsulating code in a single undo.
    
    Use in a with statement
    Wrapper for cmds.undoInfo(openChunk=1)/cmds.undoInfo(closeChunk=1)
    
    >>> import pymel.core as pm
    >>> pm.ls("MyNode*", type='transform')
    []
    >>> with pm.UndoChunk():
    ...     res = pm.createNode('transform', name="MyNode1")
    ...     res = pm.createNode('transform', name="MyNode2")
    ...     res = pm.createNode('transform', name="MyNode3")
    >>> pm.ls("MyNode*", type='transform')
    [nt.Transform(u'MyNode1'), nt.Transform(u'MyNode2'), nt.Transform(u'MyNode3')]
    >>> pm.undo() # Due to the undo chunk, all three are undone at once
    >>> pm.ls("MyNode*", type='transform')
    []
    """
    
    
    
    def __enter__(self):
        pass
    
    
    def __exit__(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class ReferenceEdit(str):
    """
    Parses a reference edit command string into various components based on the edit type.
    This is the class returned by pymel's version of the 'referenceQuery' command.
    """
    
    
    
    def remove(self, force=False):
        """
        Remove the reference edit. if 'force=True' then the reference will be unloaded from the scene (if it is not already unloaded)
        """
    
        pass
    
    
    def __new__(cls, editStr, fileReference=None, successful=None):
        pass
    
    
    __dict__ = None
    
    editData = None
    
    fullNamespace = None
    
    namespace = None
    
    rawEditData = None


class FileInfo(object):
    """
    store and get custom data specific to this file:
    
        >>> from pymel.all import *
        >>> fileInfo['lastUser'] = env.user()
    
    if the python structures have valid __repr__ functions, you can
    store them and reuse them later:
    
        >>> fileInfo['cameras'] = str( ls( cameras=1) )
        >>> camList = eval(fileInfo['cameras'])
        >>> camList[0]
        nt.Camera(u'frontShape')
    
    for backward compatibility it retains it's original syntax as well:
    
        >>> fileInfo( 'myKey', 'myData' )
    """
    
    
    
    def __call__(self, *args, **kwargs):
        pass
    
    
    def __contains__(self, item):
        pass
    
    
    def __delitem__(self, item):
        pass
    
    
    def __getitem__(self, item):
        pass
    
    
    def __init__(self, *p, **k):
        pass
    
    
    def __iter__(self):
        pass
    
    
    def __setitem__(self, item, value):
        pass
    
    
    def get(self, key, default=None):
        pass
    
    
    def has_key(self, item):
        pass
    
    
    def items(self):
        pass
    
    
    def keys(self):
        pass
    
    
    def pop(self, *args):
        pass
    
    
    def values(self):
        pass
    
    
    def __new__(cls, *p, **k):
        """
        # redefine __new__
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class WorkspaceEntryDict(object):
    def __contains__(self, key):
        pass
    
    
    def __getitem__(self, item):
        pass
    
    
    def __init__(self, entryType):
        pass
    
    
    def __iter__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def __setitem__(self, item, value):
        pass
    
    
    def get(self, item, default=None):
        pass
    
    
    def has_key(self, key):
        pass
    
    
    def items(self):
        pass
    
    
    def keys(self):
        pass
    
    
    def values(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class Namespace(unicode):
    """
    #===============================================================================
    # Namespace
    #===============================================================================
    """
    
    
    
    def __add__(self, other):
        pass
    
    
    def __cmp__(self, other):
        pass
    
    
    def __eq__(self, other):
        pass
    
    
    def __ge__(self, other):
        pass
    
    
    def __gt__(self, other):
        pass
    
    
    def __le__(self, other):
        pass
    
    
    def __lt__(self, other):
        pass
    
    
    def __ne__(self, other):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def clean(self, haltOnError=True, reparentOtherChildren=True):
        """
        Deletes all nodes in this namespace
        
        Parameters
        ----------
        haltOnError : bool
            If true, and reparentOtherChildren is set, and there is an error in
            reparenting, then raise an Exception (no rollback is performed);
            otherwise, ignore the failed reparent, and continue
        reparentOtherChildren : bool
            If True, then if any transforms in this namespace have children NOT
            in this namespace, then will attempt to reparent these children
            under world (errors during these reparenting attempts is controlled
            by haltOnError)
        """
    
        pass
    
    
    def getNode(self, nodeName, verify=True):
        pass
    
    
    def getParent(self):
        pass
    
    
    def listNamespaces(self, recursive=False, internal=False):
        """
        List the namespaces contained within this namespace.
        
        :parameters:
        recursive : `bool`
            Set to True to enable recursive search of sub (and sub-sub, etc)
            namespaces
        internal : `bool`
            By default, this command filters out certain automatically created
            maya namespaces (ie, :UI, :shared); set to True to show these
            internal namespaces as well
        """
    
        pass
    
    
    def listNodes(self, recursive=False, internal=False):
        """
        List the nodes contained within this namespace.
        
        :parameters:
        recursive : `bool`
            Set to True to enable recursive search of sub (and sub-sub, etc)
            namespaces
        internal : `bool`
            By default, this command filters out nodes in certain automatically
            created maya namespaces (ie, :UI, :shared); set to True to show
            these internal namespaces as well
        """
    
        pass
    
    
    def ls(self, pattern='*', **kwargs):
        pass
    
    
    def move(self, other, force=False):
        pass
    
    
    def remove(self, haltOnError=True, reparentOtherChildren=True):
        """
        Removes this namespace
        
        Recursively deletes any nodes and sub-namespaces
        
        Parameters
        ----------
        haltOnError : bool
            If true, and reparentOtherChildren is set, and there is an error in
            reparenting, then raise an Exception (no rollback is performed);
            otherwise, ignore the failed reparent, and continue
        reparentOtherChildren : bool
            If True, then if any transforms in this namespace have children NOT
            in this namespace, then will attempt to reparent these children
            under world (errors during these reparenting attempts is controlled
            by haltOnError)
        """
    
        pass
    
    
    def setCurrent(self):
        pass
    
    
    def shortName(self):
        pass
    
    
    def splitAll(self):
        pass
    
    
    def create(cls, name):
        pass
    
    
    def getCurrent(cls):
        pass
    
    
    def __new__(cls, namespace, create=False):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class FileReference(object):
    """
    A class for manipulating references which inherits Path and path.  you can create an
    instance by supplying the path to a reference file, its namespace, or its reference node to the
    appropriate keyword. The namespace and reference node of the reference can be retreived via
    the namespace and refNode properties. The namespace property can also be used to change the namespace
    of the reference.
    
    Use listReferences command to return a list of references as instances of the FileReference class.
    
    It is important to note that instances of this class will have their copy number stripped off
    and stored in an internal variable upon creation.  This is to maintain compatibility with the numerous methods
    inherited from the path class which requires a real file path. When calling built-in methods of FileReference,
    the path will automatically be suffixed with the copy number before being passed to maya commands, thus ensuring
    the proper results in maya as well.
    """
    
    
    
    def __eq__(self, other):
        pass
    
    
    def __ge__(self, other):
        pass
    
    
    def __gt__(self, other):
        pass
    
    
    def __hash__(self):
        pass
    
    
    def __init__(self, pathOrRefNode=None, namespace=None, refnode=None):
        pass
    
    
    def __le__(self, other):
        pass
    
    
    def __lt__(self, other):
        pass
    
    
    def __melobject__(self):
        pass
    
    
    def __ne__(self, other):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def __str__(self):
        pass
    
    
    def clean(self, **kwargs):
        """
        Remove edits from the passed in reference node. The reference must be in an unloaded state. To remove a particular type of edit, use the editCommand flag. If no flag is specified, all edits will be removed.                    
        
        Flags:
          - editCommand:
              For use with cleanReference. Remove only this type of edit. Supported edits are: setAttr addAttr deleteAttr connectAttr
              disconnectAttr and parent
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def copyNumberList(self):
        """
        When queried, this flag returns a string array containing a number that uniquely identifies each instance the file is used.                       
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def exportAnim(self, exportPath, **kwargs):
        """
        Export the main scene animation nodes and animation helper nodes from all referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the specified reference file. See -ean/exportAnim flag description for details on usage of animation files.                    
        
        Flags:
          - force:
              Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
              remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
              root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
              prompting a dialog that warns user about the lost of edits.
          - referenceNode:
              This flag is only used during queries. In MEL, if it appears before -query then it must be followed by the name of one
              of the scene's reference nodes. That will determine the reference to be queried by whatever flags appear after -query.
              If the named reference node does not exist within the scene the command will fail with an error. In Python the
              equivalent behavior is obtained by passing the name of the reference node as the flag's value. In MEL, if this flag
              appears after -query then it takes no argument and will cause the command to return the name of the reference node
              associated with the file given as the command's argument. If the file is not a reference or for some reason does not
              have a reference node (e.g. the user deleted it) then an empty string will be returned. If the file is not part of the
              current scene then the command will fail with an error. In Python the equivalent behavior is obtained by passing True as
              the flag's value.       In query mode, this flag can accept a value.
          - type:
              Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
              audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
              file types that match this file.
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def exportSelectedAnim(self, exportPath, **kwargs):
        """
        Export the main scene animation nodes and animation helper nodes from the selected referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the selected nodes of a specified reference file. See -ean/exportAnim flag description for details on usage of animation files.                       
        
        Flags:
          - force:
              Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
              remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
              root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
              prompting a dialog that warns user about the lost of edits.
          - referenceNode:
              This flag is only used during queries. In MEL, if it appears before -query then it must be followed by the name of one
              of the scene's reference nodes. That will determine the reference to be queried by whatever flags appear after -query.
              If the named reference node does not exist within the scene the command will fail with an error. In Python the
              equivalent behavior is obtained by passing the name of the reference node as the flag's value. In MEL, if this flag
              appears after -query then it takes no argument and will cause the command to return the name of the reference node
              associated with the file given as the command's argument. If the file is not a reference or for some reason does not
              have a reference node (e.g. the user deleted it) then an empty string will be returned. If the file is not part of the
              current scene then the command will fail with an error. In Python the equivalent behavior is obtained by passing True as
              the flag's value.       In query mode, this flag can accept a value.
          - type:
              Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
              audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
              file types that match this file.
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def getReferenceEdits(self, **kwargs):
        """
        Get a list of ReferenceEdit objects for this node
        
        Adapted from:
        referenceQuery -editString -onReferenceNode <self.refNode>
        
        Notes
        -----
        By default, removes all edits. If neither of successfulEdits or
        failedEdits is given, they both default to True. If only one is given,
        the other defaults to the opposite value.
        """
    
        pass
    
    
    def importContents(self, removeNamespace=False):
        """
        Remove the encapsulation of the reference around the data within the specified file.    This makes the contents of the specified file part of the current scene and all references to the original file are lost. Returns the name of the reference that was imported.                    
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def isDeferred(self):
        """
        When used in conjunction with the -reference flag, this flag determines if the reference is loaded, or if loading is deferred.C: The default is false.Q: When queried, this flag returns true if the reference is deferred, or false if the reference is not deferred. If this is used with -rfn/referenceNode, the -rfn flag must come before -q.                        
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def isLoaded(self):
        """
        When used in conjunction with the -reference flag, this flag determines if the reference is loaded, or if loading is deferred.C: The default is false.Q: When queried, this flag returns true if the reference is deferred, or false if the reference is not deferred. If this is used with -rfn/referenceNode, the -rfn flag must come before -q.                        
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def isUsingNamespaces(self):
        """
        Returns boolean. Queries whether the specified reference file uses namespaces or renaming prefixes.                       
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def load(self, newFile=None, **kwargs):
        """
        This flag loads a file and associates it with the passed reference node. If the reference node does not exist, the command will fail. If the file is already loaded, then this flag will reload the same file.If a file is not given, the command will load (or reload) the last used reference file. 
        
        Flags:
          - loadNoReferences:
              This flag is obsolete and has been replaced witht the loadReferenceDepth flag. When used with the -open flag, no
              references will be loaded. When used with -i/import, -r/reference or -lr/loadReference flags, will load the top-most
              reference only.
          - loadReferenceDepth:
              Used to specify which references should be loaded. Valid types are all, noneand topOnly, which will load all references,
              no references and top-level references only, respectively. May only be used with the -o/open, -i/import, -r/reference or
              -lr/loadReference flags. When noneis used with -lr/loadReference, only path validation is performed. This can be used to
              replace a reference without triggering reload. Not using loadReferenceDepth will load references in the same loaded or
              unloaded state that they were in when the file was saved. Additionally, the -lr/loadReference flag supports a fourth
              type, asPrefs. This will force any nested references to be loaded according to the state (if any) stored in the current
              scene file, rather than according to the state saved in the reference file itself.
          - returnNewNodes:
              Used to control the return value in open, import, loadReference, and reference operations. It will force the file
              command to return a list of new nodes added to the current scene.
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def lock(self):
        """
        Locks attributes and nodes from the referenced file.                      
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def namespaceExists(self):
        """
        Returns true if the specified namespace exists, false if not.                     
        
        
        Derived from mel command `maya.cmds.namespace`
        """
    
        pass
    
    
    def nodes(self):
        """
        Returns string array. A main flag used to query the contents of the target reference.                                     
        
        
        Derived from mel command `maya.cmds.referenceQuery`
        """
    
        pass
    
    
    def parent(self):
        """
        Returns the parent FileReference object, or None
        """
    
        pass
    
    
    def remove(self):
        """
        Remove the given file reference from its parent. This will also Remove everything this file references. Returns the name of the file removed. If the reference is alone in its namespace, remove the namespace. If there are objects remaining in the namespace after the file reference is removed, by default, keep the remaining objects in the namespace. To merge the objects remaining in the namespace to the parent or root namespace, use flags mergeNamespaceWithParent or mergeNamespaceWithRoot. The empty file reference namespace is then removed. To forcibly delete all objects, use flag force. The empty file reference namespace is then removed.                      
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def removeReferenceEdits(self, editCommand=None, force=False, **kwargs):
        """
        Remove edits from the reference.
        
        Parameters
        ----------
        editCommand : str
            If specified, remove only edits of a particular type: addAttr,
            setAttr, connectAttr, disconnectAttr or parent
        force : bool
            Unload the reference if it is not unloaded already
        successfulEdits : bool
            Whether to remove successful edits
        failedEdits : bool
            Whether to remove failed edits
        
        Notes
        -----
        By default, removes all edits. If neither of successfulEdits or
        failedEdits is given, they both default to True. If only one is given,
        the other defaults to the opposite value. This will only succeed on
        unapplied edits (ie, on unloaded nodes, or failed edits)... However,
        like maya.cmds.file/maya.cmds.referenceEdit, no error will be raised
        if there are no unapplied edits to work on. This may change in the
        future, however...
        """
    
        pass
    
    
    def replaceWith(self, newFile, **kwargs):
        """
        This flag loads a file and associates it with the passed reference node. If the reference node does not exist, the command will fail. If the file is already loaded, then this flag will reload the same file.If a file is not given, the command will load (or reload) the last used reference file. 
        
        Flags:
          - loadNoReferences:
              This flag is obsolete and has been replaced witht the loadReferenceDepth flag. When used with the -open flag, no
              references will be loaded. When used with -i/import, -r/reference or -lr/loadReference flags, will load the top-most
              reference only.
          - loadReferenceDepth:
              Used to specify which references should be loaded. Valid types are all, noneand topOnly, which will load all references,
              no references and top-level references only, respectively. May only be used with the -o/open, -i/import, -r/reference or
              -lr/loadReference flags. When noneis used with -lr/loadReference, only path validation is performed. This can be used to
              replace a reference without triggering reload. Not using loadReferenceDepth will load references in the same loaded or
              unloaded state that they were in when the file was saved. Additionally, the -lr/loadReference flag supports a fourth
              type, asPrefs. This will force any nested references to be loaded according to the state (if any) stored in the current
              scene file, rather than according to the state saved in the reference file itself.
          - returnNewNodes:
              Used to control the return value in open, import, loadReference, and reference operations. It will force the file
              command to return a list of new nodes added to the current scene.
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def selectAll(self):
        """
        Select all the components of this file as well as its child files.  Note that the file specified must be one that is already opened in this Maya session. The default behavior is to replace the existing selection. Use with the addflag to keep the active selection list.                      
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def subReferences(self):
        pass
    
    
    def unload(self):
        """
        This flag will unload the reference file associated with the passed reference node.                       
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def unlock(self):
        """
        Locks attributes and nodes from the referenced file.                      
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def unresolvedPath(self):
        pass
    
    
    def withCopyNumber(self):
        """
        return the path with the copy number at the end
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    fullNamespace = None
    
    namespace = None
    
    path = None
    
    refNode = None


class Path(pathClass):
    """
    A basic Maya file class. it gets most of its power from the path class written by Jason Orendorff.
    see path.py for more documentation.
    """
    
    
    
    def __repr__(self):
        pass
    
    
    def getTypeName(self, **kwargs):
        """
        Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of file types that match this file.                        
        
        
        Derived from mel command `maya.cmds.file`
        """
    
        pass
    
    
    def setSubType(self, **kwargs):
        pass


class Translator(object):
    """
    Provides information about a Maya translator, which is used for reading
    and/or writing file formats.
    
    >>> ascii = Translator('mayaAscii')
    >>> ascii.ext
    u'ma'
    >>> bin = Translator.fromExtension( 'mb' )
    >>> bin
    Translator(u'mayaBinary')
    >>> bin.name
    u'mayaBinary'
    >>> bin.hasReadSupport()
    True
    """
    
    
    
    def __init__(self, name):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def __str__(self):
        pass
    
    
    def extension(self):
        pass
    
    
    def filter(self):
        pass
    
    
    def getDefaultOptions(self):
        pass
    
    
    def getFileCompression(self):
        pass
    
    
    def hasReadSupport(self):
        pass
    
    
    def hasWriteSupport(self):
        pass
    
    
    def optionsScript(self):
        pass
    
    
    def setDefaultOptions(self, options):
        pass
    
    
    def setFileCompression(self, compression):
        pass
    
    
    def fromExtension(ext, mode=None, caseSensitive=False):
        pass
    
    
    def listRegistered():
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    ext = None
    
    name = None


class Workspace(object):
    """
    This class is designed to lend more readability to the often confusing workspace command.
    The four types of workspace entries (objectType, fileRule, renderType, and variable) each
    have a corresponding dictiony for setting and accessing these mappings.
    
        >>> from pymel.all import *
        >>> workspace.fileRules['mayaAscii']
        u'scenes'
        >>> workspace.fileRules.keys() # doctest: +ELLIPSIS
        [...u'mayaAscii', u'mayaBinary',...]
        >>> 'mayaBinary' in workspace.fileRules
        True
        >>> workspace.fileRules['super'] = 'data'
        >>> workspace.fileRules.get( 'foo', 'some_default' )
        'some_default'
    
    the workspace dir can be confusing because it works by maintaining a current working directory that is persistent
    between calls to the command.  In other words, it works much like the unix 'cd' command, or python's 'os.chdir'.
    In order to clarify this distinction, the names of these flags have been changed in their class method counterparts
    to resemble similar commands from the os module.
    
    old way (still exists for backward compatibility)
        >>> proj = workspace(query=1, dir=1)
        >>> proj  # doctest: +ELLIPSIS
        u'...'
        >>> workspace(create='mydir')
        >>> workspace(dir='mydir') # move into new dir
        >>> workspace(dir=proj) # change back to original dir
    
    new way
        >>> proj = workspace.getcwd()
        >>> proj  # doctest: +ELLIPSIS
        Path('...')
        >>> workspace.mkdir('mydir')
        >>> workspace.chdir('mydir')
        >>> workspace.chdir(proj)
    
    All paths are returned as an pymel.core.system.Path class, which makes it easy to alter or join them on the fly.
        >>> workspace.path / workspace.fileRules['mayaAscii']  # doctest: +ELLIPSIS
        Path('...')
    """
    
    
    
    def __call__(self, *args, **kwargs):
        """
        provides backward compatibility with cmds.workspace by allowing an instance
        of this class to be called as if it were a function
        """
    
        pass
    
    
    def __init__(self, *p, **k):
        pass
    
    
    def expandName(self, path):
        pass
    
    
    def chdir(self, newdir):
        pass
    
    
    def getName(self):
        pass
    
    
    def getPath(self):
        pass
    
    
    def getcwd(self):
        pass
    
    
    def mkdir(self, newdir):
        pass
    
    
    def new(self, workspace):
        pass
    
    
    def open(self, workspace):
        pass
    
    
    def save(self):
        pass
    
    
    def update(self):
        pass
    
    
    def __new__(cls, *p, **k):
        """
        # redefine __new__
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    name = None
    
    path = None
    
    
    
    fileRules = {}
    
    
    objectTypes = {}
    
    
    renderTypes = {}
    
    
    variables = {}



def recordAttr(*args, **kwargs):
    """
    This command sets up an attribute to be recorded.  When the record command is executed, any changes to this attribute
    are recorded.  When recording stops these changes are turned into keyframes. If no attributes are specified all
    attributes of the node are recorded. When the query flag is used, a list of the attributes being recorded will be
    returned. In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify the attribute to record                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``delete`` / ``d``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Do not record the specified attributes                    Flag can have multiple arguments, passed either as a tuple or a list.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.recordAttr`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # This command will setup the translateX and translateY
        # attributes for recording.
        pm.recordAttr( at=['translateX', 'translateZ'] )
    """

    pass


def undo(*args, **kwargs):
    """
    Takes the most recent command from the undo list and undoes it.
    
    
    Derived from mel command `maya.cmds.undo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # In this particular example, each line needs to be executed
        # separately one after the other. Executing lines separately
        # guaranties that commands are properly registered in the undo
        # stack.
        
        pm.polyCube()
        # Result: [nt.Transform(u'pCube1'), nt.PolyCube(u'polyCube1')] #
        
        pm.polySphere()
        # Result: [nt.Transform(u'pSphere1'), nt.PolySphere(u'polySphere1')] #
        
        pm.undo()
        # Undo: pm.polySphere()
         #
        
        pm.undo()
        # Undo: pm.polyCube()
         #
    """

    pass


def _safePyNode(n):
    pass


def launchImageEditor(*args, **kwargs):
    """
    Launch the appropriate application to edit/view the image files specified. This command works only on the Macintosh and
    Windows platforms.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``editImageFile`` / ``eif``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If the file is a PSD, then the specified verison of Photoshop is launched, and the file is opened in it. If file is any other image type, then the preferred image|
    |  | editor is launched, and the file is opened in it.                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``viewImageFile`` / ``vif``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Opens up an Image editor to view images.                          Flag can have multiple arguments, passed either as a tuple or a list.                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.launchImageEditor`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Create a blinn shader with a psd file texture.
        pm.shadingNode('blinn', asShader=True)
        # Result: nt.Blinn(u'blinn1') #
        pm.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
        # Result: nt.ShadingEngine(u'blinn1SG') #
        pm.connectAttr('blinn1.outColor', 'blinn1SG.surfaceShader', f=True)
        pm.shadingNode('psdFileTex', asTexture=True)
        # Result: nt.PsdFileTex(u'psdFileTex1') #
        pm.connectAttr('psdFileTex1.outColor', 'blinn1.color')
        pm.setAttr('psdFileTex1.fileTextureName', 'C:/test.psd', type='string')
        
        # Create a poly plane, and assign the blinn shader to it.
        pm.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
        # Result: [nt.Transform(u'pPlane1'), nt.PolyPlane(u'polyPlane1')] #
        pm.sets(e=True, forceElement='blinn1SG')
        
        # Now you can launch Photoshop to edit this psd texture file
        pm.launchImageEditor(eif=pm.getAttr('psdFileTex1.fileTextureName'))
    """

    pass


def dirmap(*args, **kwargs):
    """
    Use this command to map a directory to another directory. The first argument is the directory to map, and the second is
    the destination directory to map to. Directories must both be absolute paths, and should be separated with forward
    slashes ('/'). The mapping is case-sensitive on all platforms. This command can be useful when moving projects to
    another machine where some textures may not be contained in the Maya project, or when a texture archive moves to a new
    location. This command is not necessary when moving a (self-contained) project from one machine to another - instead
    copy the entire project over and set the Maya project to the new location. For one-time directory moves, if the command
    is enabled and the mapping configured correctly, when a scene is opened and saved the mapped locations will be reflected
    in the filenames saved with the file. To set up a permanent mapping the command should be enabled and the mappings set
    up in a script which is executed every time you launch Maya (userSetup.mel is sourced on startup). The directory
    mappings and enabled state are not preserved between Maya sessions. This command requires one mainflag that specifies
    the action to take. Flags are:-[m|um|gmd|gam|cd|en]
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``convertDirectory`` / ``cd``                                                                        | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Convert a file or directory. Returns the name of the mapped file or directory, if the command is enabled. If the given string contains one of the mapped          |
    |  | directories, the return value will have that substring replaced with the mapped one. Otherwise the given argument string will be returned. If the command is      |
    |  | disabled the given argument is always returned. Checks are not made for whether the file or directory exists. If the given string is a directory it should have a |
    |  | trailing '/'.                     Flag can have multiple arguments, passed either as a tuple or a list.                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``enable`` / ``en``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Enable directory mapping. Directory mapping is off when you start Maya. If enabled, when opening Maya scenes, file texture paths (and other file paths) will be   |
    |  | converted when the scene is opened. The -cd flag only returns mapped directories when -enable is true. Query returns whether mapping has been enabled.            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``getAllMappings`` / ``gam``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Get all current mappings. Returns string array of current mappings in format: [redirect1, replacement1, ... redirectN, replacementN]                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``getMappedDirectory`` / ``gmd``                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Get the mapped redirected directory. The given argument must exactly match the first string used with the -mapDirectory flag.                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mapDirectory`` / ``m``                                                                             | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Map a directory - the first argument is mapped to the second. Neither directory needs to exist on the local machine at the time of invocation.                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unmapDirectory`` / ``um``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Unmap a directory. The given argument must exactly match the argument used with the -mapDirectory flag.                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dirmap`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.dirmap( en=True )
        pm.dirmap( m=('/usr/maya/textures', '/share/store/textures') )
        pm.dirmap( cd='/usr/maya/textures/characters/skin1.iff' )
        # Result: u'/share/store/textures/characters/skin1.iff' #
        # Result: /share/store/textures/characters/skin1.iff"
        pm.dirmap( m=('D:/mySoundfiles', '/usr/me/sounds') )
        pm.dirmap( cd='D:/mySoundfiles/' )
        # Result: u'/usr/me/sounds/' #
        # Result: /usr/me/sounds/
    """

    pass


def cacheFileTrack(*args, **kwargs):
    """
    This command is used for inserting and removing tracks related to the caches displayed in the trax editor. It can also
    be used to modify the track state, for example, to lock or mute a track.                  In query mode, return type is
    based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``insertTrack`` / ``it``                                                                             | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to insert a new empty track at the track index specified.                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lock`` / ``l``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether clips on a track are to be locked or not.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mute`` / ``m``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether clips on a track are to be muted or not.                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeEmptyTracks`` / ``ret``                                                                      | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to remove all tracks that have no clips.                                        Flag can have multiple arguments, passed either as a tuple or a |
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeTrack`` / ``rt``                                                                             | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to remove the track with the specified index.  The track must have no clips on it before it can be removed.                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``solo`` / ``so``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether clips on a track are to be soloed or not.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``track`` / ``t``                                                                                    | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used to specify a new track index for a cache to be displayed. Track-indices are 1-based.                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.cacheFileTrack`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Move the cache clip named "cubeCache2" to track 3
        #
        pm.cacheFileTrack( 'cubeCache2', track=3 )
        # Lock the track containing the cache clip named "sphCache1"
        #
        pm.cacheFileTrack( 'sphCache1', lock=True )
        # Remove any empty cache tracks for the object "sphereShape1"
        #
        pm.cacheFileTrack('sphereShape1',removeEmptyTracks=True)
        # query the track index of the cache clip named "sphCache1"
        #
        pm.cacheFileTrack( 'sphCache1', q=True, track=True )
    """

    pass


def undoInfo(*args, **kwargs):
    """
    This command controls the undo/redo parameters.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``chunkName`` / ``cn``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the name used to identify a chunk for undo/redo purposes when opening a chunk.                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``closeChunk`` / ``cck``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Closes the chunk that was opened earlier by openChunk. Once close chunk is called, all undoable operations in the chunk will undo as a single undo operation. Use |
    |  | with CAUTION!! Improper use of this command can leave the undo queue in a bad state.                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``infinity`` / ``infinity``                                                                          | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the queue length to infinity.                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``length`` / ``l``                                                                                   | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the number of items in the undo queue. The infinity flag overrides this one.                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``openChunk`` / ``ock``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Opens a chunk so that all undoable operations after this call will fall into the newly opened chunk, until close chunk is called. Once close chunk is called, all |
    |  | undoable operations in the chunk will undo as a single undo operation. Use with CAUTION!! Improper use of this command can leave the undo queue in a bad state.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``printQueue`` / ``pq``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Prints to the Script Editor the contents of the undo queue.                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``redoName`` / ``rn``                                                                                | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns what will be redone (if anything)                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``redoQueueEmpty`` / ``rqe``                                                                         | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return true if the redo queue is empty. Return false if there is at least one command in the queue to be redone.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``state`` / ``st``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns undo/redo on or off.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stateWithoutFlush`` / ``swf``                                                                      | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns undo/redo on or off without flushing the queue. Use with CAUTION!! Note that if you  perform destructive operations while stateWithoutFlush is disabled, and|
    |  | you then enable it again, subsequent undo operations that try to go past the  destructive operations may be unstable since undo will not be able to properly      |
    |  | reconstruct the former state of the scene.                        Flag can have multiple arguments, passed either as a tuple or a list.                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``undoName`` / ``un``                                                                                | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns what will be undone (if anything)                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``undoQueueEmpty`` / ``uqe``                                                                         | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return true if the undo queue is empty. Return false if there is at least one command in the queue to be undone.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.undoInfo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Turn undo on, with an infinite queue length
        pm.undoInfo( state=True, infinity=True )
        # Turn undo on, with a queue length of 200
        pm.undoInfo( state=True, infinity=False, length=200 )
        # Turn undo off
        pm.undoInfo( state=False )
        # Query the queue length
        pm.undoInfo( q=True, length=True )
        # Result: 200 #
    """

    pass


def openFile(*args, **kwargs):
    """
    Open the specified file. Returns the name of the opened file.                     
    
    Flags:
      - loadAllDeferred:
          This flag is obsolete, and has been replaced by the loadReferenceDepth flag. When used with the -open flag, determines
          if the -deferReference flag is respected when reading in the file. If true is passed, all of the references are loaded.
          If false is passed, the -deferReference flag is respected.
      - loadNoReferences:
          This flag is obsolete and has been replaced witht the loadReferenceDepth flag. When used with the -open flag, no
          references will be loaded. When used with -i/import, -r/reference or -lr/loadReference flags, will load the top-most
          reference only.
      - loadReferenceDepth:
          Used to specify which references should be loaded. Valid types are all, noneand topOnly, which will load all references,
          no references and top-level references only, respectively. May only be used with the -o/open, -i/import, -r/reference or
          -lr/loadReference flags. When noneis used with -lr/loadReference, only path validation is performed. This can be used to
          replace a reference without triggering reload. Not using loadReferenceDepth will load references in the same loaded or
          unloaded state that they were in when the file was saved. Additionally, the -lr/loadReference flag supports a fourth
          type, asPrefs. This will force any nested references to be loaded according to the state (if any) stored in the current
          scene file, rather than according to the state saved in the reference file itself.
      - force:
          Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
          remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
          root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
          prompting a dialog that warns user about the lost of edits.
      - returnNewNodes:
          Used to control the return value in open, import, loadReference, and reference operations. It will force the file
          command to return a list of new nodes added to the current scene.
      - type:
          Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
          audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
          file types that match this file.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def loadModule(*args, **kwargs):
    """
    Maya plug-ins may be installed individually within one of Maya's standard plug-in directories, or they may be packaged
    up with other resources in a module. Each module resides in its own directory and provides a module definition file to
    make Maya aware of the plug-ins it provides. When Maya starts up it loads all of the module files it finds, making the
    module's plug-ins, scripts and other resources available for use. Note that the plug-ins themselves are not loaded at
    this time, Maya is simply made aware of them so that they can be loaded if needed. The loadModule command provides the
    ability to list and load any new modules which have been added since Maya started up, thereby avoiding the need to
    restart Maya before being able to use them.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``allModules`` / ``a``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Load all new modules not yet loaded in Maya. New modules are the one returned by the -scan option.                                        Flag can have multiple  |
    |  | arguments, passed either as a tuple or a list.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``load`` / ``ld``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Load the module specified by the module definition file.                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scan`` / ``sc``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Rescan module presence. Returns the list of module definition files found and not yet loaded into Maya. Does not load any of these newly found modules, not change|
    |  | the Maya state.                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.loadModule`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.loadModule(scan=True)
        # Result: [] #
        pm.loadModule(load='myModuleDef')
        # Result: [] #
        pm.loadModule(allModules=True)
        # Result: [] #
    """

    pass


def requires(*args, **kwargs):
    """
    This command is used during file I/O to specify the requirements needed to load the given file.  It defines what file
    format version was used to write the file, or what plug-ins are required to load the scene. The first string names a
    product (either maya, or a plug-in name) The second string gives the version. This command is only useful during file
    I/O, so users should not have any need to use this command themselves. The flags -nodeTypeand -dataTypespecify the node
    types and data types defined by the plug-in. When Maya open a scene file, it runs requirescommand in the file and load
    required plug-ins. But some plug-ins may be not loaded because they are missing. The flags -nodeTypeand -dataTypeare
    used by the missing plug-ins. If one plug-in is missing, nodes and data created by this plug-in are created as unknown
    nodes and unknown data. Maya records their original types for these unknown nodes and data. When these nodes and data
    are saved back to file, it will be possible to determine the associated missing plug-ins. And when export selected
    nodes, Maya can write out the exact required plug-ins. The flags -nodeTypeand -dataTypeis optional. In this command, if
    these flags are not given for one plug-in and the plug-in is missing, the requirescommand of this plug-in will always be
    saved back.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``dataType`` / ``dt``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify a data type defined by this plug-in. The data type is specified by MFnPlugin::registerData() when register the plug-in.                   Flag can have   |
    |  | multiple arguments, passed either as a tuple or a list.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``nodeType`` / ``nt``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify a node type defined by this plug-in. The node type is specified by MFnPlugin::registerNode() when register the plug-in.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.requires`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.requires( 'maya', '7.0' )
        pm.requires( 'simpleLoftNode.so', '1.0' )
        pm.requires( 'gpuCache', '1.0', nodeType='gpuCache')
    """

    pass


def renameFile(newname, *args, **kwargs):
    """
    Rename the scene. Used mostly during save to set the saveAs name. Returns the new name of the scene.                      
    
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def listInputDeviceButtons(*args, **kwargs):
    """
    This command lists all of the buttons of the specified input device specified as an argument.
    
    
    Derived from mel command `maya.cmds.listInputDeviceButtons`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Returns a list of the buttons of the spaceball.
        pm.listInputDeviceButtons( 'spaceball' )
    """

    pass


def error(*args, **kwargs):
    """
    The error command is provided so that the user can issue error messages from his/her scripts and control execution in
    the event of runtime errors.  The string argument is displayed in the command window (or stdout if running in batch
    mode) after being prefixed with an error message heading and surrounded by //.  The error command also causes execution
    to terminate with an error. Using error is like raising an exception because the error will propagate up through the
    call chain. You can use catch to handle the error from the caller side. If you don't want execution to end, then you
    probably want to use the warning command instead.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``noContext`` / ``n``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Do not include the context information with the error message.                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showLineNumber`` / ``sl``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Obsolete. Will be deleted in the next version of Maya. Use the checkbox in the script editor that enables line number display instead.                            |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.error`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        import maya.cmds as cmds
        def lightError():
            l = pm.ls( lights=True )
            if len(l) == 0:
                pm.error( "No Lights" )
        lightError()
        # The above will produce the following output and raise a RuntimeError
        # exception from the script containing it:
        #
        #   # Error: No Lights #
        #
        # If the option to display line numbers or the stack trace is turned on
        # the following output will be produced and the same exception raised:
        #
        #   # Error: line 13 of 'lightError' in '"maya console'": No Lights #
        #
    """

    pass


def internalVar(*args, **kwargs):
    """
    This command returns the values of internal variables.  No modification of these variables is supported.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``userAppDir`` / ``uad``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the user application directory.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``userBitmapsDir`` / ``ubd``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the user bitmaps prefs directory.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``userHotkeyDir`` / ``uhk``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the user hotkey directory.                         Flag can have multiple arguments, passed either as a tuple or a list.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``userMarkingMenuDir`` / ``umm``                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the user marking menu directory.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``userPrefDir`` / ``upd``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the user preference directory.                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``userPresetsDir`` / ``ups``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the user presets directory.                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``userScriptDir`` / ``usd``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the user script directory.                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``userShelfDir`` / ``ush``                                                                           | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the user shelves directory.                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``userTmpDir`` / ``utd``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return a temp directory.  Will check for TMPDIR environment variable, otherwise will return the current directory.                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``userWorkspaceDir`` / ``uwd``                                                                       | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the user workspace directory (also known as the projects directory).                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.internalVar`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        myScriptDir = pm.internalVar(userScriptDir=True)
    """

    pass


def dbcount(*args, **kwargs):
    """
    The dbcountcommand is used to print and manage a list of statistics collected for counting operations.  These statistics
    are displayed as a list of hits on a particular location in code, with added reference information for
    pointers/strings/whatever. If -reset is not specified then statistics are printed.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``enabled`` / ``e``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the enabled state of the counters ('on' to enable, 'off' to disable). Returns the list of all counters affected.                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``file`` / ``f``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Destination file of the enabled count objects.  Use the special names stdoutand stderrto redirect to your command window.  As well, the special name msdevis      |
    |  | available on NT to direct your output to the debug tab in the output window of Developer Studio.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``keyword`` / ``k``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Print only the counters whose name matches this keyword (default is all).                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``list`` / ``l``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List all available counters and their current enabled status. (The only thing you can do when counters are disabled.)                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxdepth`` / ``md``                                                                                | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum number of levels down to traverse and report. 0 is the default and it means continue recursing as many times as are requested.                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``quick`` / ``q``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Display only a summary for each counter type instead of the full details.                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``reset`` / ``r``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Reset all counters back to 0 and remove all but the top level counters. Returns the list of all counters affected.                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``spreadsheet`` / ``s``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Display in spreadsheet format instead of the usual nested braces. This will include a header row that contains 'Count Level1 Level2 Level3...', making the data   |
    |  | suitable for opening directly in a spreadsheet table.                                     Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dbcount`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.dbcount( e='on' )              # Enable counters
        pm.dbcount( )                     # Print all available counters
        pm.dbcount( f='myCounts.txt' )    # Print all available counters to the file "myCounts.txt"
        pm.dbcount( k='dirty' )           # Print all counters with "dirty" in their name
        pm.dbcount( r=True, k='dirty' )   # Reset counters with "dirty" in their name
        pm.dbcount( l=True )              # List all counters
        pm.dbcount( l=True, k='dirty' )   # List all counters with "dirty" in their name
        pm.dbcount( s=True, f='xls.txt' ) # Print all counters in spreadsheet form to the file "xls.txt"
    """

    pass


def saveFile(**kwargs):
    """
    Save the specified file. Returns the name of the saved file.                      
    
    Flags:
      - force:
          Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
          remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
          root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
          prompting a dialog that warns user about the lost of edits.
      - preSaveScript:
          When used with the save flag, the specified script will be executed before the file is saved.
      - postSaveScript:
          When used with the save flag, the specified script will be executed after the file is saved.
      - type:
          Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
          audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
          file types that match this file.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def exportSelectedAnimFromReference(exportPath, **kwargs):
    """
    Export the main scene animation nodes and animation helper nodes from the selected referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the selected nodes of a specified reference file. See -ean/exportAnim flag description for details on usage of animation files.                       
    
    Flags:
      - force:
          Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
          remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
          root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
          prompting a dialog that warns user about the lost of edits.
      - referenceNode:
          This flag is only used during queries. In MEL, if it appears before -query then it must be followed by the name of one
          of the scene's reference nodes. That will determine the reference to be queried by whatever flags appear after -query.
          If the named reference node does not exist within the scene the command will fail with an error. In Python the
          equivalent behavior is obtained by passing the name of the reference node as the flag's value. In MEL, if this flag
          appears after -query then it takes no argument and will cause the command to return the name of the reference node
          associated with the file given as the command's argument. If the file is not a reference or for some reason does not
          have a reference node (e.g. the user deleted it) then an empty string will be returned. If the file is not part of the
          current scene then the command will fail with an error. In Python the equivalent behavior is obtained by passing True as
          the flag's value.       In query mode, this flag can accept a value.
      - type:
          Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
          audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
          file types that match this file.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def profilerTool(*args, **kwargs):
    """
    This script is intended to be used by the profilerPanel to interact with the profiler tool's view (draw region). It can
    be used to control some behaviors about the profiler Tool.               In query mode, return type is based on queried
    flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``categoryView`` / ``cat``                                                                           | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Change view mode to category view                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cpuView`` / ``cpu``                                                                                | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Change view mode to cpu view                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``destroy`` / ``dtr``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Destroy the profiler tool Internal flag. Should not be used by user.                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exists`` / ``ex``                                                                                  | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query if the profiler tool view exists. Profiler tool can only exist after profilerTool -makeis called.                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``findNext`` / ``fn``                                                                                | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used along with flag -searchEvent.                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``findPrevious`` / ``fp``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used along with flag -searchEvent.                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``frameAll`` / ``fa``                                                                                | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Frame on all events in the profilerToolView                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``frameSelected`` / ``fs``                                                                           | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Frame on all selected events in the profilerToolView                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``isolateSegment`` / ``isolateSegment``                                                              | *int*                         | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Isolate a specified segment. A segment is a set of events that happened in one animation frame. You can use flag -segmentCount to query the number of segments in |
    |  | the event buffer. The segment index starts from 0. If the specified segment does not exist, an error will be thrown.                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``make`` / ``mk``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Make the profiler tool and parent it to the most recent layout created Internal flag. Should not be used by user.                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``matchWholeWord`` / ``mww``                                                                         | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells profiler tool if it should match whole word when searching event(s). The default value is false.                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``searchEvent`` / ``se``                                                                             | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Search event(s). You can set -matchWholeWord before you use -searchEvent. If -matchWholeWord has been set to true, the profiler tool will search event(s) whose   |
    |  | name exactly matches with the string. If -matchWholeWord has been set to false, the profiler tool will search event(s) whose name contains the string. If         |
    |  | -findNext is also used along with this flag, the profiler tool will find the first event next to the current selected event. If -findPrevious is also used along  |
    |  | with this flag, the profiler tool will find the first event previous to the current selected event. If currently don't have a selected event or there are multiple|
    |  | selected events, the search will start at the first event in profiler buffer. If -findNext and -findPrevious are not used along with this flag, the profiler tool |
    |  | will find all events.                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``segmentCount`` / ``sc``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the number of segments in the event buffer.                                       Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showAllEvent`` / ``sa``                                                                            | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Show all events (if events were hidden by filtering) (true) or Hide all events (false)                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showSelectedEvents`` / ``ss``                                                                      | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Show only the selected events (true) or hide all selected events (false)                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showSelectedEventsRepetition`` / ``ssr``                                                           | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Show only the selected events repetition based on their comment (true) or Hide all selected events repetition based on their comment (false)                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``threadView`` / ``thd``                                                                             | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Change view mode to thread view                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unisolateSegment`` / ``uis``                                                                       | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Unisolate current isolated segment. If no segment is currently isolated, nothing will happen.                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.profilerTool`
    """

    pass


def getModifiers(*args, **kwargs):
    """
    This command returns the current state of the modifier keys. The state of each modifier can be obtained by testing for
    the modifier's corresponding bit value in the return value. Shift is bit 1, Ctrl is bit 3, Alt is bit 4, and bit 5 is
    the 'Windows' key on Windows keyboards and the Command key on Mac keyboards.  See the provided example for more details
    on testing for each modifier's bit value.
    
    
    Derived from mel command `maya.cmds.getModifiers`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        def PrintModifiers(*args):
            mods = pm.getModifiers()
            print 'Modifiers are:'
            if (mods " 1) " 0: print ' Shift'
            if (mods " 4) " 0: print ' Ctrl'
            if (mods " 8) " 0: print ' Alt'
            if (mods " 16): print ' Command/Windows'
        
        pm.window()
        pm.columnLayout()
        pm.button( label='Press Me', command=PrintModifiers )
        pm.showWindow()
    """

    pass


def clearCache(*args, **kwargs):
    """
    Even though dependency graph values are computed or dirty they may still occupy space temporarily within the nodes.
    This command goes in to all of the data that can be regenerated if required and removes it from the caches (datablocks),
    thus clearing up space in memory.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``allNodes`` / ``all``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If toggled then all nodes in the graph are cleared.  Otherwise only those nodes that are selected are cleared.                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``computed`` / ``c``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If toggled then remove all data that is computable.  (Warning: If the data is requested for redraw then the recompute will immediately fill the data back in.)    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dirty`` / ``d``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If toggled then remove all heavy data that is dirty.                                      Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.clearCache`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Clear one node's datablock cache
        pm.clearCache( 'node' )
        # Clear caches in all dependency graph nodes
        pm.clearCache( all=True )
        # Result: 0 #
    """

    pass


def convertUnit(*args, **kwargs):
    """
    This command converts values between different units of measure.  The command takes a string, because a string can
    incorporate unit names as well as values (see examples).
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``fromUnit`` / ``f``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The unit to convert from.  If not supplied, it is assumed to be the system default.  The from unit may also be supplied as part of the value e.g. 11.2m (11.2     |
    |  | meters).                                                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``toUnit`` / ``t``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The unit to convert to.  If not supplied, it is assumed to be the system default                          Flag can have multiple arguments, passed either as a    |
    |  | tuple or a list.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.convertUnit`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Returns string "4.80315in", which is 12.2cm in inches.
        pm.convertUnit( '12.2', fromUnit='cm', toUnit='in' )
        # Result: u'4.80315in' #
        
        # Returns string "3.499563yd", which is 3.2m in yards.
        pm.convertUnit( '3.2m', toUnit='yard' )
        # Result: u'3.499563yd' #
        
        # Returns float value 13.716, which is 5.4 inches in cm (default system units).
        pm.convertUnit( '5.4', fromUnit='inch' )
        # Result: u'13.716' #
    """

    pass


def sceneEditor(*args, **kwargs):
    """
    This creates an editor for managing the files in a scene.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``control`` / ``ctl``                                                                                | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible, at times, for an     |
    |  | editor to exist without a control. This flag returns NONEif no control is present.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``defineTemplate`` / ``dt``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Puts a command in a mode where any other flags and args are parsed and added to the command template specified in the argument. They will be used as default      |
    |  | arguments in any subsequent invocations of the command when templateName is set as the current template.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``docTag`` / ``dtg``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attaches a tag to the Maya editor.                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exists`` / ``ex``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true|false depending upon whether the specified object exists.  Other flags are ignored.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``filter`` / ``f``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of an itemFilter object to be placed on this editor. This filters the information coming onto the main list of the editor.                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``forceMainConnection`` / ``fmc``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will use as its source of content.  The editor will only display items contained in the       |
    |  | selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used|
    |  | to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``highlightConnection`` / ``hlc``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will synchronize with its highlight list.  Not all editors have a highlight list. For those   |
    |  | that do, it is a secondary selection list.                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lockMainConnection`` / ``lck``                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original          |
    |  | mainConnection are ignored.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mainListConnection`` / ``mlc``                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will use as its source of content.  The editor will only display items contained in the       |
    |  | selectionConnection object.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``onlyParents`` / ``op``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When used with the 'selectItem' or 'selectReference' queries it indicates that, if both a parent and a child file or reference are selected, only the parent will |
    |  | be returned.                                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``panel`` / ``pnl``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the panel that the editor belongs to.  By default if an editor is created in the create callback of a scripted panel it will belong to that panel.  If  |
    |  | an editor doesn't belong to a panel it will be deleted when the window that it is in is deleted.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``parent`` / ``p``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``refreshReferences`` / ``rr``                                                                       | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Force refresh of references                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectCommand`` / ``sc``                                                                           | *script*                      | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A script to be executed when an item is selected.                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectItem`` / ``si``                                                                              | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query or change the currently selected item. When queried, the currently selected file name will be return.                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectReference`` / ``sr``                                                                         | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the currently selected reference. Returns the name of the currently selected reference node.                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectionConnection`` / ``slc``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will synchronize with its own selection list.  As the user selects things in this editor, they|
    |  | will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the change.                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shortName`` / ``shn``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When used with the 'selectItem' query it indicates that the file name returned will be the short name (i.e. just a file name without any directory paths). If this|
    |  | flag is not present, the full name and directory path will be returned.                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stateString`` / ``sts``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query only flag.  Returns the MEL command that will edit an editor to match the current editor state. The returned command string uses the string variable        |
    |  | $editorName in place of a specific name.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unParent`` / ``up``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies that the editor should be removed from its layout. This cannot be used with query.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unlockMainConnection`` / ``ulk``                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unresolvedName`` / ``un``                                                                          | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When used with the 'selectItem' query it indicates that the file name returned will be unresolved (i.e. it will be the path originally specified when the file was|
    |  | loaded into Maya; this path may contain environment variables and may not exist on disk). If this flag is not present, the resolved name will    be returned.     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``updateMainConnection`` / ``upd``                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``useTemplate`` / ``ut``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Force the command to use a command template other than the current one.                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``withoutCopyNumber`` / ``wcn``                                                                      | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When used with the 'selectItem' query it indicates that the file name returned will not have a copy number appended to the end. If this flag is not present, the  |
    |  | file name returned may have a copy number appended to the end.                   Flag can have multiple arguments, passed either as a tuple or a list.            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.sceneEditor`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        window = pm.window()
        pm.paneLayout()
        # Result: ui.PaneLayout('window1|paneLayout12') #
        pm.sceneEditor()
        # Result: u'sceneEditor1' #
        pm.showWindow(window)
    """

    pass


def cacheFileMerge(*args, **kwargs):
    """
    If selected/specified caches can be successfully merged, will return the start/end frames of the new cache followed by
    the start/end frames of any gaps in the merged cache for which no data should be written to file. In query mode, will
    return the names of geometry associated with the specified cache file nodes.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``endTime`` / ``et``                                                                                 | *time*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the end frame of the merge range. If not specified, will figure out range from times of caches being merged.                                    Flag can|
    |  | have multiple arguments, passed either as a tuple or a list.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``geometry`` / ``g``                                                                                 | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query-only flag used to find the geometry nodes associated with the specified cache files.                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``startTime`` / ``st``                                                                               | *time*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the start frame of the merge range. If not specified, will figure out range from the times of the caches being merged.                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.cacheFileMerge`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Find associated geometry nodes
        #
        geom = pm.cacheFileMerge('cache1', 'cache2' ,query=True, geometry=True)
        # Validate merging of caches and find out start/end times.
        # This will give a warning if there is a gap letting you know that
        # simulation data will fill the gap.
        #
        startEndTimes = pm.cacheFileMerge('cache1', 'cache2')
        # Result: { 0, 20, 5, 10 }
        start = startEndTimes[0]
        end = startEndTimes[1]
        gapStart = startEndTimes[2]
        gapEnd = startEndTimes[3]
        # Create a new merged cache, using simulation data to fill in
        # any gaps between cache1 and cache2.
        #
        cacheFiles = pm.cacheFile(fileName='mergedCache', startTime=start, endTime=end, points=geom[0])
        switch = maya.mel.eval('createHistorySwitch("pPlaneShape1", false)');
        pm.cacheFile( attachFile=True, f=cacheFiles[0], ia='%s.inp[0]' % switch)
        pm.setAttr( '%s.playFromCache' % switch, 1 )
        # Alternatively, can use append to make sure that we interpolate
        # for the frames in the gap between cache1 and cache2.
        #
        cacheFiles = pm.cacheFile(fileName='mergedCache', startTime=start, endTime=gapStart, points=geom[0])
        switch = maya.mel.eval('createHistorySwitch("pPlane1", false)');
        pm.cacheFile( attachFile=True, f=cacheFiles[0], ia='%s.inp[0]' % switch)
        pm.setAttr( '%s.playFromCache' % switch, 1 )
        pm.cacheFile( replaceCachedFrame=True, startTime=gapEnd, endTime=end, points=geom[0] )
    """

    pass


def getInputDeviceRange(*args, **kwargs):
    """
    This command lists the minimum and maximum values the device axis can return.  This value is the raw device values
    before any mapping is applied.  If you don't specify an axis the values for all axes of the device are returned.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``maxValue`` / ``max``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | list only the maximum value of the axis                   Flag can have multiple arguments, passed either as a tuple or a list.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minValue`` / ``min``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | list only the minimum value of the axis                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.getInputDeviceRange`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # This will return a single value which is the minimum value
        # the spaceball translate:X axis can return.
        pm.getInputDeviceRange( 'spaceball', 'translate:X', min=True )
        
        # This will return an array containing the maximum values for
        # all of the spaceball axes.
        pm.getInputDeviceRange( 'spaceball', max=True )
        
        # Warning:
        #     Maya is dependent on the device driver or plugin to supply it with
        #     the correct value.  Some device drivers don't return correct
        #     information.
    """

    pass


def rehash(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.rehash`
    """

    pass


def diskCache(*args, **kwargs):
    """
    Command to create, clear, or close disk cache(s).                In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``append`` / ``a``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Append at the end and not to flush the existing cache                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cacheType`` / ``ct``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the type of cache to overwrite.  mcfpfor particle playback cache, mcfifor particle initial cache. mcjfor jiggle cache. This option is only activated    |
    |  | during the cache creation.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``close`` / ``c``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Close the cache given the disk cache node name.  If -eco/enabledCachesOnly is trueonly enabled disk cache nodes are affected.                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``closeAll`` / ``ca``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Close all disk cache files. If -eco/enabledCachesOnly is trueonly enabled disk cache nodes are affected.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``delete`` / ``d``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Delete the cache given the disk cache node name.  If -eco/enabledCachesOnly is trueonly enabled disk cache nodes are affected.                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deleteAll`` / ``da``                                                                               | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Delete all disk cache files.  If -eco/enabledCachesOnly is trueonly enabled disk cache nodes are affected.                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``empty`` / ``e``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Clear the content of the disk cache with the given disk cache node name.  If -eco/enabledCachesOnly is trueonly enabled disk cache nodes are affected.            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``emptyAll`` / ``ea``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Clear the content of all disk caches.  If -eco/enabledCachesOnly is trueonly enabled disk cache nodes are affected.                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``enabledCachesOnly`` / ``eco``                                                                      | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When present, this flag restricts the -ea/emptyAll, so that only enableddisk caches (i.e., disk cache nodes with the .enableattribute set to true) are affected.  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``endTime`` / ``et``                                                                                 | *time*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the end frame of the cache range.                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``frameRangeType`` / ``frt``                                                                         | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the type of frame range to use, namely Render Globals, Time Slider, and Start/End.  In the case of Time Slider, startFrame and endFrame need to be      |
    |  | specified.  (This flag is now obsolete.  Please use the -startTime and -endTime flags to specify the frame range explicitly.)                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``overSample`` / ``os``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Over sample if true. Otherwise, under sample.                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``samplingRate`` / ``sr``                                                                            | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies how frequently to sample relative to each frame. When over-sampling (-overSample has been specified), this parameter determines how many times per frame|
    |  | the runup will be evaluated. When under-sampling (the default, when -overSample has not been specified), the runup will evaluate only once per srframes, where    |
    |  | sris the value specified to this flag.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``startTime`` / ``st``                                                                               | *time*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the start frame of the cache range.                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``tempDir`` / ``tmp``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query-only flag for the location of temporary diskCache files.                                    Flag can have multiple arguments, passed either as a tuple or a |
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.diskCache`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Explicitly specify the settings for disk cache
        # creation: the start time to 3 and the end time to 10.
        pm.diskCache( startTime=3, endTime=10 )
        # Specify to use over sampling and with sampling
        # rate set to 2, sampling twice for each frame.
        pm.diskCache( overSample=True, samplingRate=2 )
        # Delete all caches
        pm.diskCache( deleteAll=True )
        # Clear the cache content for diskCache3's cache.
        pm.diskCache( empty='diskCache3' )
        # Close all the disk caches.
        pm.diskCache( emptyAll=True )
    """

    pass


def unknownNode(*args, **kwargs):
    """
    Allows querying of the data stored for unknown nodes (nodes that are defined by a plug-in that Maya could not load when
    loading a scene file).
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``plugin`` / ``p``                                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``realClassName`` / ``rcn``                                                                          | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the real class name of the node.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``realClassTag`` / ``rct``                                                                           | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the real class IFF tag of the node.                        Flag can have multiple arguments, passed either as a tuple or a list.                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.unknownNode`
    """

    pass


def devicePanel(*args, **kwargs):
    """
    This command is now obsolete. It is included only for the purpose of file compatibility. It creates a blank panel.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``control`` / ``ctl``                                                                                | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``copy`` / ``cp``                                                                                    | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``createString`` / ``cs``                                                                            | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``defineTemplate`` / ``dt``                                                                          | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``docTag`` / ``dtg``                                                                                 | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``editString`` / ``es``                                                                              | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exists`` / ``ex``                                                                                  | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``init`` / ``init``                                                                                  | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``isUnique`` / ``iu``                                                                                | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``label`` / ``l``                                                                                    | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``menuBarVisible`` / ``mbv``                                                                         | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``needsInit`` / ``ni``                                                                               | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``parent`` / ``p``                                                                                   | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``popupMenuProcedure`` / ``pmp``                                                                     | *callable*                    |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``replacePanel`` / ``rp``                                                                            | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``tearOff`` / ``to``                                                                                 | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``tearOffCopy`` / ``toc``                                                                            | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unParent`` / ``up``                                                                                | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``useTemplate`` / ``ut``                                                                             | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.devicePanel`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # This example creates a new device panel in its own window
        window = pm.window()
        pm.paneLayout()
        # Result: ui.PaneLayout('window1|paneLayout4') #
        pm.devicePanel()
        # Result: ui.DevicePanel('devicePanel1') #
        pm.showWindow( window )
    """

    pass


def exportSelected(exportPath, **kwargs):
    """
    Export the selected items into the specified file. Returns the name of the exported file.                         
    
    Flags:
      - force:
          Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
          remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
          root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
          prompting a dialog that warns user about the lost of edits.
      - constructionHistory:
          For use with exportSelected to specify whether attached construction history should be included in the export.
      - channels:
          For use with exportSelected to specify whether attached channels should be included in the export.
      - constraints:
          For use with exportSelected to specify whether attached constraints should be included in the export.
      - expressions:
          For use with exportSelected to specify whether attached expressions should be included in the export.
      - shader:
          For use with exportSelected to specify whether attached shaders should be included in the export.
      - preserveReferences:
          Modifies the various import/export flags such that references are imported/exported as actual references rather than
          copies of those references.
      - type:
          Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
          audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
          file types that match this file.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def imfPlugins(*args, **kwargs):
    """
    This command queries all the available imf plugins for its name, keyword or image file extension. Only one of the
    attributes (name, keyword or extension) can be queried at a time. If no flags are specified, this command returns a list
    of all available plugin names.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``extension`` / ``ext``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | image file extension                                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``keyword`` / ``key``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | imf keyword                                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``multiFrameSupport`` / ``mfs``                                                                      | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | multi frame IO is supported                                       Flag can have multiple arguments, passed either as a tuple or a list.                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pluginName`` / ``pn``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | imf plugin name                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``readSupport`` / ``rs``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | read operation is supported                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``writeSupport`` / ``ws``                                                                            | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | write operation is supported                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.imfPlugins`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.imfPlugins( query=True )
        # Result: [u'mentalrayCT', u'mentalrayMAP', u'mentalrayST', u'Alias', u'BMP (Microsoft Windows bitmap)', u'DDS', u'GIF', u'JPEG', u'Kodak Cineon', u'Maya Image', u'PNG', u'PostScript (Encapsulated)', u'Quantel', u'Silicon Graphics', u'Softimage', u'Sony Playstation', u'Targa', u'TIFF', u'Wavefront', u'XPM', u'Radiance Picture File'] #
        # returns a list of all imf plugin names
        pm.imfPlugins( 'pluginName', query=True, ext=True )
        # returns image file extension of the plugin
        pm.imfPlugins( 'pluginName', query=True, key=True )
        # returns IMF keyword of the plugin
        pm.imfPlugins( 'imfKeyWord', query=True, pn=True )
        # returns plugin name corresponding to imf keyword
        pm.imfPlugins( 'imfKeyWord', query=True, ws=True )
        # returns true if this plugin key supports write operations
        pm.imfPlugins( 'imfKeyWord', query=True, rs=True )
        # returns true if this plugin key supports read operations
        pm.imfPlugins( 'imfKeyWord', query=True, mfs=True )
        # returns true if this plugin key supports multiframe input/output
    """

    pass


def ogs(*args, **kwargs):
    """
    OGS is one of the viewport renderers. As there is a lot of effort involved in migrating functionality it will evolve
    over several releases. As it evolves it is prudent to provide safeguards to get the database back to a known state. That
    is the function of this command, similar to how 'dgdirty' is used to restore state to the dependency graph.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``deviceInformation`` / ``di``                                                                       | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If used then output the current device information.                                       Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``enableHardwareInstancing`` / ``hwi``                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Enables/disables new gpu instancing of instanceable render items in OGS.                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fragmentEditor`` / ``fe``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If used then launch the fragment editor UI.                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``gpuMemoryUsed`` / ``gpu``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If used then output the estimated amount of GPU memory in use (in MB).                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rebakeTextures`` / ``rbt``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If used then re-bake all baked textures for OGS.                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``regenerateUVTilePreview`` / ``rup``                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If used then regenerate all UV tiles preview textures for OGS.                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``reloadTextures`` / ``rlt``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If used then reload all textures for OGS.                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``reset`` / ``r``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If used then reset the entire OGS database for all viewports using it. In query mode the number of viewports that would be affected is returned but the reset is  |
    |  | not actually done.  If no viewport is using OGS then OGS will stop listening to DG changes.                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.ogs`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        // Reset the database for all panels running the OGS renderer.
        // Returns the number of panels affected.
        pm.ogs( reset=True )
        // Result: [modelPanel1] //
    """

    pass


def setInputDeviceMapping(*args, **kwargs):
    """
    The command sets a scale and offset for all attachments made to a specified device axis. Any attachment made to a mapped
    device axis will have the scale and offset applied to its values. The value from the device is multiplied by the scale
    and the offset is added to this product. With an absolute mapping, the attached attribute gets the resulting value. If
    the mapping is relative, the final value is the offset added to the scaled difference between the current device value
    and the previous device value. This mapping will be applied to the device data before any mappings defined by the
    setAttrMapping command. A typical use would be to scale a device's input so that it is within a usable range. For
    example, the device mapping can be used to calibrate a spaceball to work in a specific section of a scene. As an
    example, if the space ball is setup with absolute device mappings, constantly pressing in one direction will cause the
    attached attribute to get a constant value. If a relative mapping is used, and the spaceball is pressed in one
    direction, the attached attribute will jump a constantly increasing (or constantly decreasing) value and will find a
    rest value equal to the offset. There are important differences between how the relative flag is handled by this command
    and the setAttrMapping command. (See the setAttrMapping documentation for specifics on how it calculates relative
    values). In general, both a relative device mapping (this command) and a relative attachment mapping (setAttrMapping)
    should not be used together on the same axis.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``absolute`` / ``a``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | report absolute axis values                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``axis`` / ``ax``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify the axis to map                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``device`` / ``d``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify which device to map                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``offset`` / ``o``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify the axis offset value                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``relative`` / ``r``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | report the change in axis value since the last sample                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scale`` / ``s``                                                                                    | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify the axis scale value                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``view`` / ``v``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | translate the device coordinates into the coordinates of the active camera                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``world`` / ``w``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | translate the device coordinates into world space coordinates                     Flag can have multiple arguments, passed either as a tuple or a list.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.setInputDeviceMapping`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.assignInputDevice( '"move -r XAxis YAxis ZAxis"', d='spaceball' )
        pm.setInputDeviceMapping( d='spaceball', ax=['XAxis', 'YAxis', 'ZAxis'], scale=0.01, r=True )
        
        # The first command will assign the move command to the spaceball.
        # The second command will scale the three named axes by 0.01 and
        # only return the changes in device position.
    """

    pass


def _correctPath(path):
    pass


def importFile(filepath, **kwargs):
    """
    Import the specified file. Returns the name of the imported file.                         
    
    Flags:
      - loadNoReferences:
          This flag is obsolete and has been replaced witht the loadReferenceDepth flag. When used with the -open flag, no
          references will be loaded. When used with -i/import, -r/reference or -lr/loadReference flags, will load the top-most
          reference only.
      - loadReferenceDepth:
          Used to specify which references should be loaded. Valid types are all, noneand topOnly, which will load all references,
          no references and top-level references only, respectively. May only be used with the -o/open, -i/import, -r/reference or
          -lr/loadReference flags. When noneis used with -lr/loadReference, only path validation is performed. This can be used to
          replace a reference without triggering reload. Not using loadReferenceDepth will load references in the same loaded or
          unloaded state that they were in when the file was saved. Additionally, the -lr/loadReference flag supports a fourth
          type, asPrefs. This will force any nested references to be loaded according to the state (if any) stored in the current
          scene file, rather than according to the state saved in the reference file itself.
      - defaultNamespace:
          Use the default name space for import and referencing.  This is an advanced option.  If set, then on import or
          reference, Maya will attempt to place all nodes from the imported or referenced file directly into the root (default)
          name space, without invoking any name clash resolution algorithms.  If the names of any of the new objects    already
          exist in the root namespace, then errors will result. The user of this flag is responsible for creating a name clash
          resolution mechanism outside of Maya to avoid such errors. Note:This flag    is intended only for use with custom file
          translators written through    the API. Use at your own risk.
      - deferReference:
          When used in conjunction with the -reference flag, this flag determines if the reference is loaded, or if loading is
          deferred.C: The default is false.Q: When queried, this flag returns true if the reference is deferred, or false if the
          reference is not deferred. If this is used with -rfn/referenceNode, the -rfn flag must come before -q.
      - groupReference:
          Used only with the -r or the -i flag. Used to group all the imported/referenced items under a single transform.
      - groupName:
          Used only with the -gr flag. Optionally used to set the name of the transform node that the imported/referenced items
          will be grouped under.
      - renameAll:
          If true, rename all newly-created nodes, not just those whose names clash with existing nodes. Only available with
          -i/import.
      - renamingPrefix:
          The string to use as a prefix for all objects from this file. This flag has been replaced by -ns/namespace.
      - swapNamespace:
          Can only be used in conjunction with the -r/reference or -i/import flags. This flag will replace any occurrences of a
          given namespace to an alternate specified namespace. This namespace swapwill occur as the file is referenced in. It
          takes in two string arguments. The first argument specifies the namespace to replace. The second argument specifies the
          replacement namespace. Use of this flag, implicitly enables the use of namespaces and cannot be used with
          deferReference.
      - returnNewNodes:
          Used to control the return value in open, import, loadReference, and reference operations. It will force the file
          command to return a list of new nodes added to the current scene.
      - preserveReferences:
          Modifies the various import/export flags such that references are imported/exported as actual references rather than
          copies of those references.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def _setTypeKwargFromExtension(path, kwargs, mode='write'):
    pass


def createReference(filepath, **kwargs):
    """
    Create a reference to the specified file. Returns the name of the file referenced.Query all file references from the specified file.                      
    
    Flags:
      - loadNoReferences:
          This flag is obsolete and has been replaced witht the loadReferenceDepth flag. When used with the -open flag, no
          references will be loaded. When used with -i/import, -r/reference or -lr/loadReference flags, will load the top-most
          reference only.
      - loadReferenceDepth:
          Used to specify which references should be loaded. Valid types are all, noneand topOnly, which will load all references,
          no references and top-level references only, respectively. May only be used with the -o/open, -i/import, -r/reference or
          -lr/loadReference flags. When noneis used with -lr/loadReference, only path validation is performed. This can be used to
          replace a reference without triggering reload. Not using loadReferenceDepth will load references in the same loaded or
          unloaded state that they were in when the file was saved. Additionally, the -lr/loadReference flag supports a fourth
          type, asPrefs. This will force any nested references to be loaded according to the state (if any) stored in the current
          scene file, rather than according to the state saved in the reference file itself.
      - defaultNamespace:
          Use the default name space for import and referencing.  This is an advanced option.  If set, then on import or
          reference, Maya will attempt to place all nodes from the imported or referenced file directly into the root (default)
          name space, without invoking any name clash resolution algorithms.  If the names of any of the new objects    already
          exist in the root namespace, then errors will result. The user of this flag is responsible for creating a name clash
          resolution mechanism outside of Maya to avoid such errors. Note:This flag    is intended only for use with custom file
          translators written through    the API. Use at your own risk.
      - deferReference:
          When used in conjunction with the -reference flag, this flag determines if the reference is loaded, or if loading is
          deferred.C: The default is false.Q: When queried, this flag returns true if the reference is deferred, or false if the
          reference is not deferred. If this is used with -rfn/referenceNode, the -rfn flag must come before -q.
      - groupReference:
          Used only with the -r or the -i flag. Used to group all the imported/referenced items under a single transform.
      - groupLocator:
          Used only with the -r and the -gr flag. Used to group the output of groupReference under a locator
      - groupName:
          Used only with the -gr flag. Optionally used to set the name of the transform node that the imported/referenced items
          will be grouped under.
      - namespace:
          The namespace name to use that will group all objects during importing and referencing. Change the namespace used to
          group all the objects from the specified referenced file. The reference must have been created with the Using
          Namespacesoption, and must be loaded. Non-referenced nodes contained in the existing namespace will also be moved to the
          new namespace. The new namespace will be created by this command and can not already exist. The old namespace will be
          removed.
      - referenceNode:
          This flag is only used during queries. In MEL, if it appears before -query then it must be followed by the name of one
          of the scene's reference nodes. That will determine the reference to be queried by whatever flags appear after -query.
          If the named reference node does not exist within the scene the command will fail with an error. In Python the
          equivalent behavior is obtained by passing the name of the reference node as the flag's value. In MEL, if this flag
          appears after -query then it takes no argument and will cause the command to return the name of the reference node
          associated with the file given as the command's argument. If the file is not a reference or for some reason does not
          have a reference node (e.g. the user deleted it) then an empty string will be returned. If the file is not part of the
          current scene then the command will fail with an error. In Python the equivalent behavior is obtained by passing True as
          the flag's value.       In query mode, this flag can accept a value.
      - renamingPrefix:
          The string to use as a prefix for all objects from this file. This flag has been replaced by -ns/namespace.
      - swapNamespace:
          Can only be used in conjunction with the -r/reference or -i/import flags. This flag will replace any occurrences of a
          given namespace to an alternate specified namespace. This namespace swapwill occur as the file is referenced in. It
          takes in two string arguments. The first argument specifies the namespace to replace. The second argument specifies the
          replacement namespace. Use of this flag, implicitly enables the use of namespaces and cannot be used with
          deferReference.
      - sharedReferenceFile:
          Can only be used in conjunction with the -r/reference flag and the -ns/namespace flag (there is no prefix support). This
          flag modifies the '-r/reference' flag to indicate that all nodes within that reference should be treated as shared
          nodes. New copies    of those nodes will not be created if a copy already exists. Instead, the shared node will be
          merged with the existing node. The specifics of what happens when two nodes are merged depends on the node type. This
          flag cannot be used in conjunction with -shd/sharedNodes.
      - sharedNodes:
          This flag modifies the '-r/reference' flag to indicate that certain    types of nodes within that reference should be
          treated as shared nodes. All shared nodes will be placed in the default namespace. New copies of those nodes will not be
          created if a copy already exists in the default namespace, instead the shared node will be merged with the    existing
          node. The specifics of what happens when two nodes are merged depends on the node type. In general attribute values will
          not be merged, meaning the values set on any existing shared nodes will be retained, and the values of the nodes being
          merged in will be ignored. The valid options are displayLayers, shadingNetworks, renderLayersByName, and
          renderLayersById. This flag is multi-use; it may be specified multiple times to for example, share both display layers
          and shading networks. Two shading networks will only be merged if    they are identical: the network    of nodes feeding
          into the shading group must be arranged identically with equivalent nodes have the same name and node type. Additionally
          if a network is animated or contains a DAG object or expression it will not be mergeable. This flag cannot be used in
          conjunction with -srf/sharedReferenceFile.
      - returnNewNodes:
          Used to control the return value in open, import, loadReference, and reference operations. It will force the file
          command to return a list of new nodes added to the current scene.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def listInputDevices(*args, **kwargs):
    """
    This command lists all input devices that maya knows about.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``free`` / ``f``                                                                                     | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``primary`` / ``p``                                                                                  | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``secondary`` / ``s``                                                                                | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.listInputDevices`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Returns a list of devices.
        pm.listInputDevices()
        # Result: [u'melvin', u'virtualClock'] #
    """

    pass


def date(*args, **kwargs):
    """
    Returns information about current time and date. Use the predefined formats, or the -formatflag to specify the output
    format.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``date`` / ``d``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the current date. Format is YYYY/MM/DD                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``format`` / ``f``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies a string defining how the date and time should be represented. All occurences of the keywords below will be replaced with the corresponding values:     |
    |  | KeywordBecomesYYYYCurrent year, using 4 digitsYYLast two digits of the current yearMMCurrent month, with leading 0 if necessaryDDCurrent day, with leading 0 if   |
    |  | necessaryhhCurrent hour, with leading 0 if necessarymmCurrent minute, with leading 0 if necessaryssCurrent second, with leading 0 if necessaryFlag can have       |
    |  | multiple arguments, passed either as a tuple or a list.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shortDate`` / ``sd``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the current date. Format is MM/DD                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shortTime`` / ``st``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the current time. Format is hh:mm                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``time`` / ``t``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the current time. Format is hh:mm:ss                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.date`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Get the current date and time
        pm.date()
        # Result: u'2013/02/18 19:14:25' #
        # Get only the month and day
        pm.date( shortDate=True )
        # Result: u'02/18' #
        # Get the date and time in a fancy format
        pm.date( format='Year is YY (or YYYY), month is MM, day is DD. And it is now hh:mm:ss' )
        # Result: u'Year is 13 (or 2013), month is 02, day is 18. And it is now 19:14:25' #
    """

    pass


def feof(fileid):
    """
    Reproduces the behavior of the mel command of the same name. if writing pymel scripts from scratch,
    you should use a more pythonic construct for looping through files:
    
    >>> f = open('myfile.txt') # doctest: +SKIP
    ... for line in f:
    ...     print line
    
    This command is provided for python scripts generated by mel2py
    """

    pass


def deviceEditor(*args, **kwargs):
    """
    This creates an editor for creating/modifying attachments to input devices.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``control`` / ``ctl``                                                                                | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible, at times, for an     |
    |  | editor to exist without a control. This flag returns NONEif no control is present.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``defineTemplate`` / ``dt``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Puts a command in a mode where any other flags and args are parsed and added to the command template specified in the argument. They will be used as default      |
    |  | arguments in any subsequent invocations of the command when templateName is set as the current template.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``docTag`` / ``dtg``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attaches a tag to the Maya editor.                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exists`` / ``ex``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true|false depending upon whether the specified object exists.  Other flags are ignored.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``filter`` / ``f``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of an itemFilter object to be placed on this editor. This filters the information coming onto the main list of the editor.                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``forceMainConnection`` / ``fmc``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will use as its source of content.  The editor will only display items contained in the       |
    |  | selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used|
    |  | to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``highlightConnection`` / ``hlc``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will synchronize with its highlight list.  Not all editors have a highlight list. For those   |
    |  | that do, it is a secondary selection list.                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lockMainConnection`` / ``lck``                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original          |
    |  | mainConnection are ignored.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mainListConnection`` / ``mlc``                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will use as its source of content.  The editor will only display items contained in the       |
    |  | selectionConnection object.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``panel`` / ``pnl``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the panel that the editor belongs to.  By default if an editor is created in the create callback of a scripted panel it will belong to that panel.  If  |
    |  | an editor doesn't belong to a panel it will be deleted when the window that it is in is deleted.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``parent`` / ``p``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectionConnection`` / ``slc``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will synchronize with its own selection list.  As the user selects things in this editor, they|
    |  | will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the change.                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stateString`` / ``sts``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query only flag.  Returns the MEL command that will edit an editor to match the current editor state. The returned command string uses the string variable        |
    |  | $editorName in place of a specific name.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``takePath`` / ``tp``                                                                                | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The path used for writing/reading take data through the editor.                   Flag can have multiple arguments, passed either as a tuple or a list.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unParent`` / ``up``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies that the editor should be removed from its layout. This cannot be used with query.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unlockMainConnection`` / ``ulk``                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``updateMainConnection`` / ``upd``                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``useTemplate`` / ``ut``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Force the command to use a command template other than the current one.                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.deviceEditor`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # This example creates a new device editor in its own window
        window = pm.window()
        pm.paneLayout()
        # Result: ui.PaneLayout('window1|paneLayout3') #
        pm.deviceEditor('myDeviceEditor')
        # Result: ui.DeviceEditor('myDeviceEditor') #
        pm.showWindow( window )
    """

    pass


def attrCompatibility(*args, **kwargs):
    """
    This command is used by Maya to handle compatibility issues between file format versions by providing a mechanism to
    describe differences between two versions.  Plug-in writers can make use of this command to handle attribute
    compatibility changes to files.The first optional command argument argument is a node type name and the second optional
    command argument is the short name of an attribute.Warning:Only use this command to describe changes in names or
    attributes of nodes that youhave written as plugins.  Do notuse this command to change information about builtin
    dependency graph nodes. Removing attributes on a plug-in node is a special case. Use a separate attrCompatibility call
    with pluginNode flag and name so that these attributes can be tracked even though the plug-in may not be loaded. Only
    one flag may be used per invocation of the command. If multiple flags are provided one will arbitrarily be chosen as the
    action to perform and the others will be silently ignored.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``addAttr`` / ``a``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Add the given attribute to the named node.                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``clear`` / ``clr``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Clear out the compatibility table. This is only used internally for debugging purposes.                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dumpTable`` / ``dmp``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Dump the current contents of the compatibility table. This is only used internally for debugging purposes.                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``enable`` / ``e``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Enable or disable the compatibility table. This is only used internally for debugging purposes.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``nodeRename`` / ``nr``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Replace all uses of the node type 'nodeName' with given string.                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pluginNode`` / ``pn``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Registers the string argument as a plug-in node type. This is necessary for subsequent attrCompatibility calls that reference node attributes of unloaded plug-   |
    |  | ins. Specifically, this works in the case when attributes are being removed.                       Flag can have multiple arguments, passed either as a tuple or a|
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeAttr`` / ``rm``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Remove the given attribute from the named node.                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``renameAttr`` / ``r``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Change the short name of the attribute specified in the command's arguments to the new short name provided as a parameter to this flag. Once the mapping between  |
    |  | short names has been established, Maya will handle the long names automatically.                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``typ``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Change the type of the given attribute to the given type.                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``version`` / ``v``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the version target for subsequent commands to the given string.                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.attrCompatibility`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Rename '.x' attributes in old files to '.tx' for all nodes
        # of type 'transform'
        #
        pm.attrCompatibility( 'transform', 'x', r='tx' )
        
        # Rename the old 'group' node to the new 'transform' node
        #
        pm.attrCompatibility( 'group', nr='transform' )
        
        # This will cause all subsequent attrCompatibility calls to translate
        # files from older versions to version 1.0.
        #
        pm.attrCompatibility( v='1.0' )
    """

    pass


def preloadRefEd(*args, **kwargs):
    """
    This creates an editor for managing which references will be read in (loaded) and which deferred (unloaded) upon opening
    a file.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``control`` / ``ctl``                                                                                | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible, at times, for an     |
    |  | editor to exist without a control. This flag returns NONEif no control is present.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``defineTemplate`` / ``dt``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Puts a command in a mode where any other flags and args are parsed and added to the command template specified in the argument. They will be used as default      |
    |  | arguments in any subsequent invocations of the command when templateName is set as the current template.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``docTag`` / ``dtg``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attaches a tag to the Maya editor.                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exists`` / ``ex``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true|false depending upon whether the specified object exists.  Other flags are ignored.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``filter`` / ``f``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of an itemFilter object to be placed on this editor. This filters the information coming onto the main list of the editor.                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``forceMainConnection`` / ``fmc``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will use as its source of content.  The editor will only display items contained in the       |
    |  | selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used|
    |  | to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``highlightConnection`` / ``hlc``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will synchronize with its highlight list.  Not all editors have a highlight list. For those   |
    |  | that do, it is a secondary selection list.                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lockMainConnection`` / ``lck``                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original          |
    |  | mainConnection are ignored.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mainListConnection`` / ``mlc``                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will use as its source of content.  The editor will only display items contained in the       |
    |  | selectionConnection object.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``panel`` / ``pnl``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the panel that the editor belongs to.  By default if an editor is created in the create callback of a scripted panel it will belong to that panel.  If  |
    |  | an editor doesn't belong to a panel it will be deleted when the window that it is in is deleted.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``parent`` / ``p``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectCommand`` / ``sc``                                                                           | *callable*                    |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectFileNode`` / ``sf``                                                                          | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the currently selected load setting. Returns the id of the currently selected load setting. This id can be used as an argument to the selLoadSettings       |
    |  | command.                      Flag can have multiple arguments, passed either as a tuple or a list.                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectionConnection`` / ``slc``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will synchronize with its own selection list.  As the user selects things in this editor, they|
    |  | will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the change.                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stateString`` / ``sts``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query only flag.  Returns the MEL command that will edit an editor to match the current editor state. The returned command string uses the string variable        |
    |  | $editorName in place of a specific name.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unParent`` / ``up``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies that the editor should be removed from its layout. This cannot be used with query.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unlockMainConnection`` / ``ulk``                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``updateMainConnection`` / ``upd``                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``useTemplate`` / ``ut``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Force the command to use a command template other than the current one.                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.preloadRefEd`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        window = pm.window()
        pm.paneLayout()
        # Result: ui.PaneLayout('window1|paneLayout10') #
        pm.preloadRefEd()
        # Result: u'preloadRefEd1' #
        pm.showWindow(window)
    """

    pass


def listNamespaces(root=None, recursive=False, internal=False):
    """
    Returns a list of the namespaces in the scene
    """

    pass


def untitledFileName():
    """
    Obtain the base filename used for untitled scenes. In localized environments, this string will contain a translated value.
    """

    pass


def dgmodified(*args, **kwargs):
    """
    The dgmodifiedcommand is used to find out which nodes in the           dependency graph have been modified.  This is
    mostly useful for fixing           instances where file new asks you to save when no changes have been           made to
    the scene.
    
    
    Derived from mel command `maya.cmds.dgmodified`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # list all modified nodes
        pm.dgmodified()
    """

    pass


def openGLExtension(*args, **kwargs):
    """
    Command returns the extension name depending on whether a given OpenGL extension is supported or not. The input is the
    extension string to the -extension flag. If the -extension flag is not used, or if the string argument to this flag is
    an empty string than all extension names are returned in a single string. If the extension exists it is not necessary
    true that the extension is supported. This command can only be used when a modeling view has been created. Otherwise no
    extensions will have been initialized and the resulting string will always be the empty string.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``extension`` / ``ext``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the OpenGL extension to query.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``renderer`` / ``rnd``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies to query the OpenGL renderer.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``vendor`` / ``vnd``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies to query the company responsible for the OpenGL implementation.                                         Flag can have multiple arguments, passed either |
    |  | as a tuple or a list.                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``version`` / ``ver``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies to query the OpenGL version.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.openGLExtension`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Query for the multitexturing extension GL_ARB_multitexture
        pm.openGLExtension( extension='GL_ARB_multitexture' )
        # Result: u'GL_ARB_multitexture' #
        # Query for all the extensions
        pm.openGLExtension( extension='' )
        # Result: u'GL_ARB_transpose_matrix GL_ARB_vertex_program GL_ARB_vertex_blend GL_ARB_window_pos GL_ARB_shader_objects GL_ARB_vertex_shader GL_ARB_shading_language_100 GL_EXT_multi_draw_arrays GL_EXT_clip_volume_hint GL_EXT_rescale_normal GL_EXT_draw_range_elements GL_EXT_fog_coord GL_EXT_gpu_program_parameters GL_EXT_geometry_shader4 GL_EXT_transform_feedback GL_APPLE_client_storage GL_APPLE_specular_vector GL_APPLE_transform_hint GL_APPLE_packed_pixels GL_APPLE_fence GL_APPLE_vertex_array_object GL_APPLE_vertex_program_evaluators GL_APPLE_element_array GL_APPLE_flush_render GL_APPLE_aux_depth_stencil GL_NV_texgen_reflection GL_NV_light_max_exponent GL_IBM_rasterpos_clip GL_SGIS_generate_mipmap GL_ARB_imaging GL_ARB_point_parameters GL_ARB_texture_env_crossbar GL_ARB_texture_border_clamp GL_ARB_multitexture GL_ARB_texture_env_add GL_ARB_texture_cube_map GL_ARB_texture_env_dot3 GL_ARB_multisample GL_ARB_texture_env_combine GL_ARB_texture_compression GL_ARB_texture_mirrored_repeat GL_ARB_shadow GL_ARB_depth_texture GL_ARB_fragment_program GL_ARB_fragment_program_shadow GL_ARB_fragment_shader GL_ARB_occlusion_query GL_ARB_point_sprite GL_ARB_texture_non_power_of_two GL_ARB_vertex_buffer_object GL_ARB_pixel_buffer_object GL_ARB_draw_buffers GL_ARB_shader_texture_lod GL_ARB_half_float_vertex GL_EXT_compiled_vertex_array GL_EXT_framebuffer_object GL_EXT_texture_rectangle GL_ARB_texture_rectangle GL_EXT_texture_env_add GL_EXT_blend_color GL_EXT_blend_minmax GL_EXT_blend_subtract GL_EXT_texture_lod_bias GL_EXT_abgr GL_EXT_bgra GL_EXT_stencil_wrap GL_EXT_texture_filter_anisotropic GL_EXT_secondary_color GL_EXT_blend_func_separate GL_EXT_shadow_funcs GL_EXT_stencil_two_side GL_EXT_depth_bounds_test GL_EXT_texture_compression_s3tc GL_EXT_texture_compression_dxt1 GL_EXT_texture_sRGB GL_EXT_blend_equation_separate GL_EXT_texture_mirror_clamp GL_EXT_packed_depth_stencil GL_EXT_provoking_vertex GL_APPLE_flush_buffer_range GL_APPLE_ycbcr_422 GL_APPLE_rgb_422 GL_APPLE_vertex_array_range GL_APPLE_texture_range GL_APPLE_float_pixels GL_ATI_texture_float GL_ARB_texture_float GL_ARB_half_float_pixel GL_APPLE_pixel_buffer GL_APPLE_object_purgeable GL_NV_point_sprite GL_NV_blend_square GL_NV_fog_distance GL_NV_depth_clamp GL_NV_multisample_filter_hint GL_NV_fragment_program_option GL_NV_fragment_program2 GL_NV_vertex_program2_option GL_NV_vertex_program3 GL_ATI_texture_mirror_once GL_ATI_texture_env_combine3 GL_ATI_separate_stencil GL_SGIS_texture_edge_clamp GL_SGIS_texture_lod GL_EXT_vertex_array_bgra ' #
        # Query for the renderer name
        pm.openGLExtension( renderer=True )
        # Result: u'NVIDIA GeForce 7300 GT OpenGL Engine' #
        # Query for the vendor
        pm.openGLExtension( vendor=True )
        # Result: u'NVIDIA Corporation' #
        # Query for the OpenGL version
        pm.openGLExtension( version=True )
        # Result: u'2.1 NVIDIA-1.6.36' #
    """

    pass


def fileBrowserDialog(*args, **kwargs):
    """
    The fileBrowserDialog and fileDialog commands have now been deprecated. Both commands are still callable, but it is
    recommended that the fileDialog2 command be used instead.  To maintain some backwards compatibility, both
    fileBrowserDialog and fileDialog will convert the flags/values passed to them into the appropriate flags/values that the
    fileDialog2 command uses and will call that command internally.  It is not guaranteed that this compatibility will be
    able to be maintained in future versions so any new scripts that are written should use fileDialog2. See below for an
    example of how to change a script to use fileDialog2.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``actionName`` / ``an``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Script to be called when the file is validated.                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dialogStyle`` / ``ds``                                                                             | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | 0 for old style dialog1 for Windows 2000 style Explorer style2 for Explorer style with Shortcuttip at bottom                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fileCommand`` / ``fc``                                                                             | *script*                      | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The script to run on command action                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fileType`` / ``ft``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the type of file to filter.  By default this can be any one of: mayaAscii, mayaBinary, mel, OBJ, directory, plug-in, audio, move, EPS, Illustrator, image.    |
    |  | plug-ins may define their own types as well.                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``filterList`` / ``fl``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify file filters. Used with dialog style 1 and 2. Each string should be a description followed by a comma followed by a semi-colon separated list of file     |
    |  | extensions with wildcard.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``includeName`` / ``includeName``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Include the given string after the actionName in parentheses. If the name is too long, it will be shortened to fit on the dialog (for example,                    |
    |  | /usr/alias/commands/scripts/fileBrowser.mel might be shortened to /usr/...pts/fileBrowser.mel)                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mode`` / ``m``                                                                                     | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Defines the mode in which to run the file brower: 0 for read1 for write2 for write without paths (segmented files)4 for directories have meaning when used with   |
    |  | the action+100 for returning short names                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``operationMode`` / ``om``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Enables the option dialog. Valid strings are: ImportReferenceSaveAsExportAllExportActive                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``tipMessage`` / ``tm``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Message to be displayed at the bottom of the style 2 dialog box.                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``windowTitle`` / ``wt``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the window title of a style 1 or 2 dialog box                         Flag can have multiple arguments, passed either as a tuple or a list.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.fileBrowserDialog`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Old way:
        def importImage( fileName, fileType):
           pm.file( fileName, i=True );
           return 1
        
        pm.fileBrowserDialog( m=0, fc=importImage, ft='image', an='Import_Image', om='Import' )
        
        # Recommended way:
        filename = pm.fileDialog2(fileMode=1, caption="Import Image")
        pm.file( filename[0], i=True );
    """

    pass


def assignInputDevice(*args, **kwargs):
    """
    This command associates a command string (i.e. a mel script) with the input device.  When the device moves or a button
    on the device is pressed, the command string is executed as if you typed it into the window.  If the command string
    contains the names of buttons or axes of the device, the current value of these buttons/axes are substituted in.
    Buttons are reported as booleans and axes as doubles. This command is most useful for associating buttons on a device
    with commands.  For using a device to capture continous movements it is much more efficient to attach the device
    directly into the dependency graph.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``clutch`` / ``c``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify a clutch button.  This button must be down for the command string to be executed. If no clutch is specified the command string is executed everytime the  |
    |  | device state changes                                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``continuous`` / ``ct``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | if this flag is set the command string is continously (once for everytime the device changes state).  By default if a clutch button is specified the command      |
    |  | string is only executed once when the button is pressed.                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``device`` / ``d``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify which device to assign the command string.                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``immediate`` / ``im``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Immediately executes the command, without using the queue.                        Flag can have multiple arguments, passed either as a tuple or a list.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``multiple`` / ``m``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | if this flag is set the other command strings associated with this device are not deleted. By default, when a new command string is attached to the device, all   |
    |  | other command strings are deleted.                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.assignInputDevice`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.assignInputDevice( 'setKeyframe', d='spaceball', c='Button1' )
        
        # This command will assign button1 on the spaceball with
        # the setKeyframe command.  This is very much like using
        # the spaceball buttons as hotkeys.
        
        pm.assignInputDevice( '"currentTime -e Axis0"', d='midi', ct=True, m=True )
        
        # This command will execute the command to set the time
        # to the value of the first midi slider.  As the slider
        # moves this command will be executed.  So the slider
        # will control time.
    """

    pass


def namespaceInfo(*args, **kwargs):
    """
    This command displays information about a namespace. The target namespace can optionally be specified on the command
    line. If no namespace is specified, the command will display information about the current namespace. A namespace is a
    simple grouping of objects under a given name. Each item in a namespace can then be identified by its own name, along
    with what namespace it belongs to.  Namespaces can contain other namespaces like sets, with the restriction that all
    namespaces are disjoint. Namespaces are primarily used to resolve name-clash issues in Maya, where a new object has the
    same name as an existing object (from importing a file, for example). Using namespaces, you can have two objects with
    the same name, as long as they are contained in different namespaces. Note that namespaces are a simple grouping of
    names, so they do not effect selection, the DAG, the Dependency Graph, or any other aspect of Maya.  All namespace names
    are colon-separated. The namespace format flags are: baseName(shortName), fullNameand absoluteName. The flags are used
    in conjunction with the main query flags to specify the desired namespace format of the returned result. They can also
    be used to return the different formats of a specified namespace. By default, when no format is specified, the result
    will be returned as a full name.
    
    Modifications:
        - returns an empty list when the result is None
        - returns wrapped classes for listOnlyDependencyNodes
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``absoluteName`` / ``an``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The absolute name of the namespace is a full |
    |  | namespace path, starting from the root namespace :and including all parent namespaces.  For example :ns:ballis an absolute namespace name while ns:ballis not. The|
    |  | absolute namespace name is invariant and is not affected by the current namespace or relative namespace modes. See also other format modifiers 'baseName',        |
    |  | 'fullName', etc                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``baseName`` / ``bn``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The base name of the namespace contains only |
    |  | the leaf level name and does not contain its parent namespace(s). For example the base name of an object named ns:ballis ball. This mode will always return the   |
    |  | base name in the same manner, and is not affected by the current namespace or relative namespace mode. See also other format modifiers 'absoluteName', 'fullName',|
    |  | etc The flag 'shortName' is a synonym for 'baseName'.                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``currentNamespace`` / ``cur``                                                                       | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Display the name of the current namespace.                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dagPath`` / ``dp``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag modifies the 'listNamespace' and 'listOnlyDependencyNodes' flags to indicate that the names of any dag objects returned will include as much of the dag |
    |  | path as is necessary to make the names unique. If this flag is not present, the names returned will not include any dag paths.                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fullName`` / ``fn``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The full name of the namespace contains both |
    |  | the namespace path and the base name, but without the leading colon representing the root namespace. For example ns:ballis a full name, whereas :ns:ballis an     |
    |  | absolute name. This mode is affected by the current namespace and relative namespace modes. See also other format modifiers 'baseName', 'absoluteName', etc.      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``internal`` / ``int``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used together with the 'listOnlyDependencyNodes' flag. When this flag is set, the returned list will include internal nodes (for example itemFilters)|
    |  | that are not listed by default.                        Flag can have multiple arguments, passed either as a tuple or a list.                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``isRootNamespace`` / ``ir``                                                                         | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true if the namespace is root(:), false if not.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listNamespace`` / ``ls``                                                                           | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List the contents of the namespace.                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listOnlyDependencyNodes`` / ``lod``                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List all dependency nodes in the namespace.                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listOnlyNamespaces`` / ``lon``                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List all namespaces in the namespace.                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``parent`` / ``p``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Display the parent of the namespace. By default, the list returned will not include internal nodes (such as itemFilters). To include the internal nodes, use the  |
    |  | 'internal' flag.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``recurse`` / ``r``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Can be specified with 'listNamespace', 'listOnlyNamespaces' or 'listOnlyDependencyNode' to cause the listing to recursively include any child namespaces of the   |
    |  | namespaces;                                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shortName`` / ``sn``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is deprecated and may be removed in future releases of Maya. It is a synonym for the baseName flag. Please use the baseName flag instead.               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.namespaceInfo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # List the contents of the current namespace
        #
        pm.namespaceInfo( listNamespace=True )
        # Result: [u'CubeCompass', u'CustomGPUCacheFilter', u'DefaultAllLightsFilter', u'DefaultAllLightsFilter1', u'DefaultAllLightsFilter2', u'DefaultAllLightsFilter6', u'DefaultAllRenderClassificationsFilter', u'DefaultAllRenderClassificationsFilter1', u'DefaultAllRenderNodesFilter', u'DefaultAllShadingNodesFilter', u'DefaultBakeSetsFilter', u'DefaultBakeSetsFilter2', u'DefaultBasicRenderNodesFilter', u'DefaultCameraShapesFilter', u'DefaultCameraShapesFilter1', u'DefaultCameraShapesFilter4', u'DefaultCameraShapesImagePlanesFilter', u'DefaultCameraShapesImagePlanesFilter3', u'DefaultContainerFilter', u'DefaultContainerNodeFilter', u'DefaultExclLightShapesFilter', u'DefaultGeometryFilter', u'DefaultHiddenAttributesFilter', u'DefaultIkHandlesFilter', u'DefaultImagePlanesFilter', u'DefaultImagePlanesFilter1', u'DefaultImagePlanesFilter4', u'DefaultJointsFilter', u'DefaultLightLinkingLightFilter', u'DefaultLightShapesFilter', u'DefaultLightShapesPostProcsFilter', u'DefaultLightShapesPostProcsFilter1', u'DefaultLightShapesPostProcsFilter2', u'DefaultLightShapesTexturesFilter', u'DefaultLightShapesTexturesFilter1', u'DefaultLightsAndOpticalFXFilter', u'DefaultLightsAndOpticalFXFilter4', u'DefaultMaterialsAndShaderGlowFilter', u'DefaultMaterialsAndShaderGlowFilter6', u'DefaultMaterialsFilter', u'DefaultMaterialsFilter1', u'DefaultMaterialsFilter2', u'DefaultMaterialsFilter8', u'DefaultMaterialsTexturesLightShapesFilter', u'DefaultMaterialsTexturesLightShapesFilter1', u'DefaultMrContourContrastFilter', u'DefaultMrContourOutputFilter', u'DefaultMrContourShaderFilter', u'DefaultMrContourStoreFilter', u'DefaultMrDataConversionFilter', u'DefaultMrDisplacementFilter', u'DefaultMrEmitterFilter', u'DefaultMrEnvironmentFilter', u'DefaultMrGeometryFilter', u'DefaultMrLensFilter', u'DefaultMrLightFilter', u'DefaultMrLightmapFilter', u'DefaultMrMaterialFilter', u'DefaultMrMiscFilter', u'DefaultMrNodesFilter', u'DefaultMrOutputFilter', u'DefaultMrPhotonFilter', u'DefaultMrPhotonVolumeFilter', u'DefaultMrSampleCompositingFilter', u'DefaultMrShadowFilter', u'DefaultMrStateFilter', u'DefaultMrTextureFilter', u'DefaultMrVolumeFilter', u'DefaultNURBSObjectsFilter', u'DefaultNoShaderGlowFilter', u'DefaultNonExclLightShapesFilter', u'DefaultOpticalFXFilter', u'DefaultOpticalFXFilter1', u'DefaultOpticalFXFilter5', u'DefaultPolygonObjectsFilter', u'DefaultPostProcFilter', u'DefaultRenderUtilitiesFilter', u'DefaultRenderUtilitiesFilter5', u'DefaultRenderingFilter', u'DefaultSGLightShapesFilter', u'DefaultSGLightShapesTexturesFilter', u'DefaultSetsFilter', u'DefaultShaderGlowFilter', u'DefaultShaderGlowFilter1', u'DefaultShaderGlowFilter2', u'DefaultShaderGlowFilter8', u'DefaultShadingGroupsAndMaterialsFilter', u'DefaultShadingGroupsFilter', u'DefaultShadingGroupsFilter1', u'DefaultShadingGroupsFilter2', u'DefaultShadingGroupsFilter3', u'DefaultShadingGroupsFilter4', u'DefaultShadingGroupsFilter5', u'DefaultShadingGroupsFilter6', u'DefaultShadingGroupsFilter7', u'DefaultShadingGroupsFilter8', u'DefaultSubdivObjectsFilter', u'DefaultTextures2dFilter', u'DefaultTextures3dFilter', u'DefaultTexturesFilter', u'DefaultTexturesFilter1', u'DefaultTexturesFilter7', u'DefaultTexturesSGFilter', u'DefaultUsesImageFileFilter', u'Manipulator1', u'UI', u'UniversalManip', u'animCurveFilter', u'animLayersFilter', u'characterPartition', u'characterSetsFilter', u'clipsFilter', u'clusterSetsFilter', u'defaultCreaseDataSet', u'defaultHardwareRenderGlobals', u'defaultLayer', u'defaultLightList1', u'defaultLightSet', u'defaultObjectSet', u'defaultRenderGlobals', u'defaultRenderLayer', u'defaultRenderLayerFilter', u'defaultRenderQuality', u'defaultRenderUtilityList1', u'defaultRenderingList1', u'defaultResolution', u'defaultSetFilter', u'defaultShaderList1', u'defaultTextureList1', u'defaultViewColorManager', u'deformerSetsFilter', u'dof1', u'drivenKeyFilter', u'dynController1', u'dynamicFilter', u'expressionFilter', u'front', u'frontShape', u'globalCacheControl', u'groundPlane', u'groundPlane_transform', u'hardwareRenderGlobals', u'hardwareRenderingGlobals', u'hyperGraphInfo', u'hyperGraphLayout', u'ikSystem', u'initialMaterialInfo', u'initialParticleSE', u'initialShadingGroup', u'jointClusterSetsFilter', u'keyableFilter', u'lambert1', u'latticeSetsFilter', u'layerManager', u'layersFilter', u'lightLinker1', u'lightLinkingObjectFilter', u'lightList1', u'lightSetFilter', u'lightSetFilter1', u'nonLinearSetsFilter', u'notAnimLayersFilter', u'objectAttrFilter1', u'objectAttrFilter2', u'objectAttrFilter3', u'objectAttrFilter4', u'objectAttrFilter5', u'objectAttrFilter6', u'objectAttrFilter7', u'objectAttrFilter8', u'objectFilter17', u'objectFilter18', u'objectFilter19', u'objectFilter20', u'objectFilter21', u'objectNameFilter1', u'objectNameFilter2', u'objectNameFilter3', u'objectNameFilter4', u'objectScriptFilter1', u'objectScriptFilter2', u'objectScriptFilter3', u'objectScriptFilter4', u'objectScriptFilter5', u'objectScriptFilter6', u'objectScriptFilter7', u'objectScriptFilter8', u'objectScriptFilter9', u'objectScriptFilter10', u'objectTypeFilter1', u'objectTypeFilter2', u'objectTypeFilter3', u'objectTypeFilter4', u'objectTypeFilter5', u'objectTypeFilter6', u'objectTypeFilter7', u'objectTypeFilter8', u'objectTypeFilter9', u'objectTypeFilter10', u'objectTypeFilter11', u'objectTypeFilter12', u'objectTypeFilter13', u'objectTypeFilter14', u'objectTypeFilter15', u'objectTypeFilter16', u'objectTypeFilter17', u'objectTypeFilter18', u'objectTypeFilter19', u'objectTypeFilter20', u'objectTypeFilter21', u'objectTypeFilter22', u'objectTypeFilter23', u'objectTypeFilter24', u'objectTypeFilter25', u'objectTypeFilter26', u'objectTypeFilter27', u'objectTypeFilter28', u'objectTypeFilter29', u'objectTypeFilter30', u'objectTypeFilter31', u'objectTypeFilter32', u'objectTypeFilter33', u'objectTypeFilter34', u'objectTypeFilter35', u'objectTypeFilter36', u'objectTypeFilter37', u'objectTypeFilter38', u'objectTypeFilter39', u'objectTypeFilter40', u'objectTypeFilter41', u'objectTypeFilter42', u'objectTypeFilter43', u'objectTypeFilter44', u'objectTypeFilter45', u'objectTypeFilter46', u'objectTypeFilter47', u'objectTypeFilter48', u'objectTypeFilter49', u'objectTypeFilter50', u'objectTypeFilter51', u'objectTypeFilter52', u'objectTypeFilter67', u'objectTypeFilter68', u'objectTypeFilter69', u'objectTypeFilter70', u'objectTypeFilter71', u'objectTypeFilter72', u'objectTypeFilter73', u'objectTypeFilter74', u'objectTypeFilter75', u'objectTypeFilter76', u'objectTypeFilter77', u'objectTypeFilter78', u'objectTypeFilter79', u'otherDeformerSetsFilter', u'particleCloud1', u'partitionFilter', u'persp', u'perspShape', u'polyMergeEdgeToolDefaults', u'polyMergeFaceToolDefaults', u'postProcessList1', u'publishedFilter', u'relationshipPanel1LeftAttrFilter', u'relationshipPanel1RightAttrFilter', u'renderGlobalsList1', u'renderLayerFilter', u'renderLayerManager', u'renderPartition', u'renderPassSetsFilter', u'renderPassesFilter', u'renderableObjectSetFilter', u'renderableObjectSetFilter1', u'renderableObjectSetFilter2', u'renderableObjectShapeFilter', u'renderableObjectShapeFilter1', u'renderableObjectShapeFilter2', u'renderableObjectsAndSetsFilter', u'renderableObjectsAndSetsFilter1', u'renderingSetsFilter', u'rotateFilter', u'scaleFilter', u'scaleRotateTranslateFilter', u'selectionListOperator1', u'selectionListOperator2', u'selectionListOperator3', u'selectionListOperator4', u'selectionListOperator5', u'selectionListOperator6', u'selectionListOperator7', u'selectionListOperator8', u'selectionListOperator9', u'selectionListOperator10', u'selectionListOperator11', u'selectionListOperator12', u'selectionListOperator13', u'selectionListOperator14', u'selectionListOperator15', u'selectionListOperator16', u'selectionListOperator17', u'selectionListOperator18', u'selectionListOperator19', u'selectionListOperator20', u'selectionListOperator21', u'selectionListOperator22', u'selectionListOperator23', u'selectionListOperator24', u'selectionListOperator25', u'selectionListOperator26', u'selectionListOperator27', u'selectionListOperator28', u'selectionListOperator29', u'selectionListOperator30', u'selectionListOperator57', u'selectionListOperator58', u'selectionListOperator59', u'selectionListOperator60', u'selectionListOperator61', u'selectionListOperator62', u'selectionListOperator63', u'selectionListOperator64', u'selectionListOperator65', u'selectionListOperator66', u'sequenceManager1', u'shaderGlow1', u'shared', u'side', u'sideShape', u'skinClusterSetsFilter', u'strokeGlobals', u'time1', u'top', u'topShape', u'translateFilter', u'world'] #
        
        # List the parent of the current namespace
        #
        pm.namespaceInfo( parent=True )
        # Result: u'' #
        
        # List the parent of the current namespace with short name
        #
        pm.namespaceInfo( parent=True, shortName=True )
        # Result: u'' #
        
        # Determine if the current namespace is root
        #
        pm.namespaceInfo( rootNamespace=True )
        
        # List the parent of the current namespace with absolute name
        #
        pm.namespaceInfo( parent=True, absoluteName=True )
        
        # List dependency nodes including internal nodes
        #
        pm.namespaceInfo(listOnlyDependencyNodes = True,  internal = True);
        
        # samples of query info of specified namespace
        pm.namespace( set =":" )
        pm.namespace( add ="sample" )
        pm.namespace( set =":sample" )
        pm.namespace( add ="sun" )
        
        # List the contents of the specified namespace
        #
        pm.namespaceInfo( ":sample", listNamespace=True )
        # Result: sample:sun
        
        # List the parent of the specified namespace
        #
        pm.namespaceInfo( ":sample:sun", parent=True )
        # result: sample
        
        # List the parent of the specified namespace with baseName name
        #
        pm.namespaceInfo( ":sample:sun", parent=True, baseName=True )
        # result: sample
        
        # Determine if the specified namespace is root
        #
        pm.namespaceInfo( ":", isRootNamespace=True )
        # result: True
        
        # List the parent of the specified namespace with absolute name
        #
        pm.namespaceInfo( ":sample:sun", parent=True, absoluteName=True )
        # result: :sample
        
        # List dependency nodes including internal nodes
        #
        pm.namespaceInfo(  ":sample", listOnlyNamespaces = True )
        # result: sample:sun
        
        # Query the namespace name and have it returned in different formats
        #
        pm.namespaceInfo( ":sample:sun", baseName = True )
        # result: "sun"
        
        pm.namespaceInfo( ":sample:sun", fullName = True )
        # result: "sample:sun"
        
        pm.namespaceInfo( "sample:sun", absoluteName = True )
        # result: ":sample:sun"
    """

    pass


def getModulePath(*args, **kwargs):
    """
    Returns the module path for a given module name.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``moduleName`` / ``mn``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The name of the module whose path you want to retrieve.                                           Flag can have multiple arguments, passed either as a tuple or a |
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.getModulePath`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.getModulePath(moduleName='myModule')
    """

    pass


def reference(*args, **kwargs):
    """
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``connectionsBroken`` / ``cb``                                                                       | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``connectionsMade`` / ``cm``                                                                         | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dagPath`` / ``dp``                                                                                 | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``editCommand`` / ``ec``                                                                             | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``filename`` / ``f``                                                                                 | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``isNodeReferenced`` / ``inr``                                                                       | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``longName`` / ``ln``                                                                                | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``node`` / ``n``                                                                                     | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``referenceNode`` / ``rfn``                                                                          | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shortName`` / ``sn``                                                                               | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.reference`
    """

    pass


def exportAll(exportPath, **kwargs):
    """
    Export everything into a single file. Returns the name of the exported file.                      
    
    Flags:
      - force:
          Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
          remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
          root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
          prompting a dialog that warns user about the lost of edits.
      - preserveReferences:
          Modifies the various import/export flags such that references are imported/exported as actual references rather than
          copies of those references.
      - type:
          Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
          audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
          file types that match this file.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def listNamespaces_old():
    """
    Deprecated
    Returns a list of the namespaces of referenced files.
    REMOVE In Favor of listReferences('dict') ?
    """

    pass


def dbmessage(*args, **kwargs):
    """
    The dbmessagecommand is used to install monitors for certain message types, dumping debug information as they are sent
    so that the flow of messages can be examined.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``file`` / ``f``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Destination file of the message monitoring information.  Use the special names stdoutand stderrto redirect to your command window.  As well, the special name     |
    |  | msdevis available on NT to direct your output to the debug tab in the output window of Developer Studio. Default value is stdout.                                 |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``list`` / ``l``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List all available message types and their current enabled status.                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``monitor`` / ``m``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the monitoring state of the message type ('on' to enable, 'off' to disable). Returns the list of all message types being monitored after the change in state. |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``t``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Monitor only the messages whose name matches this keyword (default is all).                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dbmessage`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.dbmessage( m='on' )                  # Enable monitoring of all messages
        pm.dbmessage( l=True )                  # Print all available messages and monitoring state
        pm.dbmessage( f='msgs.txt' )            # Redirect all message output to the file "msgs.txt"
        pm.dbmessage( t='dgNodeAdded', m='on' ) # Turn on monitoring for the "dgNodeAdded" message
    """

    pass


def exportAnim(exportPath, **kwargs):
    """
    Export all animation nodes and animation helper nodes from all objects in the scene. The resulting animation export file will contain connections to objects that are not included in the animation file. As a result, importing/referencing this file back in will require objects of the same name to be present, else errors will occur. The -sns/swapNamespace flag is available for swapping the namespaces of given objects to another namespace. This use of namespaces can be used to re-purpose the animation file to multiple targets using a consistent naming scheme.  The exportAnim flag will not export animation layers. For generalized file export of animLayers and other types of nodes, refer to the exportEdits command. Or use the Export Layers functionality.                    
    
    Flags:
      - force:
          Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
          remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
          root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
          prompting a dialog that warns user about the lost of edits.
      - type:
          Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
          audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
          file types that match this file.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def cmdFileOutput(*args, **kwargs):
    """
    This command will open a text file to receive all of the commands and results that normally get printed to the Script
    Editor window or console. The file will stay open until an explicit -close with the correct file descriptor or a
    -closeAll, so care should be taken not to leave a file open. To enable logging to commence as soon as Maya starts up,
    the environment variable MAYA_CMD_FILE_OUTPUT may be specified prior to launching Maya. Setting MAYA_CMD_FILE_OUTPUT to
    a filename will create and output to that given file. To access the descriptor after Maya has started, use the -query
    and -open flags together.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``close`` / ``c``                                                                                    | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Closes the file corresponding to the given descriptor. If -3 is returned, the file did not exist. -1 is returned on error, 0 is returned on successful close.     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``closeAll`` / ``ca``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Closes all open files.                    Flag can have multiple arguments, passed either as a tuple or a list.                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``open`` / ``o``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Opens the given file for writing (will overwrite if it exists and is writable). If successful, a value is returned to enable status queries and file close. -1 is |
    |  | returned if the file cannot be opened for writing. The -open flag can also be specified in -query mode. In query mode, if the named file is currently opened, the |
    |  | descriptor for the specified file is returned, otherwise -1 is returned. This is an easy way to check if a given file is currently open.                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``status`` / ``s``                                                                                   | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Queries the status of the given descriptor. -3 is returned if no such file exists, -2 indicates the file is not open, -1 indicates an error condition, 0 indicates|
    |  | file is ready for writing.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.cmdFileOutput`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.cmdFileOutput( o='dbOutput.txt' )
        # Result: 1 #
        print( 'This message is in the file\n' )
        # This message is in the file
        pm.cmdFileOutput( s=1 )
        # Result: 0 #
        pm.cmdFileOutput( s=2 )
        # Result: -3 #
        pm.cmdFileOutput( c=1 )
        # Result: 0 #
        # Notice that the 'This message is in the file' string is in the file,
        # as are all of the entered commands and the
        # '# Result: ...' lines, etc.
        
        # Turn on logging to a file on Maya startup so as to log all error
        # messages which happen on startup.
        #
        # Set the environment variable MAYA_CMD_FILE_OUTPUT to "trace.txt"
        # Start up Maya
        # Messages should now be logged to the file "trace.txt" as well as the
        # script editor window.
        
        # Turn off logging to the filename specified by $MAYA_CMD_FILE_OUTPUT
        # after Maya has completed startup.
        #
        import os
        traceFile = os.environ[ "MAYA_CMD_FILE_OUTPUT" ]
        descriptor = pm.cmdFileOutput( q=True, o=traceFile )
        if -1 != descriptor:
                pm.cmdFileOutput( close=descriptor )
    """

    pass


def moduleInfo(*args, **kwargs):
    """
    Returns information on modules found by Maya.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``definition`` / ``d``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns module definition file name for the module specified by the -moduleName parameter.                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listModules`` / ``lm``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns an array containing the names of all currently loaded modules.                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``moduleName`` / ``mn``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The name of the module whose information you want to retrieve. Has to be used with either -definition / -path / -version flags.                                   |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``path`` / ``p``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the module path for the module specified by the -moduleName parameter.                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``version`` / ``v``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the module version for the module specified by the -moduleName parameter.                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.moduleInfo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.moduleInfo(listModules=True)
        # Result: [u'mayatomr', u'substance'] #
        pm.moduleInfo(definition=True, moduleName='myModule')
        pm.moduleInfo(path=True, moduleName='myModule')
        pm.moduleInfo(version=True, moduleName='myModule')
    """

    pass


def namespace(*args, **kwargs):
    """
    This command allows a namespace to be created, set or removed. A namespace is a simple grouping of objects under a given
    name. Namespaces are primarily used to resolve name-clash issues in Maya, where a new object has the same name as an
    existing object (from importing a file, for example).  Using namespaces, you can have two objects with the same name, as
    long as they are contained in differenct namespaces. Namespaces are reminiscent of hierarchical structures like file
    systems where namespaces are analogous to directories and objects are analogous to files. The colon (':') character is
    the separator used to separate the names of namespaces and nodes instead of the slash ('/') or backslash ('\')
    character.  Namespaces can contain other namespaces as well as objects.  Like objects, the names of namespaces must be
    unique within another namespace. Objects and namespaces can be in only one namespace. Namespace names and object names
    don't clash so a namespace and an object contained in another namespace can have the same name. There is an unnamed root
    namespace specified with a leading colon (':').  Any object not in a named namespace is in the root namespace. Normally,
    the leading colon is omitted from the name of an object as it's presence is implied. The presence of a leading colon is
    important when moving objects between namespaces using the 'rename' command.  For the 'rename' command, the new name is
    relative to the current namespace unless the new name is fully qualified with a leading colon. Namespaces are created
    using the 'add/addNamespace' flag. By default they are created under the current namespace. Changing the current
    namespace is done with the 'set/setNamespace' flag. To reset the current namespace to the root namespace, use 'namespace
    -set :;'. Whenever an object is created, it is added by default to the current namespace. When creating a new namespace
    using a qualified name, any intervening namespaces which do not yet exist will be automatically created. For example, if
    the name of the new namespace is specified as A:Band the current namespace already has a child namespace named Athen a
    new child namespace named Bwill be created under A. But if the current namespace does not yet have a child named Athen
    it will be created automatically. This applies regardless of the number of levels in the provided name (e.g. A:B:C:D).
    The 'p/parent' flag can be used to explicitly specify the parent namespace under which the new one should be created,
    rather than just defaulting to the current namespace. If the name given for the new namespace is absolute (i.e. it
    begins with a colon, as in :A:B) then both the current namespace and the 'parent' flag will be ignored and the new
    namespace will be created under the root namespace. The relativeNamespace flag can be used to change the way node names
    are displayed in the UI and returned by the 'ls' command. Here are some specific details on how the return from the 'ls'
    command works in relativeNamespace mode: List all mesh objects in the scene:ls -type mesh;The above command lists all
    mesh objects in the root and any child namespaces. In relative name lookup mode, all names will be displayed relative to
    the current namespace. When not in relative name lookup mode (the default behaviour in Maya), results are printed
    relative to the root namespace. Using a \*wildcard:namespace -set myNS;ls -type mesh \*;In relative name lookup mode,
    the \*will match to the current namespace and thus the ls command will list only those meshes defined within the current
    namespace (i.e. myNs). If relative name lookup is off (the default behaviour in Maya), names are root-relative and thus
    \*matches the root namespace, with the net result being that only thoses meshes defined in the root namespace will be
    listed. You can force the root namespace to be listed when in relative name lookup mode by specifying :\*as your search
    pattern (i.e. ls -type mesh :\*which lists those meshes defined in the root namespace only). Note that you can also use
    :\*when relative name lookup mode is off to match the root if you want a consistent way to list the root. Listing child
    namespace contents:ls -type mesh \*:\*;For an example to list all meshes in immediate child namespaces, use \*:\*. In
    relative name lookup mode \*:\*lists those meshes in immediate child namespaces of the current namespaces. When not in
    relative name lookup mode, \*:\*lists meshes in namespaces one level below the root. Recursive listing of namespace
    contents:Example: ls -type mesh -recurse on \*The 'recurse' flag is provided on the lscommand to recursively traverse
    any child namespaces. In relative name lookup mode, the above example command will list all meshes in the current and
    any child namespaces of current. When not in relative name lookup mode, the above example command works from the root
    downwards and is thus equivalent to ls -type mesh.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``absoluteName`` / ``an``                                                                            | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a general flag which can be used to specify the desired format for the namespace(s) returned by the command. The absolute name of the namespace is a full |
    |  | namespace path, starting from the root namespace :and including all parent namespaces.  For example :ns:ballis an absolute namespace name while ns:ballis not.    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``addNamespace`` / ``add``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Create a new namespace with the given name. Both qualified names (A:B) and unqualified names (A) are acceptable. If any of the higher-level namespaces in a       |
    |  | qualified name do not yet exist, they will be created. If the supplied name contains invalid characters it will first be modified as per the validateName flag.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``collapseAncestors`` / ``ch``                                                                       | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Delete all empty ancestors of the given namespace. An empty namespace is a a namespace that does not contain any objects or other nested namespaces               |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deleteNamespaceContent`` / ``dnc``                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with the 'rm/removeNamespace' flag to indicate that when removing a namespace the contents of the namespace will also be removed.                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exists`` / ``ex``                                                                                  | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true if the specified namespace exists, false if not.                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``force`` / ``f``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with 'mv/moveNamespace' to force the move operation to ignore name clashes.                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``isRootNamespace`` / ``ir``                                                                         | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true if the specified namespace is root, false if not.                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mergeNamespaceWithParent`` / ``mnp``                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with the 'rm/removeNamespace' flag. When removing a namespace, move the rest of the namespace content to the parent namespace.                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mergeNamespaceWithRoot`` / ``mnr``                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with the 'rm/removeNamespace' flag. When removing a namespace, move the rest of the namespace content to the root namespace.                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``moveNamespace`` / ``mv``                                                                           | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Move the contents of the first namespace into the second namespace. Child namespaces will also be moved. Attempting to move a namespace containing referenced     |
    |  | nodes will result in an error; use the 'file' command ('file -edit -namespace') to change a reference namespace. If there are objects in the source namespace with|
    |  | the same name as objects in the destination namespace, an error will be issued. Use the 'force' flag to override this error - name clashes will be resolved by    |
    |  | renaming the objects to ensure uniqueness.                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``parent`` / ``p``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with the 'addNamespace' or 'rename' flags to specifiy the parent of the new namespace. The full namespace parent path is required. When using 'addNamespace' |
    |  | with an absolute name, the 'parent' will be ignored and the command will display a warning                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``recurse`` / ``r``                                                                                  | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Can be used with the 'exists' flag to recursively look for the specified namespace                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``relativeNames`` / ``rel``                                                                          | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns on relative name lookup, which causes name lookups within Maya to be relative to the current namespace. By default this is off, meaning that name lookups   |
    |  | are always relative to the root namespace. Be careful turning this feature on since commands such as setAttr will behave differently. It is wise to only turn this|
    |  | feature on while executing custom procedures that you have written to be namespace independent and turning relativeNames off when returning control from your     |
    |  | custom procedures. Note that Maya will turn on relative naming during file I/O. Although it is not recommended to leave relativeNames turned on, if you try to    |
    |  | toggle the value during file I/O you may notice that the value stays onbecause Maya has already temporarily enabled it internally. When relativeNames are enabled,|
    |  | the returns provided by the 'ls' command will be relative to the current namespace. See the main description of this command for more details.                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeNamespace`` / ``rm``                                                                         | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Deletes the given namespace.  The namespace must be empty for it to be deleted.                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rename`` / ``ren``                                                                                 | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Rename the first namespace to second namespace name. Child namespaces will also be renamed. Both names are relative to the current namespace. Use the 'parent'    |
    |  | flag to specify a parent namespace for the renamed namespace. An error is issued if the second namespace name already exists. If the supplied name contains       |
    |  | invalid characters it will first be modified as per the validateName flag.                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``setNamespace`` / ``set``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the current namespace.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``validateName`` / ``vn``                                                                            | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Convert the specified name to a valid name to make it contain no illegal characters. The leading illegal characters will be removed and other illegal characters  |
    |  | will be converted to '_'. Specially, the leading numeric characters and trailing space characters will be also removed.  Full name path can be validated as well. |
    |  | However, if the namespace of the path does not exist, command will only return the base name. For example, :nonExistentNS:namewill be converted to name.  If the  |
    |  | entire name consists solely of illegal characters, e.g. 123which contains only leading digits, then the returned string will be empty.                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.namespace`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Create three namespaces
        pm.namespace( add='FOO' )
        # Result: u'FOO' #
        pm.namespace( add='BAR' )
        # Result: u'BAR' #
        pm.namespace( add='FRED' )
        # Result: u'FRED' #
        
        # Create namespace with qualified name
        pm.namespace( add="A:B" )
        # Result: u'A:B' #
        
        # Create namespace with qualified name
        pm.namespace( add="C:D", parent="A:B" )
        # Result: u'A:B:C:D' #
        
        # Create namespace with qualified name
        pm.namespace( add=":A:B:C:D:E" )
        # Result: u'A:B:C:D:E' #
        
        # Set the current namespace to FOO
        pm.namespace( set='FOO' )
        # Result: u'FOO' #
        
        # Create the namespace BAR Under FOO. Note there are
        # two "BAR" namespaces, :BAR and :FOO:BAR.
        pm.namespace( add='BAR' )
        # Result: u'FOO:BAR' #
        
        # Check to see that the BAR namespace exists within the current
        # namespace (FOO)
        pm.namespace( exists='BAR' )
        # Result: True #
        
        # Check to see that the FRED namespace exists under the root namespace
        pm.namespace( exists=':FRED' )
        # Result: True #
        
        # Create two objects. It gets added to the current namespace FOO;
        pm.sphere( n='sphere1' )
        # Result: [nt.Transform(u'FOO:sphere1'), nt.MakeNurbSphere(u'FOO:makeNurbSphere1')] #
        pm.sphere( n='sphere2' )
        # Result: [nt.Transform(u'FOO:sphere2'), nt.MakeNurbSphere(u'FOO:makeNurbSphere2')] #
        
        # Move sphere1 from namespace FOO to FOO:BAR. Note that we
        # need to qualify sphere1 with the namespace FOO because
        # "sphere1" identifies a non-existent object in the root namespace.
        pm.rename( 'FOO:sphere1', 'BAR:sphere1' )
        # Result: nt.Transform(u'FOO:BAR:sphere1') #
        
        # Move sphere2 from namespace FOO to BAR.  Note the leading
        # colon on the new name.
        pm.rename( 'FOO:sphere2', ':BAR:sphere2' )
        # Result: nt.Transform(u'BAR:sphere2') #
        
        # query the current namespace (using the namespaceInfo command)
        pm.namespaceInfo( currentNamespace=True )
        # Result: u'FOO' #
        
        # remove the namespace FRED (it must be empty)
        pm.namespace( set=':' )
        # Result: u'' #
        pm.namespace( rm='FRED' )
        
        # Check to see that the FRED namespace has been removed
        pm.namespace( exists=':FRED' )
        # Result: False #
        
        # Rename namespace BAR to JOE
        # Note: this is done by creating JOE, moving the contents of
        # BAR into JOE, and then removing the (now empty) BAR.
        pm.namespace( set=':' )
        # Result: u'' #
        pm.namespace( add='JOE' )
        # Result: u'JOE' #
        pm.namespace( mv=('BAR', 'JOE') )
        # Result: u'BAR' #
        pm.namespace( rm='BAR' )
        
        # JOE should now contain a single node: 'sphere2'.
        # Move the contents of JOE into FRANK, when FRANK already
        # has a 'sphere2' node. The '-force'
        # flag is needed.
        pm.namespace( set=':' )
        # Result: u'' #
        pm.namespace( add='FRANK' )
        # Result: u'FRANK' #
        pm.namespace( set='FRANK' )
        # Result: u'FRANK' #
        pm.sphere( n='sphere2' )
        # Result: [nt.Transform(u'FRANK:sphere2'), nt.MakeNurbSphere(u'FRANK:makeNurbSphere1')] #
        pm.namespace( force=True, mv=(':JOE', ':FRANK') )
        # Result: u'JOE' #
        # In moving 'sphere2' from JOE to FRANK it will be renamed to
        # 'sphere3' to ensure uniqueness.
        # The namespace FRANK should now contain 'sphere2', 'sphere2Shape',
        # and 'sphere3'.
        
        # Determine whether the given namespace is root
        #
        pm.namespace( query=True, isRootNamespace="FOO" )
        # Result: False #
        
        #Set return value to be absolute namespace name
        #
        print(pm.namespace(add = "testAbsoluteName", absoluteName = True))
        
        #Create a sample hierachy that contains only empty namespaces, then collapse it
        #
        pm.namespace( set = ":")
        # Result: u'' #
        pm.namespace( add = "emptyLevel1")
        # Result: u'emptyLevel1' #
        pm.namespace( add = "emptyLevel2", parent = "emptyLevel1")
        # Result: u'emptyLevel1:emptyLevel2' #
        pm.namespace( add = "leaf", parent = "emptyLevel1:emptyLevel2")
        # Result: u'emptyLevel1:emptyLevel2:leaf' #
        pm.namespace( collapseAncestors = "emptyLevel1:emptyLevel2:leaf")
        # Result: u'leaf' #
        
        # Create a sample for removing an existed namespace.
        # This command can also be used together with three option parameters named
        # deleteNamespaceContent/mergeNamespaceWithParent/mergeNamespaceWithRoot.
        # The functionality of the three option parameters will also be displayed in the
        # following sample.
        # Note: The three option parameters are mutually exclusive.
        #       Without any option parameters specified, the default way it performances that
        #       it can only remove a namespace that is empty. If you want to remove any namespace
        #       with contents, please add option parameter deleteNamespaceContent.
        #
        pm.namespace( set = ":")
        # Result: u'' #
        pm.namespace( add = ":RM_TEST_ROOT:FOO:BAR:JOE")
        # Result: u'RM_TEST_ROOT:FOO:BAR:JOE' #
        pm.sphere( name = ":RM_TEST_ROOT:FOO:obj1")
        # Result: [nt.Transform(u'RM_TEST_ROOT:FOO:obj1'), nt.MakeNurbSphere(u'makeNurbSphere1')] #
        pm.sphere( name = ":RM_TEST_ROOT:FOO:BAR:obj2")
        # Result: [nt.Transform(u'RM_TEST_ROOT:FOO:BAR:obj2'), nt.MakeNurbSphere(u'makeNurbSphere2')] #
        
        # Trying to remove a namespace that is not empty without option parameter,
        # user will get an error message show that maya cannot remove a namespace that
        # is not empty.
        #
        #pm.namespace( removeNamespace = ":RM_TEST_ROOT:FOO") # Run this command you'll get an error.
        
        # Trying to remove an empty namespace.
        # Namespace :RM_TEST_ROOT:FOO:BAR:JOE has been removed successfully by the command.
        #
        pm.namespace( removeNamespace = ":RM_TEST_ROOT:FOO:BAR:JOE")
        
        pm.undo()
        
        # Usage of deleteNamespaceContent option parameter:
        # Remove all the contents in the target namespace specified in the command and
        # remove the namespace
        #
        pm.namespace( removeNamespace = ":RM_TEST_ROOT:FOO:BAR", deleteNamespaceContent = True)
        
        pm.undo()
        
        # Usage of mergeNamespaceWithParent parameter:
        # Move the content of the target namespace specified in the command to its parent
        # namespace and remove the namespace.
        #
        pm.namespace( removeNamespace = ":RM_TEST_ROOT:FOO:BAR", mergeNamespaceWithParent = True)
        
        pm.undo()
        
        # Usage of mergeNamespaceWithRoot parameter:
        # Move the content of the target namespace specified in the command to the root
        # namespace and remove the namespace.
        #
        pm.namespace( removeNamespace = ":RM_TEST_ROOT:FOO:BAR", mergeNamespaceWithRoot = True)
    """

    pass


def iterReferences(parentReference=None, recursive=False, namespaces=False, refNodes=False, references=True, recurseType='depth', loaded=None, unloaded=None):
    """
    returns references in the scene as a list of value tuples.
    
    The values in the tuples can be namespaces, refNodes (as PyNodes), and/or
    references (as FileReferences), and are controlled by their respective
    keywords (and are returned in that order).  If only one of the three options
    is True, the result will not be a list of value tuples, but will simply be a
    list of values.
    
    Parameters
    ----------
    parentReference : string, `Path`, or `FileReference`
        a reference to get sub-references from. If None (default), the current
        scene is used.
    
    recursive : bool
        recursively determine all references and sub-references
    
    namespaces : bool
        controls whether namespaces are returned
    
    refNodes : bool
        controls whether reference PyNodes are returned
    
    refNodes : bool
        controls whether FileReferences returned
    
    recurseType : string
        if recursing, whether to do a 'breadth' or 'depth' first search;
        defaults to a 'depth' first
    
    loaded : bool or None
        whether to return loaded references in the return result; if both of
        loaded/unloaded are not given (or None), then both are assumed True;
        if only one is given, the other is assumed to have the opposite boolean
        value
    
    unloaded : bool or None
        whether to return unloaded references in the return result; if both of
        loaded/unloaded are not given (or None), then both are assumed True;
        if only one is given, the other is assumed to have the opposite boolean
        value
    """

    pass


def sceneUIReplacement(*args, **kwargs):
    """
    This command returns existing scene based UI that can be utilized by the scene that is being loaded. It can also delete
    any such UI that is not used by the loading scene.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``clear`` / ``cl``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Frees any resources allocated by the command.                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deleteRemaining`` / ``dr``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Delete any UI that is scene dependent and has not been referenced by this command since the last update.                          Flag can have multiple          |
    |  | arguments, passed either as a tuple or a list.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``getNextFilter`` / ``gf``                                                                           | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the next filter of the specified type with the specified name.                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``getNextPanel`` / ``gp``                                                                            | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the next panel of the specified type, preferably with the specified label.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``getNextScriptedPanel`` / ``gsp``                                                                   | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the next scripted panel of the specified scripted panel type, preferably with the specified label.                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``update`` / ``u``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Updates the state of the command to reflect the current state of the application.  The string argument is the name of the main window pane layout holding the     |
    |  | panels.                                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.sceneUIReplacement`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        import maya.mel as mm
        gMainPane = mm.eval( 'global string $gMainPane; $temp = $gMainPane;' )
        pm.sceneUIReplacement( update=gMainPane )
        # Result: u'1' #
        
        # Try to find the modelPanel named Top View
        pm.sceneUIReplacement( getNextPanel=('modelPanel','Top View') )
        # Result: u'modelPanel1' #
        pm.modelPanel( 'modelPanel1', q=True, label=True )
        # Result: u'Top View' #
        
        # Try to find Front View
        pm.sceneUIReplacement( getNextPanel=('modelPanel', 'Front View') )
        # Result: u'modelPanel3' #
        pm.modelPanel( 'modelPanel3', q=True, label=True )
        # Result: u'Front View' #
        
        # Is there another Front View?  (No: all we find is a model panel called Persp View)
        pm.sceneUIReplacement( getNextPanel=('modelPanel', 'Front View') )
        # Result: u'modelPanel4' #
        # Result: modelPanel4
        pm.modelPanel( 'modelPanel4', q=True, label=True )
        # Result: u'Persp View' #
        # Result: Persp View
    """

    pass


def referenceEdit(*args, **kwargs):
    """
    Use this command to remove and change the modifications which have been applied to references. A valid commandTarget is
    either a reference node, a reference file, a node in a reference, or a plug from a reference. Only modifications that
    have been made from the currently open scene can be changed or removed. The 'referenceQuery -topReference' command can
    be used to determine what modifications have been made to a given commandTarget. Additionally only unapplied edits will
    be affected. Edits are unapplied when the node(s) which they affect are unloaded, or when they could not be successfully
    applied. By default this command only works on failed edits (this can be adjusted using the -failedEditsand
    -successfulEditsflags). Specifying a reference node as the command target is equivalent to specifying every node in the
    target reference file as a target. In this situation the results may differ depending on whether the target reference is
    loaded or unloaded. When it is unloaded edits which affect both a node in the target reference and a node in one of its
    decendant references may be missed (e.g. they may not be removed). Edits which only affect nodes in the target reference
    or one of its ancestral references, however, should be removed as expected. This is because when a reference is unloaded
    Maya no longer retains detailed information about which nodes belong to it. NOTE: When specifying a plug it is important
    to use the appropriate long attribute name.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``applyFailedEdits`` / ``afe``                                                                       | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attempts to apply any unapplied edits. This flag is useful if previously failing edits have been fixed using the -changeEditTarget flag. This flag can only be    |
    |  | used on loaded references. If the command target is a referenced node, the associated reference is used instead.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``changeEditTarget`` / ``cet``                                                                       | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used to change a target of the specified edits. This flag takes two parameters: the old target of the edits, and the new target to change it to. The target can   |
    |  | either be a node name (node), a node and attribute name (node.attr), or just an attribute name (.attr). If an edit currently affects the old target, it will be   |
    |  | changed to affect the new target. You should use 'referenceQuery' to determine the format of the edit targets. As an example most edits store the long name of the|
    |  | attribute (e.g. translateX), so when specifying the old target, a long name must also be used. If the short name is specified (e.g. tx), chances are the edit     |
    |  | won't be retargeted.                                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``editCommand`` / ``ec``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a secondary flag used to indicate which type of reference edits should be considered by the command. If this flag is not specified all edit types will be |
    |  | included. This flag requires a string parameter. Valid values are: addAttr, connectAttr, deleteAttr, disconnectAttr, parent, setAttr, lockand unlock. In some     |
    |  | contexts, this flag may be specified more than once to specify multiple edit types to consider.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``failedEdits`` / ``fld``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a secondary flag used to indicate whether or not failed edits should be acted on (e.g. queried, removed, etc...). A failed edit is an edit which could not|
    |  | be successfully applied the last time its reference was loaded. An edit can fail for a variety of reasons (e.g. the referenced node to which it applies was       |
    |  | removed from the referenced file). By default failed edits will be acted on.                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``onReferenceNode`` / ``orn``                                                                        | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a secondary flag used to indicate that only those edits which are stored on the indicated reference node should be considered. This flag only supports    |
    |  | multiple uses when specified with the exportEditscommand.                                          Flag can have multiple arguments, passed either as a tuple or a|
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeEdits`` / ``r``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Remove edits which affect the specified unloaded commandTarget.                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``successfulEdits`` / ``scs``                                                                        | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a secondary flag used to indicate whether or not successful edits should be acted on (e.g. queried, removed, etc...). A successful edit is any edit which |
    |  | was successfully applied the last time its reference was loaded. This flag will have no affect if the commandTarget is loaded. By default successful edits will   |
    |  | not be acted on.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.referenceEdit`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #
        # EXAMPLE FOR -removeEdits
        #
        # Assume:
        # main.ma contains a reference to mid.ma.
        # mid.ma contains a reference to bot.ma.
        # NOTE: The target reference must be unloaded for the
        # following commands to work.
        # Remove all the edits which apply to mid.ma.
        # This can be done by specifying either the reference
        # node or the reference file.
        pm.referenceEdit( 'midRN', removeEdits=True )
        pm.referenceEdit( 'mid.ma', removeEdits=True )
        # Remove all "setAttr" edits which apply to mid.ma.
        # This can be done by specifying either the reference
        # node or the reference file.
        pm.referenceEdit( 'midRN', editCommand='setAttr', removeEdits=True )
        pm.referenceEdit( 'mid.ma', editCommand='setAttr', removeEdits=True )
        # Remove all the "parent" edits which apply to mid:pSphere1.
        pm.referenceEdit( 'mid:pSphere1', editCommand='parent', removeEdits=True )
        # Remove all the "connectAttr" edits which apply to mid:pSphere1.translateX.
        pm.referenceEdit( 'mid:pSphere1.translateX', editCommand='connectAttr', removeEdits=True )
        # Remove all the edits which apply to bot.ma and are stored on midRN.
        # The referenceEdit command is only capable of removing edits which
        # are stored on a top level reference node. The only edits which
        # are stored on a top level reference node are those which were made
        # from the main scene. If you had previously opened mid.ma and made
        # modifications to bot.ma, those edits can only be removed by opening
        # mid.ma and issuing a referenceEdit command.
        #
        pm.referenceEdit( 'mid:botRN', removeEdits=True )
        pm.referenceEdit( 'bot.ma', removeEdits=True )
        #
        # EXAMPLE FOR -changeEditTarget
        #
        tempDir = pm.internalVar(utd=True)
        # Create a reference containing pSphere1.
        #
        pm.file( f=True, new=True )
        pm.polySphere( ch=1, r=1, sx=20, sy=20, ax=(0, 1, 0) )
        newFileName = '%sref.ma' % tempDir
        pm.file( rename=newFileName )
        pm.file( f=True, s=True, type='mayaAscii')
        # Reference the file in and position pSphere1
        #
        pm.file( f=True, new=True )
        pm.file( newFileName, r=True, ns='ref' )
        pm.select( 'ref:pSphere1', r=True )
        pm.move( 5, 5, 5 )
        topFileName = '%stop.ma' % tempDir
        pm.file( rename=topFileName )
        pm.file( f=True, s=True, type='mayaAscii')
        # Later on its determined that pSphere1 is actually
        # BobMrozowski.
        #
        pm.file( newFileName, f=True, o=True )
        pm.rename( 'pSphere1', 'BobMrozowski' )
        pm.file( f=True, s=True, type='mayaAscii')
        # Now go to open your main scene again...
        #
        pm.file( topFileName, f=True, o=True )
        # ... and notice that BobMrozowski is back at
        # the origin.
        #
        # So remap all edits so that anything that used to
        # affect ref:pSphere1 now affects ref:BobMrozowski...
        #
        pm.referenceEdit( 'refRN', changeEditTarget=('ref:pSphere1','ref:BobMrozowski') )
        # ... and then force all previously failing edits affecting
        # refRN to be re-applied.
        #
        pm.referenceEdit( 'refRN', applyFailedEdits=True )
        # BobMrozowski should now be back at 5 5 5.
        #
    """

    pass


def detachDeviceAttr(*args, **kwargs):
    """
    This command detaches connections between device axes and node attributes.  The command line arguments are the same as
    for the corresponding attachDeviceAttr except for the clutch argument which can not be used in this command. In query
    mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``all`` / ``all``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Delete all attachments on every device.                   Flag can have multiple arguments, passed either as a tuple or a list.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The attribute to detach. This flag must be used with the -d/device flag.                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``axis`` / ``ax``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The axis to detach. This flag must be used with the -d/device flag.                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``device`` / ``d``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Delete the attachment for this device. If the -ax/axis flag is not used, all of the attachments connected to this device are detached.                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selection`` / ``sl``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Detaches selection attachments.                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.detachDeviceAttr`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.detachDeviceAttr( d='spaceball', ax='XAxis', at='translateX' )
    """

    pass


def fileDialog2(*args, **kwargs):
    """
    This command provides a dialog that allows users to select files or directories.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``cancelCaption`` / ``cc``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If the dialogStyle flag is set to 2 then this provides a caption for the Cancel button within the dialog.                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``caption`` / ``cap``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Provide a title for the dialog.                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dialogStyle`` / ``ds``                                                                             | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | 1 On Windows or Mac OS X will use a native style file dialog.2 Use a custom file dialog with a style that is consistent across platforms.                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fileFilter`` / ``ff``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Provide a list of file type filters to the dialog.  Multiple filters should be separated by double semi-colons.  See the examples section.                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fileMode`` / ``fm``                                                                                | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Indicate what the dialog is to return. 0 Any file, whether it exists or not.1 A single existing file.2 The name of a directory.  Both directories and files are   |
    |  | displayed in the dialog.3 The name of a directory.  Only directories are displayed in the dialog.4 Then names of one or more existing files.                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fileTypeChanged`` / ``ftc``                                                                        | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | MEL only.  The string is interpreted as a MEL callback, to be called when the user-selected file type changes.  The callback is of the form: global proc          |
    |  | MyCustomFileTypeChanged(string $parent, string $newType) The parent argument is the parent layout into which controls have been added using the optionsUICreate   |
    |  | flag.  The newType argument is the new file type.                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``hideFileExtensions`` / ``hfe``                                                                     | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``okCaption`` / ``okc``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If the dialogStyle flag is set to 2 then this provides a caption for the OK, or Accept, button within the dialog.                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``optionsUICommit`` / ``ocm``                                                                        | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | MEL only.  The string is interpreted as a MEL callback, to be called when the dialog is successfully dismissed.  It will not be called if the user cancels the    |
    |  | dialog, or closes the window using window title bar controls or other window system means.  The callback is of the form: global proc                              |
    |  | MyCustomOptionsUICommit(string $parent) The parent argument is the parent layout into which controls have been added using the optionsUICreate flag.              |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``optionsUICreate`` / ``ocr``                                                                        | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | MEL only.  The string is interpreted as a MEL callback, to be called on creation of the file dialog.  The callback is of the form: global proc                    |
    |  | MyCustomOptionsUISetup(string $parent) The parent argument is the parent layout into which controls can be added.  This parent is the right-hand pane of the file |
    |  | dialog.                                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``optionsUIInit`` / ``oin``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | MEL only.  The string is interpreted as a MEL callback, to be called just after file dialog creation, to initialize controls.  The callback is of the form: global|
    |  | proc MyCustomOptionsUIInitValues(string $parent, string $filterType) The parent argument is the parent layout into which controls have been added using the       |
    |  | optionsUICreate flag.  The filterType argument is the initial file filter.                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``returnFilter`` / ``rf``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If true, the selected filter will be returned as the last item in the string array along with the selected files.                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectFileFilter`` / ``sff``                                                                       | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify the initial file filter to select.  Specify just the begining text and not the full wildcard spec.                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectionChanged`` / ``sc``                                                                        | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | MEL only.  The string is interpreted as a MEL callback, to be called when the user changes the file selection in the file dialog.  The callback is of the form:   |
    |  | global proc MyCustomSelectionChanged(string $parent, string $selection) The parent argument is the parent layout into which controls have been added using the    |
    |  | optionsUICreate flag.  The selection argument is the full path to the newly-selected file.                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``setProjectBtnEnabled`` / ``spe``                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``startingDirectory`` / ``dir``                                                                      | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Provide the starting directory for the dialog.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.fileDialog2`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        import maya.cmds as cmds
        
        basicFilter = "*.mb"
        pm.fileDialog2(fileFilter=basicFilter, dialogStyle=2)
        
        singleFilter = "All Files (*.*)"
        pm.fileDialog2(fileFilter=singleFilter, dialogStyle=2)
        
        multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
        pm.fileDialog2(fileFilter=multipleFilters, dialogStyle=2)
    """

    pass


def translator(*args, **kwargs):
    """
    Set or query parameters associated with the file translators specified in as the argument.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``defaultFileRule`` / ``dfr``                                                                        | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the default file rule value, can return as well                   Flag can have multiple arguments, passed either as a tuple or a list.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``defaultOptions`` / ``do``                                                                          | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return/set a string of default options used by this translator.                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``extension`` / ``ext``                                                                              | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the default file extension for this translator.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fileCompression`` / ``cmp``                                                                        | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the compression action to take when a file is saved. Possible values are compressed, uncompressedasCompressed.                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``filter`` / ``f``                                                                                   | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the filter string used for this translator.                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``list`` / ``l``                                                                                     | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return a string array of all the translators that are loaded.                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``loaded`` / ``ld``                                                                                  | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true if the given translator is currently loaded.                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``objectType`` / ``ot``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is obsolete. This will now return the same results as defaultFileRule going forward.                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``optionsScript`` / ``os``                                                                           | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the name of the options script to use to post the user options UI. When this script is invoked it will expect the name of the parent layout in which the    |
    |  | options will be displayed as well as the name of the callback to be invoked once the apply button has been depressed in the options area.                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``readSupport`` / ``rs``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true if this translator supports read operations.                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``writeSupport`` / ``ws``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true if this translator supports write operations.                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.translator`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Returns true if dxf files can be read.
        pm.translator( 'dxf', q=True, rs=True )
    """

    pass


def loadReference(filepath, **kwargs):
    """
    This flag loads a file and associates it with the passed reference node. If the reference node does not exist, the command will fail. If the file is already loaded, then this flag will reload the same file.If a file is not given, the command will load (or reload) the last used reference file. 
    
    Flags:
      - loadNoReferences:
          This flag is obsolete and has been replaced witht the loadReferenceDepth flag. When used with the -open flag, no
          references will be loaded. When used with -i/import, -r/reference or -lr/loadReference flags, will load the top-most
          reference only.
      - loadReferenceDepth:
          Used to specify which references should be loaded. Valid types are all, noneand topOnly, which will load all references,
          no references and top-level references only, respectively. May only be used with the -o/open, -i/import, -r/reference or
          -lr/loadReference flags. When noneis used with -lr/loadReference, only path validation is performed. This can be used to
          replace a reference without triggering reload. Not using loadReferenceDepth will load references in the same loaded or
          unloaded state that they were in when the file was saved. Additionally, the -lr/loadReference flag supports a fourth
          type, asPrefs. This will force any nested references to be loaded according to the state (if any) stored in the current
          scene file, rather than according to the state saved in the reference file itself.
      - returnNewNodes:
          Used to control the return value in open, import, loadReference, and reference operations. It will force the file
          command to return a list of new nodes added to the current scene.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def fileDialog(*args, **kwargs):
    """
    The fileBrowserDialog and fileDialog commands have now been deprecated. Both commands are still callable, but it is
    recommended that the fileDialog2 command be used instead.  To maintain some backwards compatibility, both
    fileBrowserDialog and fileDialog will convert the flags/values passed to them into the appropriate flags/values that the
    fileDialog2 command uses and will call that command internally.  It is not guaranteed that this compatibility will be
    able to be maintained in future versions so any new scripts that are written should use fileDialog2. See below for an
    example of how to change a script to use fileDialog2.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``application`` / ``app``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a Maconly flag. This brings up the dialog which selects only the application bundle.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``defaultFileName`` / ``dfn``                                                                        | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set default file name. This flag is available under writemode                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directoryMask`` / ``dm``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This can be used to specify what directory and file names will be displayed in the dialog.  If not specified, the current directory will be used, with all files  |
    |  | displayed. The string may contain a path name, and must contain a wild-carded file specifier. (eg \*.ccor /usr/u/\*) If just a path is specified, then the last   |
    |  | directory in the path is taken to be a file specifier, and this will not produce the desired results.                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mode`` / ``m``                                                                                     | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Defines the mode in which to run the file dialog: 0 for read1 for writeWrite mode can not be used in conjunction with the -application flag.                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``title`` / ``t``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set title text. The default value under writemode is Save As. The default value under readmode is Open.                   Flag can have multiple arguments, passed|
    |  | either as a tuple or a list.                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.fileDialog`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Old way:
        pm.fileDialog()
        pm.fileDialog( directoryMask='/usr/u/bozo/myFiles/*.ma' )
        pm.fileDialog( dm='*.cc' )
        
        # Recommended way:
        pm.fileDialog2(startingDirectory ="/usr/u/bozo/myFiles/", fileFilter="Maya Ascii (*.ma)")
    """

    pass


def listDeviceAttachments(*args, **kwargs):
    """
    This command lists the current set of device attachments. The listing is in the form of the commands required to
    recreate them.  This includes both attachments and device mappings.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify the attribute attachments to list                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``axis`` / ``ax``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify the axis attachments to list                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``clutch`` / ``c``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List only attachment clutched with this button                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``device`` / ``d``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify which device attachments to list                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``file`` / ``f``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify the name of the file to write out device attachments.                     Flag can have multiple arguments, passed either as a tuple or a list.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selection`` / ``sl``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag list only attachments on selection                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``write`` / ``w``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Write out device attachments to a file specified by the -f flag, is set.  If -f is not set, it'll write out to a file named for the device.                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.listDeviceAttachments`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.listDeviceAttachments()# List all attachments
        # Result: [u'\n', u'', u'\tsetInputDeviceMapping -d "virtualClock" -ax "hours" -s 1 -o 0 -a ;\n\tsetInputDeviceMapping -d "virtualClock" -ax "minutes" -s 1 -o 0 -a ;\n\tsetInputDeviceMapping -d "virtualClock" -ax "seconds" -s 1 -o 0 -a ;\n'] #
        
        # List attachments on the spaceball that are clutched on Button1
        pm.listDeviceAttachments( d='spaceball', c='Button1' )
        
        # write out attachments for the spaceball device, since there is
        # no file name specified, attachments will be written out to
        # spaceball.mel
        pm.listDeviceAttachments( d='spaceball', w=True )
        
        # write out attachments for all devices, since there is not file
        # name specified, attachments will be written out to devices.mel
        pm.listDeviceAttachments( w=True )
    """

    pass


def saveAs(newname, **kwargs):
    pass


def shotTrack(*args, **kwargs):
    """
    This command is used for inserting and removing tracks related to the shots displayed in the Sequencer. It can also be
    used to modify the track state, for example, to lock or mute a track.             In query mode, return type is based on
    queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``insertTrack`` / ``it``                                                                             | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to insert a new empty track at the track index specified.                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lock`` / ``l``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether shots on a track are to be locked or not.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mute`` / ``m``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether shots on a track are to be muted or not.                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``numTracks`` / ``nt``                                                                               | *int*                         | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | To query the number of tracks                                     Flag can have multiple arguments, passed either as a tuple or a list.                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeEmptyTracks`` / ``ret``                                                                      | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to remove all tracks that have no clips.                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeTrack`` / ``rt``                                                                             | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to remove the track with the specified index.  The track must have no clips on it before it can be removed.                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selfmute`` / ``sm``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether shots on a track are to be muted or not (unlike mute, this disregards soloing).                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``solo`` / ``so``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether shots on a track are to be soloed or not.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``swapTracks`` / ``st``                                                                              | *int, int*                    | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to swap the contents of two specified tracks.                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unsolo`` / ``uso``                                                                                 | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether shots on a track are to be unsoloed or not.                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.shotTrack`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #  Move the shot named "shot2" to track 3
        #
        pm.shotTrack( 'shot2', track=3 )
        # Lock the track containing the shot named "shot1"
        #
        pm.shotTrack( 'shot1', lock=True )
        # Remove any empty tracks
        #
        pm.shotTrack(removeEmptyTracks=True)
        # shotTrack -q -track shot1;
        #
        pm.shotTrack( 'shot1', q=True, track=True )
    """

    pass


def getReferences(parentReference=None, recursive=False):
    pass


def dynamicLoad(*args, **kwargs):
    """
    Dynamically load the DLL passed as argument.             In query mode, return type is based on queried flag.
    
    
    Derived from mel command `maya.cmds.dynamicLoad`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.dynamicLoad( 'libDynSlice.dll' )
    """

    pass


def referenceQuery(*args, **kwargs):
    """
    Use this command to find out information about references and referenced nodes. A valid target is either a reference
    node, a reference file, or a referenced node. Some flags don't require a target, see flag descriptions for more
    information on what effect this has. When a scene contains multiple levels of file references, those edits which affect
    a nested reference may be stored on several different reference nodes. For example: A.ma has a reference to B.ma which
    has a reference to C.ma which contains a poly sphere (pSphere1). If you were to open B.ma and translate the sphere, an
    edit would be stored on CRN which refers to a node named C:pSphere1. If you were then to open A.ma and parent the
    sphere, an edit would be stored on BRN which refers to a node named B:C:pSphere1. It is important to note that when
    querying edits which affect a nested reference, the edits will be returned in the same format that they were applied. In
    the above example, opening A.ma and querying all edits which affect C.ma, would return two edits a parent edit affecting
    B:C:pSphere1, and a setAttr edit affecting C:pSphere1. Since there is currently no node named C:pSphere1 (only
    B:C:pSphere1) care will have to be taken when interpreting the returned information. The same care should be taken when
    referenced DAG nodes have been parented or instanced. Continuing with the previous example, let's say that you were to
    open A.ma and, instead of simply parenting pSphere1, you were to instance it. While A.ma is open, B:C:pSphere1may now be
    an amibiguous name, replaced by |B:C:pSphere1and group1|B:C:pSphere1. However querying the edits which affect C.ma would
    still return a setAttr edit affecting C:pSphere1since it was applied prior to B:C:pSphere1 being instanced. Some tips:
    1. Use the '-topReference' flag to query only those edits which were applied    from the currently open file. 2. Use the
    '-onReferenceNode' flag to limit the results to those edits where    are stored on a given reference node. You can then
    use various string    manipulation techniques to extrapolate the current name of any affected    nodes.
    
    Modifications:
        - When queried for 'es/editStrings', returned a list of ReferenceEdit objects
        - By default, returns all edits. If neither of successfulEdits or
          failedEdits is given, they both default to True. If only one is given,
          the other defaults to the opposite value.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``child`` / ``ch``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags to indicate the the children of the target reference will be returned. Returns a string     |
    |  | array.                                                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dagPath`` / ``dp``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag modifies the '-n/-nodes' flag to indicate that the names of any dag objects returned will include as much of the dag path as is necessary to make the   |
    |  | names unique. If this flag is not present, the names returned will not include any dag paths.                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``editAttrs`` / ``ea``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns string array. A main flag used to query the edits that have been applied to the target. Only the names of the attributes involved in the reference edit   |
    |  | will be returned. If an edit involves multiple attributes (e.g. connectAttredits) the nodes will be returned as separate, consecutive entries in the string array.|
    |  | A valid target is either a reference node, a reference file, or a referenced node. If a referenced node is specified, only those edits which affect that node will|
    |  | be returned. If a reference file or reference node is specified any edit which affects a node in that reference will be returned. If no target is specified all   |
    |  | edits are returned. This command can be used on both loaded and unloaded references. By default it will return all the edits, formatted as MEL commands, which    |
    |  | apply to the target. This flag can be used in combination with the '-ea/-editAttrs' flag to indicate that the names of both the involved nodes and attributes will|
    |  | be returned in the format 'node.attribute'.                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``editCommand`` / ``ec``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a secondary flag used to indicate which type of reference edits should be considered by the command. If this flag is not specified all edit types will be |
    |  | included. This flag requires a string parameter. Valid values are: addAttr, connectAttr, deleteAttr, disconnectAttr, parent, setAttr, lockand unlock. In some     |
    |  | contexts, this flag may be specified more than once to specify multiple edit types to consider.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``editNodes`` / ``en``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns string array. A main flag used to query the edits that have been applied to the target. Only the names of the nodes involved in the reference edit will be|
    |  | returned. If an edit involves multiple nodes (e.g. connectAttredits) the nodes will be returned as separate, consecutive entries in the string array. A valid     |
    |  | target is either a reference node, a reference file, or a referenced node. If a referenced node is specified, only those edits which affect that node will be     |
    |  | returned. If a reference file or reference node is specified any edit which affects a node in that reference will be returned. If no target is specified all edits|
    |  | are returned. This command can be used on both loaded and unloaded references. By default it will return all the edits, formatted as MEL commands, which apply to |
    |  | the target. This flag can be used in combination with the '-ea/-editAttrs' flag to indicate that the names of both the involved nodes and attributes will be      |
    |  | returned in the format 'node.attribute'.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``editStrings`` / ``es``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns string array. A main flag used to query the edits that have been applied to the target. The edit will be returned as a valid MEL command. A valid target  |
    |  | is either a reference node, a reference file, or a referenced node. If a referenced node is specified, only those edits which affect that node will be returned.  |
    |  | If a reference file or reference node is specified any edit which affects a node in that reference will be returned. If no target is specified all edits are      |
    |  | returned. This command can be used on both loaded and unloaded references. By default it will return all the edits, formatted as MEL commands, which apply to the |
    |  | target. This flag cannot be used with either the '-en/-editNodes' or '-ea/-editAttrs' flags.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``failedEdits`` / ``fld``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a secondary flag used to indicate whether or not failed edits should be acted on (e.g. queried, removed, etc...). A failed edit is an edit which could not|
    |  | be successfully applied the last time its reference was loaded. An edit can fail for a variety of reasons (e.g. the referenced node to which it applies was       |
    |  | removed from the referenced file). By default failed edits will not be acted on.                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``filename`` / ``f``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns string. A main flag used to query the filename associated with the target reference.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``isExportEdits`` / ``iee``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a boolean indicating whether the specified reference node or file name is an edits file (created with the Export Edits feature)                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``isLoaded`` / ``il``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a boolean indicating whether the specified reference node or file name refers to a loaded or unloaded reference.                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``isNodeReferenced`` / ``inr``                                                                       | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns boolean. A main flag used to determine whether or not the target node comes from a referenced file. true if the target node comes from a referenced file, |
    |  | false if not.                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``isPreviewOnly`` / ``ipo``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns boolean. This flag is used to determine whether or not the target reference node is only a preview reference node.                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``liveEdits`` / ``le``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies that the edits should be returned based on the live edits database. Only valid when used in conjunction with the editStrings flag.                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``namespace`` / ``ns``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns string. This flag returns the full namespace path of the target reference, starting from the root namespace :. It can be combined with the shortName flag |
    |  | to return just the base name of the namespace.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``nodes`` / ``n``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns string array. A main flag used to query the contents of the target reference.                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``onReferenceNode`` / ``orn``                                                                        | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a secondary flag used to indicate that only those edits which are stored on the indicated reference node should be considered. This flag only supports    |
    |  | multiple uses when specified with the exportEditscommand.                                          Flag can have multiple arguments, passed either as a tuple or a|
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``parent`` / ``p``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags to indicate the the parent of the target reference will be returned.                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``parentNamespace`` / ``pns``                                                                        | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A main flag used to query and return the parent namespace of the target reference.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``referenceNode`` / ``rfn``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns string. A main flag used to query the reference node associated with the target reference.                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shortName`` / ``shn``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag modifies the '-f/-filename' and '-ns/-namespace' flags. Used with the '-f/-filename' flag indicates that the file name returned will be the short name  |
    |  | (i.e. just a file name without any directory paths). If this flag is not present, the full name and directory path will be returned. Used with the                |
    |  | '-ns/-namespace' flag indicates that the namespace returned will be the base name of the namespace. (i.e. the base name of the full namespace path :AAA:BBB:CCCis |
    |  | CCC                                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showDagPath`` / ``sdp``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Shows/hides the full dag path for edits. If false only displays the node-name of reference edits. Must be used with the -editNodes, -editStrings or -editAttrs    |
    |  | flag.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showNamespace`` / ``sns``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Shows/hides the namespaces on nodes in the reference edits. Must be used with the -editNodes, -editStrings or -editAttrs flag                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``successfulEdits`` / ``scs``                                                                        | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a secondary flag used to indicate whether or not successful edits should be acted on (e.g. queried, removed, etc...). A successful edit is any edit which |
    |  | was successfully applied the last time its reference was loaded. By default successful edits will be acted on.                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``topReference`` / ``tr``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag modifies the '-rfn/-referenceNode' flag to indicate the top level ancestral reference of the target reference will be returned.                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unresolvedName`` / ``un``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag modifies the '-f/-filename' flag to indicate that the file name returned will be unresolved (i.e. it will be the path originally specified when the file|
    |  | was loaded into Maya; this path may contain environment variables and may not exist on disk). If this flag is not present, the resolved name will     be returned.|
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``withoutCopyNumber`` / ``wcn``                                                                      | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag modifies the '-f/-filename' flag to indicate that the file name returned will not have a copy number (e.g. '{1}') appended to the end. If this flag is  |
    |  | not present, the file name returned may have a copy number appended to the end.                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.referenceQuery`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Build a sample scene:
        # main scene contains a reference to mid.ma.
        # mid.ma contains a reference to bot.ma.
        # Create bot.ma with a poly sphere.
        #
        pm.polySphere()
        # Result: [nt.Transform(u'pSphere1'), nt.PolySphere(u'polySphere1')] #
        pm.file( rename='bot.ma' )
        pm.file( f=True, s=True, type='mayaAscii')
        # Create mid.ma with a poly cone.
        # Reference bot.ma into mid.ma and group
        # the sphere in bot.ma
        #
        pm.file( f=True, new=True )
        pm.file( 'bot.ma', r=True,ns='bot' )
        pm.polyCone()
        pm.group( 'bot:pSphere1' )
        pm.file( rename='mid.ma' )
        pm.file( f=True, s=True, type='mayaAscii')
        # Create a poly plane.
        # Reference mid.ma into the main scene,
        # move the cone in mid.ma, and connect
        # the plane to the sphere in bot.ma.
        #
        pm.file( f=True, new=True )
        pm.file( 'mid.ma', r=True, ns='mid' )
        pm.select( 'mid:pCone1', r=True )
        pm.move( 5, 5, 5, r=True )
        pm.polyPlane()
        pm.connectAttr( 'pPlane1.ty', 'mid:bot:polySphere1.radius' )
        # Now perform some queries:
        #
        pm.referenceQuery( 'midRN',filename=True )
        # Result: C:/Documents and Settings/user/My Documents/maya/projects/default/scenes/mid.ma
        pm.referenceQuery( 'mid:pCone1', filename=True, shortName=True )
        # Result: mid.ma
        pm.referenceQuery( 'mid:botRN', filename=True, parent=True )
        # Result: C:/Documents and Settings/user/My Documents/maya/projects/default/scenes/mid.ma
        pm.referenceQuery( 'mid.ma', referenceNode=True )
        # Result: midRN
        pm.referenceQuery( 'C:/Documents and Settings/user/My Documents/maya/projects/default/scenes/bot.ma', referenceNode=True)
        # Result: mid:botRN
        pm.referenceQuery( 'bot.ma', referenceNode=True, parent=True )
        # Result: midRN
        pm.referenceQuery( 'bot.ma', referenceNode=True, topReference=True )
        # Result: midRN
        pm.referenceQuery( 'mid:botRN',nodes=True )
        [u'mid:bot:pPlane1', u'mid:bot:pPlaneShape1', u'mid:bot:outputCloth1', u'mid:bot:nCloth1', u'mid:bot:nClothShape1', u'mid:bot:dynamicConstraint1', u'mid:bot:dynamicConstraintShape1', u'mid:bot:nurbsSphere1', u'mid:bot:nurbsSphereShape1', u'mid:bot:pSphere1', u'mid:bot:pSphereShape1', u'mid:bot:lightLinker1', u'mid:bot:layerManager', u'mid:bot:defaultLayer', u'mid:bot:renderLayerManager', u'mid:bot:defaultRenderLayer', u'mid:bot:polyPlane1', u'mid:bot:nucleus1', u'mid:bot:nComponent1', u'mid:bot:uiConfigurationScriptNode', u'mid:bot:sceneConfigurationScriptNode', u'mid:bot:nClothShape1Cache1Start', u'mid:bot:cacheBlend1', u'mid:bot:nClothShape1Cache2', u'mid:bot:nClothShape1Cache1End', u'mid:bot:makeNurbSphere1', u'mid:bot:polySphere1']
        pm.referenceQuery( 'pPlane1', isNodeReferenced=True )
        # Result: 0
        pm.referenceQuery( 'mid:pCone1', isNodeReferenced=True )
        # Result: 1
        pm.referenceQuery( 'mid:botRN', parentNamespace=True )
        # Result: mid
        pm.referenceQuery( 'mid:bot:pSphere1', parentNamespace=True )
        # Result: mid
        pm.referenceQuery( 'C:/Documents and Settings/user/My Documents/maya/projects/default/scenes/bot.ma', parentNamespace=True )
        # Result: mid
        print pm.referenceQuery( 'bot.ma', namespace=True )
        # Result: :mid:bot
        print pm.referenceQuery( 'mid:botRN', namespace=True )
        # Result: :mid:bot
        print pm.referenceQuery( 'bot.ma', namespace=True, shortName=True )
        # Result: bot
        print pm.referenceQuery( 'mid.ma', namespace=True )
        # Result: :mid
        print pm.referenceQuery( 'mid.ma', namespace=True, shortName=True )
        # Result: mid
    """

    pass


def showHelp(*args, **kwargs):
    """
    Invokes a web browser to open the on-line documentation and help files. It will open the help page for a given topic, or
    open a browser to a specific URL.               In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``absolute`` / ``a``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The specified URLis an absolute URL that should be passed directly to the web browser.                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``docs`` / ``d``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Use this flag to directly specify a help file relative to the on-line documentation root.                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``helpTable`` / ``ht``                                                                               | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Use this flag to specify which file will be used to search for help topics when the -d/docs and -a/absolute flags are not used. If only a file name is specified  |
    |  | and not a path, then the file is assumed to be in the maya application directory.If this flag does not accept an argument if it is queried.The default value is   |
    |  | helpTable.                                       Flag can have multiple arguments, passed either as a tuple or a list.                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.showHelp`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # View the documentation for the launchBrowser command
        #
        pm.showHelp( 'Commands/showHelp.html', docs=True )
        # Result: u'http://download.autodesk.com/global/docs/maya2014/en_us/Commands/showHelp.html' #
        # View the Autodesk home page
        #
        pm.showHelp( 'http://www.autodesk.com/', absolute=True )
        # Result: u'http://www.autodesk.com/' #
        # Query for the full path to the help page on the Align Tool
        #
        pm.showHelp( 'AlignTool', q=True )
        # Result: u'http://download.autodesk.com/global/docs/maya2014/en_us/files/Modify__Align_Tool.htm' #
        # Set the help lookup-table to $MAYA_APP_DIR/customHelpTable
        #
        pm.showHelp( 'customHelpTable', helpTable=True )
        # View the help topic "Particle" found in customHelpTable.dat
        #
        pm.showHelp( 'Particle' )
    """

    pass


def audioTrack(*args, **kwargs):
    """
    This command is used for inserting and removing tracks related to the audio clips displayed in the sequencer. It can
    also be used to modify the track state, for example, to lock or mute a track.               In query mode, return type
    is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``insertTrack`` / ``it``                                                                             | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to insert a new empty track at the track index specified. Indices are 1-based.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lock`` / ``l``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether all audio clips on the same track as the specified audio node are to be locked at their current location and track.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mute`` / ``m``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether all audio clips on the same track as the specified audio node are to be muted or not.                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``numTracks`` / ``nt``                                                                               | *int*                         | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | To query the number of audio tracks                                       Flag can have multiple arguments, passed either as a tuple or a list.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeEmptyTracks`` / ``ret``                                                                      | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to remove all tracks that have no clips.                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeTrack`` / ``rt``                                                                             | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to remove the track with the specified index.  The track must have no clips on it before it can be removed.                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``solo`` / ``so``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies whether all audio clips on the same track as the specified audio node are to be soloed or not.                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``swapTracks`` / ``st``                                                                              | *int, int*                    | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to swap the contents of two specified tracks. Indices are 1-based.                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.audioTrack`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #  Move the audio clip named "audio2" to track 3
        #
        pm.audioTrack( 'audio2', track=3 )
        # Lock the track containing the audio clip named "audio1"
        #
        pm.audioTrack( 'audio1', lock=True )
        # Remove any empty tracks
        #
        pm.audioTrack(removeEmptyTracks=True)
        # audioTrack -q -track audio1;
        #
        pm.audioTrack( 'audio1', q=True, track=True )
    """

    pass


def autoSave(*args, **kwargs):
    """
    Provides an interface to the auto-save mechanism.                In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``destination`` / ``dst``                                                                            | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the option for where auto-save files go. 0 - auto-saves go into the workspace autosave folder 1 - auto-saves go into the named folder (set with the -folder  |
    |  | flag) 2 - auto-saves go into a folder set by an environment variable (MAYA_AUTOSAVE_FOLDER)                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``destinationFolder`` / ``df``                                                                       | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Queries the actual destination folder for auto-saves, based on the current setting of the -destination flag, workspace rules and environment variables. Resolves  |
    |  | environment variables etc. and makes any relative path absolute (resolved relative to the workspace root). The returned string will end with a trailing separator |
    |  | ('/').                         Flag can have multiple arguments, passed either as a tuple or a list.                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``enable`` / ``en``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Enables or disables auto-saves.                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``folder`` / ``fol``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the folder for auto-saves used if the destination option is 1.                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``interval`` / ``int``                                                                               | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the interval between auto-saves (in seconds). The default interval is 600 seconds (10 minutes).                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``limitBackups`` / ``lim``                                                                           | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets whether the number of auto-save files is limited.                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxBackups`` / ``max``                                                                             | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the maximum number of auto-save files, if limiting is in effect.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perform`` / ``p``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Invokes the auto-save process.                                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``prompt`` / ``prm``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets whether the auto-save prompts the user before auto-saving.                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.autoSave`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # set the interval between auto-saves to 5 minutes
        #
        pm.autoSave( int=300 )
        
        # query the auto-save interval
        #
        pm.autoSave( q=True, int=True )
        # Result: 300.0 #
    """

    pass


def reloadImage(*args, **kwargs):
    """
    This command reloads an xpm image from disk. This can be used when the file has changed on disk and needs to be
    reloaded. The first string argument is the file name of the .xpm file. The second string argument is the name of a
    control using the specified pixmap.
    
    
    Derived from mel command `maya.cmds.reloadImage`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.reloadImage( 'image.xpm', 'iconTextButtonName' )
        pm.reloadImage( 'image', 'shelfButtonName' )
        pm.reloadImage( '~/bitmaps/maya/image.xpm', 'toolButtonName' )
    """

    pass


def mouse(*args, **kwargs):
    """
    This command allows to configure mouse.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``enableScrollWheel`` / ``esw``                                                                      | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Enable or disable scroll wheel support.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mouseButtonTracking`` / ``mbt``                                                                    | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the number (1, 2 or 3) of mouse buttons to track.Note: this is only supported on Macintosh                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mouseButtonTrackingStatus`` / ``mbs``                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | returns the current number of mouse buttons being tracked.                        Flag can have multiple arguments, passed either as a tuple or a list.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scrollWheelStatus`` / ``sws``                                                                      | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | returns the current status of scroll wheel support.                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.mouse`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.mouse( enableScrollWheel=False )
        
        mouseEnabled = pm.mouse(scrollWheelStatus=True)
        
        pm.mouse( mouseButtonTracking=1 )
        
        numberOfMouseButtons = pm.mouse(mouseButtonTrackingStatus=True)
    """

    pass


def listReferences(parentReference=None, recursive=False, namespaces=False, refNodes=False, references=True, loaded=None, unloaded=None):
    """
    Like iterReferences, except returns a list instead of an iterator.
    
    
    returns references in the scene as a list of value tuples.
    
    The values in the tuples can be namespaces, refNodes (as PyNodes), and/or
    references (as FileReferences), and are controlled by their respective
    keywords (and are returned in that order).  If only one of the three options
    is True, the result will not be a list of value tuples, but will simply be a
    list of values.
    
    Parameters
    ----------
    parentReference : string, `Path`, or `FileReference`
        a reference to get sub-references from. If None (default), the current
        scene is used.
    
    recursive : bool
        recursively determine all references and sub-references
    
    namespaces : bool
        controls whether namespaces are returned
    
    refNodes : bool
        controls whether reference PyNodes are returned
    
    refNodes : bool
        controls whether FileReferences returned
    
    recurseType : string
        if recursing, whether to do a 'breadth' or 'depth' first search;
        defaults to a 'depth' first
    
    loaded : bool or None
        whether to return loaded references in the return result; if both of
        loaded/unloaded are not given (or None), then both are assumed True;
        if only one is given, the other is assumed to have the opposite boolean
        value
    
    unloaded : bool or None
        whether to return unloaded references in the return result; if both of
        loaded/unloaded are not given (or None), then both are assumed True;
        if only one is given, the other is assumed to have the opposite boolean
        value
    """

    pass


def unloadPlugin(*args, **kwargs):
    """
    Unload plug-ins from Maya. After the successful execution of this command, plug-in services will no longer be available.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``addCallback`` / ``ac``                                                                             | *script*                      | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Add a procedure to be called just before a plugin is unloaded. The procedure should have one string argument, which will be the plugin's name.                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``force`` / ``f``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Unload the plugin even if it is providing services.  This is not recommended.  If you unload a plug-in that implements a node or data type in the scene, those    |
    |  | instances will be converted to unknown nodes or data and the scene will no longer behave properly. Maya may become unstable or even crash. If you use this flag   |
    |  | you are advised to save your scene in MayaAscii format and restart Maya as soon as possible.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeCallback`` / ``rc``                                                                          | *script*                      | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Remove a procedure which was previously added with -addCallback.                          Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.unloadPlugin`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Unload the plugin that has the internal name "newNode"
        #
        pm.unloadPlugin( 'newNode.py' )
    """

    pass


def findType(*args, **kwargs):
    """
    The findTypecommand is used to search through a dependency subgraph on a certain node to find all nodes of the given
    type. The search can go either upstream (input connections) or downstream (output connections). The plug/attribute
    dependencies are not taken into account when searching for matching nodes, only the connections.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``deep`` / ``d``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Find all nodes of the given type instead of just the first.                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exact`` / ``e``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Match node types exactly instead of any in a node hierarchy.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``forward`` / ``f``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Look forwards (downstream) through the graph rather than backwards (upstream) for matching nodes.                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``t``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Type of node to look for (e.g. transform). This flag is mandatory.                                        Flag can have multiple arguments, passed either as a    |
    |  | tuple or a list.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.findType`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.createNode( 'transform', name='silly' )
        # Result: nt.Transform(u'silly') #
        pm.createNode( 'transform', name='putty' )
        # Result: nt.Transform(u'putty') #
        pm.connectAttr( 'silly.tx', 'putty.tx' )
        # Find transform nodes connected to node "silly"
        #
        pm.findType( type='transform', 'silly' )
        silly
        pm.select( 'silly' )
        #
        # Same again from selection list
        #
        pm.findType( type='transform' )
        silly
        pm.setKeyframe( t=10 )
        #
        # Find all time nodes
        #
        pm.findType( type='time', deep=True, e=True )
        u'time1'  
        #
        # Find all anim curve nodes
        #
        pm.findType( type="animCurve", deep=True )
        u'silly_visibility', u'silly_translateX', u'silly_translateY', u'silly_translateZ', u'silly_rotateX', u'silly_rotateY', u'silly_rotateZ', u'silly_scaleX', u'silly_scaleY', u'silly_scaleZ'
    """

    pass


def pluginDisplayFilter(*args, **kwargs):
    """
    Register, deregister or query a plugin display filter. Plug-ins can use this command to register their own display
    filters which will appear in the 'Show' menus on Maya's model panels.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``classification`` / ``cls``                                                                         | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The classification used to filter objects in Viewport 2.0. This classification is the same as MFnPlugin::registerNode(). If the node was registered with multiple |
    |  | classifications, use the one beginning with drawdb. The default value of this flag is an empty string (). It will not filter any objects in Viewport 2.0.         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deregister`` / ``dr``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Deregister a plugin display filter.                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exists`` / ``ex``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true if the specified filter exists, false otherwise. Other flags are ignored.                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``label`` / ``l``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The string to be displayed for this filter in the UI. E.g. in the 'Show' menu of a model panel. The default value of this flag is the same as the plugin display  |
    |  | filter name.                                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listFilters`` / ``lf``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns an array of all plugin display filters.                                           Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``register`` / ``r``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Register a plugin display filter. The -register is implied if both -register and -deregister flags are missing in create mode. You are responsible for            |
    |  | deregistering any filters which you register. Filters are reference counted, meaning that if you register the same filter twice then you will have to deregister  |
    |  | it twice as well.                                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.pluginDisplayFilter`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #    Register a plugin display filter.
        #
        pm.pluginDisplayFilter('myDisplayFilter', register = 1, label = 'My Display Filter', classification = 'drawdb/geometry/myShape')
        # Result: u'myDisplayFilter' #
        #    Deregister a plugin display filter.
        #
        pm.pluginDisplayFilter('myDisplayFilter', deregister = 1)
        # Result: u'myDisplayFilter' #
        #    List all plugin display filters.
        #
        filters = pm.pluginDisplayFilter(q = 1, listFilters = 1)
        #    Query the label of a display filter
        #
        label = pm.pluginDisplayFilter('myDisplayFilter', q = 1, label = 1)
    """

    pass


def flushUndo(*args, **kwargs):
    """
    Removes everything from the undo queue, freeing up memory.
    
    
    Derived from mel command `maya.cmds.flushUndo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.flushUndo()
    """

    pass


def displayInfo(*args, **kwargs):
    pass


def redo(*args, **kwargs):
    """
    Takes the most recently undone command from the undo list and redoes it.
    
    
    Derived from mel command `maya.cmds.redo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # In this particular example, each line needs to be executed
        # separately one after the other. Executing lines separately
        # guaranties that commands are properly registered in the undo
        # stack.
        
        pm.polyCube()
        # Result: [nt.Transform(u'pCube1'), nt.PolyCube(u'polyCube1')] #
        
        pm.undo()
        # Undo: pm.polyCube()
         #
        
        pm.redo()
        # Redo: pm.polyCube()
         #
        [u'pCube1', u'polyCube1']
    """

    pass


def exportSelectedAnim(exportPath, **kwargs):
    """
    Export all animation nodes and animation helper nodes from the selected objects in the scene. See -ean/exportAnim flag description for details on usage of animation files.                       
    
    Flags:
      - force:
          Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
          remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
          root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
          prompting a dialog that warns user about the lost of edits.
      - type:
          Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
          audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
          file types that match this file.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def sceneName():
    """
    return the name of the current scene.                     
    
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def _translateEditFlags(kwargs, addKwargs=True):
    """
    Given the pymel values for successfulEdits/failedEdits (which may be
    True, False, or None), returns the corresponding maya.cmds values to use
    """

    pass


def dagObjectCompare(*args, **kwargs):
    """
    dagObjectCompare can be used to compare to compare objects based on: type -  Currently supports transform nodes and
    shape nodesrelatives - Compares DAG objects' children and parentsconnections - Checks to make sure the two dags are
    connected to the same sources and destinationsattributes - Checks to make sure that the properties of active attributes
    are the same
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``a``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Compare dag object attributes                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``bail`` / ``b``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Bail on first error or bail on category. Legal values are never, first, and category.                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``connection`` / ``c``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Compare dag connections                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``namespace`` / ``n``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The baseline namespace                                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``relative`` / ``r``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | dag relatives                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``short`` / ``s``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Compress output to short form (not as verbose)                                    Flag can have multiple arguments, passed either as a tuple or a list.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``t``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Compare based on dag object type                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dagObjectCompare`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Compare two objects based on type and their relatives where one is in the namespace "base":
        pm.dagObjectCompare( t=True, r=True, n="base" )
        # Compare two objects based on their connections and attributes where one is in the namespace "base" , break on first error:
        pm.dagObjectCompare( c=True, a=True, b="first")
        # Compare two objects based on their type, connections, attributes, relatives and break on error while finishing current category:
        pm.dagObjectCompare( t=True, r=True, c=True, a=True, b=True, category=True, n="base")
    """

    pass


def getFileList(*args, **kwargs):
    """
    Returns a list of files matching an optional wildcard pattern. Note that this command works directly on raw system files
    and does not go through standard Maya file path resolution.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``filespec`` / ``fs``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | wildcard specifier for search.                    Flag can have multiple arguments, passed either as a tuple or a list.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``folder`` / ``fld``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | return a directory listing                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.getFileList`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # List the contents of the user's projects directory
        #
        pm.getFileList( folder=pm.internalVar(userWorkspaceDir=True) )
        # Result: [u'default', u'mydir'] #
        
        # List all MEL files in the user's script directory
        #
        pm.getFileList( folder=pm.internalVar(userScriptDir=True), filespec='*.mel' )
        # Result: [] #
    """

    pass


def dbtrace(*args, **kwargs):
    """
    The dbtracecommand is used to manipulate trace objects.           The keyword is the only mandatory argument, indicating
    which trace           object is to be altered.           Trace Objects to affect (keywordKEY)Optional filtering criteria
    (filterFILTER)Function (off, outputFILE, mark, titleTITLE, timed: default operation is to enable traces)You can use the
    query mode to find out which keywords are currently           active (query with no arguments) or inactive (query with
    the offargument).           You can enhance that query with or without a keyword argument to find           out where
    their output is going (query with the outputargument), out what filters are currently applied (query with the
    filterargument), or if their output will be           timestamped (query with the timedargument).                 In
    query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``filter`` / ``f``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the filter object for these trace objects (see 'dgfilter')                                    Flag can have multiple arguments, passed either as a tuple or a |
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``keyword`` / ``k``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Keyword of the trace objects to affect                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mark`` / ``m``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Display a mark for all outputs of defined trace objects                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``off`` / ``boolean``                                                                                | *Toggle the traces off.  If   | .. image:: /images/create.gif |
    |                                                                                                      | omitted it will turn them on.*|                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``output`` / ``o``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Destination file of the affected trace objects.  Use the special names stdoutand stderrto redirect to your command window. The special name msdevis available on  |
    |  | Windows to direct your output to the debug tab in the output window of Visual Studio.                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``timed`` / ``tm``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turn on/off timing information in the output of the specified trace objects.                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``title`` / ``t``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Display a title mark for all outputs of defined trace objects                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``verbose`` / ``v``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Include all traces in output and filter queries, not just those turned on.                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dbtrace`
    """

    pass


def cacheFileCombine(*args, **kwargs):
    """
    Creates a cacheBlend node that can be used to combine, layer or blend multiple cacheFiles for a given object.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``cacheIndex`` / ``ci``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A query only flag that returns the index related to the cache specified with the connectCache flag.                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``channelName`` / ``cnm``                                                                            | *unicode*                     | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in conjunction with the connectCache flag to indicate the channel(s) that should be connected.  If not specified, the first channel in the file is used.     |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``connectCache`` / ``cc``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | An edit flag that specifies a cacheFile node that should be connected to the next available index on the specified cacheBlend node. As a query flag, it returns a |
    |  | string array containing the cacheFiles that feed into the specified cacheBlend node. In query mode, this flag can accept a value.                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``keepWeights`` / ``kw``                                                                             | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a flag for use in combination with the connectCache flag only. By default, the connectCache flag will set all weights other than the newly added          |
    |  | cacheWeight to 0 so that the new cache gets complete control. This flag disables that behavior so that all existing blend weights are retained.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``layerNode`` / ``ln``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A query flag that returns a string array of the existing cacheBlends on the selected object(s). Returns an empty string array if no cacheBlends are found.        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``nextAvailable`` / ``na``                                                                           | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A query flag that returns the next available index on the selected cacheBlend node.                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``object`` / ``obj``                                                                                 | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used in combination with the objectIndex flag. It is used to specify the object whose index you wish to query.                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``objectIndex`` / ``oi``                                                                             | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | In edit mode, used in conjunction with the connectCache flag to indicate the objectIndex to be connected. In query mode, returns the index related to the object  |
    |  | specified with the object flag.                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.cacheFileCombine`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Create a cacheBlend node so that additional caches can be added to
        # the shape. This will attach the existing cacheFile on the shape
        # to the new cacheBlend node.
        #
        pm.select( 'cachedShape', r=True )
        newBlend = pm.cacheFileCombine()
        # attach an additional cacheFile to the cacheBlend node
        #
        pm.cacheFileCombine( newBlend[0], e=True, cc='cacheFile2' )
        # query the index of the newly connected cache
        #
        pm.cacheFileCombine( newBlend[0], cc='cacheFile2', query=True, cacheIndex=True )
        # When more than one object is driven by the caches connected
        # to the cacheBlend node, the -channelName and -objectIndex flags can be
        # used to control which is connected.
        #
        # Query the objectIndex for the armShape geometry driven by cacheBlend3:
        #
        index = pm.cacheFileCombine('cacheBlend3' ,object='armShape', query=True, objectIndex=True)
        # Connect another cache up to drive the armShape
        #
        pm.cacheFileCombine( 'cacheBlend3', channelName='myChannel', objectIndex=index, e=True, cc='cacheFile2' )
    """

    pass


def dgInfo(*args, **kwargs):
    """
    This command prints information about the DG in a text-oriented manner.  The scope of the information printed is the
    entire graph if the -all flag is used, the nodes/plugs on the command line if they were specified, and the selection
    list, in that order. Each plug on a connection will have two pieces of state information displayed together at the end
    of the line on which they are printed. CLEAN PROPis the normal state for a graph that has been successfully evaluated.
    It indicates that the plug value in the node's datablock is correct and that any successive changes to it (or values
    upstream from it) are propagated to all plugs depending on it (e.g. downstream connections or affectedoutputs). DIRTY
    BLOCKis the normal state for a plug whose upstream values have changed but no evaluation request has come through for
    that plug's value. The DIRTYpart indicates that the current value of the plug held in the datablock may or may not be
    correct, depending on how the upstream values affect it. Requesting it directly via a getAttrcommand or indirectly via a
    request for values downstream of it will trigger a DG evaluation of all upstream plugs. The BLOCKpart is an optimization
    that prevents excessive dirty flag propagation when many values are changing e.g. a frame change in an animated sequece.
    It means that any changes to values upstream from this plug will not send any further dirty messages to
    downstream/affected plugs. DIRTY PROPis a less common but still valid state for a plug whose upstream values have
    changed but no evaluation request has come through for that plug's value. Like the DIRTY BLOCKstate it will trigger an
    evaluaton when it's value is requested. Where it differs is that when another change comes through from an upstream plug
    this plug will (again) propagate the dirty message to all downstream/affected plugs. You will only see this state when
    the DG was not certain that all downstream plugs were notified of their dirty status the last time this plug was marked
    dirty itself (e.g. if the dirty propagation was intercepted by a node or the graph connections changed since the last
    dirty message). CLEAN BLOCKshould never be seen in a valid DG. This indicates that while the value of the plug is clean
    (i.e. valid) it will not propagate a dirty state when its value changes. That means downstream nodes will not be
    notified that the graph is changing and they will not evaluate properly. Recovering from this invalid state requires
    entering the command dgdirty -ato mark everything dirty and restart proper evaluation. (Think of this command as the
    CTL-ALT-DELof the DG world.)
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``allNodes`` / ``all``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Use the entire graph as the context                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``connections`` / ``c``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Print the connection information                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dirty`` / ``d``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only print dirty/clean nodes/plugs/connections.  Default is both                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``island`` / ``island``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Print detailed debug information about the island for each node.  Note that this flag will typically generate a large amount of debug information, so it is       |
    |  | recommended that the list of nodes passed to the command be brief when using the islandDetail flag. The information includes the full list of nodes in the island,|
    |  | as well as all islands connected to the island.                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``nodes`` / ``n``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Print the specified nodes (or the entire graph if -all is used)                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``nonDeletable`` / ``nd``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Include non-deletable nodes as well (normally not of interest)                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``outputFile`` / ``of``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Send the output to the file FILE instead of STDERR                                        Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``propagation`` / ``p``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only print propagating/not propagating nodes/plugs/connections. Default is both.                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``short`` / ``s``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Print using short format instead of long                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``size`` / ``sz``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Show datablock sizes for all specified nodes. Return value is tuple of all selected nodes (NumberOfNodes, NumberOfDatablocks, TotalDatablockMemory)               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``subgraph`` / ``sub``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Print the subgraph affected by the node or plugs (or all nodes in the graph grouped in subgraphs if -all is used)                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``nt``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Filter output to only show nodes of type NODETYPE                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dgInfo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # create a node
        pm.createNode('transform',name='NODE')
        # Result: nt.Transform(u'NODE') #
        pm.setKeyframe('NODE.translate')
        # Result: 3 #
        # Print all things connected to node NODE
        pm.dgInfo( 'NODE', c=True )
        # Print all connections currently in the graph
        pm.dgInfo( c=True, all=True )
        # Print the datablock size of all nodes currently in the graph
        pm.dgInfo( sz=True, all=True )
        # Result: [281, 281, 38264] #
        # Return: [12, 12, 12314]
        # Print all connections to attribute tx on node NODE
        pm.dgInfo('NODE.tx',c=True)
        # Print all dirty connections in the entire graph
        pm.dgInfo( c=True, all=True, d=True )
    """

    pass


def exportEdits(*args, **kwargs):
    """
    Use this command to export edits made in the scene to a separate file. The exported file can be subsequently imported to
    another scene. Edits may include: nodes, connections and reference edits such as value changes. The nodes that are
    included in the exported file will be based on the options used. At least one option flag which describes the set of
    target nodes to include in the exported file must be specified (e.g. 'selected', 'onReferenceNode'). Use the inclusion
    flags ('includeAnimation', 'includeShaders', 'includeNetwork') to specify which additional related nodes will be added
    to the export list. In export mode, when the command completes successfully, the name of the exported file will be
    returned. In query mode, this command will return information about the contents of the export file.  No file export is
    performed in query mode. Currently query mode will return the list of nodes that will be considered for inclusion in the
    exported file based on the combination of options specified
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``editCommand`` / ``ec``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a secondary flag used to indicate which type of reference edits should be considered by the command. If this flag is not specified all edit types will be |
    |  | included. This flag requires a string parameter. Valid values are: addAttr, connectAttr, deleteAttr, disconnectAttr, parent, setAttr, lockand unlock. In some     |
    |  | contexts, this flag may be specified more than once to specify multiple edit types to consider.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``excludeHierarchy`` / ``ehr``                                                                       | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | By default exporting passes all DAG parents and DAG history to the export file. To prevent any DAG relations not otherwise connected to the target nodes to be    |
    |  | output, specify the -excludeHierarchy flag.                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``excludeNode`` / ``en``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Prevent the node from being included in the list of nodes being exported. This flag is useful to exclude specific scene nodes that might otherwise be exported. In|
    |  | the case where more than one Maya node has the same name, you can specify the DAG path to uniquely identify the node.                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exportSelected`` / ``exs``                                                                         | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The selected nodes and their connections to each other will be exported. Additionally, any dangling connections to non-exported nodes will be exported. Any       |
    |  | default nodes (the internal nodes that Maya creates on startup) that are selected are skipped. Please note that when using the exportSelected flag, only selected |
    |  | nodes are exported, and -include/-exclude flags such as -includeHierarchy are ignored.                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``force`` / ``f``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Force the export action to take place. This flag is required to overwrite an existing file.                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``includeAnimation`` / ``ian``                                                                       | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Additionally includes animation nodes and animation helper nodes associated with the target nodes being exported.                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``includeConstraints`` / ``ic``                                                                      | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Additionally include constraint-related nodes associated with the target nodes being exported.                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``includeDeformers`` / ``idf``                                                                       | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Additionally include deformer networks associated with the target nodes being exported.                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``includeNetwork`` / ``inw``                                                                         | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Additionally includes the network of nodes connected to the target nodes being exported.                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``includeNode`` / ``includeNode``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Additionally include the named node in the list of nodes being exported. In the case where more than one Maya node has the same name, you can specify the DAG path|
    |  | to uniquely identify the node.                                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``includeSetAttrs`` / ``isa``                                                                        | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When using the -selected/-sel flag, if any of the selected nodes are referenced, also include/exclude any setAttr edits on those nodes. If used with the          |
    |  | -onReferenceNode/-orn flag, include/exclude any setAttr edits on the reference.                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``includeSetDrivenKeys`` / ``sdk``                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Additionally include setDrivenKey-related nodes associated with the target nodes being exported.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``includeShaders`` / ``ish``                                                                         | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Additionally include shaders associated with the target nodes being exported.                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``onReferenceNode`` / ``orn``                                                                        | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a secondary flag used to indicate that only those edits which are stored on the indicated reference node should be considered. This flag only supports    |
    |  | multiple uses when specified with the exportEditscommand.                                          Flag can have multiple arguments, passed either as a tuple or a|
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selected`` / ``sel``                                                                               | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Export will operate on the list of nodes currently selected. This flag differs from the exportSelected flag in that the selected nodes are not exported, only the |
    |  | edits on them, and any nodes found via the include flags the are used (such as includeAnimation, includeNetwork and so on).                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``typ``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the type of the exported file. Valid values are editMAor editMB. Note that this command respects the global defaultExtensionssetting for file naming that is  |
    |  | controlled with the file command defaultExtensions option.  See the file command for more information.                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.exportEdits`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # query nodes to be exported, target is selected nodes, include related shaders
        nodeList = pm.exportEdits(query=1,selected=1,includeShaders=1)
        # exported selected nodes and related animation nodes to file
        pm.exportEdits("myExportFile.ma",type='editMA',selected=1,includeShaders=1)
        # Result: C:/Documents and Settings/user/My Documents/maya/projects/default/scenes/myExportFile.editMA
    """

    pass


def warning(*args, **kwargs):
    """
    The warning command is provided so that the user can issue warning messages from his/her scripts. The string argument is
    displayed in the command window (or stdout if running in batch mode) after being prefixed with a warning message heading
    and surrounded by the appropriate language separators (# for Python, // for Mel).
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``noContext`` / ``n``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Do not include the context information with the warning message.                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showLineNumber`` / ``sl``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Obsolete. Will be deleted in the next version of Maya. Use the checkbox in the script editor that enables line number display instead.                            |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.warning`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        import maya.cmds as cmds
        def lightWarning():
            l = pm.ls( lights=True )
            if len(l) == 0:
                pm.warning( "No Lights" )
        lightWarning()
        #
        # The above will produce the following output:
        #
        #   # Warning: No Lights #
        #
        # When the option to show line numbers in errors is enabled the output will
        # be the following:
        #
        #   # Warning: line 4 of 'lightWarning' in '"maya console'": No Lights #
        #
    """

    pass


def unknownPlugin(*args, **kwargs):
    """
    Allows querying of the unknown plug-ins used by the scene, and provides a means to remove them.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``dataTypes`` / ``dt``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the data types associated with the given unknown plug-in. This will always be empty for pre-Maya 2014 files.                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``list`` / ``l``                                                                                     | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Lists the unknown plug-ins in the scene.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``nodeTypes`` / ``nt``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the node types associated with the given unknown plug-in. This will always be empty for pre-Maya 2014 files.                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``remove`` / ``r``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Removes the given unknown plug-in from the scene. For Maya 2014 files and onwards, this will fail if node or data types defined by the plug-in are still in use.  |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``version`` / ``v``                                                                                  | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the version string of the given unknown plug-in.                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.unknownPlugin`
    """

    pass


def timer(*args, **kwargs):
    """
    Allow simple timing of scripts and commands. The resolution of this timer is at the level of your OS's
    gettimeofday()function.  Note:This command does not handle stacked calls. For example, this code below will give an
    incorrect answer on the second timer -ecall.timer -s; timer -s; timer -e; timer -e; To do this use named timers: timer
    -s; timer -s -name innerTimer; timer -e -name innerTimer; timer -e; I the -e flag or -lap flag return the time elapsed
    since the last 'timer -s' call.I the -s flag has no return value.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``endTimer`` / ``e``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Stop the timer and return the time elapsed since the timer was started (in seconds). Once a timer is turned off it no longer exists, though it can be recreated   |
    |  | with a new start                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lapTime`` / ``lap``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Get the lap time of the timer (time elapsed since start in seconds). Unlike the endflag this keeps the timer running.                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Use a named timer for the operation. If this is omitted then the default timer is assumed.                                        Flag can have multiple          |
    |  | arguments, passed either as a tuple or a list.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``startTimer`` / ``s``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Start the timer.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.timer`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.timer( s=True )
        # Result: u"Timer 'defaultTimer' started." #
        # code being timed
        print "START: time this"
        for i in range (0, 50):
                print ("time this "+str(i))
        print "END: time this"
        pm.timer( e=True )
        # Result: 0.084618 #
        # Named timers can be used for nesting
        pm.timer( s=True, name="outerLoop" )
        # Result: u"Timer 'outerLoop' started." #
        print "START: macro loop timing"
        for i in range(0,50):
                pm.timer( s=True )
                for j in range(5,50):
                        newObjs = pm.sphere( spans=j )
                        pm.delete( newObjs )
                innerTime = pm.timer( e=True )
                lapTime = pm.timer( lap=True, name="outerLoop" )
                print "\tInner loop %d = %g" % (i, innerTime)
                print "\t       SUB = %g" % lapTime
        fullTime = pm.timer( e=True, name="outerLoop" )
        print "END: Full timing was %g" % fullTime
    """

    pass


def saveImage(*args, **kwargs):
    """
    This command creates a static image control for non-xpm files used to display a thumbnail image of the scene file.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``annotation`` / ``ann``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Annotate the control with an extra string value.                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``backgroundColor`` / ``bgc``                                                                        | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The background color of the control. The arguments correspond to the red, green, and blue color components. Each component ranges in value from 0.0 to 1.0. When  |
    |  | setting backgroundColor, the background is automatically enabled, unless enableBackground is also specified with a false value.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``currentView`` / ``cv``                                                                             | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Generate the image from the current view.                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``defineTemplate`` / ``dt``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Puts a command in a mode where any other flags and args are parsed and added to the command template specified in the argument. They will be used as default      |
    |  | arguments in any subsequent invocations of the command when templateName is set as the current template.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``docTag`` / ``dtg``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Add a documentation flag to the control.  The documentation flag has a directory structure like hierarchy. Eg. -dt render/multiLister/createNode/material         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dragCallback`` / ``dgc``                                                                           | *script*                      | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Adds a callback that is called when the middle mouse button is pressed.  The MEL version of the callback is of the form: global proc string[] callbackName(string |
    |  | $dragControl, int $x, int $y, int $mods) The proc returns a string array that is transferred to the drop site. By convention the first string in the array        |
    |  | describes the user settable message type.  Controls that are application defined drag sources may ignore the callback. $mods allows testing for the key modifiers |
    |  | CTL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTL, 3 == CTL + SHIFT. In Python, it is similar, but there are two ways to specify the     |
    |  | callback.  The recommended way is to pass a Python function object as the argument.  In that case, the Python callback should have the form: def callbackName(    |
    |  | dragControl, x, y, modifiers ): The values of these arguments are the same as those for the MEL version above. The other way to specify the callback in Python is |
    |  | to specify a string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values|
    |  | are passed in a dictionary with the keys dragControl, x, y, modifiers.  The dragControlvalue is a string and the other values are integers (eg the callback string|
    |  | could be print '%(dragControl)s %(x)d %(y)d %(modifiers)d'                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dropCallback`` / ``dpc``                                                                           | *script*                      | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Adds a callback that is called when a drag and drop operation is released above the drop site.  The MEL version of the callback is of the form: global proc       |
    |  | callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type) The proc receives a string array that is transferred from the   |
    |  | drag source. The first string in the msgs array describes the user defined message type. Controls that are application defined drop sites may ignore the callback.|
    |  | $type can have values of 1 == Move, 2 == Copy, 3 == Link. In Python, it is similar, but there are two ways to specify the callback.  The recommended way is to    |
    |  | pass a Python function object as the argument.  In that case, the Python callback should have the form: def pythonDropTest( dragControl, dropControl, messages, x,|
    |  | y, dragType ): The values of these arguments are the same as those for the MEL version above. The other way to specify the callback in Python is to specify a     |
    |  | string to be executed.  In that case, the string will have the values substituted into it via the standard Python format operator.  The format values are passed  |
    |  | in a dictionary with the keys dragControl, dropControl, messages, x, y, type.  The dragControlvalue is a string and the other values are integers (eg the callback|
    |  | string could be print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``enable`` / ``en``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The enable state of the control.  By default, this flag is set to true and the control is enabled.  Specify false and the control will appear dimmed or greyed-out|
    |  | indicating it is disabled.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``enableBackground`` / ``ebg``                                                                       | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Enables the background color of the control.                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exists`` / ``ex``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true|false depending upon whether the specified object exists.  Other flags are ignored.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fullPathName`` / ``fpn``                                                                           | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the full path name of the widget, which includes all the parents                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``height`` / ``h``                                                                                   | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The height of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``image`` / ``i``                                                                                    | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``isObscured`` / ``io``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return whether the control can actually be seen by the user. The control will be obscured if its state is invisible, if it is blocked (entirely or partially) by  |
    |  | some other control, if it or a parent layout is unmanaged, or if the control's window is invisible or iconified.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``manage`` / ``m``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Manage state of the control.  An unmanaged control is not visible, nor does it take up any screen real estate.  All controls are created managed by default.      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``noBackground`` / ``nbg``                                                                           | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Clear/reset the control's background. Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this|
    |  | flag is inherited by children of this control.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``numberOfPopupMenus`` / ``npm``                                                                     | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the number of popup menus attached to this control.                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``objectThumbnail`` / ``ot``                                                                         | *unicode*                     | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Use an image of the named object, if possible.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``parent`` / ``p``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The parent layout for this control.                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``popupMenuArray`` / ``pma``                                                                         | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the names of all the popup menus attached to this control.                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``preventOverride`` / ``po``                                                                         | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If true, this flag disallows overriding the control's attribute via the control's right mouse button menu.                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``sceneFile`` / ``sf``                                                                               | *unicode*                     | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The name of the file that the icon is to be associated with.                      Flag can have multiple arguments, passed either as a tuple or a list.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``useTemplate`` / ``ut``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Force the command to use a command template other than the current one.                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``visible`` / ``vis``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The visible state of the control.  A control is created visible by default.  Note that a control's actual appearance is also dependent on the visible state of its|
    |  | parent layout(s).                                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``visibleChangeCommand`` / ``vcc``                                                                   | *script*                      | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Command that gets executed when visible state of the control changes.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``width`` / ``w``                                                                                    | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The width of the control.  The control will attempt to be this size if it is not overruled by parent layout conditions.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.saveImage`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        window = pm.window('window')
        pm.paneLayout()
        # Result: ui.PaneLayout('window|paneLayout11') #
        pm.saveImage( currentView=True )
        # Result: u'window|paneLayout11|saveImage1' #
        pm.showWindow( window )
    """

    pass


def _safeEval(s):
    pass


def melInfo(*args, **kwargs):
    """
    This command returns the names of all global MEL procedures that are currently defined as a string array. The user can
    query the definition of each MEL procedure using the whatIscommand.
    
    
    Derived from mel command `maya.cmds.melInfo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Query the names of all the global MEL procedures currently defined.
        #
        procs = pm.melInfo()
    """

    pass


def _getTypeFromExtension(path, mode='write'):
    """
    Parameters
    ----------
    path : str
        path from with to pull the extension from - note that it may NOT be
        ONLY the extension - ie, "obj" and ".obj", will not work, but
        "foo.obj" will
    mode : {'write', 'read'}
        the type is basically a string name of a file translator, which can
        have different ones registered for reading or writing; this specifies
        whether you're looking for the read or write translator
    """

    pass


def selLoadSettings(*args, **kwargs):
    """
    This command is used to edit and query information about the implicit load settings. Currently this is primarily
    intended for internal use within the Preload Reference Editor. selLoadSettings acts on load setting IDs. When implict
    load settings are built for a target scene, there will be one load setting for each reference in the target scene. Each
    load setting has a numerical ID which is its index in a pre-order traversal of the target reference hierarchy (with the
    root scenefile being assigned an ID of 0). Although the IDs are numerical they must be passed to the command as string
    array. Example: Given the scene: a        / \       b   c          / \         d   e where: a references b and c c
    references d and e the IDs will be as follows: a = 0 b = 1 c = 2 d = 3 e = 4 selLoadSettings can be used to change the
    load state of a reference: whether it will be loaded or unloaded (deferred) when the target scene is opened. Note:
    selLoadSettings can accept multiple command parameters, but the order must be selected carefully such that no reference
    is set to the loaded state while its parent is in the unlaoded state. Given the scene: a | b [-] | c [-] where: a
    references b b references c a = 0 b = 1 c = 2 and b and c are currently in the unloaded state. The following command
    will succeed and change both b and c to the loaded state: selLoadSettings -e -deferReference 0 12; whereas the following
    command will fail and leave both b and c in the unloaded state: selLoadSettings -e -deferReference 0 21; Bear in mind
    that the following command will also change both b and c to the loaded state: selLoadSettings -e -deferReference 0 1;
    This is because setting a reference to the loaded state automatically sets all child references to the loaded state as
    well. And vice versa, setting a reference the the unloaded state automatically sets all child reference to the unloaded
    state.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``activeProxy`` / ``ap``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Change or query the active proxy of a proxy set. In query mode, returns the proxyTag of the active proxy; in edit mode, finds the proxy in the proxySet with the  |
    |  | given tag and makes it the active proxy.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deferReference`` / ``dr``                                                                          | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Change or query the load state of a reference.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fileName`` / ``fn``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the file name reference file(s) associated with the indicated load setting(s).                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``numSettings`` / ``ns``                                                                             | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the number of settings in the group of implicit load settings. This is equivalent to number of references in the scene plus 1.                             |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``proxyManager`` / ``pm``                                                                            | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the name(s) of the proxy manager(s) associated with the indicated load setting(s).                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``proxySetFiles`` / ``psf``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the name(s) of the proxy(ies) available in the proxy set associated with the indicated load setting(s).                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``proxySetTags`` / ``pst``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the name(s) of the proxy tag(s) available in the proxy set associated with the indicated load setting(s).                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``proxyTag`` / ``pt``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the name(s) of the proxy tag(s) associated with the indicated load setting(s).                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``referenceNode`` / ``rfn``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the name(s) of the reference node(s) associated with the indicated load setting(s).                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shortName`` / ``shn``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Formats the return value of the 'fileName' query flag to only return the short name(s) of the reference file(s).                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unresolvedName`` / ``un``                                                                          | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Formats the return value of the 'fileName' query flag to return the unresolved name(s) of the reference file(s). The unresolved file name is the file name used   |
    |  | when the reference was created, whether or not that file actually exists on disk. When Maya encounters a file name which does not exist on disk it attempts to    |
    |  | resolve the name by looking for the file in a number of other locations. By default the 'fileName' flag will return this resolved value.                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.selLoadSettings`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Given the scene:
        #
        #
        #        a [+]
        #       /     \
        #      b [-]   c [+]
        #             /     \
        #            d [-]   e [+]
        #
        # With the IDs:
        #    a = 0
        #    b = 1
        #    c = 2
        #    d = 3
        #    e = 4
        # set c, d, and e to the unloaded state
        pm.selLoadSettings( '2', '3', '4', e=True, deferReference=1 )
        # this will also set c, d, and e to the unloaded state
        pm.selLoadSettings( '2', e=True, deferReference=1 )
        # set b to the loaded state
        pm.selLoadSettings( '1', e=True, deferReference=0 )
        # set b and d to the loaded state
        pm.selLoadSettings( '1', '3', e=True, deferReference=0 )
    """

    pass


def timerX(*args, **kwargs):
    """
    Used to calculate elapsed time. This command returns sub-second accurate time values. It is useful from scripts for
    timing the length of operations. Call this command before and after the operation you wish to time. On the first call,
    do not use any flags. It will return the start time. Save this value. After the operation, call this command a second
    time, and pass the saved start time using the -st flag. The elapsed time will be returned.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``startTime`` / ``st``                                                                               | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When this flag is used, the command returns the elapsed time since the specified start time.                      Flag can have multiple arguments, passed either |
    |  | as a tuple or a list.                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.timerX`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Example 1: Simple timing
        #
        start = pm.timerX()
        # code that is being timed
        totalTime = pm.timerX(startTime=start)
        print "Total time: ", totalTime
        
        # Example 2: Iterative timing
        #
        startTime = pm.timerX()
        for i in range(0,5):
          elapsedTime = pm.timerX()
          print "Elapsed Time: ", elapsedTime
        
        # Example 3: Stacked timing calls
        #
        startTime1 = pm.timerX()
        startTime2 = pm.timerX()
        for i in range(0,5):
          elapsedTime = pm.timerX()
          print "Elapsed Time: ", elapsedTime
        
        totalTime = pm.timerX(startTime=startTime1)
        print "Total Time: ", totalTime
    """

    pass


def loadPlugin(*args, **kwargs):
    """
    Load plug-ins into Maya. The parameter(s) to this command are either the names or pathnames of plug-in files.  The
    convention for naming plug-ins is to use a .so extension on Linux, a .mll extension on Windows and .bundle extension on
    Mac OS X. If no extension is provided then the default extension for the platform will be used. To load a Python plugin
    you must explicitly supply the '.py' extension. If the plugin was specified with a pathname then that is where the
    plugin will be searched for. If no pathname was provided then the current working directory (i.e. the one returned by
    Maya's 'pwd' command) will be searched, followed by the directories in the MAYA_PLUG_IN_PATH environment variable. When
    the plug-in is loaded, the name used in Maya's internal plug-in registry for the plug-in information will be the file
    name with the extension removed.  For example, if you load the plug-in newNode.mllthe name used in the Maya's registry
    will be newNode.  This value as well as that value with either a .so, .mllor .bundleextension can be used as valid
    arguments to either the unloadPlugin or pluginInfo commands.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``addCallback`` / ``ac``                                                                             | *script*                      | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Add a MEL or Python callback script to be called after a plug-in is loaded.  For MEL, the procedure should have the following signature: global proc              |
    |  | procedureName(string $pluginName).  For Python, you may specify either a script as a string, or a Python callable object such as a function.  If you specify a    |
    |  | string, then put the formatting specifier %swhere you want the name of the plug-in to be inserted.  If you specify a callable such as a function, then the name of|
    |  | the plug-in will be passed as an argument.                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``allPlugins`` / ``a``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Cause all plug-ins in the search path specified in MAYA_PLUG_IN_PATH to be loaded.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set a user defined name for the plug-ins that are loaded.  If the name is already taken, then a number will be added to the end of the name to make it unique.    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``qObsolete`` / ``q``                                                                                | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``quiet`` / ``qt``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Don't print a warning if you attempt to load a plug-in that is already loaded.                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeCallback`` / ``rc``                                                                          | *script*                      | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Removes a procedure which was previously added with -addCallback.                         Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.loadPlugin`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Load the plug-in named "newNode" into Maya.
        #
        pm.loadPlugin( 'newNode.py' )
        
        # Load all the plug-ins found in all the directories that are
        # included in MAYA_PLUG_IN_PATH.
        #
        pm.loadPlugin( allPlugins=True )
    """

    pass


def exportAsReference(exportPath, **kwargs):
    """
    Export the selected objects into a reference file with the given name. The file is saved on disk during the process. Returns the name of the reference created.                   
    
    Flags:
      - namespace:
          The namespace name to use that will group all objects during importing and referencing. Change the namespace used to
          group all the objects from the specified referenced file. The reference must have been created with the Using
          Namespacesoption, and must be loaded. Non-referenced nodes contained in the existing namespace will also be moved to the
          new namespace. The new namespace will be created by this command and can not already exist. The old namespace will be
          removed.
      - renamingPrefix:
          The string to use as a prefix for all objects from this file. This flag has been replaced by -ns/namespace.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def sysFile(*args, **kwargs):
    """
    This command provides a system independent way to create a directory or to rename or delete a file.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``copy`` / ``cp``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Copy the file to the name given by the newFileName paramter.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``delete`` / ``delete``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Deletes the file.                                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``makeDir`` / ``md``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Create the directory path given in the parameter. This will create the entire path if more than one directory needs to be created.                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``move`` / ``mov``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Behaves identically to the -rename flag and remains for compatibility with old scripts                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeEmptyDir`` / ``red``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Delete the directory path given in the parameter if the directory is empty. The command will not delete a directory which is not empty.                   Flag can|
    |  | have multiple arguments, passed either as a tuple or a list.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rename`` / ``ren``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Rename the file to the name given by the newFileName parameter.                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.sysFile`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Create a new directory path
        pm.sysFile( 'C:/temp/mayaStuff', makeDir=True )# Windows
        # Result: False #
        pm.sysFile( '/tmp/mayaStuff', makeDir=True )# Unix
        # Result: True #
        
        # Move a scene to the new directory (we can rename it at the same time).
        pm.sysFile( 'C:/maya/projects/default/scenes/myScene.mb', rename='C:/temp/mayaStuff/myScene.mb.trash' )# Windows
        # Result: False #
        pm.sysFile( '/maya/projects/default/scenes/myScene.mb', rename='/tmp/mayaStuff/myScene.mb.trash' )# Unix
        # Result: False #
        
        
        # Rename the scene to "myScene.will.be.deleted"
        pm.sysFile( 'C:/temp/mayaStuff/myScene.mb.trash', rename='C:/temp/mayaStuff/myScene.will.be.deleted' )# Windows
        # Result: False #
        pm.sysFile( '/tmp/mayaStuff/myScene.mb.trash', rename='/tmp/mayaStuff/myScene.will.be.deleted' )# Unix
        # Result: False #
        
        # Copy a scene to the new directory
        destWindows = "C:/temp/mayaStuff/myScene.mb.trash"
        srcWindows = "C:/maya/projects/default/scenes/myScene.mb"
        pm.sysFile( srcWindows, copy=destWindows )# Windows
        # Result: False #
        
        destUnix = "/tmp/mayaStuff/myScene.mb.trash"
        srcUnix = "maya/projects/default/scenes/myScene.mb"
        pm.sysFile( srcUnix, copy=destUnix )# Unix
        # Result: False #
        
        # Delete the scene
        pm.sysFile( 'C:/temp/mayaStuff/myScene.will.be.deleted', delete=True )# Windows
        # Result: False #
        pm.sysFile( '/tmp/mayaStuff/myScene.will.be.deleted', delete=True )# Unix
        # Result: False #
    """

    pass


def exportAnimFromReference(exportPath, **kwargs):
    """
    Export the main scene animation nodes and animation helper nodes from all referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the specified reference file. See -ean/exportAnim flag description for details on usage of animation files.                    
    
    Flags:
      - force:
          Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
          remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
          root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
          prompting a dialog that warns user about the lost of edits.
      - referenceNode:
          This flag is only used during queries. In MEL, if it appears before -query then it must be followed by the name of one
          of the scene's reference nodes. That will determine the reference to be queried by whatever flags appear after -query.
          If the named reference node does not exist within the scene the command will fail with an error. In Python the
          equivalent behavior is obtained by passing the name of the reference node as the flag's value. In MEL, if this flag
          appears after -query then it takes no argument and will cause the command to return the name of the reference node
          associated with the file given as the command's argument. If the file is not a reference or for some reason does not
          have a reference node (e.g. the user deleted it) then an empty string will be returned. If the file is not part of the
          current scene then the command will fail with an error. In Python the equivalent behavior is obtained by passing True as
          the flag's value.       In query mode, this flag can accept a value.
      - type:
          Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
          audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
          file types that match this file.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def launch(*args, **kwargs):
    """
    Launch the appropriate application to open the document, web page or directory specified.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``directory`` / ``dir``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A directory.                      Flag can have multiple arguments, passed either as a tuple or a list.                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``movie`` / ``mov``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A movie file. The only acceptable movie file formats are MPEG, Quicktime, and Windows Media file. The file's name must end with .mpg, .mpeg, .mp4, .wmv, .mov, or |
    |  | .qt.                                                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pdfFile`` / ``pdf``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A PDF (Portable Document Format) document. The file's name must end with .pdf.                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``webPage`` / ``web``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A web page.                                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.launch`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #launch a web browser to open webpage http://www.autodesk.com
        pm.launch(web="http://www.autodesk.com")
        # Result: u'http://www.autodesk.com' #
    """

    pass


def fcheck(*args, **kwargs):
    """
    Invokes the fcheck program to display images in a separate window.
    
    
    Derived from mel command `maya.cmds.fcheck`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # View the image "myImage.iff"
        #
        pm.fcheck( 'myImage.iff' )
        # Result: u'' #
        # You can also display several images at once using filenames with
        # wildcards (each in a separate window)
        #
        pm.fcheck( 'myTest*' )
        # Result: u'' #
        # You can display an animation using a trailing dot (.) on the
        # filename.
        #
        pm.fcheck( 'mySequence.' )
        # Result: u'' #
    """

    pass


def memory(*args, **kwargs):
    """
    Used to query essential statistics on memory availability and usage. By default memory sizes are returned in bytes.
    Since Maya's command engine only supports 32-bit signed integers, any returned value which cannot fit into 31 bits will
    be truncated to 2,147,483,647 and a warning message displayed. To avoid having memory sizes truncated use one of the
    memory size flags to return the value in larger units (e.g. megabytes) or use the asFloat flag to return the value as a
    float.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``asFloat`` / ``af``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Causes numeric values to be returned as floats rather than ints. This can be useful if you wish to retain some of the significant digits lost when using the unit |
    |  | size flags.                                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``debug`` / ``dbg``                                                                                  | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``freeMemory`` / ``fr``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns size of free memory                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``gigaByte`` / ``gb``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return memory sizes in gigabytes (1024\*1024\*1024 bytes)                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``heapMemory`` / ``he``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns size of memory heap                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``kiloByte`` / ``kb``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return memory sizes in kilobytes (1024 bytes)                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``megaByte`` / ``mb``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return memory sizes in megabytes (1024\*1024 bytes)                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pageFaults`` / ``pf``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns number of page faults                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pageReclaims`` / ``pr``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns number of page reclaims                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``physicalMemory`` / ``phy``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns size of physical memory                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``summary`` / ``sum``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a summary of memory usage. The size flags are ignored and all memory sizes are given in megabytes.                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``swapFree`` / ``swf``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns size of free swap                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``swapLogical`` / ``swl``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns size of logical swap                      Flag can have multiple arguments, passed either as a tuple or a list.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``swapMax`` / ``swm``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns maximum swap size                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``swapPhysical`` / ``swp``                                                                           | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns size of physical swap                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``swapReserved`` / ``swr``                                                                           | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``swapVirtual`` / ``swv``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns size of virtual swap                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``swaps`` / ``sw``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns number of swaps                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.memory`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.memory(freeMemory=True)
        # Result: 0 #
        
        pm.memory(freeMemory=True megaByte=True)
        521
        
        pm.memory(freeMemory=True megaByte=True asFloat=True)
        521.33203125
    """

    pass


def pluginInfo(*args, **kwargs):
    """
    This command provides access to the plug-in registry of the application. It is used mainly to query the characteristics
    of registered plug-ins. Plugins automatically become registered the first time that they are loaded. The argument is
    either the internal name of the plug-in or the path to access it.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``activeFile`` / ``af``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Restricts the command to the active file only, not the entire scene. This only affects the -dependNode/-dn and -pluginsInUse/-pu flags. For use during export     |
    |  | selected.                                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``animCurveInterp`` / ``aci``                                                                        | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the animation curve interpolators registered by this plug-in.                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``apiVersion`` / ``av``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string containing the version of the API that this plug-in was compiled with.  See the comments in MTypes.h for the details on how to interpret this    |
    |  | value.                                                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``autoload`` / ``a``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets whether or not this plug-in should be loaded every time the application starts up. Returns a boolean in query mode.                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cacheFormat`` / ``cf``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the registered geometry cache formats                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``changedCommand`` / ``cc``                                                                          | *script*                      | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Adds a callback that will get executed every time the plug-in registry changes. Any other previously registered callbacks will also get called.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``command`` / ``c``                                                                                  | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the normal commands registered by this plug-in. Constraint, control, context and model editor commands are  |
    |  | not included.                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``constraintCommand`` / ``cnc``                                                                      | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the constraint commands registered by this plug-in.                         Flag can have multiple          |
    |  | arguments, passed either as a tuple or a list.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``controlCommand`` / ``ctc``                                                                         | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the control commands registered by this plug-in.                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``data`` / ``d``                                                                                     | *unicode, unicode*            | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the data types registered by this plug-in.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dependNode`` / ``dn``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the custom nodes types registered by this plug-in.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dependNodeByType`` / ``dnt``                                                                       | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array of all registered node types within a specified class of nodes.  Each custom node type registered by a plug-in belongs to a more general   |
    |  | class of node types as specified by its MPxNode::Type. The flag's argument is an MPxNode::Type as a string.  For example, if you want to list all registered      |
    |  | Locator nodes, you should specify kLocatorNode as a argument to this flag.                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dependNodeId`` / ``dni``                                                                           | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns an integer array containing the ids of all of the custom node types registered by this plug-in.                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``device`` / ``dv``                                                                                  | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the devices registered by this plug-in.                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dragAndDropBehavior`` / ``ddb``                                                                    | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the drag and drop behaviors registered by this plug-in.                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``iksolver`` / ``ik``                                                                                | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the ik solvers registered by this plug-in.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listPlugins`` / ``ls``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing all the plug-ins that are currently loaded.                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listPluginsPath`` / ``lsp``                                                                        | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``loadPluginPrefs`` / ``lpp``                                                                        | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Loads the plug-in preferences (ie. autoload) from pluginPrefs.mel into Maya.                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``loaded`` / ``l``                                                                                   | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a boolean specifying whether or not the plug-in is loaded.                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``modelEditorCommand`` / ``mec``                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the model editor commands registered by this plug-in.                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string containing the internal name by which the plug-in is registered.                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``path`` / ``p``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string containing the absolute path name to the plug-in.                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pluginsInUse`` / ``pu``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing all the plug-ins that are currently being used in the scene.                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``registered`` / ``r``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a boolean specifying whether or not plug-in is currently registered with the system.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``remove`` / ``rm``                                                                                  | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Removes the given plug-in's record from the registry. There is no return value.                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``renderer`` / ``rdr``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the renderers registered by this plug-in.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``savePluginPrefs`` / ``spp``                                                                        | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Saves the plug-in preferences (ie. autoload) out to pluginPrefs.mel                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``serviceDescriptions`` / ``sd``                                                                     | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If there are services in use, then this flag will return a string array containing short descriptions saying what those services are.                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``settings`` / ``set``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns an array of values with the loaded, autoload, registered flags                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``tool`` / ``t``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the tool contexts registered by this plug-in.                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``translator`` / ``tr``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string array containing the names of all of the file translators registered by this plug-in.                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unloadOk`` / ``uo``                                                                                | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a boolean that specifies whether or not the plug-in can be safely unloaded.  It will return false if the plug-in is currently in use.  For example, if the|
    |  | plug-in adds a new dependency node type, and an instance of that node type is present in the scene, then this query will return false.                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``userNamed`` / ``u``                                                                                | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a boolean specifying whether or not the plug-in has been assigned a name by the user.                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``vendor`` / ``vd``                                                                                  | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string containing the vendor of the plug-in.                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``version`` / ``v``                                                                                  | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a string containing the version the plug-in.                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``writeRequires`` / ``wr``                                                                           | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets whether or not this plug-in should write requirescommand into the saved file. requirescommand could autoload the plug-in when you open or import that saved  |
    |  | file. This way, Maya will load the plug-in when a file is being loaded for some specified reason, such as to create a customized UI or to load some plug-in data  |
    |  | that is not saved in any node or attributes. For example, stereoCamerais using this flag for its customized UI.                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.pluginInfo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # List the plugins that are currently loaded
        pm.pluginInfo( query=True, listPlugins=True )
        # Result: [u'OpenEXRLoader', u'DirectConnect', u'AbcImport', u'mayaHIK', u'Mayatomr', u'ikSpringSolver', u'tiffFloatReader', u'AbcExport', u'VectorRender', u'ArubaTessellator', u'quatNodes', u'mayaCharacterization', u'gpuCache', u'rotateHelper', u'Substance', u'MayaMuscle', u'OneClick', u'AutodeskPacketFile', u'retargeterNodes', u'fbxmaya', u'matrixNodes', u'stereoCamera', u'sceneAssembly', u'ik2Bsolver'] #
        
        # Find the vendor of a plugin
        pm.pluginInfo( 'newNode.py', query=True, vendor=True )
        
        # Find the commands provided by a given plug-in
        pm.pluginInfo( 'helloCmd.py', query=True, command=True )
        
        # Turn on autoloading for a plug-in
        pm.pluginInfo( 'newNode.py', edit=True, autoload=True )
        
        # Return all custom locators registered by plug-ins.
        pm.pluginInfo( query=True, dependNodeByType="kLocatorNode" )
    """

    pass


def hitTest(*args, **kwargs):
    """
    The hitTestcommand hit-tests a point in the named control and returns a list of items underneath the point. The point is
    specified in pixels with the origin (0,0) at the top-left corner. This position is compatible with the coordinates
    provided by a drop-callback. The types of items that may be returned depends upon the specific control; not all controls
    currently support hit-testing.
    
    
    Derived from mel command `maya.cmds.hitTest`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #    Let's say that you have the name of a model editor that was
        #    created elsewhere.
        #
        editor = "MyModelEditor"
        #    Here's your drop callback:
        #
        def myModelEditorDropCallback( dragControl,
                                                                   dropControl,
                                                                   msgs,
                                                                   x,
                                                                   y,
                                                                   type ):
                #       Inside the callback we can hit-test the (x,y) drop-point
                #       against the control. This will return a list of DAG objects
                #       underneath the drop-point.
                #
                objects = pm.hitTest( dropControl, x, y )
                if len( objects ):
                        #       The hit-test returned something. You can now do something
                        #       with these objects.
                        pass
        #
        #       Attach a drop callback to this model editor.
        #
        try:
                control = pm.editor( editor ,query=True, control=True )
                if pm.control( control, exists=True ):
                        pm.control( control, edit=True, dropCallback=myModelEditorDropCallback )
        except RuntimeError:
                pass
    """

    pass


def dgtimer(*args, **kwargs):
    """
    This command measures dependency graph node performance by managing timers on a per-node basis. Logically, each DG node
    has a timer associated with it which records the amount of real time spent in various operations on its plugs. The time
    measurement includes the cost of copying data to the node on behalf of the operation, MEL commands executed by an
    expression contained in an expression invoked by the node, and includes any wait time such as when a fileTexture node
    loads an image file from disk. Most DG operations are reported including compute, draw, and dirty propagation. The
    various operations we measure are called metricsand the types of timers are called timer types. The various metrics are
    always measured when timing is on, but are only queried when specified via the -show and -hide flags. The metrics
    currently supported are listed in detail under the -show flag below. For each metric we support a standard set of timer
    types. There are three of these: selffor self time (the time specific to the node and not its children), inclusive(time
    including children of the node), and count(number of operations of the given metric on the node). The timing mechanism
    which is used by dgtimeris built into the DG itself, thus ALL depend nodes can be timed and there is no need for
    programmers writing plug-ins using the OpenMaya API to add any special code in order for their nodes to be timed -- its
    all handled transparently. The dgtimercommand allows node timers to be turned on, off, reset to zero, and have their
    current value displayed, and these operations can be performed globally on all nodes or on a specific set of nodes
    defined by name, type or parentage. Note that all timer measurements are computed in real time(the same time measurement
    you get from a wristwatch) as opposed to CPU time(which only measures time when the processor is executing your code).
    All times are displayed in seconds. Use the -query flag to display the current timer values on a node, use -on to turn
    on timing, use -off to turn off timing, and -reset to reset timers to zero. To display the values measured during
    timing, there are two approaches. The first method is to use the -query flag can be used to report the information which
    has been measured. The second method is to use the query methods available on the OpenMaya class MFnDependencyNode (see
    the OpenMaya documentation for details). What follows is a description of what is generated via -query. The output is
    broken out into several sections and these are described as follows: SECTION 1:Section 1 of the dgtimer output contains
    global information. This section can be disabled via the -hoHeader flag. These values are reset whenever a global timer
    reset occurs (i.e. dgtimer -reset;is specified). The global values which are reported are: Total real time:the total
    wall-clock time since the last global timer reset. This is the actual time which has been spent as you might measure it
    measure it with your watch. On a multi-processing system, this value will always remain true to to real time (unlike
    userand systime).Total user time:the total time the CPU(s) spent processing Maya not including any system time since the
    last global timer reset.Total sys time:the total time the CPU(s) spent in operating system calls on behalf of Maya since
    the last global timer reset. Summary of each metric for all nodes:a summary of self and count for each metric that we
    measure:Real time in callbacksreports the self time and count for the callbackmetric.Real time in computereports the
    self time and count for the computemetric.Real time in dirty propagationreports the self time and count for the
    dirtymetric.Real time in drawingreports the self time and count for the drawmetric.Real time fetching data from
    plugsreports the self time and count for the fetchmetric.Breakdown of select metrics in greater detail:a reporting of
    certain combinations of metrics that we measure:Real time in compute invoked from callbackreports the self time spent in
    compute when invoked either directly or indirectly by a callback.Real time in compute not invoked from callbackreports
    the self time spent in compute not invoked either directly or indirectly by a callback.SECTION 2:Section 2 of the
    dgtimer -query output contains per-node information. There is a header which describes the meaning of each column,
    followed by the actual per-node data, and this is ultimately followed by a footer which summarises the totals per
    column. Note that the data contained in the footer is the global total for each metric and will include any nodes that
    have been deleted since the last reset, so the value in the footer MAY exceed what you get when you total the individual
    values in the column. To prevent the header and footer from appearing, use the -noHeader flag to just display the per-
    node data. The columns which are displayed are as follows: Rank:The order of this node in the sorted list of all nodes,
    where the list is sorted by -sortMetric and -sortType flag values (if these are omitted the default is to sort by self
    compute time).ON:Tells you if the timer for that node is currently on or off. (With dgtimer, you have the ability to
    turn timing on and off on a per-node basis).Per-metric information:various columns are reported for each metric. The
    name of the metric is reported at in the header in capital letters (e.g. DRAW). The standard columns for each metric
    are:Self:The amount of real time (i.e. elapsed time as you might measure it with a stopwatch) spent performing the
    operation (thus if the metric is DRAW, then this will be time spent drawing the node).Inclusive:The amount of real time
    (i.e. elapsed time as you might measure it with a stopwatch) spent performing the operation including any child
    operations that were invoked on behalf of the operation (thus if the metric is DRAW, then this will be the total time
    taken to draw the node including any child operations).Count:The number of operations that occued on this node (thus if
    the metric is DRAW, then the number of draw operations on the node will be reported).Sort informationif a column is the
    one being used to sort all the per-node dgtimer information, then that column is followed by a Percentand
    Cumulativecolumn which describe a running total through the listing. Note that -sortType noneprevents these two columns
    from appearing and implicitely sorts on selftime.After the per-metric columns, the node name and type are
    reported:TypeThe node type.NameThe name of the node. If the node is file referenced and you are using namespaces, the
    namespace will be included. You can also force the dagpath to be displayed by specifying the -uniqueName flag.Plug-in
    nameIf the node was implemented in an OpenMaya plug-in, the name of that plug-in is reported.SECTION 3:Section 3 of the
    dgtimer -query output describes time spent in callbacks. Note that section 3 only appears when the CALLBACK metric is
    shown (see the -show flag). The first part is SECTION 3.1 lists the time per callback with each entry comprising: The
    name of the callback, such as attributeChangedMsg. These names are internal Maya names, and in the cases where the
    callback is available through the OpenMaya API, the API access to the callback is similarly named.The name is followed
    by a breakdown per callbackId. The callbackId is an identifying number which is unique to each client that is registered
    to a callback and can be deduced by the user, such as through the OpenMaya API. You can cross-reference by finding the
    same callbackId value listed in SECTIONs 3.1 and 3.3.Self time (i.e. real time spent within that callbackId type not
    including any child operations which occur while processing the callback).Percent (see the -sortType flag). Note that
    the percent values are listed to sum up to 100% for that callback. This is not a global percent.Cumulative (see the
    -sortType flag).Inclusive time (i.e. real time spent within that callbackId including any child operations).Count
    (number of times the callbackId was invoked).API lists Yif the callbackId was defined through the OpenMaya API, and Nif
    the callbackId was defined internally within Maya.Node lists the name of the node this callbackId was associated with.
    If the callbackId was associated with more than one node, the string \*multiple\*is printed. If there was no node
    associated with the callbackId (or its a callback type in which the node is hard to deduce), the entry is blank.After
    the callbackId entries are listed, a dashed line is printed followed by a single line listing the self, inclusive and
    count values for the callback. Note that the percent is relative to the global callback time.At the bottom of SECTION
    3.1 is the per-column total. The values printed match the summation at the bottom of the listing in section 2. Note that
    the values from SECTION 3.1 include any nodes that have been deleted since the last reset. The thresholding parameters
    (-threshold, -rangeLower, -rangeUpper and -maxDisplay) are honoured when generating the listing. The sorting of the rows
    and display of the Percent and Cumulative columns obeys the -sortType flag. As the listing can be long, zero entries are
    not displayed. The second part is SECTION 3.2 which lists the data per callbackId. As noted earlier, the callbackId is
    an identifying number which is unique to each client that is registered to a callback and can be deduced by the user,
    such as through the OpenMaya API. The entries in SECTION 3.2 appear as follows: CallbackId the numeric identifier for
    the callback. You can cross reference by finding the same callbackId value listed in SECTIONs 3.1 and 3.3.For each
    callbackId, the data is broken down per-callback:Callback the name of the callback, e.g. attributeChangedMsg.Percent,
    Cumulative, Inclusive, Count, API and Node entries as described in SECTION 3.1.After the callback entries are listed for
    the callbackId, a dashed followed by a summary line is printed. The summary line lists the self, inclusive and count
    values for the callback. Note that the percent is relative to the global callback time.The third part is SECTION 3.3
    which lists data per-callback per-node. The nodes are sorted based on the -sortType flag, and for each node, the
    callbacks are listed, also sorted based on the -sortType flag. As this listing can be long, zero entries are not
    displayed. An important note for SECTION 3.3 is that only nodes which still exist are displayed. If a node has been
    deleted, no infromation is listed.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``combineType`` / ``ct``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Causes all nodes of the same type (e.g. animCurveTA) to be combined in the output display.                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``hide`` / ``hi``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is the converse of -show. As with -show, it is a query-only flag which can be specified multiple times. If you do specify -hide, we display all columns |
    |  | except those listed by the -hide flags.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``hierarchy`` / ``h``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used to specify that a hierarchy of the dependency graph be affected, thus -reset -hierarchy -name ballwill reset the timers on the node named balland all of its |
    |  | descendents in the dependency graph.                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDisplay`` / ``m``                                                                               | *int*                         | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Truncates the display so that only the most expenive nentries are printed in the output display.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in conjunction with -reset or -query to specify the name of the node to reset or print timer values for. When querying a single timer, only a single line of |
    |  | output is generated (i.e. the global timers and header information is omitted). Note that one can force output to the script editor window via the -outputFile    |
    |  | MELoption to make it easy to grab the values in a MEL script. Note: the -name and -type flag cannot be used together.                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``noHeader`` / ``nh``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in conjunction with -query to prevent any header or footer information from being printed. All that will be output is the per-node timing data. This option  |
    |  | makes it easier to parse the output such as when you output the query to a file on disk using the -outputFileoption.                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``outputFile`` / ``o``                                                                               | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies where the output of timing or tracing is displayed. The flag takes a string argument which accepts three possible values: The name of a file on disk.Or |
    |  | the keyword stdout, which causes output to be displayed on the terminal window (Linux and Macintosh), and the status window on Windows.Or the keyword MEL, which  |
    |  | causes output to be displayed in the Maya Script Editor (only supported with -query).The stdoutsetting is the default behaviour. This flag can be used with the   |
    |  | -query flag as well as the -trace flag. When used with the -trace flag, any tracing output will be displayed on the destination specified by the -outputFile (or  |
    |  | stdout if -outputFile is omitted). Tracing operations will continue to output to the destination until you specify the -trace and -outputFile flags again. When   |
    |  | used with the -query flag, timing output will be displayed to the destination specified by the -outputFile (or stdoutif -outputFile is omitted). Here are some    |
    |  | examples of how to use the -query, -trace and -outputFile flags: Example: output the timing information to a single file on disk:dgtimer -on;                     |
    |  | // Turn on timing create some animated scene content; play -wait;                                        // Play the scene through dgtimer -query -outputFile     |
    |  | /tmp/timing.txt// Output node timing information to a file on disk Example: output the tracing information to a single file on disk:dgtimer -on;                  |
    |  | // Turn on timing create some animated scene content; dgtimer -trace on -outputFile /tmp/trace.txt// Turn on tracing and output the results to file play -wait;   |
    |  | // Play the scene through; trace info goes to /tmp/trace.txt dgtimer -query;                                    // But the timing info goes to the terminal window|
    |  | play -wait;                                        // Play the scene again, trace info still goes to /tmp/trace.txt Example: two runs, outputting the trace       |
    |  | information and timing information to separate files:dgtimer -on;                                       // Turn on timing create some animated scene content;     |
    |  | dgtimer -trace on -outputFile /tmp/trace1.txt// Turn on tracing and output the results to file play -wait;                                        // Play the     |
    |  | scene through dgtimer -query -outputFile /tmp/query1.txt// Output node timing information to another file dgtimer -reset; dgtimer -trace on -outputFile           |
    |  | /tmp/trace2.txt// Output tracing results to different file play -wait;                                        // Play the scene through dgtimer -query -outputFile|
    |  | /tmp/query2.txt// Output node timing information to another file Tips and tricks:Outputting the timing results to the script editor makes it easy to use the      |
    |  | results in MEL e.g. string $timing[] = `dgtimer -query -outputFile MEL`.It is important to note that the -outputFile you specify with -trace is totally           |
    |  | independent from the one you specify with -query.If the file you specify already exists, Maya will empty the file first before outputting data to it (and if the  |
    |  | file is not writable, an error is generated instead).                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``overhead`` / ``oh``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns on and off the measurement of timing overhead. Under ordinary circumstances the amount of timing overhead is minimal compared with the events being         |
    |  | measured, but in complex scenes, one might find the overhead to be measurable. By default this option is turned off. To enable it, specify dgtimer -overhead      |
    |  | trueprior to starting timing. When querying timing, the overhead is reported in SECTION 1.2 of the dgtimer output and is not factored out of each individual      |
    |  | operation.                                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rangeLower`` / ``rgl``                                                                             | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag can be specified to limit the range of nodes which are displayed in a query, or the limits of the heat map with -updateHeatMap. The value is the lower  |
    |  | percentage cutoff for the nodes which are processed. There is also a -rangeLower flag which sets the lower range limit. The default value is 0, meaning that all  |
    |  | nodes with timing value below the upper range limit are considered.                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rangeUpper`` / ``rgu``                                                                             | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag can be specified to limit the range of nodes which are displayed in a query, or the limits of the heat map with -updateHeatMap. The value is the upper  |
    |  | percentage cutoff for the nodes which are processed. There is also a -rangeLower flag which sets the lower range limit. The default value is 100, meaning that all|
    |  | nodes with timing value above the lower range limit are considered.                                           Flag can have multiple arguments, passed either as a|
    |  | tuple or a list.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``reset`` / ``r``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Resets the node timers to zero. By default, the timers on all nodes as well as the global timers are reset, but if specified with the -name or -type flags, only  |
    |  | the timers on specified nodes are reset.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``returnCode`` / ``rc``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag has been replaced by the more general -returnType flag. The -returnCode flag was unfortunately specific to the compute metric only. It exists only for  |
    |  | backwards compatability purposes. It will be removed altogether in a future release. Here are some handy equivalences: To get the total number of nodes:OLD WAY:  |
    |  | dgtimer -rc nodecount -q;// Result:325//NEW WAY: dgtimer -returnType total -sortType none -q;// Result:325//OLD WAY: dgtimer -rc count -q;// Result:1270//To get  |
    |  | the sum of the compute count column:NEW WAY: dgtimer -returnType total -sortMetric compute -sortType count -q;// Result:1270//OLD WAY: dgtimer -rc selftime -q;// |
    |  | Result:0.112898//To get the sum of the compute self column:NEW WAY: dgtimer -returnType total -sortMetric compute -sortType self -q;// Result:0.112898//          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``returnType`` / ``rt``                                                                              | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies what the double value returned by the dgtimer command represents. By default, the value returned is the global total as displayed in SECTION 1|
    |  | for the column we are sorting on in the per-node output (the sort column can be specified via the -sortMetric and -sortType flags). However, instead of the total |
    |  | being returned, the user can instead request the individual entries for the column. This flag is useful mainly for querying without forcing any output. The flag  |
    |  | accepts the values total, to just display the column total, or allto display all entries individually. For example, if you want to get the total of draw self time|
    |  | without any other output simply specify the following: dgtimer -returnType total -sortMetric draw -sortType self -threshold 100 -noHeader -query;// Result:       |
    |  | 7718.01 // To instead get each individual entry, change the above query to: dgtimer -returnType all -sortMetric draw -sortType self -threshold 100 -noHeader      |
    |  | -query;// Result: 6576.01 21.91 11.17 1108.92 // To get the inclusive dirty time for a specific node, use -name as well as -returnType all: dgtimer -name         |
    |  | virginia-returnType all -sortMetric dirty -sortType inclusive -threshold 100 -noHeader -query;Note: to get the total number of nodes, use -sortType none          |
    |  | -returnType total.  To get the on/off status for each node, use -sortType none -returnType all.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``show`` / ``sh``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in conjunction with -query to specify which columns are to be displayed in the per-node section of the output. -show takes an argument, which can be all(to  |
    |  | display all columns), callback(to display the time spent during any callback processing on the node not due to evaluation), compute(to display the time spent in  |
    |  | the node's compute methods), dirty(to display time spent propagating dirtiness on behalf of the node), draw(to display time spent drawing the node), compcb(to    |
    |  | display time spent during callback processing on node due to compute), and compncb(to display time spent during callback processing on node NOT due to compute).  |
    |  | The -show flag can be used multiple times, but cannot be specified with -hide. By default, if neither -show, -hide, or -sort are given, the effective display mode|
    |  | is: dgtimer -show compute -query.                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``sortMetric`` / ``sm``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in conjunction with -query to specify which metric is to be sorted on when the per-node section of the output is generated, for example drawtime. Note that  |
    |  | the -sortType flag can also be specified to define which timer is sorted on: for example dgtimer -sortMetric draw -sortType count -querywill sort the output by   |
    |  | the number of times each node was drawn. Both -sortMetric and -sortType are optional and you can specify one without the other. The -sortMetric flag can only be  |
    |  | specified at most once. The flag takes the following arguments: callback(to sort on time spent during any callback processing on the node), compute(to sort on the|
    |  | time spent in the node's compute methods), dirty(to sort on the time spent propagating dirtiness on behalf of the node), draw(to sort on time spent drawing the   |
    |  | node), fetch(to sort on time spent copying data from the datablock), The default, if -sortMetric is omitted, is to sort on the first displayed column. Note that  |
    |  | the sortMetric is independent of which columns are displayed via -show and -hide. Sort on a hidden column is allowed. The column selected by -sortMetric and      |
    |  | -sortType specifies which total is returned by the dgtimer command on the MEL command line. This flag is also used with -updateHeatMap to specify which metric to |
    |  | build the heat map for.                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``sortType`` / ``st``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in conjunction with -query to specify which timer is to be sorted on when the per-node section of the output is generated, for example selftime. Note that   |
    |  | the -sortMetric flag can also be specified to define which metric is sorted on: for example dgtimer -sortMetric draw -sortType count -querywill sort the output by|
    |  | the number of times each node was drawn. Both -sortMetric and -sortType are optional and you can specify one without the other. The -sortType flag can be         |
    |  | specified at most once. The flag takes the following arguments: self(to sort on self time, which is the time specific to the node and not its children),          |
    |  | inclusive(to sort on the time including children of the node), count(to sort on the number of times the node was invoked). and none(to sort on self time, but do  |
    |  | not display the Percent and Cumulative columns in the per-node display, as well as cause the total number of nodes in Maya to be returned on the command line).   |
    |  | The default, if -sortType is omitted, is to sort on self time. The column selected by -sortMetric and -sortType specifies which total is returned by the dgtimer  |
    |  | command on the MEL command line. The global total as displayed in SECTION 1 of the listing is returned. The special case of -sortType nonecauses the number of    |
    |  | nodes in Maya to instead be returned. This flag is also used with -updateHeatMap to specify which metric to build the heat map for.                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``threshold`` / ``th``                                                                               | *float*                       | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Truncates the display once the value falls below the threshold value. The threshold applies to whatever timer is being used for sorting. For example, if our sort |
    |  | key is self compute time (i.e. -sortMetric is computeand -sortType is self) and the threshold parameter is 20.0, then only nodes with a compute self-time of 20.0 |
    |  | or higher will be displayed. (Note that -threshold uses absolute time. There are the similar -rangeUpper and -rangeLower parameters which specify a range using   |
    |  | percentage).                                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``timerOff`` / ``off``                                                                               | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns off node timing. By default, the timers on all nodes are turned off, but if specified with the -name or -type flags, only the timers on specified nodes are |
    |  | turned off. If the timers on all nodes become turned off, then global timing is also turned off as well.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``timerOn`` / ``on``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns on node timing. By default, the timers on all nodes are turned on, but if specified with the -name or -type flags, only the timers on specified nodes are   |
    |  | turned on. The global timers are also turned on by this command. Note that turning on timing does NOT reset the timers to zero. Use the -reset flag to reset the  |
    |  | timers. The idea for NOT resetting the timers is to allow the user to arbitrarily turn timing on and off and continue to add to the existing timer values.        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``trace`` / ``tr``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns on or off detailed execution tracing. By default, tracing is off. If enabled, each timeable operation is logged when it starts and again when it ends. This |
    |  | flag can be used in conjunction with -outputFile to specify where the output is generated to. The following example shows how the output is                       |
    |  | formatted:dgtimer:begin: compute 3 particleShape1Deformed particleShape1Deformed.lastPosition The above is an example of the output when -trace is true that marks|
    |  | the start of an operation. For specific details on each field: the dgtimer:begin:string is an identifying marker to flag that this is a begin operation record.   |
    |  | The second argument, computein our example, is the operation metric. You can view the output of each given metric via dgtimer -qby specifying the -show flag. The |
    |  | integer which follows (3 in this case) is the depth in the operation stack, and the third argument is the name of the node (particleShape1Deformed). The fourth   |
    |  | argument is specific to the metric. For compute, it gives the name of the plug being computed. For callback, its the internal Maya name of the callback. For      |
    |  | dirty, its the name of the plug that dirtiness is being propagated from.dgtimer:end: compute 3 particleShape1Deformed 0.000305685 0.000305685 The above is the end|
    |  | operation record. The compute, 3and particleShapeDeformedarguments were described in the dgtimer:beginoverview earlier. The two floating-point arguments are self |
    |  | time and inclusive time for the operation measured in seconds. The inclusive measure lists the total time since the matching dgtimer:begin:entry for this         |
    |  | operation, while the self measure lists the inclusive time minus any time consumed by child operations which may have occurred during execution of the current    |
    |  | operation. As noted elsewhere in this document, these two times are wall clock times, measuring elapsed time including any time in which Maya was idle or         |
    |  | performing system calls. Since dgtimer can measure some non-node qualities in Maya, such as global message callbacks, a -is displayed where the node name would   |
    |  | ordinarily be displayed. The -means not applicable.                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``t``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in conjunction with -reset or -query to specify the type of the node(s) (e.g. animCurveTA) to reset or print timer values for. When querying, use of the     |
    |  | -combineType flag will cause all nodes of the same type to be combined into one entry, and only one line of output is generated (i.e. the global timers and header|
    |  | information is omitted). Note: the -name and -type flag cannot be used together.                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``uniqueName`` / ``un``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used to specify that the DAG nodes listed in the output should be listed by their unique names.  The full DAG path to the object will be printed out instead of   |
    |  | just the node name.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``updateHeatMap`` / ``uhm``                                                                          | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Forces Maya's heat map to rebuild based on the specified parameters. The heat map is an internal dgtimer structure used in mapping intensity values to colourmap  |
    |  | entries during display by the HyperGraph Editor. There is one heat map shared by all editors that are using heat map display mode. Updating the heat map causes   |
    |  | the timer values on all nodes to be analysed to compose the distribution of entries in the heat map. The parameter is the integer number of divisions in the map  |
    |  | and should equal the number of available colours for displaying the heat map. This flag can be specified with the -rangeLower and -rangeUpper flags to limit the  |
    |  | range of displayable to lie between the percentile range. The dgtimer command returns the maximum timing value for all nodes in Maya for the specified metric and |
    |  | type. Note: when the display range includes 0, the special zeroth (exactly zero) slot in the heat map is avilable.                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dgtimer`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Turns on node timing and resets the timers.
        pm.dgtimer( on=True )
        # Turns off node timing. Note that this does not reset the
        # timers.
        pm.dgtimer( off=True )
        # Prints the current timer values to the default (stdout).
        pm.dgtimer( query=True )
        # Result: [0.0] #
        # To reset the timers:
        pm.dgtimer( reset=True )
        # Turn on node timing and reset the timer values to zero.
        # Then, playback the scene, turn off timing and dump to a file.
        # Turn on timing without resetting the timers, and repeat.
        pm.dgtimer( on=True, reset=True )
        pm.play( wait=True )
        pm.dgtimer( off=True )
        pm.dgtimer( outputFile='/home/virginia/timing/dgtrace_once.txt', query=True )
        pm.dgtimer( on=True )
        pm.play( wait=True )
        pm.dgtimer( off=True )
        pm.dgtimer( outputFile='/home/virginia/timing/dgtrace_twice.txt', query=True )
    """

    pass


def dgdirty(*args, **kwargs):
    """
    The dgdirtycommand is used to force a dependency graph dirty message on a node or plug.  Used for debugging to find
    evaluation problems.  If no nodes are specified then the current selection list is used. If the listflag is used it will
    return the list of things currently marked as dirty (or clean if the cleanflag was also used). The returned values will
    be the names of plugs either clean/dirty themselves, at both ends of a clean/dirty connection, or representing the
    location of clean/dirty data on the node. Be careful using this option in conjunction with the allflag, the list could
    be huge.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``allPlugs`` / ``a``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Ignore the selected or specified objects and dirty (or clean) all plugs.                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``clean`` / ``c``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this flag is set then the attributes are cleaned.  Otherwise they are set to dirty.                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``implicit`` / ``i``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this flag is set then allow the implicit or default nodes to be processed as well. Otherwise they will be skipped for efficiency.                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``list`` / ``l``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When this flag is specified then instead of sending out dirty/clean messages the list of currently dirty/clean objects will be returned. The allPlugsand          |
    |  | cleanflags are respected to narrow guide the values to be returned. The value of the flag tells what will be reported. dataor d= show plugs that have dirty/clean |
    |  | dataplugor p= show plugs that have dirty/clean statesconnectionor c= show plugs with connections that have dirty/clean statesQuery this flag to find all legal    |
    |  | values of the flag. Query this flag with its value already set to get a description of what that value means. Note that pand cmodes are restricted to plugs that  |
    |  | have connections or non-standard state information. Other attributes will not have state information to check, though they will have data. In the case of array   |
    |  | attributes only the children that have values currently set will be considered. No attempt will be made to evaluate them in order to update the available child   |
    |  | lists. e.g. if you have a DAG with transform T1 and shape S1 the instanced attribute S1.wm[0] will be reported. If in a script you create a second instance T2-S1 |
    |  | and immediately list the plugs again before evaluation you will still only see S1.wm[0]. The new S1.wm[1] won't be reported until it is created through an        |
    |  | evaluation, usually caused by refresh, a specific getAttr command, or an editor update. Note that the list is only for selected nodes. Unlike when dirty messages |
    |  | are sent this does not travel downstream.                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``propagation`` / ``p``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this flag is set then the ability of dirty messages to flow through the graph is left enabled.                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showTiming`` / ``st``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this flag is used then show how long the dirty messages took to propagate.                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``verbose`` / ``v``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Prints out all of the plugs being set dirty on stdout.                                    Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dgdirty`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Set everything in the entire scene dirty
        #
        pm.dgdirty(a=True);
        
        # Set all connected plugs dirty on "myNode"
        #
        pm.dgdirty( 'myNode' )
        # Result: 5
        # 5 plugs were set dirty
        
        #  Set all connected plugs dirty on "locator1"
        pm.dgdirty( 'locator1' )
        # Result: 0
        # 0 plugs were connected so no dirty message was sent
        
        # Set myNode.tx dirty
        pm.select( 'myNode.tx' )
        pm.dgdirty()
        # Result: 1
    """

    pass


def attachDeviceAttr(*args, **kwargs):
    """
    This command associates a device/axis pair with a node/attribute pair. When the device axis moves, the value of the
    attribute is set to the value of the axis. This value can be scaled and offset using the setAttrScale command. In query
    mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify the attribute to attach to                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``axis`` / ``ax``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify the axis to attach from.                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``camera`` / ``cam``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag attaches the device/axis to the current camera. The mapping between device axes and camera controls is uses a heuristic based on the device descripton. |
    |  | The interaction is a copy of the mouse camera navigation controls.                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cameraRotate`` / ``cr``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag attaches the device/axis to the current cameras rotation controls.                      Flag can have multiple arguments, passed either as a tuple or a |
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cameraTranslate`` / ``ct``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag attaches the device/axis to the current cameras translate controls.                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``clutch`` / ``c``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify a clutch button.  This button must be down for the command string to be executed. If no clutch is specified the command string is executed everytime the  |
    |  | device state changes                                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``device`` / ``d``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | specify which device to assign the command string.                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selection`` / ``sl``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag attaches to the nodes in the selection list. This is different from the default arguments of the command since changing the selection will change the   |
    |  | attachments.                                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.attachDeviceAttr`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.attachDeviceAttr( 'surface1.translateX', d='spaceball', ax='XAxis' )
        
        # This command will assign the XAxis of the spaceball to
        # the translateX attribute of surface1.  This
        # assignment is independent of the selection list (i.e.
        # if surface1 was selected when the command is executed,
        # surface1 will be translated by the spaceball regardless
        # of the current selection.)
        
        pm.attachDeviceAttr( d='spaceball', ax='XAxis', at='translateX' )
        
        # This command will assign the XAxis of the spaceball to
        # the translateX attribute of the selected objects.
        
        pm.attachDeviceAttr( d='wacom', ax='puck:X', c='puckButton1', at='translateX', sl=True )
        pm.attachDeviceAttr( d='wacom', ax='puck:Y', c='puckButton1', at='translateY', sl=True )
        
        # This command will attach the wacom puck X and Y axes to the
        # X and Y translate attributes of the selected items.
        # When the selection changes so does the attachment.
        # The -c option means you can only move the selected items
        # with the puck when button1 on the puck is down.
    """

    pass


def displayString(*args, **kwargs):
    """
    Assign a string value to a string identifier. Allows you define a string in one location and then refer to it by its
    identifier in many other locations. Formatted strings are also supported (NOTE however, this functionality is now
    provided in a more general fashion by the format command, use of format is recommended). You may embed up to 3 special
    character sequences ^1s, ^2s, and ^3s to perform automatic string replacement. The embedded characters will be replaced
    with the extra command arguments. See example section for more detail. Note the extra command arguments do not need to
    be display string identifiers.              In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``delete`` / ``d``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to remove an identifer string. The command will fail if the identifier does not exist.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exists`` / ``ex``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true or false depending upon whether the specified identifier exists.                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``keys`` / ``k``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List all displayString keys that match the identifier string. The identifier string may be a whole or partial key string. The command will return a list of all   |
    |  | identifier keys that contain this identifier string as a substring.                                       Flag can have multiple arguments, passed either as a    |
    |  | tuple or a list.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``replace`` / ``r``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Since a displayString command will fail if it tries to assign a new value to an existing identifer, this flag is required to allow updates to the value of an     |
    |  | already-existing identifier.  If the identifier does not already exist, a new identifier is added as if the -replace flag were not present.                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``value`` / ``v``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The display string\'s value. If you do not specify this flag when creating a display string then the value will be the same as the identifier.                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.displayString`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #    Associate a string with an identifier.
        #
        pm.displayString( 'kExampleHelloWorld', value='Hello world' )
        #    Query string associated with an identifer.
        #
        pm.displayString( 'kExampleHelloWorld', query=True, value=True )
        #    Define a simple formatted string to append ellipses.
        #
        pm.displayString( 'kExampleEllipsesFormat', value='^1s...' )
        pm.displayString( 'kExampleEllipsesFormat', 'kExampleHelloWorld', query=True, value=True )
        #    Define a formatted string using all the available
        #    embedded characters.
        #
        pm.displayString( 'kExampleAnotherFormat', value='These ^1s are ^2s me ^3s' )
        pm.displayString( 'kExamplePretzels', value='pretzels' )
        pm.displayString( 'kExampleAnotherFormat', 'kExamplePretzels', 'making', 'thirsty', query=True, value=True )
        # Obtain a list of matching displayString keys.
        # In the first example  a list of  all keys containing the substring
        # "niceName".
        # In the second example a list of all keys in the string set
        # m_testStrings
        pm.displayString( 'niceName', query=True, keys=True )
        pm.displayString( 'm_testStrings.', query=True, keys=True )
        #    If you do not specify the -v/value flag on creating then
        #    the value will be the same as the identifier.
        #
        pm.displayString( 'kExampleMissingValue' )
        pm.displayString( 'kExampleMissingValue', query=True, value=True )
    """

    pass


def displayWarning(*args, **kwargs):
    pass


def setAttrMapping(*args, **kwargs):
    """
    This command applies an offset and scale to a specified device attachment. This command is different than the
    setInputDeviceMapping command, which applies a mapping to a device axis. The value from the device is multiplied by the
    scale and the offset is added to this product. With an absolute mapping, the attached attribute gets the resulting
    value. If the mapping is relative, the resulting value is added to the previous calculated value. The calculated value
    will also take into account the setInputDeviceMapping, if it was defined. As an example, if the space ball is setup with
    absolute attachment mappings, pressing in one direction will cause the attached attribute to get a constant value. If a
    relative mapping is used, and the spaceball is pressed in one direction, the attached attribute will get a constantly
    increasing (or constantly decreasing) value. Note that the definition of relative is different than the definition used
    by the setInputDeviceMapping command. In general, both a relative attachment mapping (this command) and a relative
    device mapping (setInputDeviceMapping) should not be used together one the same axis. In query mode, return type is
    based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``absolute`` / ``a``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Make the mapping absolute.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The attribute used in the attachment.                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``axis`` / ``ax``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The axis on the device used in the attachment.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``clutch`` / ``c``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The clutch button used in the attachment.                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``device`` / ``d``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The device used in the attachment.                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``offset`` / ``o``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify the offset value.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``relative`` / ``r``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Make the mapping relative.                        Flag can have multiple arguments, passed either as a tuple or a list.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scale`` / ``s``                                                                                    | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify the scale value.                                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selection`` / ``sl``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies the mapping should be on the selected objects                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.setAttrMapping`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.attachDeviceAttr( d='spaceball', ax='XAxis', at='translateX' )
        pm.setAttrMapping( d='spaceball', ax='XAxis', at='translateX', scale=0.01 )
        
        # The first command will assign the XAxis of the spaceball to
        # the translateX attribute of the selected objects.
        # The second command sets the scaling of attribute value to
        # 0.01 of the value of the axis. This results in finer control
        # since the motions of the spaceball are damped.
    """

    pass


def dgeval(*args, **kwargs):
    """
    The dgevalcommand is used to force a dependency graph evaluate of a node or plug.  Used for debugging to find
    propagation problems. Normally the selection list is used to determine which objects to evaluate, but you can add to the
    selection list by specifying which objects you want on the command line.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``src`` / ``src``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is obsolete. Do not use.                        Flag can have multiple arguments, passed either as a tuple or a list.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``verbose`` / ``v``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this flag is used then the results of the evaluation(s) is/are printed on stdout.                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dgeval`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Evaluate all (connected) plugs on "myNode"
        pm.dgeval( 'myNode' )
        # Result: 5
        # This means that 5 plugs were evaluated
        
        # Evaluate myNode.tx only
        pm.select( 'myNode.tx' )
        pm.dgeval()
        # Result: 1
    """

    pass


def allNodeTypes(*args, **kwargs):
    """
    This command returns a list containing the type names of every kind of creatable node registered with the system. Note
    that some node types are abstract and cannot be created. These will not show up on this list. (e.g. transform and
    polyShape both inherit from dagObject, but dagObject  cannot be created directly so it will not appear on this list.)
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``includeAbstract`` / ``ia``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Show every node type, even the abstract ones which cannot be created via the 'createNode' command. These will have the suffix (abstract)appended to them in the   |
    |  | list.                                     Flag can have multiple arguments, passed either as a tuple or a list.                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.allNodeTypes`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.allNodeTypes()
        # Result: [u'AISEnvFacade', u'AlembicNode', u'ComputeGlobal', u'ComputeLocal', u'CustomRigDefaultMappingNode', u'CustomRigRetargeterNode', u'HIKCharacterNode', u'HIKCharacterStateClient', u'HIKControlSetNode', u'HIKEffector2State', u'HIKEffectorFromCharacter', u'HIKFK2State', u'HIKPinning2State', u'HIKProperty2State', u'HIKRetargeterNode', u'HIKSK2State', u'HIKSkeletonGeneratorNode', u'HIKSolverNode', u'HIKState2Effector', u'HIKState2FK', u'HIKState2GlobalSK', u'HIKState2SK', u'abcimport', u'addDoubleLinear', u'addMatrix', u'adskMaterial', u'adskPrepareRenderGlobals', u'aimConstraint', u'airField', u'airManip', u'alignCurve', u'alignManip', u'alignSurface', u'ambientLight', u'angleBetween', u'angleDimension', u'animBlend', u'animBlendInOut', u'animBlendNodeAdditive', u'animBlendNodeAdditiveDA', u'animBlendNodeAdditiveDL', u'animBlendNodeAdditiveF', u'animBlendNodeAdditiveFA', u'animBlendNodeAdditiveFL', u'animBlendNodeAdditiveI16', u'animBlendNodeAdditiveI32', u'animBlendNodeAdditiveRotation', u'animBlendNodeAdditiveScale', u'animBlendNodeBoolean', u'animBlendNodeEnum', u'animBlendNodeTime', u'animClip', u'animCurveTA', u'animCurveTL', u'animCurveTT', u'animCurveTU', u'animCurveUA', u'animCurveUL', u'animCurveUT', u'animCurveUU', u'animLayer', u'anisotropic', u'annotationShape', u'apfEntityNode', u'apfFileNode', u'arcLengthDimension', u'areaLight', u'arrayMapper', u'arrowManip', u'artAttrPaintTest', u'assemblyDefinition', u'assemblyReference', u'attachCurve', u'attachSurface', u'attrHierarchyTest', u'audio', u'avgCurves', u'avgCurvesManip', u'avgNurbsSurfacePoints', u'avgSurfacePoints', u'axesActionManip', u'ballProjManip', u'barnDoorManip', u'baseLattice', u'bevel', u'bevelManip', u'bevelPlus', u'bezierCurve', u'bezierCurveToNurbs', u'blendColorSets', u'blendColors', u'blendDevice', u'blendManip', u'blendShape', u'blendTwoAttr', u'blendWeighted', u'blindDataTemplate', u'blinn', u'boneLattice', u'boolean', u'boundary', u'brownian', u'brush', u'builtin_bsdf_architectural', u'builtin_bsdf_architectural_comp', u'builtin_bsdf_ashikhmin', u'builtin_bsdf_carpaint', u'builtin_bsdf_lambert', u'builtin_bsdf_mirror', u'builtin_bsdf_phong', u'bulge', u'bump2d', u'bump3d', u'buttonManip', u'cMuscleCreator', u'cMuscleDebug', u'cMuscleDirection', u'cMuscleDisplace', u'cMuscleDisplay', u'cMuscleFalloff', u'cMuscleKeepOut', u'cMuscleMultiCollide', u'cMuscleObject', u'cMuscleRelative', u'cMuscleShader', u'cMuscleSmartCollide', u'cMuscleSmartConstraint', u'cMuscleSpline', u'cMuscleSplineDeformer', u'cMuscleStretch', u'cMuscleSurfAttach', u'cMuscleSystem', u'cacheBlend', u'cacheFile', u'camera', u'cameraManip', u'cameraPlaneManip', u'cameraSet', u'cameraView', u'centerManip', u'character', u'characterMap', u'characterOffset', u'checker', u'choice', u'chooser', u'circleManip', u'circleSweepManip', u'clamp', u'clipGhostShape', u'clipLibrary', u'clipScheduler', u'clipToGhostData', u'closeCurve', u'closeSurface', u'closestPointOnMesh', u'closestPointOnSurface', u'cloth', u'cloud', u'cluster', u'clusterFlexorShape', u'clusterHandle', u'coiManip', u'collisionModel', u'colorProfile', u'componentManip', u'composeMatrix', u'concentricProjManip', u'condition', u'container', u'containerBase', u'contour_composite', u'contour_contrast_function_levels', u'contour_contrast_function_simple', u'contour_only', u'contour_ps', u'contour_shader_combi', u'contour_shader_curvature', u'contour_shader_depthfade', u'contour_shader_factorcolor', u'contour_shader_framefade', u'contour_shader_layerthinner', u'contour_shader_maxcolor', u'contour_shader_silhouette', u'contour_shader_simple', u'contour_shader_widthfromcolor', u'contour_shader_widthfromlight', u'contour_shader_widthfromlightdir', u'contour_store_function', u'contour_store_function_simple', u'contrast', u'copyColorSet', u'copyUVSet', u'cpManip', u'crater', u'creaseSet', u'createBPManip', u'createCVManip', u'createColorSet', u'createEPManip', u'createUVSet', u'cubeManip', u'cubicProjManip', u'curveEdManip', u'curveFromMeshCoM', u'curveFromMeshEdge', u'curveFromSubdivEdge', u'curveFromSubdivFace', u'curveFromSurfaceBnd', u'curveFromSurfaceCoS', u'curveFromSurfaceIso', u'curveInfo', u'curveIntersect', u'curveNormalizerAngle', u'curveNormalizerLinear', u'curveSegmentManip', u'curveVarGroup', u'cylindricalLightLocator', u'cylindricalProjManip', u'dagContainer', u'dagPose', u'dataBlockTest', u'decomposeMatrix', u'defaultLightList', u'defaultRenderUtilityList', u'defaultRenderingList', u'defaultShaderList', u'defaultTextureList', u'deformBend', u'deformBendManip', u'deformFlare', u'deformFlareManip', u'deformSine', u'deformSineManip', u'deformSquash', u'deformSquashManip', u'deformTwist', u'deformTwistManip', u'deformWave', u'deformWaveManip', u'deleteColorSet', u'deleteComponent', u'deleteUVSet', u'detachCurve', u'detachSurface', u'dgs_material', u'dgs_material_photon', u'dielectric_material', u'dielectric_material_photon', u'directedDisc', u'directionManip', u'directionalLight', u'discLightLocator', u'discManip', u'diskCache', u'displacementShader', u'displayLayer', u'displayLayerManager', u'distanceBetween', u'distanceDimShape', u'distanceManip', u'dof', u'dofManip', u'doubleShadingSwitch', u'dpBirailSrf', u'dragField', u'dropoffLocator', u'dropoffManip', u'dynAttenuationManip', u'dynController', u'dynGlobals', u'dynHolder', u'dynSpreadManip', u'dynamicConstraint', u'editMetadata', u'emitterManip', u'enableManip', u'envBall', u'envChrome', u'envCube', u'envFacade', u'envFog', u'envSky', u'envSphere', u'environmentFog', u'eulerToQuat', u'explodeNurbsShell', u'expression', u'extendCurve', u'extendCurveDistanceManip', u'extendSurface', u'extendSurfaceDistanceManip', u'extrude', u'extrudeManip', u'facade', u'ffBlendSrf', u'ffBlendSrfObsolete', u'ffFilletSrf', u'ffd', u'fieldManip', u'fieldsManip', u'file', u'filletCurve', u'filterClosestSample', u'filterEuler', u'filterResample', u'filterSimplify', u'fitBspline', u'flexorShape', u'flow', u'fluidEmitter', u'fluidShape', u'fluidSliceManip', u'fluidTexture2D', u'fluidTexture3D', u'follicle', u'forceUpdateManip', u'fosterParent', u'fourByFourMatrix', u'fractal', u'frameCache', u'freePointManip', u'freePointTriadManip', u'gammaCorrect', u'geoConnectable', u'geoConnector', u'geometryConstraint', u'geometryFilter', u'geometryOnLineManip', u'geometryVarGroup', u'globalCacheControl', u'globalStitch', u'gpuCache', u'granite', u'gravityField', u'greasePencilSequence', u'greasePlane', u'greasePlaneRenderShape', u'grid', u'groupId', u'groupParts', u'guide', u'hairConstraint', u'hairSystem', u'hairTubeShader', u'hardenPoint', u'hardwareRenderGlobals', u'hardwareRenderingGlobals', u'heightField', u'hierarchyTestNode1', u'hierarchyTestNode2', u'hierarchyTestNode3', u'hikEffector', u'hikFKJoint', u'hikFloorContactMarker', u'hikGroundPlane', u'hikHandle', u'hikIKEffector', u'hikSolver', u'historySwitch', u'holdMatrix', u'hsvToRgb', u'hwReflectionMap', u'hwRenderGlobals', u'hyperGraphInfo', u'hyperLayout', u'hyperView', u'ik2Bsolver', u'ikEffector', u'ikHandle', u'ikMCsolver', u'ikPASolver', u'ikRPManip', u'ikRPsolver', u'ikSCsolver', u'ikSplineManip', u'ikSplineSolver', u'ikSpringSolver', u'ikSystem', u'imagePlane', u'implicitBox', u'implicitCone', u'implicitSphere', u'indexManip', u'insertKnotCurve', u'insertKnotSurface', u'instancer', u'intersectSurface', u'inverseMatrix', u'isoparmManip', u'jiggle', u'joint', u'jointCluster', u'jointClusterManip', u'jointFfd', u'jointLattice', u'jointTranslateManip', u'keyframeRegionManip', u'keyingGroup', u'lambert', u'lattice', u'layeredShader', u'layeredTexture', u'leastSquaresModifier', u'leather', u'lightFog', u'lightInfo', u'lightLinker', u'lightList', u'lightManip', u'limitManip', u'lineManip', u'lineModifier', u'locator', u'lodGroup', u'lodThresholds', u'loft', u'lookAt', u'luminance', u'makeGroup', u'makeIllustratorCurves', u'makeNurbCircle', u'makeNurbCone', u'makeNurbCube', u'makeNurbCylinder', u'makeNurbPlane', u'makeNurbSphere', u'makeNurbTorus', u'makeNurbsSquare', u'makeTextCurves', u'makeThreePointCircularArc', u'makeThreePointCircularArcManip', u'makeTwoPointCircularArc', u'makeTwoPointCircularArcManip', u'mandelbrot', u'mandelbrot3D', u'manip2DContainer', u'manipContainer', u'mapVizShape', u'marble', u'markerManip', u'materialFacade', u'materialInfo', u'membrane', u'mentalrayCCMeshProxy', u'mentalrayCurveApprox', u'mentalrayDisplaceApprox', u'mentalrayFramebuffer', u'mentalrayGlobals', u'mentalrayIblShape', u'mentalrayItemsList', u'mentalrayLightProfile', u'mentalrayOptions', u'mentalrayOutputPass', u'mentalrayPhenomenon', u'mentalrayRenderPass', u'mentalrayShader', u'mentalraySubdivApprox', u'mentalraySurfaceApprox', u'mentalrayTessellation', u'mentalrayText', u'mentalrayTexture', u'mentalrayUserBuffer', u'mentalrayUserData', u'mentalrayVertexColors', u'mesh', u'meshVarGroup', u'mi_bump_flakes', u'mi_car_paint_phen', u'mi_car_paint_phen_x', u'mi_car_paint_phen_x_passes', u'mi_metallic_paint', u'mi_metallic_paint_output_mixer', u'mi_metallic_paint_x', u'mi_metallic_paint_x_passes', u'mia_ciesky', u'mia_envblur', u'mia_exposure_photographic', u'mia_exposure_photographic_rev', u'mia_exposure_simple', u'mia_lens_bokeh', u'mia_light_surface', u'mia_material', u'mia_material_x', u'mia_material_x_passes', u'mia_photometric_light', u'mia_physicalsky', u'mia_physicalsun', u'mia_portal_light', u'mia_roundcorners', u'mib_amb_occlusion', u'mib_bent_normal_env', u'mib_blackbody', u'mib_bump_basis', u'mib_bump_map', u'mib_bump_map2', u'mib_cie_d', u'mib_color_alpha', u'mib_color_average', u'mib_color_intensity', u'mib_color_interpolate', u'mib_color_mix', u'mib_color_spread', u'mib_continue', u'mib_data_bool', u'mib_data_bool_array', u'mib_data_color', u'mib_data_color_array', u'mib_data_get_bool', u'mib_data_get_color', u'mib_data_get_int', u'mib_data_get_scalar', u'mib_data_get_shader', u'mib_data_get_shader_bool', u'mib_data_get_shader_color', u'mib_data_get_shader_int', u'mib_data_get_shader_scalar', u'mib_data_get_shader_vector', u'mib_data_get_string', u'mib_data_get_texture', u'mib_data_get_vector', u'mib_data_int', u'mib_data_int_array', u'mib_data_scalar', u'mib_data_scalar_array', u'mib_data_shader', u'mib_data_shader_array', u'mib_data_string', u'mib_data_string_array', u'mib_data_texture', u'mib_data_texture_array', u'mib_data_vector', u'mib_data_vector_array', u'mib_dielectric', u'mib_fast_occlusion', u'mib_fg_occlusion', u'mib_geo_add_uv_texsurf', u'mib_geo_cone', u'mib_geo_cube', u'mib_geo_cylinder', u'mib_geo_instance', u'mib_geo_instance_mlist', u'mib_geo_sphere', u'mib_geo_square', u'mib_geo_torus', u'mib_glossy_reflection', u'mib_glossy_refraction', u'mib_illum_blinn', u'mib_illum_cooktorr', u'mib_illum_hair', u'mib_illum_lambert', u'mib_illum_phong', u'mib_illum_ward', u'mib_illum_ward_deriv', u'mib_lens_clamp', u'mib_lens_stencil', u'mib_light_infinite', u'mib_light_photometric', u'mib_light_point', u'mib_light_spot', u'mib_lightmap_sample', u'mib_lightmap_write', u'mib_lookup_background', u'mib_lookup_cube1', u'mib_lookup_cube6', u'mib_lookup_cylindrical', u'mib_lookup_spherical', u'mib_map_get_color', u'mib_map_get_integer', u'mib_map_get_integer_array', u'mib_map_get_scalar', u'mib_map_get_scalar_array', u'mib_map_get_transform', u'mib_map_get_vector', u'mib_opacity', u'mib_passthrough_bump_map', u'mib_photon_basic', u'mib_ptex_lookup', u'mib_ray_marcher', u'mib_reflect', u'mib_refract', u'mib_refraction_index', u'mib_shadow_transparency', u'mib_texture_checkerboard', u'mib_texture_filter_lookup', u'mib_texture_lookup', u'mib_texture_lookup2', u'mib_texture_polkadot', u'mib_texture_polkasphere', u'mib_texture_remap', u'mib_texture_rotate', u'mib_texture_turbulence', u'mib_texture_vector', u'mib_texture_wave', u'mib_transparency', u'mib_twosided', u'mib_volume', u'mila_5layers', u'mila_5layers_phen', u'mila_adapter', u'mila_diffuse', u'mila_emission', u'mila_fastsss', u'mila_flakes_adapter', u'mila_get_normal', u'mila_layers', u'mila_material', u'mila_material_std', u'mila_reflection', u'mila_refraction', u'mila_translucency', u'mila_transparency', u'mip_binaryproxy', u'mip_cameramap', u'mip_card_opacity', u'mip_fgshooter', u'mip_gamma_gain', u'mip_grayball', u'mip_matteshadow', u'mip_matteshadow_mtl', u'mip_mirrorball', u'mip_motion_vector', u'mip_motionblur', u'mip_rayswitch', u'mip_rayswitch_advanced', u'mip_rayswitch_environment', u'mip_rayswitch_stage', u'mip_render_subset', u'misss_call_shader', u'misss_fast_lmap_maya', u'misss_fast_shader', u'misss_fast_shader2', u'misss_fast_shader2_x', u'misss_fast_shader_x', u'misss_fast_shader_x_passes', u'misss_fast_simple_maya', u'misss_fast_skin_maya', u'misss_fast_skin_phen', u'misss_fast_skin_phen_d', u'misss_lambert_gamma', u'misss_lightmap_phen', u'misss_lightmap_write', u'misss_mia_skin2_phen', u'misss_mia_skin2_phen_d', u'misss_mia_skin2_surface_phen', u'misss_physical', u'misss_physical_phen', u'misss_set_normal', u'misss_skin_specular', u'motionPath', u'motionPathManip', u'motionTrail', u'motionTrailShape', u'mountain', u'moveBezierHandleManip', u'moveVertexManip', u'movie', u'mpBirailSrf', u'multDoubleLinear', u'multMatrix', u'multilisterLight', u'multiplyDivide', u'mute', u'nCloth', u'nComponent', u'nParticle', u'nRigid', u'nearestPointOnCurve', u'network', u'newtonField', u'newtonManip', u'noise', u'nonLinear', u'normalConstraint', u'nucleus', u'nurbsCurve', u'nurbsCurveToBezier', u'nurbsSurface', u'nurbsTessellate', u'nurbsToSubdiv', u'nurbsToSubdivProc', u'objectAttrFilter', u'objectBinFilter', u'objectFilter', u'objectMultiFilter', u'objectNameFilter', u'objectRenderFilter', u'objectScriptFilter', u'objectSet', u'objectTypeFilter', u'ocean', u'oceanShader', u'offsetCos', u'offsetCosManip', u'offsetCurve', u'offsetCurveManip', u'offsetSurface', u'offsetSurfaceManip', u'oldBlindDataBase', u'oldGeometryConstraint', u'oldNormalConstraint', u'oldTangentConstraint', u'opticalFX', u'orientConstraint', u'orientationMarker', u'oversampling_lens', u'pairBlend', u'paramDimension', u'parentConstraint', u'parti_volume', u'parti_volume_photon', u'particle', u'particleAgeMapper', u'particleCloud', u'particleColorMapper', u'particleIncandMapper', u'particleSamplerInfo', u'particleTranspMapper', u'partition', u'passContributionMap', u'passMatrix', u'path_material', u'pfxHair', u'pfxToon', u'phong', u'phongE', u'physical_lens_dof', u'physical_light', u'pivot2dManip', u'pivotAndOrientManip', u'place2dTexture', u'place3dTexture', u'planarProjManip', u'planarTrimSurface', u'plusMinusAverage', u'pointConstraint', u'pointEmitter', u'pointLight', u'pointMatrixMult', u'pointOnCurveInfo', u'pointOnCurveManip', u'pointOnLineManip', u'pointOnPolyConstraint', u'pointOnSurfManip', u'pointOnSurfaceInfo', u'pointOnSurfaceManip', u'poleVectorConstraint', u'polyAppend', u'polyAppendVertex', u'polyAutoProj', u'polyAutoProjManip', u'polyAverageVertex', u'polyBevel', u'polyBlindData', u'polyBoolOp', u'polyBridgeEdge', u'polyChipOff', u'polyCloseBorder', u'polyCollapseEdge', u'polyCollapseF', u'polyColorDel', u'polyColorMod', u'polyColorPerVertex', u'polyCone', u'polyConnectComponents', u'polyCopyUV', u'polyCrease', u'polyCreaseEdge', u'polyCreateFace', u'polyCreateToolManip', u'polyCube', u'polyCut', u'polyCutManip', u'polyCutManipContainer', u'polyCylProj', u'polyCylinder', u'polyDelEdge', u'polyDelFacet', u'polyDelVertex', u'polyDuplicateEdge', u'polyEdgeToCurve', u'polyEditEdgeFlow', u'polyExtrudeEdge', u'polyExtrudeFace', u'polyExtrudeManip', u'polyExtrudeManipContainer', u'polyExtrudeVertex', u'polyFlipEdge', u'polyFlipUV', u'polyHelix', u'polyHoleFace', u'polyLayoutUV', u'polyMapCut', u'polyMapDel', u'polyMapSew', u'polyMapSewMove', u'polyMappingManip', u'polyMergeEdge', u'polyMergeFace', u'polyMergeUV', u'polyMergeVert', u'polyMergeVertsManip', u'polyMirror', u'polyModifierManip', u'polyMoveEdge', u'polyMoveFace', u'polyMoveFacetUV', u'polyMoveUV', u'polyMoveUVManip', u'polyMoveVertex', u'polyMoveVertexManip', u'polyNormal', u'polyNormalPerVertex', u'polyNormalizeUV', u'polyOptUvs', u'polyPipe', u'polyPlanarProj', u'polyPlane', u'polyPlatonicSolid', u'polyPoke', u'polyPokeManip', u'polyPrimitiveMisc', u'polyPrism', u'polyProj', u'polyProjManip', u'polyProjectCurve', u'polyPyramid', u'polyQuad', u'polyReduce', u'polySelectEditFeedbackManip', u'polySeparate', u'polySewEdge', u'polySmooth', u'polySmoothFace', u'polySmoothProxy', u'polySoftEdge', u'polySphProj', u'polySphere', u'polySpinEdge', u'polySplit', u'polySplitEdge', u'polySplitRing', u'polySplitToolManip1', u'polySplitVert', u'polyStraightenUVBorder', u'polySubdEdge', u'polySubdFace', u'polyToSubdiv', u'polyToolFeedbackManip', u'polyTorus', u'polyTransfer', u'polyTriangulate', u'polyTweak', u'polyTweakUV', u'polyUVRectangle', u'polyUnite', u'polyVertexNormalManip', u'polyWedgeFace', u'positionMarker', u'postProcessList', u'precompExport', u'projectCurve', u'projectTangent', u'projectTangentManip', u'projection', u'projectionManip', u'projectionMultiManip', u'projectionUVManip', u'propModManip', u'propMoveTriadManip', u'proxyManager', u'psdFileTex', u'quadPtOnLineManip', u'quadShadingSwitch', u'quatAdd', u'quatConjugate', u'quatInvert', u'quatNegate', u'quatNormalize', u'quatProd', u'quatSub', u'quatToEuler', u'radialField', u'ramp', u'rampShader', u'rbfSrf', u'rbfSrfManip', u'rebuildCurve', u'rebuildSurface', u'record', u'rectangularLightLocator', u'reference', u'remapColor', u'remapHsv', u'remapValue', u'renderBox', u'renderCone', u'renderGlobals', u'renderGlobalsList', u'renderLayer', u'renderLayerManager', u'renderPass', u'renderPassSet', u'renderQuality', u'renderRect', u'renderSphere', u'renderTarget', u'renderedImageSource', u'resolution', u'resultCurveTimeToAngular', u'resultCurveTimeToLinear', u'resultCurveTimeToTime', u'resultCurveTimeToUnitless', u'reverse', u'reverseCurve', u'reverseCurveManip', u'reverseSurface', u'reverseSurfaceManip', u'revolve', u'revolveManip', u'revolvedPrimitiveManip', u'rgbToHsv', u'rigidBody', u'rigidConstraint', u'rigidSolver', u'rock', u'rotateHelper', u'rotateLimitsManip', u'rotateManip', u'rotateUV2dManip', u'roundConstantRadius', u'roundConstantRadiusManip', u'roundRadiusCrvManip', u'roundRadiusManip', u'sampler', u'samplerInfo', u'scaleConstraint', u'scaleLimitsManip', u'scaleManip', u'scaleUV2dManip', u'screenAlignedCircleManip', u'script', u'scriptManip', u'sculpt', u'selectionListOperator', u'sequenceManager', u'sequencer', u'setRange', u'shaderGlow', u'shadingEngine', u'shadingMap', u'shellTessellate', u'shot', u'simpleTestNode', u'simpleVolumeShader', u'singleShadingSwitch', u'sketchPlane', u'skinBinding', u'skinCluster', u'smoothCurve', u'smoothTangentSrf', u'snapshot', u'snapshotShape', u'snow', u'softMod', u'softModHandle', u'softModManip', u'solidFractal', u'spBirailSrf', u'sphericalLightLocator', u'sphericalProjManip', u'spotCylinderManip', u'spotLight', u'spotManip', u'spring', u'squareSrf', u'squareSrfManip', u'stencil', u'stereoRigCamera', u'stitchAsNurbsShell', u'stitchSrf', u'stitchSrfManip', u'stroke', u'strokeGlobals', u'stucco', u'styleCurve', u'subCurve', u'subSurface', u'subdAddTopology', u'subdAutoProj', u'subdBlindData', u'subdCleanTopology', u'subdHierBlind', u'subdLayoutUV', u'subdMapCut', u'subdMapSewMove', u'subdMappingManip', u'subdPlanarProj', u'subdProjManip', u'subdTweak', u'subdTweakUV', u'subdiv', u'subdivCollapse', u'subdivComponentId', u'subdivReverseFaces', u'subdivSurfaceVarGroup', u'subdivToNurbs', u'subdivToPoly', u'substance', u'substanceOutput', u'surfaceEdManip', u'surfaceInfo', u'surfaceLuminance', u'surfaceSampler', u'surfaceShader', u'surfaceVarGroup', u'symmetryConstraint', u'tangentConstraint', u'texLattice', u'texLatticeDeformManip', u'texMoveShellManip', u'texSmoothManip', u'texSmudgeUVManip', u'textButtonManip', u'textManip2D', u'texture3dManip', u'textureBakeSet', u'textureToGeom', u'time', u'timeFunction', u'timeToUnitConversion', u'timeWarp', u'toggleManip', u'toggleOnLineManip', u'toolDrawManip', u'toolDrawManip2D', u'toonLineAttributes', u'towPointOnCurveManip', u'towPointOnSurfaceManip', u'trans2dManip', u'transUV2dManip', u'transferAttributes', u'transform', u'transformGeometry', u'translateLimitsManip', u'translateManip', u'translateUVManip', u'transmat', u'transmat_photon', u'transposeMatrix', u'trim', u'trimManip', u'trimWithBoundaries', u'triplanarProjManip', u'tripleShadingSwitch', u'trsInsertManip', u'trsManip', u'turbulenceField', u'turbulenceManip', u'tweak', u'uniformField', u'unitConversion', u'unitToTimeConversion', u'unknown', u'unknownDag', u'unknownTransform', u'untrim', u'useBackground', u'user_ibl_env', u'user_ibl_rect', u'uv2dManip', u'uvChooser', u'vectorProduct', u'vectorRenderGlobals', u'vertexBakeSet', u'viewColorManager', u'volumeAxisField', u'volumeBindManip', u'volumeFog', u'volumeLight', u'volumeNoise', u'volumeShader', u'vortexField', u'water', u'weightGeometryFilter', u'wire', u'wood', u'wrap', u'writeToColorBuffer', u'writeToDepthBuffer', u'writeToLabelBuffer', u'writeToVectorBuffer', u'wtAddMatrix', u'xformManip'] #
        pm.allNodeTypes(includeAbstract=True)
        # Result: [u'AISEnvFacade', u'AlembicNode', u'ComputeGlobal', u'ComputeLocal', u'CustomRigDefaultMappingNode', u'CustomRigRetargeterNode', u'HIKCharacterNode', u'HIKCharacterStateClient', u'HIKControlSetNode', u'HIKEffector2State', u'HIKEffectorFromCharacter', u'HIKFK2State', u'HIKPinning2State', u'HIKProperty2State', u'HIKRetargeterNode', u'HIKSK2State', u'HIKSkeletonGeneratorNode', u'HIKSolverNode', u'HIKState2Effector', u'HIKState2FK', u'HIKState2GlobalSK', u'HIKState2SK', u'abcimport', u'abstractBaseCreate (abstract)', u'abstractBaseNurbsConversion (abstract)', u'addDoubleLinear', u'addMatrix', u'adskAssetInstanceNode_TdependNode (abstract)', u'adskAssetInstanceNode_TdnTx2D (abstract)', u'adskAssetInstanceNode_TlightShape (abstract)', u'adskMaterial', u'adskPrepareRenderGlobals', u'aimConstraint', u'airField', u'airManip', u'alignCurve', u'alignManip', u'alignSurface', u'ambientLight', u'angleBetween', u'angleDimension', u'animBlend', u'animBlendInOut', u'animBlendNodeAdditive', u'animBlendNodeAdditiveDA', u'animBlendNodeAdditiveDL', u'animBlendNodeAdditiveF', u'animBlendNodeAdditiveFA', u'animBlendNodeAdditiveFL', u'animBlendNodeAdditiveI16', u'animBlendNodeAdditiveI32', u'animBlendNodeAdditiveRotation', u'animBlendNodeAdditiveScale', u'animBlendNodeBase (abstract)', u'animBlendNodeBoolean', u'animBlendNodeEnum', u'animBlendNodeTime', u'animClip', u'animCurve (abstract)', u'animCurveTA', u'animCurveTL', u'animCurveTT', u'animCurveTU', u'animCurveUA', u'animCurveUL', u'animCurveUT', u'animCurveUU', u'animLayer', u'anisotropic', u'annotationShape', u'apfEntityNode', u'apfFileNode', u'arcLengthDimension', u'areaLight', u'arrayMapper', u'arrowManip', u'artAttrPaintTest', u'assembly (abstract)', u'assemblyDefinition', u'assemblyReference', u'attachCurve', u'attachSurface', u'attrHierarchyTest', u'audio', u'avgCurves', u'avgCurvesManip', u'avgNurbsSurfacePoints', u'avgSurfacePoints', u'axesActionManip', u'bakeSet (abstract)', u'ballProjManip', u'barnDoorManip', u'baseGeometryVarGroup (abstract)', u'baseLattice', u'baseShadingSwitch (abstract)', u'bevel', u'bevelManip', u'bevelPlus', u'bezierCurve', u'bezierCurveToNurbs', u'birailSrf (abstract)', u'blend (abstract)', u'blendColorSets', u'blendColors', u'blendDevice', u'blendManip', u'blendShape', u'blendTwoAttr', u'blendWeighted', u'blindDataTemplate', u'blinn', u'boneLattice', u'boolean', u'boundary', u'boundaryBase (abstract)', u'brownian', u'brush', u'builtin_bsdf_architectural', u'builtin_bsdf_architectural_comp', u'builtin_bsdf_ashikhmin', u'builtin_bsdf_carpaint', u'builtin_bsdf_lambert', u'builtin_bsdf_mirror', u'builtin_bsdf_phong', u'bulge', u'bump2d', u'bump3d', u'buttonManip', u'cMuscleCreator', u'cMuscleDebug', u'cMuscleDirection', u'cMuscleDisplace', u'cMuscleDisplay', u'cMuscleFalloff', u'cMuscleKeepOut', u'cMuscleMultiCollide', u'cMuscleObject', u'cMuscleRelative', u'cMuscleShader', u'cMuscleSmartCollide', u'cMuscleSmartConstraint', u'cMuscleSpline', u'cMuscleSplineDeformer', u'cMuscleStretch', u'cMuscleSurfAttach', u'cMuscleSystem', u'cacheBase (abstract)', u'cacheBlend', u'cacheFile', u'camera', u'cameraManip', u'cameraPlaneManip', u'cameraSet', u'cameraView', u'centerManip', u'character', u'characterMap', u'characterOffset', u'checker', u'choice', u'chooser', u'circleManip', u'circleSweepManip', u'clamp', u'clientDevice (abstract)', u'clipGhostShape', u'clipLibrary', u'clipScheduler', u'clipToGhostData', u'closeCurve', u'closeSurface', u'closestPointOnMesh', u'closestPointOnSurface', u'cloth', u'cloud', u'cluster', u'clusterFlexorShape', u'clusterHandle', u'coiManip', u'collisionModel', u'colorProfile', u'componentManip', u'composeMatrix', u'concentricProjManip', u'condition', u'constraint (abstract)', u'container', u'containerBase', u'contour_composite', u'contour_contrast_function_levels', u'contour_contrast_function_simple', u'contour_only', u'contour_ps', u'contour_shader_combi', u'contour_shader_curvature', u'contour_shader_depthfade', u'contour_shader_factorcolor', u'contour_shader_framefade', u'contour_shader_layerthinner', u'contour_shader_maxcolor', u'contour_shader_silhouette', u'contour_shader_simple', u'contour_shader_widthfromcolor', u'contour_shader_widthfromlight', u'contour_shader_widthfromlightdir', u'contour_store_function', u'contour_store_function_simple', u'contrast', u'controlPoint (abstract)', u'copyColorSet', u'copyUVSet', u'cpManip', u'crater', u'creaseSet', u'createBPManip', u'createCVManip', u'createColorSet', u'createEPManip', u'createUVSet', u'cubeManip', u'cubicProjManip', u'curveEdManip', u'curveFromMesh (abstract)', u'curveFromMeshCoM', u'curveFromMeshEdge', u'curveFromSubdiv (abstract)', u'curveFromSubdivEdge', u'curveFromSubdivFace', u'curveFromSurface (abstract)', u'curveFromSurfaceBnd', u'curveFromSurfaceCoS', u'curveFromSurfaceIso', u'curveInfo', u'curveIntersect', u'curveNormalizer (abstract)', u'curveNormalizerAngle', u'curveNormalizerLinear', u'curveRange (abstract)', u'curveSegmentManip', u'curveShape (abstract)', u'curveVarGroup', u'cylindricalLightLocator', u'cylindricalProjManip', u'dagContainer', u'dagNode (abstract)', u'dagPose', u'dataBlockTest', u'decomposeMatrix', u'defaultLightList', u'defaultRenderUtilityList', u'defaultRenderingList', u'defaultShaderList', u'defaultTextureList', u'deformBend', u'deformBendManip', u'deformFlare', u'deformFlareManip', u'deformFunc (abstract)', u'deformSine', u'deformSineManip', u'deformSquash', u'deformSquashManip', u'deformTwist', u'deformTwistManip', u'deformWave', u'deformWaveManip', u'deformableShape (abstract)', u'deleteColorSet', u'deleteComponent', u'deleteUVSet', u'detachCurve', u'detachSurface', u'dgs_material', u'dgs_material_photon', u'dielectric_material', u'dielectric_material_photon', u'dimensionShape (abstract)', u'directedDisc', u'directionManip', u'directionalLight', u'discLightLocator', u'discManip', u'diskCache', u'displacementShader', u'displayLayer', u'displayLayerManager', u'distanceBetween', u'distanceDimShape', u'distanceManip', u'dof', u'dofManip', u'doubleShadingSwitch', u'dpBirailSrf', u'dragField', u'dropoffLocator', u'dropoffManip', u'dynAttenuationManip', u'dynBase (abstract)', u'dynController', u'dynGlobals', u'dynHolder', u'dynSpreadManip', u'dynamicConstraint', u'editMetadata', u'emitterManip', u'enableManip', u'entity (abstract)', u'envBall', u'envChrome', u'envCube', u'envFacade', u'envFog', u'envSky', u'envSphere', u'environmentFog', u'eulerToQuat', u'explodeNurbsShell', u'expression', u'extendCurve', u'extendCurveDistanceManip', u'extendSurface', u'extendSurfaceDistanceManip', u'extrude', u'extrudeManip', u'facade', u'ffBlendSrf', u'ffBlendSrfObsolete', u'ffFilletSrf', u'ffd', u'field (abstract)', u'fieldManip', u'fieldsManip', u'file', u'filletCurve', u'filter (abstract)', u'filterClosestSample', u'filterEuler', u'filterResample', u'filterSimplify', u'fitBspline', u'flexorShape', u'flow', u'fluidEmitter', u'fluidShape', u'fluidSliceManip', u'fluidTexture2D', u'fluidTexture3D', u'follicle', u'forceUpdateManip', u'fosterParent', u'fourByFourMatrix', u'fractal', u'frameCache', u'freePointManip', u'freePointTriadManip', u'gammaCorrect', u'geoConnectable', u'geoConnector', u'geometryConstraint', u'geometryFilter', u'geometryOnLineManip', u'geometryShape (abstract)', u'geometryVarGroup', u'globalCacheControl', u'globalStitch', u'gpuCache', u'granite', u'gravityField', u'greasePencilSequence', u'greasePlane', u'greasePlaneRenderShape', u'grid', u'groundPlane (abstract)', u'groupId', u'groupParts', u'guide', u'hairConstraint', u'hairSystem', u'hairTubeShader', u'hardenPoint', u'hardwareRenderGlobals', u'hardwareRenderingGlobals', u'heightField', u'hierarchyTestNode1', u'hierarchyTestNode2', u'hierarchyTestNode3', u'hikEffector', u'hikFKJoint', u'hikFloorContactMarker', u'hikGroundPlane', u'hikHandle', u'hikIKEffector', u'hikSolver', u'historySwitch', u'holdMatrix', u'hsvToRgb', u'hwReflectionMap', u'hwRenderGlobals', u'hwShader (abstract)', u'hyperGraphInfo', u'hyperLayout', u'hyperView', u'ik2Bsolver', u'ikEffector', u'ikHandle', u'ikMCsolver', u'ikPASolver', u'ikRPManip', u'ikRPsolver', u'ikSCsolver', u'ikSolver (abstract)', u'ikSplineManip', u'ikSplineSolver', u'ikSpringSolver', u'ikSystem', u'imagePlane', u'imageSource (abstract)', u'implicitBox', u'implicitCone', u'implicitSphere', u'indexManip', u'insertKnotCurve', u'insertKnotSurface', u'instancer', u'intersectSurface', u'inverseMatrix', u'isoparmManip', u'jiggle', u'joint', u'jointCluster', u'jointClusterManip', u'jointFfd', u'jointLattice', u'jointTranslateManip', u'keyframeRegionManip', u'keyingGroup', u'lambert', u'lattice', u'layeredShader', u'layeredTexture', u'leastSquaresModifier', u'leather', u'light (abstract)', u'lightFog', u'lightInfo', u'lightLinker', u'lightList', u'lightManip', u'limitManip', u'lineManip', u'lineModifier', u'locator', u'lodGroup', u'lodThresholds', u'loft', u'lookAt', u'luminance', u'makeCircularArc (abstract)', u'makeGroup', u'makeIllustratorCurves', u'makeNurbCircle', u'makeNurbCone', u'makeNurbCube', u'makeNurbCylinder', u'makeNurbPlane', u'makeNurbSphere', u'makeNurbTorus', u'makeNurbsSquare', u'makeTextCurves', u'makeThreePointCircularArc', u'makeThreePointCircularArcManip', u'makeTwoPointCircularArc', u'makeTwoPointCircularArcManip', u'mandelbrot', u'mandelbrot3D', u'manip2D (abstract)', u'manip2DContainer', u'manip3D (abstract)', u'manipContainer', u'mapVizShape', u'marble', u'markerManip', u'materialFacade', u'materialInfo', u'membrane', u'mentalrayCCMeshProxy', u'mentalrayCurveApprox', u'mentalrayDisplaceApprox', u'mentalrayFramebuffer', u'mentalrayGlobals', u'mentalrayIblShape', u'mentalrayItemsList', u'mentalrayLightProfile', u'mentalrayOptions', u'mentalrayOutputPass', u'mentalrayPhenomenon', u'mentalrayRenderPass', u'mentalrayShader', u'mentalraySubdivApprox', u'mentalraySurfaceApprox', u'mentalrayTessellation', u'mentalrayText', u'mentalrayTexture', u'mentalrayUserBuffer', u'mentalrayUserData', u'mentalrayVertexColors', u'mesh', u'meshVarGroup', u'mi_bump_flakes', u'mi_car_paint_phen', u'mi_car_paint_phen_x', u'mi_car_paint_phen_x_passes', u'mi_metallic_paint', u'mi_metallic_paint_output_mixer', u'mi_metallic_paint_x', u'mi_metallic_paint_x_passes', u'mia_ciesky', u'mia_envblur', u'mia_exposure_photographic', u'mia_exposure_photographic_rev', u'mia_exposure_simple', u'mia_lens_bokeh', u'mia_light_surface', u'mia_material', u'mia_material_x', u'mia_material_x_passes', u'mia_photometric_light', u'mia_physicalsky', u'mia_physicalsun', u'mia_portal_light', u'mia_roundcorners', u'mib_amb_occlusion', u'mib_bent_normal_env', u'mib_blackbody', u'mib_bump_basis', u'mib_bump_map', u'mib_bump_map2', u'mib_cie_d', u'mib_color_alpha', u'mib_color_average', u'mib_color_intensity', u'mib_color_interpolate', u'mib_color_mix', u'mib_color_spread', u'mib_continue', u'mib_data_bool', u'mib_data_bool_array', u'mib_data_color', u'mib_data_color_array', u'mib_data_get_bool', u'mib_data_get_color', u'mib_data_get_int', u'mib_data_get_scalar', u'mib_data_get_shader', u'mib_data_get_shader_bool', u'mib_data_get_shader_color', u'mib_data_get_shader_int', u'mib_data_get_shader_scalar', u'mib_data_get_shader_vector', u'mib_data_get_string', u'mib_data_get_texture', u'mib_data_get_vector', u'mib_data_int', u'mib_data_int_array', u'mib_data_scalar', u'mib_data_scalar_array', u'mib_data_shader', u'mib_data_shader_array', u'mib_data_string', u'mib_data_string_array', u'mib_data_texture', u'mib_data_texture_array', u'mib_data_vector', u'mib_data_vector_array', u'mib_dielectric', u'mib_fast_occlusion', u'mib_fg_occlusion', u'mib_geo_add_uv_texsurf', u'mib_geo_cone', u'mib_geo_cube', u'mib_geo_cylinder', u'mib_geo_instance', u'mib_geo_instance_mlist', u'mib_geo_sphere', u'mib_geo_square', u'mib_geo_torus', u'mib_glossy_reflection', u'mib_glossy_refraction', u'mib_illum_blinn', u'mib_illum_cooktorr', u'mib_illum_hair', u'mib_illum_lambert', u'mib_illum_phong', u'mib_illum_ward', u'mib_illum_ward_deriv', u'mib_lens_clamp', u'mib_lens_stencil', u'mib_light_infinite', u'mib_light_photometric', u'mib_light_point', u'mib_light_spot', u'mib_lightmap_sample', u'mib_lightmap_write', u'mib_lookup_background', u'mib_lookup_cube1', u'mib_lookup_cube6', u'mib_lookup_cylindrical', u'mib_lookup_spherical', u'mib_map_get_color', u'mib_map_get_integer', u'mib_map_get_integer_array', u'mib_map_get_scalar', u'mib_map_get_scalar_array', u'mib_map_get_transform', u'mib_map_get_vector', u'mib_opacity', u'mib_passthrough_bump_map', u'mib_photon_basic', u'mib_ptex_lookup', u'mib_ray_marcher', u'mib_reflect', u'mib_refract', u'mib_refraction_index', u'mib_shadow_transparency', u'mib_texture_checkerboard', u'mib_texture_filter_lookup', u'mib_texture_lookup', u'mib_texture_lookup2', u'mib_texture_polkadot', u'mib_texture_polkasphere', u'mib_texture_remap', u'mib_texture_rotate', u'mib_texture_turbulence', u'mib_texture_vector', u'mib_texture_wave', u'mib_transparency', u'mib_twosided', u'mib_volume', u'mila_5layers', u'mila_5layers_phen', u'mila_adapter', u'mila_diffuse', u'mila_emission', u'mila_fastsss', u'mila_flakes_adapter', u'mila_get_normal', u'mila_layers', u'mila_material', u'mila_material_std', u'mila_reflection', u'mila_refraction', u'mila_translucency', u'mila_transparency', u'mip_binaryproxy', u'mip_cameramap', u'mip_card_opacity', u'mip_fgshooter', u'mip_gamma_gain', u'mip_grayball', u'mip_matteshadow', u'mip_matteshadow_mtl', u'mip_mirrorball', u'mip_motion_vector', u'mip_motionblur', u'mip_rayswitch', u'mip_rayswitch_advanced', u'mip_rayswitch_environment', u'mip_rayswitch_stage', u'mip_render_subset', u'misss_call_shader', u'misss_fast_lmap_maya', u'misss_fast_shader', u'misss_fast_shader2', u'misss_fast_shader2_x', u'misss_fast_shader_x', u'misss_fast_shader_x_passes', u'misss_fast_simple_maya', u'misss_fast_skin_maya', u'misss_fast_skin_phen', u'misss_fast_skin_phen_d', u'misss_lambert_gamma', u'misss_lightmap_phen', u'misss_lightmap_write', u'misss_mia_skin2_phen', u'misss_mia_skin2_phen_d', u'misss_mia_skin2_surface_phen', u'misss_physical', u'misss_physical_phen', u'misss_set_normal', u'misss_skin_specular', u'motionPath', u'motionPathManip', u'motionTrail', u'motionTrailShape', u'mountain', u'moveBezierHandleManip', u'moveVertexManip', u'movie', u'mpBirailSrf', u'multDoubleLinear', u'multMatrix', u'multilisterLight', u'multiplyDivide', u'mute', u'nBase (abstract)', u'nCloth', u'nComponent', u'nParticle', u'nRigid', u'nearestPointOnCurve', u'network', u'newtonField', u'newtonManip', u'node (abstract)', u'noise', u'nonAmbientLightShapeNode (abstract)', u'nonExtendedLightShapeNode (abstract)', u'nonLinear', u'normalConstraint', u'nucleus', u'nurbsCurve', u'nurbsCurveToBezier', u'nurbsDimShape (abstract)', u'nurbsSurface', u'nurbsTessellate', u'nurbsToSubdiv', u'nurbsToSubdivProc', u'objectAttrFilter', u'objectBinFilter', u'objectFilter', u'objectMultiFilter', u'objectNameFilter', u'objectRenderFilter', u'objectScriptFilter', u'objectSet', u'objectTypeFilter', u'ocean', u'oceanShader', u'offsetCos', u'offsetCosManip', u'offsetCurve', u'offsetCurveManip', u'offsetSurface', u'offsetSurfaceManip', u'oldBlindDataBase', u'oldGeometryConstraint', u'oldNormalConstraint', u'oldTangentConstraint', u'opticalFX', u'orientConstraint', u'orientationMarker', u'orthoGrid (abstract)', u'oversampling_lens', u'pairBlend', u'paramDimension', u'parentConstraint', u'parentTessellate (abstract)', u'parti_volume', u'parti_volume_photon', u'particle', u'particleAgeMapper', u'particleCloud', u'particleColorMapper', u'particleIncandMapper', u'particleSamplerInfo', u'particleTranspMapper', u'partition', u'passContributionMap', u'passMatrix', u'path_material', u'pfxGeometry (abstract)', u'pfxHair', u'pfxToon', u'phong', u'phongE', u'physical_lens_dof', u'physical_light', u'pivot2dManip', u'pivotAndOrientManip', u'place2dTexture', u'place3dTexture', u'planarProjManip', u'planarTrimSurface', u'plane (abstract)', u'plusMinusAverage', u'pointConstraint', u'pointEmitter', u'pointLight', u'pointMatrixMult', u'pointOnCurveInfo', u'pointOnCurveManip', u'pointOnLineManip', u'pointOnPolyConstraint', u'pointOnSurfManip', u'pointOnSurfaceInfo', u'pointOnSurfaceManip', u'poleVectorConstraint', u'polyAppend', u'polyAppendVertex', u'polyAutoProj', u'polyAutoProjManip', u'polyAverageVertex', u'polyBase (abstract)', u'polyBevel', u'polyBlindData', u'polyBoolOp', u'polyBridgeEdge', u'polyChipOff', u'polyCloseBorder', u'polyCollapseEdge', u'polyCollapseF', u'polyColorDel', u'polyColorMod', u'polyColorPerVertex', u'polyCone', u'polyConnectComponents', u'polyCopyUV', u'polyCrease', u'polyCreaseEdge', u'polyCreateFace', u'polyCreateToolManip', u'polyCreator (abstract)', u'polyCube', u'polyCut', u'polyCutManip', u'polyCutManipContainer', u'polyCylProj', u'polyCylinder', u'polyDelEdge', u'polyDelFacet', u'polyDelVertex', u'polyDuplicateEdge', u'polyEdgeToCurve', u'polyEditEdgeFlow', u'polyExtrudeEdge', u'polyExtrudeFace', u'polyExtrudeManip', u'polyExtrudeManipContainer', u'polyExtrudeVertex', u'polyFlipEdge', u'polyFlipUV', u'polyHelix', u'polyHoleFace', u'polyLayoutUV', u'polyMapCut', u'polyMapDel', u'polyMapSew', u'polyMapSewMove', u'polyMappingManip', u'polyMergeEdge', u'polyMergeFace', u'polyMergeUV', u'polyMergeVert', u'polyMergeVertsManip', u'polyMirror', u'polyModifier (abstract)', u'polyModifierManip', u'polyModifierUV (abstract)', u'polyModifierWorld (abstract)', u'polyMoveEdge', u'polyMoveFace', u'polyMoveFacetUV', u'polyMoveUV', u'polyMoveUVManip', u'polyMoveVertex', u'polyMoveVertexManip', u'polyNormal', u'polyNormalPerVertex', u'polyNormalizeUV', u'polyOptUvs', u'polyPipe', u'polyPlanarProj', u'polyPlane', u'polyPlatonicSolid', u'polyPoke', u'polyPokeManip', u'polyPrimitive (abstract)', u'polyPrimitiveMisc', u'polyPrism', u'polyProj', u'polyProjManip', u'polyProjectCurve', u'polyPyramid', u'polyQuad', u'polyReduce', u'polySelectEditFeedbackManip', u'polySeparate', u'polySewEdge', u'polySmooth', u'polySmoothFace', u'polySmoothProxy', u'polySoftEdge', u'polySphProj', u'polySphere', u'polySpinEdge', u'polySplit', u'polySplitEdge', u'polySplitRing', u'polySplitToolManip1', u'polySplitVert', u'polyStraightenUVBorder', u'polySubdEdge', u'polySubdFace', u'polyToSubdiv', u'polyToolFeedbackManip', u'polyTorus', u'polyTransfer', u'polyTriangulate', u'polyTweak', u'polyTweakUV', u'polyUVRectangle', u'polyUnite', u'polyVertexNormalManip', u'polyWedgeFace', u'positionMarker', u'postProcessList', u'precompExport', u'primitive (abstract)', u'projectCurve', u'projectTangent', u'projectTangentManip', u'projection', u'projectionManip', u'projectionMultiManip', u'projectionUVManip', u'propModManip', u'propMoveTriadManip', u'proxyManager', u'psdFileTex', u'quadPtOnLineManip', u'quadShadingSwitch', u'quatAdd', u'quatConjugate', u'quatInvert', u'quatNegate', u'quatNormalize', u'quatProd', u'quatSub', u'quatToEuler', u'radialField', u'ramp', u'rampShader', u'rbfSrf', u'rbfSrfManip', u'rebuildCurve', u'rebuildSurface', u'record', u'rectangularLightLocator', u'reference', u'reflect (abstract)', u'remapColor', u'remapHsv', u'remapValue', u'renderBox', u'renderCone', u'renderGlobals', u'renderGlobalsList', u'renderLayer', u'renderLayerManager', u'renderLight (abstract)', u'renderPass', u'renderPassSet', u'renderQuality', u'renderRect', u'renderSphere', u'renderTarget', u'renderedImageSource', u'resolution', u'resultCurve (abstract)', u'resultCurveTimeToAngular', u'resultCurveTimeToLinear', u'resultCurveTimeToTime', u'resultCurveTimeToUnitless', u'reverse', u'reverseCurve', u'reverseCurveManip', u'reverseSurface', u'reverseSurfaceManip', u'revolve', u'revolveManip', u'revolvedPrimitive (abstract)', u'revolvedPrimitiveManip', u'rgbToHsv', u'rigidBody', u'rigidConstraint', u'rigidSolver', u'rock', u'rotateHelper', u'rotateLimitsManip', u'rotateManip', u'rotateUV2dManip', u'roundConstantRadius', u'roundConstantRadiusManip', u'roundRadiusCrvManip', u'roundRadiusManip', u'sampler', u'samplerInfo', u'scaleConstraint', u'scaleLimitsManip', u'scaleManip', u'scaleUV2dManip', u'screenAlignedCircleManip', u'script', u'scriptManip', u'sculpt', u'selectionListOperator', u'sequenceManager', u'sequencer', u'setRange', u'shaderGlow', u'shadingDependNode (abstract)', u'shadingEngine', u'shadingMap', u'shape (abstract)', u'shellTessellate', u'shot', u'simpleTestNode', u'simpleVolumeShader', u'singleShadingSwitch', u'sketchPlane', u'skinBinding', u'skinCluster', u'smoothCurve', u'smoothTangentSrf', u'snapshot', u'snapshotShape', u'snow', u'softMod', u'softModHandle', u'softModManip', u'solidFractal', u'spBirailSrf', u'sphericalLightLocator', u'sphericalProjManip', u'spotCylinderManip', u'spotLight', u'spotManip', u'spring', u'squareSrf', u'squareSrfManip', u'stencil', u'stereoRigCamera', u'stitchAsNurbsShell', u'stitchSrf', u'stitchSrfManip', u'stroke', u'strokeGlobals', u'stucco', u'styleCurve', u'subCurve', u'subSurface', u'subdAddTopology', u'subdAutoProj', u'subdBase (abstract)', u'subdBlindData', u'subdCleanTopology', u'subdHierBlind', u'subdLayoutUV', u'subdMapCut', u'subdMapSewMove', u'subdMappingManip', u'subdModifier (abstract)', u'subdModifierUV (abstract)', u'subdModifierWorld (abstract)', u'subdPlanarProj', u'subdProjManip', u'subdTweak', u'subdTweakUV', u'subdiv', u'subdivCollapse', u'subdivComponentId', u'subdivReverseFaces', u'subdivSurfaceVarGroup', u'subdivToNurbs', u'subdivToPoly', u'substance', u'substanceOutput', u'surfaceEdManip', u'surfaceInfo', u'surfaceLuminance', u'surfaceSampler', u'surfaceShader', u'surfaceShape (abstract)', u'surfaceVarGroup', u'symmetryConstraint', u'tangentConstraint', u'texBaseDeformManip (abstract)', u'texLattice', u'texLatticeDeformManip', u'texMoveShellManip', u'texSmoothManip', u'texSmudgeUVManip', u'textButtonManip', u'textManip2D', u'texture2d (abstract)', u'texture3d (abstract)', u'texture3dManip', u'textureBakeSet', u'textureEnv (abstract)', u'textureToGeom', u'threadedDevice (abstract)', u'time', u'timeFunction', u'timeToUnitConversion', u'timeWarp', u'toggleManip', u'toggleOnLineManip', u'toolDrawManip', u'toolDrawManip2D', u'toonLineAttributes', u'towPointOnCurveManip', u'towPointOnSurfaceManip', u'trans2dManip', u'transUV2dManip', u'transferAttributes', u'transform', u'transformGeometry', u'translateLimitsManip', u'translateManip', u'translateUVManip', u'transmat', u'transmat_photon', u'transposeMatrix', u'trim', u'trimManip', u'trimWithBoundaries', u'triplanarProjManip', u'tripleShadingSwitch', u'trsInsertManip', u'trsManip', u'turbulenceField', u'turbulenceManip', u'tweak', u'uniformField', u'unitConversion', u'unitToTimeConversion', u'unknown', u'unknownDag', u'unknownTransform', u'untrim', u'useBackground', u'user_ibl_env', u'user_ibl_rect', u'uv2dManip', u'uvChooser', u'vectorProduct', u'vectorRenderGlobals', u'vertexBakeSet', u'viewColorManager', u'volumeAxisField', u'volumeBindManip', u'volumeFog', u'volumeLight', u'volumeNoise', u'volumeShader', u'vortexField', u'water', u'weightGeometryFilter', u'wire', u'wood', u'wrap', u'writeToColorBuffer', u'writeToDepthBuffer', u'writeToFrameBuffer (abstract)', u'writeToLabelBuffer', u'writeToVectorBuffer', u'wtAddMatrix', u'xformManip'] #
        # Trickier example using Python capabilities to get node types starting with 'l'
        [item for item in pm.allNodeTypes(includeAbstract=True) if item[0].lower() == 'l']
        # Result: [u'lambert', u'lattice', u'layeredShader', u'layeredTexture', u'leastSquaresModifier', u'leather', u'light (abstract)', u'lightFog', u'lightInfo', u'lightLinker', u'lightList', u'lightManip', u'limitManip', u'lineManip', u'lineModifier', u'locator', u'lodGroup', u'lodThresholds', u'loft', u'lookAt', u'luminance'] #
    """

    pass


def aaf2fcp(*args, **kwargs):
    """
    This command is used to convert an aff file to a Final Cut Pro (fcp) xml file The conversion process can take several
    seconds to complete and the command is meant to be run asynchronously
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``deleteFile`` / ``df``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Delete terporary file. Can only be used with the terminate option                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dstPath`` / ``dst``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifiy a destination path                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``getFileName`` / ``gfn``                                                                            | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query output file name                                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``progress`` / ``pr``                                                                                | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Request progress report                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``srcFile`` / ``src``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifiy a source file                                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``terminate`` / ``t``                                                                                | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Complete the task                                         Flag can have multiple arguments, passed either as a tuple or a list.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``waitCompletion`` / ``wc``                                                                          | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Wait for the conversion process to complete                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.aaf2fcp`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        handle = pm.aaf2fcp(srcFile='c:/tmp/test.aaf', dstPath='c:/tmp')
        destinationFile = pm.aff2fcp(getFileName=handle)
        pm.aaf2fcp(waitCompletion=handle)
        pm.aaf2fcp(terminate=handle,deleteFile=False)
    """

    pass


def whatsNewHighlight(*args, **kwargs):
    """
    This command is used to toggle the What's New highlighting feature, and the display of the settings dialog for the
    feature that appears on startup. In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``highlightColor`` / ``hc``                                                                          | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the color of the What's New highlight. The arguments correspond to the red, green, and blue color components. Each color component ranges in value from 0.0 to|
    |  | 1.0.                                                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``highlightOn`` / ``ho``                                                                             | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Toggle the What's New highlighting feature. When turned on, menu items and buttons introduced in the latest version will be highlighted.                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showStartupDialog`` / ``ssd``                                                                      | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set whether the settings dialog for this feature appears on startup.                      Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.whatsNewHighlight`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #    Turn on What's New highlighting if not already on.
        #
        if not pm.whatsNewHighlight(query=True, highlightOn=True):
            pm.whatsNewHighlight(highlightOn=True)
        
        #    Turn off What's New highlighting startup dialog if it is set to appear.
        #
        if pm.whatsNewHighlight(query=True, showStartupDialog=True):
            pm.whatsNewHighlight(showStartupDialog=False)
    """

    pass


def scriptNode(*args, **kwargs):
    """
    scriptNodes contain scripts that are executed when a file is loaded or when the script node is deleted. If a script
    modifies a referenced node, the changes will be tracked as reference edits unless the scriptNode was created with the
    ignoreReferenceEdits flag. The scriptNode command is used to create, edit, query, and test scriptNodes. In query mode,
    return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``afterScript`` / ``afterScript``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The script executed when the script node is deleted. C: The default is an empty string. Q: When queried, this flag returns a string.                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``beforeScript`` / ``bs``                                                                            | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The script executed during file load. C: The default is an empty string. Q: When queried, this flag returns a string.                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``executeAfter`` / ``ea``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Execute the script stored in the .after attribute of the scriptNode. This script is normally executed when the script node is deleted.                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``executeBefore`` / ``eb``                                                                           | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Execute the script stored in the .before attribute of the scriptNode. This script is normally executed when the file is loaded.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``ignoreReferenceEdits`` / ``ire``                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets whether changes made to referenced nodes during the execution of the script should be recorded as reference edits. This flag must be set when the scriptNode |
    |  | is created. If this flag is not set, changes to referenced nodes will be recorded as edits by default.                          Flag can have multiple arguments, |
    |  | passed either as a tuple or a list.                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When creating a new scriptNode, this flag specifies the name of the node. If a non-unique name is used, the name will be modified to ensure uniqueness.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scriptType`` / ``st``                                                                              | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies when the script is executed. The following values may be used: 0Execute on demand.1Execute on file load or on node deletion.2Execute on file load or on |
    |  | node deletion when not in batch mode. 3Internal4Execute on software render5Execute on software frame render6Execute on scene configuration7Execute on time        |
    |  | changedC: The default value is 0. Q: When queried, this flag returns an int.                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``sourceType`` / ``stp``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the language type for both the attached scripts. Valid values are mel(enabled by default), and python.                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.scriptNode`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #    Create a scriptNode named script that creates a sphere when a file
        #    containing this node is loaded.
        #
        nodeName = pm.scriptNode( st=2, bs='pm.sphere()', n='script', stp='python')
        
        #    Test the before script.
        #
        pm.scriptNode( nodeName, executeBefore=True )
        
        #    Add a script to create a cone when the script node is deleted.
        #
        pm.scriptNode( nodeName, e=True, as='pm.cone()', stp='python' )
        
        #    Test the after script
        #
        pm.scriptNode( nodeName, executeAfter=True )
    """

    pass


def dgfilter(*args, **kwargs):
    """
    The dgfiltercommand is used to define Dependency Graph filters that select DG objects based on certain criteria.  The
    command itself can be used to filter objects or it can be attached to a dbtraceobject to selectively filter what output
    is traced. If objects are specified then apply the filter to those objects and return a boolean indicating whether they
    passed or not, otherwise return then name of the filter.  An invalid filter will pass all objects.  For multiple objects
    the return value is the logical ANDof all object's return values.
    
    Dynamic library stub function
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``atr``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Select objects whose attribute names match the pattern.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``list`` / ``l``                                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List the available filters.  If used in conjunction with the -nameflag it will show a description of what the filter is.                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``logicalAnd`` / ``logicalAnd``                                                                      | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Logical AND of two filters.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``logicalNot`` / ``logicalNot``                                                                      | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Logical inverse of filter.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``logicalOr`` / ``logicalOr``                                                                        | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Logical OR of two filters.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Use filter named FILTER (or create new filter with that name). If no objects are specified then the name given to the filter will be returned.                    |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``node`` / ``nd``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Select objects whose node names match the pattern.                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``nodeType`` / ``nt``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Select objects whose node type names match the pattern.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``plug`` / ``p``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Select objects whose plug names match the pattern.                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dgfilter`
    """

    pass


def dbpeek(*args, **kwargs):
    """
    The dbpeekcommand is used to analyze the Maya data for information of interest. See a description of the flags for
    details on what types of things can be analyzed.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``allObjects`` / ``all``                                                                             | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Ignore any specified or selected objects and peek into all applicable objects. The definition of allObjectswill vary based on the peek operation being performed -|
    |  | see the flag documentation for details on what it means for a given operation. By default if no objects are selected or specified then it will behave as though   |
    |  | this flag were set.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``argument`` / ``a``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify one or more arguments to be passed to the operation. The acceptable values for the argument string are documented in the flag to which they will be       |
    |  | applied. If the argument itself takes a value then the value will be of the form argname=argvalue.                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``count`` / ``c``                                                                                    | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify a count to be used by the test. Different tests make different use of the count, query the operation to find out how it interprets the value. For example |
    |  | a performance test might use it as the number of iterations to run in the test, an output operation might use it to limit the amount of output it produces.       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``operation`` / ``op``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify the peeking operation to perform. The various operations are registered at run time and can be listed by querying this flag without a value. If you query |
    |  | it with a value then you get the detail values that peek operation accepts and a description of what it does. In query mode, this flag can accept a value.Flag can|
    |  | have multiple arguments, passed either as a tuple or a list.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``outputFile`` / ``of``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify the location of a file to which the information is to be dumped. Default will return the value from the command.  Use the special names stdoutand stderrto|
    |  | redirect to your command window. The special name msdevis available when debugging on Windows to direct your output to the debug tab in the output window of      |
    |  | Visual Studio.                                                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dbpeek`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        import maya.cmds as cmds
        // Find the available peek operations
        pm.dbpeek( op=True, query=True )
        # Return: ['metadata', 'nodes', 'references', 'plugIterator'] #
        // Describe the detail of a single available type
        pm.dbpeek( query=True, op='nodes' )
        # Return: 'The operation 'nodes' understands type flags 'attributes, visible'.
        The 'visible' flag filters the display list to ignore any hidden
        or internal nodes. Default is to show all nodes
        Normal display will show a count of nodes in the scene of each
        type. Adding the 'attributes' flag includes the attribute count
        for each node as well, segregated by static, extension, and dynamic types.
        '#
        # Describe the detail of a single available operation
        pm.dbpeek( query=True, op='plugIterator' )
        # Return: 'The test 'plugIterator' doesn't have any type flags.
        Suggested iteration count minimum is 1000000 for which the test machine
        measured a time of 19.234s.
        This tests the performance of the class which iterates over all of the
        networked plugs in a plug tree.
        '#
        pm.dbpeek( op='plugIterator', count=10000 )
        # Return: 'Run 10,000 loops of plug iteration over a tree of size 51, depth 4
        Total time:   17.0s
        Maximum time: 0.81s
        Minimum time: 0.23s
        Average time: 0.30s
        '#
        # Run a performance test for 1000000 loops and store the results
        pm.dbpeek( op='plugIterator', count=1000000, outputFile='MyFile.txt' )
        # Return: 0 #
        pm.loadPlugin( 'MetadataSample' )
        pm.polyPlane( name='planeLuck' )
        pm.dataStructure( asString='name=TestStructure:int32=ID )
        pm.importMetadata( asString='channel face\n stream\n TestStream\n TestStructure\n 0\n 99\n 1\n 999\n 2\n 9999\n endStream\n endChannel\n endAssociations" "planeLuckShape' )
        # Peek at the newly created metadata
        #
        pm.dbpeek( op='metadata', type='summary' )
        # Return: 'Node planeLuckShape : face( TestStream[3] )' #
    """

    pass


def profiler(*args, **kwargs):
    """
    The profiler is used to record timing information from key events within Maya, as an aid in tuning the performance of
    scenes, scripts and plug-ins. User written plug-ins and Python scripts can also generate profiling information for their
    own code through the MProfilingScope and MProfiler classes in the API. This command provides the ability to control the
    collection of profiling data and to query information about the recorded events. The recorded information can also be
    viewed graphically in the Profiler window. The buffer size cannot be changed while sampling is active, it will return an
    error The reset flag cannot be called while sampling is active, it will return an error. Any changes to the buffer size
    will only be applied on start of the next recording. You can't save and load in the same command, save has priority,
    load would be ignored.                In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``addCategory`` / ``a``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Add a new category for the profiler. Returns the index of the new category.                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``allCategories`` / ``ac``                                                                           | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the names of all categories                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``bufferSize`` / ``b``                                                                               | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Toggled : change the buffer size to fit the specified number of events (requires that sampling is off) Query : return the current buffer size The new buffer size |
    |  | will only take effect when next sampling starts. When the buffer is full, the recording stops.                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``categoryIndex`` / ``ci``                                                                           | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in conjunction with other flags, to indicate the index of the category.                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``categoryIndexToName`` / ``cin``                                                                    | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the name of the category with a given index.                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``categoryName`` / ``cn``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in conjunction with other flags, to indicate the name of the category.                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``categoryNameToIndex`` / ``cni``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the index of the category with a given name.                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``categoryRecording`` / ``cr``                                                                       | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Toggled : Enable/disable the recording of the category. Query : return if the recording of the category is On. Requires the -categoryIndex or -categoryName flag  |
    |  | to specify the category to be queried.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``clearAllMelInstrumentation`` / ``cam``                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Clear all MEL command or procedure instrumentation.                                       Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``colorIndex`` / ``coi``                                                                             | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with -instrumentMel trueto specify the color index to show the profiling result.                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``eventCPUId`` / ``eci``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the CPU ID of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``eventCategory`` / ``eca``                                                                          | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the category index the event at the given index belongs to. Requires the -eventIndex flag to specify the event to be queried.                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``eventColor`` / ``eco``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the color of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``eventCount`` / ``ec``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the number of events in the buffer                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``eventDescription`` / ``ed``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the description of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``eventDuration`` / ``edu``                                                                          | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the duration of the event at the given index, the time unit is microsecond. Note that a signal event has a 0 duration. Requires the -eventIndex flag to     |
    |  | specify the event to be queried.                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``eventIndex`` / ``ei``                                                                              | *int*                         | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used usually in conjunction with other flags, to indicate the index of the event.                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``eventName`` / ``en``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the name of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``eventStartTime`` / ``et``                                                                          | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the time of the event at the given index, the time unit is microsecond. Requires the -eventIndex flag to specify the event to be queried.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``eventThreadId`` / ``eti``                                                                          | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the thread ID of the event at the given index. Requires the -eventIndex flag to specify the event to be queried.                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``instrumentMel`` / ``instrumentMel``                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Enable/Diable the instrumentation of a MEL command or procedure. When the instrumentation is enabled, the execution of MEL command or procedure can be profiled   |
    |  | and shown in the Profiler window. To enable the instrumentation requires the -procedureName, -colorIndex and -categoryIndex flags. To disable the instrumentation |
    |  | requires the -procedureName flag.                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``load`` / ``l``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Read the recorded events from the specified file                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``output`` / ``o``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Output the recorded events to the specified file                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``procedureDescription`` / ``pd``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with -instrumentMel trueto provide a description of the MEL command or procedure being instrumented. This description can be viewed in the Profiler Tool     |
    |  | window.                                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``procedureName`` / ``pn``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with -instrumentMel to specify the name of the procedure to be enabled/disabled the instrumentation.                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeCategory`` / ``rc``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Remove an existing category for the profiler. Returns the index of the removed category.                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``reset`` / ``r``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | reset the profiler's data (requires that sampling is off)                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``sampling`` / ``s``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Toggled : Enable/disable the recording of events Query : return if the recording of events is On.                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``signalEvent`` / ``sig``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query if the event at the given index is a signal event. Requires the -eventIndex flag to specify the event to be queried. A Signal Event only remembers the start|
    |  | moment and has no knowledge about duration. It can be used in cases when the user does not care about the duration but only cares if this event does happen.      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``signalMelEvent`` / ``sim``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with -instrumentMel true, inform profiler that this instrumented MEL command or procedure will be taken as a signal event during profiling. A Signal Event   |
    |  | only remembers the start moment and has no knowledge about duration. It can be used in cases when the user does not care about the duration but only cares if this|
    |  | event does happen.                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.profiler`
    """

    pass


def filePathEditor(*args, **kwargs):
    """
    Maya can reference and use external files, such as textures or other Maya scenes. This command is used to get the
    information about those file paths and modify them in bulk. By default, only the most frequently used types of files are
    presented to the user:  TextureScene referenceAudioImage planeFor the command to manage more file types, those must be
    explicitly requested by the caller using the registerTypeflag. This flag tells the command about attributes or nodes
    that are to reveal their paths when the command is used.  Currently, the attributes specified through this flag must
    have the usedAsFileNameproperty. Supported nodes are referenceand plug-in nodes. For example: brush.flowerImageor
    referencecan be used as value for this flag.  Conversely, the deregisterTypeflag can be used to tell the command to stop
    handling certain attributes or nodes.  Once the set of attributes and nodes to be searched for external files is
    selected, the command can be used to obtain a list of plugs that contain file names. Additional information can be
    obtained, such as each file's name, directory, and report whether the file exists. Additional information about the
    associated node or plug can also be obtained, such as its name, type and label.  Finally, the command can be used to
    perform various manipulations such as editing the paths, remapping the files or verifying the presence of identically-
    named files in target directories. See the repath, copyAndRepathand replaceFieldflags for more information.  The results
    of these manipulations can be previewed before they are applied using the previewflag.                In query mode,
    return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attributeType`` / ``at``                                                                           | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the attribute type for the specified plug.                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``copyAndRepath`` / ``cr``                                                                           | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Copy a source file to the destination path and repath the plug data to the new file. The source file must have the same name as the one in the plug. The command  |
    |  | will look for the file at the specified location first. If not found, the command will try to use the original file in the plug. If the file is still not found,  |
    |  | nothing is done.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deregisterType`` / ``dt``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Deregister a file type from the list of registered types so the command stops handling it. Unless the temporaryflag is used, the type will be removed from the    |
    |  | preferences will not reappear on application restart. When the temporaryflag is specified, the deregistration is only effective for the current session. The      |
    |  | deregistration will be rejected if the type has already been unregistered. However, it is valid to deregister permanently (without the temporaryflag) a type after|
    |  | it has been temporarily deregistered.                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``force`` / ``f``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with flag repathto repath all files to the new location, including the resolved files. Otherwise, repathwill only deal with the missing files. Used with flag|
    |  | copyAndRepathto overwrite any colliding file at the destination. Otherwise, copyAndRepathwill use the existing file at the destination instead of overwriting it. |
    |  | The default value is off.                                    Flag can have multiple arguments, passed either as a tuple or a list.                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listDirectories`` / ``ld``                                                                         | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List all sub directories of the specified directory.  Only directories containing at least one file whose type is registered (see registerType) will be listed. If|
    |  | no directory is provided, all directories applicable to the scene will be returned.                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listFiles`` / ``lf``                                                                               | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List files in the specified directory. No recursion in subdirectories will be performed.                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listRegisteredTypes`` / ``lrt``                                                                    | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query the list of registered attribute types. The registered types include the auto-loaded types from the preference file and the types explicitly registered by  |
    |  | the user, both with and without the temporaryflag.                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``preview`` / ``p``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with repath, replaceStringor copyAndRepathto preview the result of the operation instead of excuting it. When it is used with repathor replaceString, the    |
    |  | command returns the new file path and a status flag indicating whether the new file exists (1) or not (0). The path name and the file status are listed in pairs. |
    |  | When it is used with copyAndRepath, the command returns the files which need copying.                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``recursive`` / ``rc``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with flag repathto search the files in the target directory and its subdirectories recursively. If the flag is on, the command will repath the plug to a file|
    |  | that has the same name in the target directory or sub directories. If the flag is off, the command will apply the directory change without verifying that the     |
    |  | resulting file exists.                                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``refresh`` / ``rf``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Clear and re-collect the file information in the scene. The command does not automatically track file path modifications in the scene. So it is the users         |
    |  | responsibility to cause refreshes in order to get up-to-date information.                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``registerType`` / ``rt``                                                                            | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Register a new file type that the command will handle and recognize from now on. Unless the temporaryflag is used, the registered type is saved in the preferences|
    |  | and reappears on application restart. The new type will be rejected if it collides with an existing type or label. One exception to this is when registering a    |
    |  | type without the temporaryflag after the type has been registered with it. This is considered as modifying the persistent/temporary property of the existing type,|
    |  | rather than registering a new type.                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``relativeNames`` / ``rel``                                                                          | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with listDirectoriesor listFilesto return the relative path of each directory or file.  Paths are relative to the current project folder. If a file or the   |
    |  | directory is not under the current project folder, the returned path will still be a full path.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``repath`` / ``r``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Replace the directory part of a file path with a specified location. The file name will be preserved.                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``replaceAll`` / ``ra``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with flag replaceString, specifies how many times the matched string will be replaced. When the flag is false, only the first matched string will be         |
    |  | replaced. Otherwise, all matched strings will be replaced. The default value is false.                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``replaceField`` / ``rfd``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with the replaceStringflag to control the scope of the replacement. Possible values are: pathOnly- only replace strings in the directory part. nameOnly- only|
    |  | replace strings in the file name, without the directory. fullPath- replace strings anywhere in the full name. The default argument is fullPath.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``replaceString`` / ``rs``                                                                           | *unicode, unicode*            | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Replace the target string with the new string in the file paths. The flag needs two arguments: the first one is the target string and the second one is the new   |
    |  | string. See the replaceFieldand replaceAllflags to control how the replacement is performed.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``status`` / ``s``                                                                                   | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with listFiles, this will cause the returned list of files to include one status flag per file: 0 if it cannot be resolved and 1 if it can. Used with        |
    |  | listDirectories, this will cause the returned list of directories to include one status flag per directory: 0 if it cannot be resolved, 1 if it can and 2 if the  |
    |  | resolution is partial. The status will be interleaved with the file/directory names, with the name appearing first. See the example for listFiles.  See the       |
    |  | withAttributeflag for another way of getting per-file information.  When multiple per-entry items appear in the list (e.g.: plug name), the status is always last.|
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``temporary`` / ``tmp``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Make the effect of the register/deregisterflag only applicable in the current session. Normally, a type registration/deregistration is permanent and is made      |
    |  | persistent via a preference file. When the temporaryflag is specified, the changes will not be saved to the preference file. When the application restarts, any   |
    |  | type that has been previously temporarily registered will not appear and any type that was temporarily deregistered will re-appear.                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``typeLabel`` / ``tl``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with registerTypeto set the label name for the new file type. Used with queryto return the type label for the specified attribute type. For default types,   |
    |  | the type label is the localized string. For other types, the type label is supplied by user.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``withAttribute`` / ``wa``                                                                           | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with listFilesto return the name of the plug using a given file. For example, if file.jpgis used by the plug node1.fileTextureName, then the returned string |
    |  | will become the pair file.jpg node1.fileTextureName.  See the statusflag for another way to get per-file information.                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.filePathEditor`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #Return the directories of the external files in Maya scene.
        #
        pm.filePathEditor(query=True, listDirectories="")
        #Return the directories of the external files which are
        #saved at the target location.
        #
        pm.filePathEditor(query=True, listDirectories="c:/textures/", status=True)
        #Return the files which are saved in the specified directory,
        #but not including the files in the sub directories.
        #Use "withAttribute" to return the associated plug
        #which is using the file.
        #Use "status" to return the information that if the files
        #exist or not.
        #For example, if "stone.jpg" exists and it is used by
        #the plug "node1.imageName", then the returned result
        #will be an ordered pair: "stone.jpg node1.imageName 1".
        #
        pm.filePathEditor(query=True, listFiles="c:/textures/", withAttribute=True, status=True)
        #Return the label of the specified type.
        #For default types, they are localized strings.
        #For other types, they are defined by user.
        #
        pm.filePathEditor(query=True, typeLabel="imagePlane")
        # Result: u'' #
        #Register and save a new file type and type label.
        #Then user can use it next time they open maya
        #
        pm.filePathEditor(registerType="containerBase.iconName", registerLabel="ContainerIcon")
        #Deregister the file type and clean the saved information
        #
        pm.filePathEditor(deregisterType="containerBase.iconName")
        #Register a new file type and type label without saving
        #
        pm.filePathEditor(registerType="containerBase.iconName", registerLabel="ContainerIcon", temporary=True)
        #Deregister the file type but do nothing on the saved information
        #
        pm.filePathEditor(deregisterType="containerBase.iconName", temporary=True)
        #Return all registered types, including default types
        #
        pm.filePathEditor(query=True, listRegisteredTypes=True)
        #Query the attribute type of the plug instance
        #
        pm.filePathEditor("node1.fileTextureName", query=True, attributeType=True)
        #Refresh all file information in the scene
        #
        pm.filePathEditor(refresh=True)
        #Recursively look for the files with the same name in
        #the target directory. Repath the plug values to those files.
        #Use "force" to edit all given plugs no matter if
        #their original paths exist or not.
        #Use "recursive" to find files recursively and to make
        #sure the files must exist.
        #
        pm.filePathEditor("node1.fileTextureName", "node2.fileTextureName", repath="e:/textures/",
                                                        force=True, recursive=True)
        #Preview the result of edit, but not to do the replacement.
        #Return the file name and the information that if the new file path
        #exists. They are listed in pairs.
        #
        pm.filePathEditor("node1.fileTextureName", "node2.fileTextureName", repath="e:/textures/", preview=True)
        #Replace strings in file path of the plugs.
        #Here, only the string "image" in the directory part
        #will be replaced by "texture".
        #
        pm.filePathEditor("node1.fileTextureName", "node2.fileTextureName", replaceField="pathOnly", replaceString=("image", "texture"), replaceAll=True)
        #Copy a file from the source to the destination and repath the plug data to the new file.
        #Use "force" to overwrite the file at the destination, if it has a name clash.
        #
        pm.filePathEditor("node1.fileTextureName", "node2.fileTextureName",  copyAndRepath=("e:/textures", "g:/image"), force=True)
    """

    pass


def listInputDeviceAxes(*args, **kwargs):
    """
    This command lists all of the axes of the specified input device.
    
    
    Derived from mel command `maya.cmds.listInputDeviceAxes`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Returns a list of the axes of the spaceball.
        pm.listInputDeviceAxes( 'spaceball' )
    """

    pass


def cacheFile(*args, **kwargs):
    """
    Creates one or more cache files on disk to store attribute data for a span of frames. The caches can be created for
    points/normals on a geometry (using the pts/points or pan/pointsAndNormals flag), for vectorArray output data (using the
    oa/outAttr flag), or for additional node specific data (using the cnd/cacheableNode flag for those nodes that support
    it). When the ia/inAttr flag is used, connects a cacheFile node that associates the data file on disk with the
    attribute. Frames can be replaced/appended to an existing cache with the rcf/replaceCachedFrame and apf/appendFrame
    flag.  Replaced frames are never deleted. They are stored in the same directory as the original cache files with the
    name provided by the f/fileName flag. If no file name is provided, the cacheFile name is prefixed with backupfollowed by
    a unique number. Single file caches are backed up in their entirety. To revert to an older version, simply attach to
    this cache. One file per frame caches only backup the description file and the frames that were replaced. To recover
    these types of caches, the user must rename these files to the original name.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``appendFrame`` / ``apf``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Appends data to the cache for the times specified by the startTime and endTime flags. If no time is provided, appends the current time. Must be used in           |
    |  | conjunction with the pts/points or cnd/cacheableNode flag. Any overwritten frames will not be deleted, but renamed as specified by the f/fileName flag.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``attachFile`` / ``af``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used to indicate that rather than creating a cache file, that an existing cache file on disk should be attached to an attribute in the scene. The inAttr flag is  |
    |  | used to specify the attribute.                                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cacheFileNode`` / ``cfn``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of the cache file node(s) we are appending/replacing to if more than one cache is attached to the specified geometries.                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cacheFormat`` / ``cf``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Cache file format, default is Maya's .mcx format, but others available via plugin                                         Flag can have multiple arguments, passed|
    |  | either as a tuple or a list.                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cacheInfo`` / ``ci``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | In create mode, used to specify a mel script returning a string array. When creating the cache, this mel script will be executed and the returned strings will be |
    |  | written to the .xml description file of the cache. In query mode, returns descriptive info stored in the cacheFile such as the user name, Maya scene name and maya|
    |  | version number.                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cacheableAttrs`` / ``cat``                                                                         | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the list of cacheable attributes defined on the accompanying cache node. This argument requires the use of the cacheableNode flag.                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cacheableNode`` / ``cnd``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a cacheable node whose contents will be cached. A cacheable node is a node that is specially designed to work with the caching mechanism.   |
    |  | An example of a cacheable node is a nCloth node.                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``channelIndex`` / ``chi``                                                                           | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A query-only flag which returns the channel index for the selected geometry for the cacheFile node specified using the cacheFileNode flag.                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``channelName`` / ``cnm``                                                                            | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When attachFile is used, used to indicate the channel in the file that should be attached to inAttr.  If not specified, the first channel in the file is used. In |
    |  | query mode, allows user to query the channels associated with a description file.                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``convertPc2`` / ``pc2``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Convert a PC2 file to the Maya cache format (true), or convert Maya cache to pc2 format (false)                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``createCacheNode`` / ``ccn``                                                                        | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used to indicate that rather than creating a cache file, that a cacheFile node should be created related to an existing cache file on disk.                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``creationChannelName`` / ``cch``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When creating a new cache, this multi-use flag specifies the channels to be cached. The names come from the cacheable channel names defined by the object being   |
    |  | cached. If this flag is not used when creating a cache, then all cacheable channels are cached.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dataSize`` / ``dsz``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a query-only flag that returns the size of the data being cached per frame. This flag is to be used in conjunction with the cacheableNode, points,        |
    |  | pointsAndNormals and outAttr flags.                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deleteCachedFrame`` / ``dcf``                                                                      | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Deletes cached data for the times specified by the startTime/endTime flags. If no time is provided, deletes the current frame. Must be used in conjunction with   |
    |  | the pts/points or cnd/cacheableNode flag. Deleted frames will not be removed from disk, but renamed as specified by the f/fileName flag.                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``descriptionFileName`` / ``dfn``                                                                    | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is a query-only flag that returns the name of the description file for an existing cacheFile node. Or if no cacheFile node is specified, it returns the      |
    |  | description file name that would be created based on the other flags specified.                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directory`` / ``dir``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the directory where the cache files will be located. If the directory flag is not specified, the cache files will be placed in the project data         |
    |  | directory.                                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``doubleToFloat`` / ``dtf``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | During cache creation, double data is stored in the file as floats.  This helps cut down file size.                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``endTime`` / ``et``                                                                                 | *time*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the end frame of the cache range.                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fileName`` / ``f``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the base file name for the cache files. If more than one object is being cached and the format is OneFilePerFrame, each cache file will be prefixed with|
    |  | this base file name. In query mode, returns the files associated with the specified cacheFile node. When used with rpf/replaceCachedFrame or apf/appendFrame      |
    |  | specifies the name of the backup files. If not specified, replaced frames will be stored with a default name. In query mode, this flag can accept a value.        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``format`` / ``fm``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the distribution format of the cache.  Valid values are OneFileand OneFilePerFrame                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``geometry`` / ``gm``                                                                                | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A query flag which returns the geometry controlled by the specified cache node                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``inAttr`` / ``ia``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of the attribute that the cache file will drive. This file is optional when creating cache files. If this flag is not used during create mode, |
    |  | the cache files will be created on disk, but will not be driving anything in the scene. This flag is required when the attachFile flag is used.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``inTangent`` / ``it``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the in-tangent type when interpolating frames before the replaced frame(s). Must be used with the ist/interpStartTime and iet/interpEndTime flags. Valid|
    |  | values are linear, smoothand step.                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``interpEndTime`` / ``iet``                                                                          | *time*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the frame until which there will be linear interpolation, beginning at endTime. Must be used with the rpf/replaceCachedFrame or apf/appendFrame flag.   |
    |  | Interpolation is achieved by removing frames between endTime and interpEndTime from the cache. Removed frames will be renamed as specified by the f/fileName flag.|
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``interpStartTime`` / ``ist``                                                                        | *time*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the frame from which to begin linear interpolation, ending at startTime. Must be used with the rpf/replaceCachedFrame or apf/appendFrame flags.         |
    |  | Interpolation is achieved by removing  frames between interpStartTime and startTime from the cache. These removed frames will will be renamed as specified by the |
    |  | f/fileName flag.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``noBackup`` / ``nb``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies that backup files should not be created for any files that may be over-written during append, replace or delete cache frames. Can only be used with the |
    |  | apf/appendFrame, rpf/replaceCachedFrame or dcf/deleteCachedFrame flags.                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``outAttr`` / ``oa``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of the attribute that will be cached to disk.                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``outTangent`` / ``ot``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the out-tangent type when interpolating frames after the replaced frame(s). Must be used with the ist/interpStartTime and iet/interpEndTime flags. Valid|
    |  | values are linear, smoothand step.                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pc2File`` / ``pcf``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the full path to the pc2 file.  Must be used in conjunction with the pc2 flag.                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pointCount`` / ``pc``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | A query flag which returns the number of points stored in the cache file. The channelName flag should be used to specify the channel to be queried.               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``points`` / ``pts``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a geometry whose points will be cached.                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pointsAndNormals`` / ``pan``                                                                       | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a geometry whose points and normals will be cached. The normals is per-vertex per-polygon. The normals cache cannot be imported back to     |
    |  | geometry. This flag can only be used to export cache file. It cannot be used with the apf/appendFrame, dcf/deleteCachedFrame and rpf/replaceCachedFrame flags.    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``prefix`` / ``p``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Indicates that the specified fileName should be used as a prefix for the cacheName.                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``refresh`` / ``r``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When used during cache creation, forces a screen refresh during caching. This causes the cache creation to be slower but allows you to see how the simulation is  |
    |  | progressing during the cache.                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``replaceCachedFrame`` / ``rcf``                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Replaces cached data for the times specified by the startTime/endTime flags. If no time is provided, replaces cache file for the current time. Must be used in    |
    |  | conjunction with the pts/points or cnd/cacheableNode flag. Replaced frames will not be deleted, but renamed as specified by the f/fileName flag.                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``replaceWithoutSimulating`` / ``rws``                                                               | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When replacing cached frames, this flag specifies whether the replacement should come from the cached node without simulating or from advancing time and letting  |
    |  | the simulation run.  This flag is valid only when neither the startTime nor endTime flags are used or when both the startTime and endTime flags specify the same  |
    |  | time value.                                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``runupFrames`` / ``rf``                                                                             | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the number of frames of runup to simulate ahead of the starting frame. The value must be greater than or equal to 0.  The default is 2.                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``sampleMultiplier`` / ``spm``                                                                       | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the sample rate when caches are being created as a multiple of simulation Rate. If the value is 1, then a sample will be cached everytime the time is   |
    |  | advanced.  If the value is 2, then every other sample will be cached, and so on.  The default is 1.                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``simulationRate`` / ``smr``                                                                         | *time*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the simulation rate when caches are being created.  During cache creation, the time will be advanced by the simulation rate, until the end time of the  |
    |  | cache is reached or surpassed.  The value is given in frames. The default value is 1 frame.                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``singleCache`` / ``sch``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When used in conjunction with the points, pointsAndNormal or cacheableNode flag, specifies whether multiple geometries should be put into a single cache or to    |
    |  | create one cache per geometry (default).                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``startTime`` / ``st``                                                                               | *time*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the start frame of the cache range.                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``staticCache`` / ``sc``                                                                             | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If false, during cache creation, do not save a cache for the object if it appears to have no animation or deformation. If true, save a cache even if the object   |
    |  | appears to have no animation or deformation. Default is true. In query mode, when supplied a shape, the flag returns true if the shape appears to have no         |
    |  | animation or deformation.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``worldSpace`` / ``ws``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If the points flag is used, turning on this flag will result in the world space positions of the points being written. The expected use of this flag is for cache |
    |  | export.                                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.cacheFile`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Create a disk cache containing the points of a plane from
        # frames 1 - 100. Typically the shape would be deforming.
        #
        pm.polyPlane()
        # Result: [nt.Transform(u'pPlane1'), nt.PolyPlane(u'polyPlane1')] #
        cacheFiles = pm.cacheFile(f='shapeCache', st=1, et=100, points='pPlaneShape1')
        # Add a historySwitch node to the history of the shape, and attach the
        # newly created cache into the historySwitch node.
        #
        switch = maya.mel.eval('createHistorySwitch("pPlaneShape1",false)')
        cacheNode = pm.cacheFile(f=cacheFiles[0], cnm='pPlaneShape1', ia='%s.inp[0]' % switch ,attachFile=True)
        pm.setAttr( '%s.playFromCache' % switch, 1 )
        # query the files associated with a cacheFile node
        #
        pm.cacheFile( cacheNode, query=True, f=True )
        # Now use the staticCache flag to indicate that the cache should not be
        # created if the object appears to have no animation.
        # Since the plane is not animated or deformed, no cache will be created.
        #
        pm.polyPlane()
        cacheFiles = pm.cacheFile(f='shapeCache', staticCache=0, st=1, et=100, points='pPlaneShape2')
        # Convert a maya cache into pc2 format. The maya cache is named
        # pSphereShape1.xml and located in the directory "c:/test/".
        #
        pm.cacheFile(pc2=0,pcf='c:/test/mypc2.pc2',f='pSphereShape1',dir='c:/test/')
        # Convert a pc2 cache into a maya cache, with the cache data in a single
        # file.
        #
        pm.cacheFile(pc2=1,pcf='c:/test/mypc2.pc2',f='mayaCache2',dir='c:/test/',format='OneFile')
    """

    pass


def openMayaPref(*args, **kwargs):
    """
    Set or query API preferences.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``errlog`` / ``el``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | toggles whether or not an error log of failed API method calls will be created.  When set to true, a file called OpenMayaErrorLogwill be created in Maya's current|
    |  | working directory.  Each time an API method fails, a detailed description of the error will be written to the file along with a mini-stack trace that indicates   |
    |  | the routine that called the failing method. Defaults to false(off).                    Flag can have multiple arguments, passed either as a tuple or a list.      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lazyLoad`` / ``lz``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | toggles whether or not plugins will be loaded with the RTLD_NOW flag or the RTLD_LAZY flag of dlopen(3C).  If set to true, RTLD_LAZY will be used.  In this mode  |
    |  | references to functions that cannot be resolved at load time will not be considered an error.  However, if one of these symbols is actually dereferenced by the   |
    |  | plug-in at run time, Maya will crash. Defaults to false(off).                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``oldPluginWarning`` / ``ow``                                                                        | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | toggles whether or not loadPlugin will generate a warning when plug-ins are loaded that were compiled against an older, and possibly incompatible Maya release.   |
    |  | Defaults to true(on).                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.openMayaPref`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Enable RTLD_LAZY binding when loading plug-ins
        pm.openMayaPref( lz=True )
        
        # Force RTLD_NOW binding when loading plug-ins
        pm.openMayaPref( lz=False )
        
        # Disable the warning about old plug-ins being loaded
        pm.openMayaPref( ow=False )
        
        # Turn on the Error log
        pm.openMayaPref( errlog=True )
        
        # Query the Error log
        pm.openMayaPref( q=True, errlog=True )
        # Result: [True] #
        
        # Turn off the Error log
        pm.openMayaPref( errlog=False )
    """

    pass


def unassignInputDevice(*args, **kwargs):
    """
    This command deletes all command strings associated with this device. In query mode, return type is based on queried
    flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``clutch`` / ``c``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only delete command attachments with this clutch.                         Flag can have multiple arguments, passed either as a tuple or a list.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``device`` / ``d``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the device to work on.                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.unassignInputDevice`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # This deletes all command strings associated with the spaceball.
        pm.unassignInputDevice( d='spaceball' )
    """

    pass


def newFile(*args, **kwargs):
    """
    Initialize the scene. Returns untitled scene with default location.                       
    
    Flags:
      - force:
          Force an action to take place. (new, open, save, remove reference, unload reference) Used with removeReference to force
          remove reference namespace even if it has contents. Cannot be used with removeReference if the reference resides in the
          root namespace. Used with unloadReference to force unload reference even if the reference node is locked, without
          prompting a dialog that warns user about the lost of edits.
      - type:
          Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in,
          audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of
          file types that match this file.
    
    Derived from mel command `maya.cmds.file`
    """

    pass


def displayError(*args, **kwargs):
    pass


def hardware(*args, **kwargs):
    """
    Return description of the hardware available in the machine.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``brdType`` / ``brd``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns IP number identifying the CPU motherboard                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cpuType`` / ``cpu``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns type of CPU                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``graphicsType`` / ``gfx``                                                                           | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns string identifying graphics hardware type                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``megaHertz`` / ``mhz``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns string identifying the speed of the CPU chip                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``numProcessors`` / ``npr``                                                                          | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns string identifying the number of processors                       Flag can have multiple arguments, passed either as a tuple or a list.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.hardware`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.hardware( cpu=True )
        # Result: [u'Quad-Core Intel Xeon Processor'] #
        pm.hardware( brd=True )
        # Result: [u'Intel Macintosh'] #
    """

    pass



workspace = Workspace()

_logger = None

_pymel_options = {}

fileInfo = FileInfo()


