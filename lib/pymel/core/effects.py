import pymel.internal.factories as _factories
from . import general as _general

def air(*args, **kwargs):
    """
    The air field simulates the effects of moving air. The affected objects will be accelerated or decelerated so that their
    velocities match that of the air. With the '-vco true' flag thrown, only accelerations are applied. By parenting an air
    field to a moving part of an object (ie. a foot of a character) and using '-i 1 -m 0 -s .5 -vco true' flags, one can
    simulate the movement of air around the foot as it moves, since the TOTAL velocity vector of the field would be only
    based on the movement of the foot. This can be done while the character walks through leaves or dust on the ground. For
    each listed object, the command creates a new field. The transform is the associated dependency node. Use connectDynamic
    to cause the field to affect a dynamic object. If fields are created,  this command returns the field names. If a field
    was queried, the results of the query are returned. If a field was edited, the field name is returned. If the -pos flag
    is specified, a field is created at the position specified. If not, if object names are provided or the active selection
    list is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the
    object; otherwise the command defaults to -pos 0 0 0. Setting the -pos flag with objects named on the command line is an
    error.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attenuation`` / ``att``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attentuation rate of field The air field attenuates so as to taper the field's magnitude to zero when the maximum distance is reached. Thus, attenuation has no   |
    |  | effect unless useMaxDistance is true and a positive maximum distance has been set.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionX`` / ``dx``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionY`` / ``dy``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionZ`` / ``dz``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Direction that the air will try to match the affected particles' velocity to. NOTE: This is not the velocity; this is only the direction. Use the -s flag to set  |
    |  | the speed.                                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``enableSpread`` / ``es``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This tells the system whether or not to use the spread angle given by '-sp'. If this is 'false' then all connected objectswithin the maximum distance will be     |
    |  | affected. Also, if this is set to 'false', all affected objects are forced to match their velocities along the direction vector. If this is set to 'true' and     |
    |  | spread is used, then the direction of the force is along the direction from the field to the object.                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fanSetup`` / ``fs``                                                                                | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Similar to 'windSetup' except that the effects of a fan or a person blowing air are approximated. The user can pass the same flags on the command line to adjust  |
    |  | them from the defaults. These are the values that get set to approximate a 'fan': inheritVelocity 1.0 inheritRotation true componentOnly false enableSpread true  |
    |  | spread .5 (45 degrees from center )                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``inheritRotation`` / ``iro``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this is set to 'true', then the direction vector described with -dx, -dy, and -dz will be considered local to the owning object. Therefore, if the owning      |
    |  | object's transform undergoes any rotation (by itself or one of its parents), the direction vector of the air field will undergo that same rotation.               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``inheritVelocity`` / ``iv``                                                                         | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Amount (from 0 to 1) of the field-owner's velocity added to the vector determined by the direction and speed flags. The combination of these two vectors makes up |
    |  | the TOTAL velocity vector for the air field. This allows the air to be determined directly by the motion of the owning object.                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``magnitude`` / ``m``                                                                                | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The speed along the direction vector that the air is moving. Use this in conjunction with the -dx -dy -dz flags.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of field                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perVertex`` / ``pv``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the     |
    |  | force field. If this flag is set to false, then the force is exerted only from the geometric center of the set of points.                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Position in space where you want to place a field. The field then emanates from this position in space rather than from an object. Note that you can both use -pos|
    |  | (creating a field at a position) and also provide object names.                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``speed`` / ``s``                                                                                    | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | How fast the affected objects' speed reaches the speed (based on the -mag, -dx, -dy, -dz flags) of the air field. This value gets clamped internally to be between|
    |  | 0.0 and 1.0.  A value of 0.0 will make the air field have no effect. A value of 1.0 will try to match the air field's speed much quicker, but not necessarily     |
    |  | immediately.                                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``spread`` / ``sp``                                                                                  | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This represents the angle from the direction vector within which objects will be affected. The values are in the range of 0 to 1. A value of 0 will result in an  |
    |  | effect only exactly in front of the air field along the direction vector. A value of 1 will result in any object in front of the owning object, 90 degrees in all |
    |  | direction from the direction vector.                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``velocityComponentOnly`` / ``vco``                                                                  | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this is 'false', the air will accelerate or decelerate the affected objects so that their velocities will eventually match the TOTAL velocity vector of the air|
    |  | field. If this is 'true', only ACCELERTION is applied to the affected objects so that their velocity component along the TOTAL velocity vector matches or is      |
    |  | greater in magnitude than the TOTAL velocity vector. This will not slow objects down to match velocities, only speed them up to match components. This is most    |
    |  | useful when using the -iv flag with a value 0.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeExclusion`` / ``vex``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``wakeSetup`` / ``wks``                                                                              | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Like the 'windSetup' and 'fanSetup', 'wakeSetup' sets certain values in the field to approximate the movement of air near a moving object, such as  a character's |
    |  | foot or hand. The values that are set are: inheritVelocity 1.0 inheritRotation false componentOnly true enableSpread false speed 0.0                    Flag can  |
    |  | have multiple arguments, passed either as a tuple or a list.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``windSetup`` / ``wns``                                                                              | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This will set some of the values above in a way that approximates the effects of a basic wind. This allows the user to then change certain values as he/she wishes|
    |  | on the same command line. First the preset values get set, and then any other flags that were passed get taken into account. These are the values that get set to |
    |  | approximate 'wind': inheritVelocity 0.0 inheritRotation true componentOnly false enableSpread false                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.air`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.air( name='particle1', m=5.0, mxd=2.0 )
        # Result: nt.AirField(u'particle1') #
        # Creates an air field with magnitude 5.0 and maximum distance 2.0,
        # and adds it to the list
        # of fields particle1 owns.
        
        pm.air( wakeSetup=True )
        # Creates an air field with no no velocity in and of itself (magnitude = 0).
        # All of the air's
        # velocity is derived from the motion of the objects that own the field.
    """

    pass


def dynCache(*args, **kwargs):
    """
    Cache the current state of all particle shapes at the current time.
    
    
    Derived from mel command `maya.cmds.dynCache`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Create an emitter and connect it to a particle shape
        pm.emitter(typ='omni', pos=(1, 1, 1), n='myEmitter')
        pm.particle(n='myParticles')
        pm.connectDynamic('myParticles', em='myEmitter')
        
        # Cache all attributes of the particle shape at time 50
        pm.playbackOptions(min=0, max=50, ast=0, aet=100)
        pm.currentTime('0');
        pm.play(w=True)
        pm.dynCache()
    """

    pass


def saveInitialState(*args, **kwargs):
    """
    saveInitialState saves the current state of dynamics objects as the initial state.  A dynamic object is a particle
    shape, rigid body, rigid constraint or rigid solver.  If no objects are specified, it saves the initial state for any
    selected objects. It returns the names of the objects for which initial state was saved.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``atr``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Save the initial state of the specified attribute only. This is a multi-use flag.                         Flag can have multiple arguments, passed either as a    |
    |  | tuple or a list.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``saveall`` / ``all``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Save the initial state for all dynamics objects in the scene.                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.saveInitialState`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.saveInitialState( 'particle1' )
        # Saves current state as initial state for particle1.
        
        pm.saveInitialState( all=True )
        # Saves current state as initial state for all dynamics objects.
    """

    pass


def setParticleAttr(*args, **kwargs):
    """
    This action will set the value of the chosen attribute for every particle or selected component in the selected or
    passed particle object. Components should not be passed to the command line. For setting the values of components, the
    components must be selected and only the particle object's names should be passed to this action. If the attribute is a
    vector attribute and the -vv flag is passed, then the three floats passed will be used to set the values.  If the
    attribute is a vector and the -fv flag is pass and the -vv flag is not passed, then the float will be repeated for each
    of the X, Y, and Z values of the attribute.  Similarly, if the attribute is a float attribute and a vector value is
    passed, then the length of the vector passed will be used for the value. Note:  The attribute passed must be a Per-
    Particle attribute.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells the action which attribute you want to set                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``floatValue`` / ``fv``                                                                              | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells what you want the value to be set to of a float attribute                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``object`` / ``o``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this flag is passed and the STRING is the name of a particle object's transform or shape, then ONLY that object will be edited, ignoring the selection list or |
    |  | command line, and ALL of its particles' values will be changed for the specified attribute.                     Flag can have multiple arguments, passed either as|
    |  | a tuple or a list.                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``randomFloat`` / ``rf``                                                                             | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells the command to add a random value from -FLOAT to +FLOAT to the results of each particle.  The default is 0.0.                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``randomVector`` / ``rv``                                                                            | *float, float, float*         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells the command to add a random value from -x,-y,-zto x,y,zto the results of each particle. The default 0 0 0.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``relative`` / ``r``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this is set to TRUE (the default is FALSE), then the float or vector value will be added to the current value for each particle.                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``vectorValue`` / ``vv``                                                                             | *float, float, float*         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells what you want the value to be set to of a vector attribute                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.setParticleAttr`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.setParticleAttr( 'particle1', at='velocity', vv=(1, 2, 3) )
        # This will set the velocity of all of the particles in particle1
        # to "" 1, 2, 3 "".
        
        pm.select( 'particleShape1.pt[0:7]', 'particleShape1.pt[11]' )
        pm.setParticleAttr( vv=(1, 2, 3), at='velocity' )
        pm.setParticleAttr( 'particleShape1', at='velocity' )
        
        # This will set the velocity of particles 0-7 and 11 of
        # particleShape1 to "" 1, 2, 3 "".  The rest of the particles are
        # not changed.
    """

    pass


def pfxstrokes(*args, **kwargs):
    """
    This command will loop through all the Paint Effects strokes, including pfxHair nodes, and write the current state of
    all the tubes to a file. For normal stroke nodes tubes must be ON in the brush or there will be no output. For pfxHair
    nodes there will always be output, but the format is different than for stroke nodes(however one can assign a brush with
    tubes = ON to a pfxHair node, in which case it will output the same format as strokes). The general file format is
    ASCII, using commas to separate numerical values and newlines between blocks of data. The format used for pfxHair nodes
    presents the hair curves points in order from root to tip of the hair. The hairs follow sequentially in the following
    fashion: NumCvs pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU pointX,pointY,pointZ,
    normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU etc... NumCvs pointX,pointY,pointZ,
    normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU etc.. The format used to output files for brushes with
    tubes=ON is more complex. The tubes can branch and the order the segments are written is the same order they are drawn
    in. Slowly drawing a tall grass brush in the paint effects panel can help to illustrate the order the segments will
    appear in the file. New tubes can start growingbefore others are finished. There is no line for NumCvs. Instead all data
    for each segment appears on each line. The data on each line is the same as passed into the paint effects runtime
    function. See the argument list of paintRuntimeFunc.mel for the order and a description of these parameters. The
    parameters match up exactly in the order they appear on a line of the output file with the order of arguments to this
    function. If one wishes to parse the output file and connect the segments together into curves the branchId, parentId
    and siblingCnt parameters can help when sorting which segment connects to which line. Using the -postCallback option
    will write out the tubes data after it has been proessed by the runTime callback.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``filename`` / ``fn``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The output file.                                          Flag can have multiple arguments, passed either as a tuple or a list.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``postCallback`` / ``pc``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Output information to the file after the Runtime Callback MEL function has been invoked. The default is to output the information prior to the callback.          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selected`` / ``sl``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only loop through the selected strokes.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.pfxstrokes`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.pfxstrokes( fn='/tmp/output_file' )
    """

    pass


def truncateHairCache(*args, **kwargs):
    """
    This command sets the end time of a hair cache to the current time. If the current time is less than the end time of the
    cache, the cache is truncated so that only the portion of the cache up to and including the current time is preserved.
    In query mode, return type is based on queried flag.
    
    
    Derived from mel command `maya.cmds.truncateHairCache`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Truncate a hair cache that has a start time of 1
        # and an end time of 25 so that only the first 10
        # frames are preserved and the end time of the
        # cache is set to 10.
        #
        pm.currentTime( 10 )
        # Result: 10.0 #
        pm.truncateHairCache()
    """

    pass


def particleExists(*args, **kwargs):
    """
    This command is used to query if a particle or soft object with the given name exists. Either the transform or shape
    name can be used as well as the name of the soft object.
    
    
    Derived from mel command `maya.cmds.particleExists`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # If the object does not exist then false (0) is returned
        pm.file( f=True, new=True )
        pm.particleExists( 'particleShape1' )
        0
        
        # Create a particle shape and then querying for
        # it will return true (1)
        pm.emitter()
        emitter1
        pm.particle()
        particle1 particleShape1
        pm.connectDynamic( 'particle1', em='emitter1' )
        particleShape1
        pm.particleExists( 'particleShape1' )
        1
        
        # You may also query using the transform name
        pm.particleExists( 'particle1' )
        1
        
        # The name of a soft body object can be used to query as well
        pm.polySphere( r=1, sx=20, sy=20, ax=(0, 1, 0), tx=2, ch=1 )
        pSphere1 polySphere1
        pm.soft( c=True )
        pSphere1Particle
        pm.particleExists( 'pSphere1Particle' )
        1
    """

    pass


def spring(*args, **kwargs):
    """
    The spring command can do any of the following:\* create a new spring object (shape plus transform).  The shape contains
    springs between the points (particles, cvs, etc.) of the objects selected or listed on the command line.\* create new
    springs and add them to an existing spring object\* edit or query certain attributes of an existing spring objectOne
    spring objectmay have hundreds or even thousands of individual springs. Certain attributes of the spring object specify
    exactly where the springs are attached to which other objects.Springs may be attached to the following: particles,
    vertices of soft bodies, CVs or edit points of curves or surfaces, vertices of polygonal objects, and points of
    lattices. In the case where one endpoint of a spring is non-dynamic (a CV, edit point, etc.), the spring does not affect
    its motion, but the motion of the point affects the spring. A spring will be created only if at least one of the
    endpoints is dynamic: for example, a spring will never be created between two CVs. A single spring object can hold
    springs which are incident to any number of other objects.The spring has creation-only flags and editable flags.
    Creation-only flags (minDistance, maxDistance, add, exclusive, all, wireframe, walklength, checkExisting) can be used
    only when creating new springs (including adding springs to existing spring object).  Editable flags modify attributes
    of an existing spring object.If a spring object is created, this command returns the names of the shape and transform.
    If a spring object is queried, the command returns the results of the query.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``addSprings`` / ``add``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If specified, springs will be added to the existing selected set of springs. (Default is to create a new spring object.)                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``allPoints`` / ``all``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If True, sets the mode of spring application to All.  This will add springs between all points selected. (Default is False.)                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``count`` / ``ct``                                                                                   | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the number of springs in the shape.  Query-only. We maintain this flag only for compatibility with earlier versions of Maya.  To get the count of springs, |
    |  | it is much faster and simpler to use the spring shape's count attribute: getAttr shapeName.count.                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``damp`` / ``dmp``                                                                                   | *float*                       |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``damping`` / ``d``                                                                                  | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Damping factor for the springs created in the spring object. (Default = 0.2 )                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dampingPS`` / ``dPS``                                                                              | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Damping factor for the springs created in the spring object. This will initialize all the entries in dampingPS to the specified value. In both the flag and the   |
    |  | attribute name, PSstands for per-spring.(Default = 0.2 )                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``endForceWeight`` / ``efw``                                                                         | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Amount of the force of the spring that gets applied to the point to which the spring ends. Valid range is from 0.0 to 1.0. (Default = 1.0 )                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exclusive`` / ``exc``                                                                              | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If true, tells the command to create springs only between pairs of points which are not in the same object. (Default is False.)                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``length`` / ``l``                                                                                   | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Vestigial form of restLength.Please use restLengthinstead.                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance between two points that a spring would be considered.                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minDistance`` / ``mnd``                                                                            | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Minimum distance between two points that a spring would be considered. (Default = 0.0. See Defaults for more information on this flag's default.)                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minMax`` / ``mm``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If True, sets the mode of the spring application to Min/Max. This will add springs between all points from the specified point groups that are between the minimum|
    |  | and maximum distance values set with min and max. (Default is False.) Note: This gets automatically set if either the min or max flags are used.                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Name of spring object.                                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``noDuplicate`` / ``nd``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Check for existing springs and don't add a new spring between two points already connected by a spring in the same object. Only the object the command is working |
    |  | on is checked.  This flag is relevant only when using -add. (Default = false)                   Flag can have multiple arguments, passed either as a tuple or a   |
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``restLength`` / ``rl``                                                                              | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Per-object rest length for the new springs. Springs can use either their per-object or per-spring rest length.  See the -lPS and -ulp flags.                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``restLengthPS`` / ``rPS``                                                                           | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Per-spring rest length for the new springs. This will initialize all the entries in restLengthPS to the specified value. If this flag is not thrown, each rest    |
    |  | length will be initialized to the distance between the two  points at the time the spring is created (i.e., the initial length of the spring).   When playing     |
    |  | back, springs can use either their per-spring or per-object rest length.  See the -rl and -urp flags. In both the flag and the attribute name, PSstands for per-  |
    |  | spring.                                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``startForceWeight`` / ``sfw``                                                                       | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Amount of the force of the spring that gets applied to the point from which the spring starts. Valid range is from 0.0 to 1.0. (Default = 1.0 )                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stiffness`` / ``s``                                                                                | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Stiffness of the springs created in the spring object. (Default = 1.0 ) -damp float Vestigial form of damping.Please use dampinginstead.                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stiffnessPS`` / ``sPS``                                                                            | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Stiffness of the springs created in the spring object. This will initialize all the entries in stiffnessPS to the specified value. In both the flag and the       |
    |  | attribute name, PSstands for per-spring.(Default = 1.0 )                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``strength`` / ``str``                                                                               | *float*                       |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``useDampingPS`` / ``udp``                                                                           | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies whether to use dampingPS (per spring damping). If set to false, the per object damping attribute value will be used. This flag simply sets the          |
    |  | useDampingPS attribute of the spring shape. In both the flag and the attribute name, PSstands for per-spring.(Default = false )                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``useRestLengthPS`` / ``urp``                                                                        | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies whether to use restLengthPS (per spring restLength). If set to false, the per object restLength attribute value will be used. This flag simply sets the |
    |  | useRestLengthPS attribute of the spring shape. In both the flag and the attribute name, PSstands for per-spring.(Default = false )                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``useStiffnessPS`` / ``usp``                                                                         | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies whether to use stiffnessPS (per spring stiffness). If set to false, the per object stiffness attribute value will be used. This flag simply sets the    |
    |  | useStiffnessPS attribute of the spring shape. In both the flag and the attribute name, PSstands for per-spring.(Default = false )                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``walkLength`` / ``wl``                                                                              | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is valid only when doing wireframe creation. It will create springs between pairs of points connected by the specified number of edges.  For example, if|
    |  | walk length is 2, each pair of points separated by no more than 2 edges will get a spring.  Walk length measures the distance between pairs of vertices just like |
    |  | the number of blocks measures the distance between two intersections in a city.                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``wireframe`` / ``wf``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If True, sets the mode of the spring application to Wireframe. This is valid only for springs created on a soft body. It will add springs along all edges         |
    |  | connecting the adjacent points (vertices or CV's) of curves and surfaces. (Default is False.)                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.spring`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.spring( 'particle1', s=1.5, d=.3, mnd=0, mxd=5, n='spring1' )
        # Creates a spring object named spring1 with a strength of 1.5 and a
        # damping factor of 0.3 containing a spring between every pair of points in
        # particle1 that are within 0.0 and 5.0 units apart (except those already
        # connected by a spring).
        
        pm.spring( 'particle1', 'spring1', add=True, mnd=0, mxd=5 )
        # Creates between every pair of points in particle1 that are within 0.0
        # and 5.0 units apart (except those already connected by a spring), and adds
        # them to the existing spring object spring1.
        
        pm.spring( 'particle1', 'spring1', add=True, mnd=0, mxd=5, ce='false' )
        # Same as the previous example, but will not check for existing springs
        # in order to avoid duplication, and will create a new spring even between
        # pairs of particles which already have one.
        
        pm.spring( 'particle1', 'particle2', exclusive=1, all=1 )
        # Creates a spring between every pair of particles such that one
        # particle is in particle1 and the other is in particle2.  Does not create
        # any springs between pairs in the same object.  Does not create springs
        # between particles already connected by a spring.
    """

    pass


def stroke(*args, **kwargs):
    """
    The stroke command creates a new Paint Effects stroke node.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the name of the stroke to the input string                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pressure`` / ``pr``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | On creation, allows the copying of the pressure mapping settings from the Paint Effects Tool. Default is false.                   Flag can have multiple          |
    |  | arguments, passed either as a tuple or a list.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``seed`` / ``s``                                                                                     | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the random seed for this stroke.                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.stroke`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.stroke( s=10, n='armScar' )
        # Result: nt.Transform(u'armScar') #
    """

    pass


def expression(*args, **kwargs):
    """
    This command describes an expression that belongs to the current scene. The expression is a block of code of unlimited
    length with a C-like syntax that can perform conversions, mathematical operations, and logical decision making on any
    numeric attribute(s) in the scene.  One expression can read and alter any number of numeric attributes.  Theoretically,
    every expression in a scene can be combined into one long expression, but it is recommended that they are separated for
    ease of use and editing, as well as efficiency.If this command is being sent by the command line or in a script, then
    the user should be sure to embed escaped newlines (\n), tabs (\t) for clarity when reading them in the expression
    editor.  Also, quotes in an expression must be escaped (\) so that they are not confused by the system as the end of
    your string.  When using the expression editor, these characters are escaped for you unless they are already within
    quotes.Note, expressions that alter or use per-particle attributes of a particle shape should use the 'dynExpression'
    command.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``alwaysEvaluate`` / ``ae``                                                                          | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this is TRUE (the default), then the expression will be evaluated whenever time changes regardless of whether the other inputs have changed, and an output is  |
    |  | requested.  If it is FALSE, then the expression will only be evaluated if one or more of the inputs changes and an output is requested.  Note, if 'time' or       |
    |  | 'frame' are inputs, then the expression will act as if this was set to TRUE.                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``animated`` / ``an``                                                                                | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``attribute`` / ``a``                                                                                | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the name of the dependency graph node to use for the expression                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``object`` / ``o``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the defaultobject for the expression.  This allows the expression writer to not type the object name for frequently-used objects.  See the examples below.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``safe`` / ``sf``                                                                                    | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true if no potential side effect can occurs running that expression. Safe expression will be optimized to evaluate only when needed even if flagged       |
    |  | alwaysEvaluate.                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shortNames`` / ``sn``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | When used with the -q/query flag, tells the command to return the expression with attribute names as short as possible. The default is to return the FULL         |
    |  | attribute name, regardless of how the user entered it into the expression, including the object names.  With this flag set, attribute names are returned as their |
    |  | short versions, and any attribute that belongs to the default object, if there is one specified, will not display the object's name.                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``string`` / ``s``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the expression string                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``timeDependent`` / ``td``                                                                           | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true if expression refer to 'time' or 'frame' keywords. Those reference force the connection to time. If the expression is flagged as safe and not time   |
    |  | dependend, then they will always evaluate on depend, even if alwaysEvaluate is on. Otherwise time change will dirty the expression.                       Flag can|
    |  | have multiple arguments, passed either as a tuple or a list.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unitConversion`` / ``uc``                                                                          | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Insert specified unit conversion nodes at creation: all, none,or angularOnly.Default is all.For angularOnly, will insert unit conversion nodes only for angular   |
    |  | attributes (allowing degrees-to-radians conversion).  This is for performance tuning. If queried, returns the option used when the expression was created or last |
    |  | edited.                                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.expression`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.expression( s='a.translateX = b.translateX * sin(c.translateX)' )
        
        pm.expression( o='ball', s='tx = sin(time);' )
    """

    pass


def addDynamic(*args, **kwargs):
    """
    Makes the objectspecified as second argument the source of an existing field or emitter specified as the first argument.
    In practical terms, what this means is that a field will emanate its force from its owner object, and an emitter will
    emit from its owner object. addDynamic makes the specified field or emitter a child of the owner's transform (adding it
    to the model if it was not already there), and makes the necessary attribute connections. If either of the arguments is
    omitted, addDynamic searches the selection list for objects to use instead. If more than one possible owner or
    field/emitter is selected, addDynamic will do nothing. If the specified field/emitter already has a source, addDynamic
    will remove the current source and replace it with the newly specified source. If a subset of the owner object's
    cvs/particles/vertices is selected, addDynamic will add the field/emitter to that subset only.
    
    Modifications:
      - returns a list of PyNode objects
    
    
    Derived from mel command `maya.cmds.addDynamic`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Create an emitter
        pm.emitter( pos=(0, 0, 0), type='omni', r=100, sro=0, nuv=0, cye='none', cyi=1, spd=1, srn=0, nsp=1, tsp=0, mxd=0, mnd=0, dx=1, dy=0, dz=0, sp=0 )
        # Result: nt.PointEmitter(u'emitter1') #
        
        # Get the emitter to emit particles
        pm.particle()
        # Result: [nt.Transform(u'particle1'), nt.Particle(u'particleShape1')] #
        # Result: particle2
        pm.connectDynamic( 'particle1', em='emitter1' )
        # Result: [u'particleShape1'] #
        
        # Create a particle to use as the source of the emitter
        pm.particle( p=((6.0, 0, 7.0), (6.0, 0, 2.0)), c=1 )
        # Result: [nt.Transform(u'particle2'), nt.Particle(u'particleShape2')] #
        # Result: particle2
        
        # Use particle2 as a source of the emitter
        pm.addDynamic( 'emitter1', 'particle2' )
        # Result: [nt.PointEmitter(u'emitter1'), nt.Particle(u'particleShape2')] #
    """

    pass


def vortex(*args, **kwargs):
    """
    A vortex field pulls objects in a circular direction, like a whirlpool or tornado.   Objects affected by the vortex
    field tend to rotate around the axis specified by -ax, -ay, and -az. The transform is the associated dependency node.
    Use connectDynamic to cause the field to affect a dynamic object. If fields are created, this command returns the names
    of each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field
    name is returned. If object names are provided or the active selection list is non-empty, the command creates a field
    for every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to
    -pos 0 0 0. Setting the -pos flag with objects named on the command line is an error.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attenuation`` / ``att``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attentuation rate of field                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``axisX`` / ``ax``                                                                                   | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | X-component of vortex axis                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``axisY`` / ``ay``                                                                                   | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Y-component of vortex axis                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``axisZ`` / ``az``                                                                                   | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Z-component of vortex axis                        Flag can have multiple arguments, passed either as a tuple or a list.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``magnitude`` / ``m``                                                                                | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Strength of field.                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of field                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perVertex`` / ``pv``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the     |
    |  | force field. If this flag is set to false, then the force is exerted only from the geometric center of the set of points.                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Position in space where you want to place a field. The gravity then emanates from this position in space rather than from an object. Note that you can both use   |
    |  | -pos (creating a field at a position) and also provide object names.                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeExclusion`` / ``vex``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.vortex`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.vortex( ax=0, ay=1.0, az=0.5 )
        # Result: nt.VortexField(u'vortexField1') #
        # Creates a vortex field with axis (0,1,0.5) for every active
        # selection. If there is no active
        # selection, it creates this field at world position (0,0,0).
    """

    pass


def colorAtPoint(*args, **kwargs):
    """
    The colorAtPointcommand is used to query textures or ocean           shaders at passed in uv coordinates.       (For
    ocean shaders uv is x and z in worldspace ).           The return value is a floating point array whose size is
    determined by either the number of input uv arguments passed in and the           the queried value.  One can query
    alpha only, rgb only, or rgba values.           The returned array is only single indexed, so if rgb is specified then
    the index for red values would be index \* 3. Blue is index \* 3 + 1, and           green is index \* 3 + 2. For rgba
    use a multiple of 4 instead of 3.           For alpha only one can simply use the index.           There are two basic
    argument formats that may be used:           colorAtPoint -u 0 -v 0   -u .2 -v .1  etc.. for all points           or
    colorAtPoint -mu 0 -mv 0  -xu 1 -xv 1 -su 10 -sv 10 // samples 100 points           If one is sampling several points
    and they are all in a regular grid           formation it is more efficient to call this routine with the latter
    method, which uses a min/max uv and number of samples, rather than           a long argument list of uv coords.
    return values (-o A or RGB or RGBA )individual UV coordinates to sample (-u float  -v float )(numbers of calls to -u and
    -v must match)uniform grid of points to sample (-su int -sv int)(may not use this in combination with -u or -v)bounds
    for sample grid  (-mu float  -mv float -xu float -xv float)
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``coordU`` / ``u``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Input u coordinate to sample texture at.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``coordV`` / ``v``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Input v coordinate to sample texture at.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxU`` / ``xu``                                                                                    | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | DEFAULT 1.0 Maximum u bounds to sample.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxV`` / ``xv``                                                                                    | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | DEFAULT 1.0 Maximum v bounds to sample.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minU`` / ``mu``                                                                                    | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | DEFAULT 0.0 Minimum u bounds to sample.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minV`` / ``mv``                                                                                    | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | DEFAULT 0.0 Minimum v bounds to sample.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``output`` / ``o``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Type of data to output:         A        = alpha only         RGB  = color only         RGBA = color and alpha                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``samplesU`` / ``su``                                                                                | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | DEFAULT 1 The number of points to sample in the U dimension.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``samplesV`` / ``sv``                                                                                | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | DEFAULT 1 The number of points to sample in the V dimension.                                      Flag can have multiple arguments, passed either as a tuple or a |
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.colorAtPoint`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # The return value is the array of values determined by the number of
        # coord flag uses or samplesU * samplesV. The default return value is alpha.
        # If instead the return value is RGB there will be 3 times as many values returned,
        # and if it is RGBA there will be 4 times as many values.
        pm.createNode( 'checker' )
        # Result: nt.Checker(u'checker1') #
        pm.colorAtPoint( 'checker1' )
        # Result: [0.5] #
        # returns the alpha value at uv (0.0,0.0) for texture checker1
        # The return array will have one entry corresponding to this alpha.
        pm.colorAtPoint( 'checker1', u=.5, v=.5 )
        # Result: [0.5] #
        # returns the alpha value at uv (0.5,0.5) for texture checker1
        # The return array will have one entry corresponding to this alpha.
        pm.colorAtPoint( 'checker1', o='RGB', u=(.5, 0.0), v=(.5, 0.1) )
        # Result: [0.5, 0.5, 0.5, 0.5, 0.5, 0.5] #
        # returns the colors at uv (0.5,0.5) and (0.0, 0.01) for texture checker1
        # The return array will have 6 values in the following order: RGBRGB
        pm.colorAtPoint( 'checker1', o='A', su=11, sv=6 )
        # Result: [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0, 1.0, 0.0, 0.0, 0.5, 0.5, 1.0, 1.0, 0.0, 0.0, 0.5, 0.5, 1.0, 1.0, 0.0, 0.0, 0.5, 0.5, 1.0, 1.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 1.0, 1.0, 0.5, 0.5, 0.0, 0.0, 1.0, 1.0, 0.5, 0.5, 0.0, 0.0, 1.0, 1.0, 0.5, 0.5, 0.0, 0.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] #
        # returns the alpha for 50 points in a uniform 11 by 6 grid mapped across
        # uv (0.0, 0.0) to uv (1.0, 1.0) The 12th point would be the first point
        # in the second row of samples where uv = (0.0, 0.2)
        pm.colorAtPoint( 'checker1', o='A', su=3, sv=3, mu=0.3, mv=0.3, xu=0.4, xv=0.4 )
        # Result: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] #
        # returns the alpha for 9 points in a uniform 3 by 3 grid mapped across
        # uv (0.3, 0.3) to uv (0.4, 0.4) The 4th point would be the first point
        # in the second row of samples where uv = (0.35, 0.3).
    """

    pass


def setDynamic(*args, **kwargs):
    """
    setDynamic sets the isDynamic attribute of particle objects on or off.  If no objects are specified, it sets the
    attribute for any selected objects.  If -all is thrown, it sets the attribute for all particle objects in the scene. By
    default it sets the attribute true (on); if the -off flag is thrown, it sets the attribute false (off). WARNING:
    setDynamic is obsolescent.  This is the last version of Maya in which it will be supported.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``allOnWhenRun`` / ``awr``                                                                           | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Obsolete, no longer suppported or necessary.                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``disableAllOnWhenRun`` / ``dwr``                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Obsolete, no longer suppported or necessary.                      Flag can have multiple arguments, passed either as a tuple or a list.                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``setAll`` / ``all``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set for all objects.                                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``setOff`` / ``off``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets isDynamic false.                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``setOn`` / ``on``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets isDynamic true.  This flag is set by default.                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.setDynamic`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.setDynamic( 'myParticles', on=True )
        # Sets myParticles.isDynamic true.
        
        pm.setDynamic( all=True, off=True )
        # Sets isDynamic false for all particle objects in the scene.
    """

    pass


def fluidCacheInfo(*args, **kwargs):
    """
    A command to get information about the fluids cache. Get the startFrame and resolution for InitialConditions. Get the
    endFrame as well for a playback cache. Note that for the playback cache, it will look at the current time (or last frame
    if the current time is past end of cache)                 In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Modifier to the hasDataflag, used to query whether a cache has data (at the current time) for a specific fluid attribute.  Valid attribute values are density,    |
    |  | velocity, temperature, fuel, color, coordinates(for texture coordinates), falloff.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cacheTime`` / ``t``                                                                                | *time*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only valid with the -hasData flag.  The time the -hasData flag uses when it queries the cache to see if there is data.                                    Flag can|
    |  | have multiple arguments, passed either as a tuple or a list.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``endFrame`` / ``ef``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns end time of cache as float.                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``hasCache`` / ``hc``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true if fluid has specified cache, false if not.                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``hasData`` / ``hd``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Queries whether a given cache has data in it at the time specified by the -time flag.  (If not -time flag is present, -hasData assumes the current time.) When    |
    |  | used with the attributeflag, indicates if data for the specified attribute exists in the cache.  When used without the attributeflag, hasDataindicates whether    |
    |  | there is data in the cache for any of the valid fluid attributes.                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``initialConditions`` / ``ic``                                                                       | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the cache to be queried is the Initial Conditionscache.                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``playback`` / ``pb``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the cache to be queried is the Playbackcache.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``resolution`` / ``re``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns cache resolution as float[].                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``startFrame`` / ``sf``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns start time for cache as float.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.fluidCacheInfo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # get start frame for Initial Conditions Cache
        pm.fluidCacheInfo( ic=True, sf=True )
        # get resolution for Initial Conditions Cache
        pm.fluidCacheInfo( ic=True, re=True )
        # get end frame for Playback Cache
        pm.fluidCacheInfo( pb=True, ef=True )
        # get resolution for Playback Cache
        pm.fluidCacheInfo( pb=True, re=True )
        # Is there data for any of the valid properties
        # in the playback cache?
        pm.fluidCacheInfo( pb=True, hd=True )
        # Is there density data in the playback cache?
        pm.fluidCacheInfo( at='density', pb=True, hd=True )
    """

    pass


def saveFluid(*args, **kwargs):
    """
    A command to save the current state of the fluid to the initial state cache. The grids to be saved are determined by the
    cache attributes: cacheDensity, cacheVelocity, etc. These attributes are normally set from the options on Set Initial
    State. The cache must be set up before invoking this command.             In query mode, return type is based on queried
    flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``currentTime`` / ``ct``                                                                             | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | cache state of fluid at current time                                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``endTime`` / ``et``                                                                                 | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | end Time for cacheing                                     Flag can have multiple arguments, passed either as a tuple or a list.                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``startTime`` / ``st``                                                                               | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | start Time for cacheing                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.saveFluid`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # save the current state to the initial conditions cache
        pm.saveFluid()
    """

    pass


def dynExport(*args, **kwargs):
    """
    Export particle data to disk files. For cache export (-format cache), dynExport also sets three attributes of the
    current dynGlobals node.  It sets the useParticleRenderCache attribute to true, and the
    min/maxFrameOfLastParticleRenderCache attributes to correspond to the min and max frames. Exported .pda or .pdb files
    are assigned a name of form object name.frame.extension, where extensionis pdaor pdb.The naming convention for .pdc
    files is similar but does not use frame numbers, it uses a more precise representation of the time instead. By default,
    the pda and pdb formats export all per-particle attributes, and all integer or float type attributes except those which
    are hidden or not storable. (Exception: level of detail is not exported, by default) The pdc format exports all
    attributes which the particle object needs for its state cache. To specify only selected attributes, use the -atr flag
    (which is multi-use).  In general, it is recommended not to use this flag with pdc type, since you need all the
    attributes in order for the cache to be useful. dynExport exports data for the current frame, or for a range of frames
    specified with -mnf and -mxf. If you are not already at the start frame, dynExport will run up the scene for you. VERY
    VERY IMPORTANT NOTE:If you use dynExport in -prompt mode, it does NOT automatically force evaluation of your objects.
    You must do this yourself from your script.  The easiest way is to request each particle object's countattribute each
    frame.  You must request the count attribute for each object you want to export, because their solvers run independently
    of one another.  In interactive mode, objects WILL get evaluated automatically and you don't have to worry about any of
    this. When exporting a particle object whose particles are created from collisions involving particles in another
    particle object(s), you must make sure you simultaneously export all the particle objects involved in the dependency
    chain otherwise you will get an empty cache file. For non-per-particle attributes, pda and pdb formats write the
    identical value once for each particle.  The following types of non-per-particle attributes can be exported: float,
    double, doubleLinear, doubleAngle, byte, short, long, enum.  The first four are exported as Real(in PDB parlance), and
    the last four as Integer.In the pda and pdb formats, particleIdand particleId0are exported as Integer, and are exported
    under the names idand id0respectively.  All other attributes are exported under their long names.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``allObjects`` / ``all``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Ignore the selection list and export all particle objects. If you also specify an object name, the -all flag will be ignored.                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``attribute`` / ``atr``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Name of attribute to be exported. If any specified object does not have one of the specified attributes, dynExport will issue an error and not do the export.     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``format`` / ``f``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Desired format: binarypdb), asciipda), or cachepdc). The pdc format is for use by the Maya particle system to cache particle data.  The pda and pdb format options|
    |  | are intended for pipelines involving other software (for example, sending the data to some program written in-house); Maya cannot read pda or pdb files. There is |
    |  | no formal description of the PDB format, but the ExploreMe/particles/readpdb directory contains the source and Makefile for a small, simple C program called      |
    |  | readpdbwhich reads it. Note that you must compile and run readpdb on the platform which you exported the files on.                      Flag can have multiple    |
    |  | arguments, passed either as a tuple or a list.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxFrame`` / ``mxf``                                                                               | *time*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Ending frame to be exported.                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minFrame`` / ``mnf``                                                                               | *time*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Starting frame to be exported. The export operation will play the scene through from min frame to max frame as it exports.                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``onlyUpdateParticles`` / ``oup``                                                                    | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``overSampling`` / ``os``                                                                            | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | OverSampling to be used during export.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``path`` / ``p``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This option allows you to specify a subdirectory of the workspace particlesdirectory where you want the exported files to be stored. By default, files are stored |
    |  | in the workspace particles directory, i.e., -path is relative to that directory. Please Read This: This is a change from previous versions of Maya in which the   |
    |  | path was relative to the workspace root directory.) You can set the particlesdirectory anywhere you want using the project window or workspace -fr command. (In   |
    |  | this way, you can use an absolute path for export). The -path flag cannot handle strings which include /or \, in other words, it lets you go down only one level  |
    |  | in the directory hierarchy. If you specify a path which doesn't exist, the action will create it if possible; if it can't create the path it will warn you and    |
    |  | fail. If you are using a project for which a particle data directory is not defined, dynExport will create a default one called particlesand add it to your       |
    |  | workspace.                                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dynExport`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.dynExport( 'particle1', mnf=5, mxf=10, os=2, atr=('position', 'velocity'), p='PDB' )
        
        # Export position and velocity attributes for particle1
        # for frames 5 through 10 at every half frame interval,
        # to files in subdirectory "PDB" of the workspace root
        # directory. The default format (binary) will be used.
    """

    pass


def getParticleAttr(*args, **kwargs):
    """
    This action will return either an array of values, or the average value and maximum offset, for a specied per-particle
    attribute of a particle object or component.  If a particle component is specified on the command line, values are
    returned for that component only.  If an object name is given instead, values are returned for all particles in that
    object.  If no object name is passed, but a particle object or component is selected, values are returned for the
    selection. If you list components, they must all be from the same particle object; the action ignores all objects after
    the first.  Likewise if you list more than one object, the actiion will return values only for the first one.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``array`` / ``a``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells the action whether you want a full array of data. If set true, the action returns an array of floats containing the values for all the specified particles. |
    |  | If set false (the default), the action returns the average value and the maximum offset from the average over the component.  If the attribute is a vector        |
    |  | attribute, the action returns six values: Average X, Average Y, Average Z, Maximum offset in X, Y, and Z of component.                      Flag can have multiple|
    |  | arguments, passed either as a tuple or a list.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells the action which attribute you want the value of. Must be a per-particle attribute.                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``object`` / ``o``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is obsolete.  Instead of using it, please pass the name of the object and/or components you want on the command line. See the examples.                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.getParticleAttr`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.getParticleAttr( 'particle1', at='velocity' )
        
        # This will return the average velocity for the entire particle
        # object as well as the maximum offset from the average.
        
        pm.getParticleAttr( 'particleShape1.pt[0:7]', 'particleShape1.pt[11]', at='velocity' )
        
        # This will return the average velocity for particles 0-7 and 11
        # as well as the maximum offset from the average.
        
        pm.getParticleAttr( 'particleShape1.pt[0:7]', 'particleShape1.pt[11]', at='position', array=1 )
        # This will return an array of 27 floats containing the position
        # values for the nine specified particles.
    """

    pass


def paintEffectsDisplay(*args, **kwargs):
    """
    Command to set the global display methods for paint effects items                In query mode, return type is based on
    queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``meshDrawEnable`` / ``me``                                                                          | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set whether mesh draw is enabled on objects                                       Flag can have multiple arguments, passed either as a tuple or a list.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.paintEffectsDisplay`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.paintEffectsDisplay( meshDrawEnable=True )
        meshDrawEnabled = pm.paintEffectsDisplay(query=True, me=True)
    """

    pass


def fluidVoxelInfo(*args, **kwargs):
    """
    Provides basic information about the mapping of a fluid voxel grid into world- or object space of the fluid.  Use this
    command to determine the center point of a voxel, or to find the voxel containing a given point, among other things.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``checkBounds`` / ``cb``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this flag is on, and the voxel index of a point that is out of bounds is requested, then we return nothing.                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``inBounds`` / ``ib``                                                                                | *int, int, int*               | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Are the three ints representing the x, y, z indices of a voxel within the bounds of the fluid's voxel grid?  True if yes, false if not.  (For 2D fluids, pass in  |
    |  | z=0 for the third argument.  See examples.)                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``objectSpace`` / ``os``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Whether the queried value should be returned in object space (TRUE), or world space (FALSE, the default).                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``radius`` / ``r``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Modifier for the -voxel flag.  Returns a list of index triples identifying voxels that fall within the given radius of the point specified by the -voxel flag.    |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``voxel`` / ``v``                                                                                    | *float, float, float*         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns array of three ints representing the x, y, z indices of the voxel within which the given point position is contained. If the checkBounds flag is on, and  |
    |  | the point is out of bounds, we return nothing. Otherwise, even if the point is out of bounds, index values are returned. When combined with the -radius flag,     |
    |  | returns an array of index triples representing a list of voxels within a given radius of the given point position.                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``voxelCenter`` / ``vc``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The center position of the specified voxels.  Returns an array of floats (three for each of the indices in the query).  (Valid only with the -xIndex, -yIndex, and|
    |  | -zIndex flags.)                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``xIndex`` / ``xi``                                                                                  | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only return values for cells with this X index                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``yIndex`` / ``yi``                                                                                  | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only return values for cells with this Y index                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``zIndex`` / ``zi``                                                                                  | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only return values for cells with this Z index                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.fluidVoxelInfo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # fluid3D is a 10x10x5 three-dimensional fluid.
        # fluid2D is a 9x9 two-dimensional fluid.
        #
        # Are the given indices within the bounds of the fluids?
        #
        pm.fluidVoxelInfo( 'fluid2D', inBounds=( 9, 9, 0) )
        # Result: false
        pm.fluidVoxelInfo( 'fluid2D', inBounds=( 8, 8, 0) )
        # Result: true
        pm.fluidVoxelInfo( 'fluid3D', inBounds=( 2, 3, 4 ) )
        # Result: true
        pm.fluidVoxelInfo( 'fluid3D', inBounds=( 12, 9, 2) )
        # Result: false
    """

    pass


def newton(*args, **kwargs):
    """
    A Newton field pulls an object towards the exerting object with force dependent on the exerting object's mass, using
    Newton's universal law of gravitation. The transform is the associated dependency node. Use connectDynamic to cause the
    field to affect a dynamic object. If fields are created, this command returns the names of each of the fields. If a
    field was queried, the results of the query are returned. If a field was edited, the field name is returned. If object
    names are provided or the active selection list is non-empty, the command creates a field for every object in the list
    and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0. Setting the -pos
    flag with objects named on the command line is an error.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attenuation`` / ``att``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attentuation rate of field                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``magnitude`` / ``m``                                                                                | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Strength of field.                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minDistance`` / ``mnd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Minimum distance at which field is exerted. Distance is in the denominator of the field force equation. Setting md to a small positive number avoids bizarre      |
    |  | behavior when the distance gets extremely small.                     Flag can have multiple arguments, passed either as a tuple or a list.                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of field                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perVertex`` / ``pv``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the     |
    |  | force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Position in space where you want to place a field. The newton then emanates from this position in space rather than from an object. Note that you can both use    |
    |  | -pos (creating a field at a position) and also provide object names.                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeExclusion`` / ``vex``                                                                        | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.newton`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.newton( 'particle1', m=5.0, mxd=2.0 )
        # Creates a newton field with magnitude 5.0 and maximum distance 2.0,
        # and adds it to the list of fields particle1 owns.
        
        pm.newton( pos=(-2, 0, 4) )
        # Creates a newton field at position (0,2,4) in world coordinates,
        # with default magnitude(1.0), attentuation (1.0),
        # and max distance (5.0).
        
        pm.newton( 'newtonField1', e=1, att=0.98 )
        # Edits the acceleration value of the field named newtonField1
        
        pm.newton( 'newtonField1', q=1, m=1 )
        # Queries newtonF ield1for its magnitude.
        
        pm.newton( 'newtonField1', e=1, mxd=10.0 )
        # Changes the maximum distance of the field called
        # "newtonField1" to 10.0.
        
        pm.newton( m=2.0 )
        # Creates a newton field with magnitude 2.0 for every active selection.
        # If no there are active
        # selections, creates such a field at world position (0,0,0).
    """

    pass


def truncateFluidCache(*args, **kwargs):
    """
    This command sets the end time of a fluid cache to the current time. If the current time is less than the end time of
    the cache, the cache is truncated so that only the portion of the cache up to and including the current time is
    preserved.                 In query mode, return type is based on queried flag.
    
    
    Derived from mel command `maya.cmds.truncateFluidCache`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Truncate a fluid cache that has a start time of 1
        # and an end time of 25 so that only the first 10
        # frames are preserved and the end time of the
        # cache is set to 10.
        #
        pm.currentTime( 10 )
        # Result: 10.0 #
        pm.truncateFluidCache()
    """

    pass


def emitter(*args, **kwargs):
    """
    Creates an emitter object. If object names are provided or if objects are selected, applies the emitter to the
    named/selected object(s)in the scene.  Particles will then be emitted from each. If no objects are named or selected, or
    if the -pos option is specified, creates a positional emitter. If an emitter was created, the command returns the name
    of the object owning the emitter, and the name of emitter shape. If an emitter was queried, the command returns the
    results of the query. Keyframeable attributes of the emitter node: rate, directionX, directionY, directionZ,
    minDistance, maxDistance, spread.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``alongAxis`` / ``alx``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Initial velocity multiplier in the direction along the central axis of the volume.  See the diagrams in the documentation.  Applies only to volume emitters.      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``aroundAxis`` / ``arx``                                                                             | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Initial velocity multiplier in the direction around the central axis of the volume.  See the diagrams in the documentation.  Applies only to volume emitters.     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``awayFromAxis`` / ``afx``                                                                           | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Initial velocity multiplier in the direction away from the central axis of the volume.  See the diagrams in the documentation.  Used only with the cylinder, cone,|
    |  | and torus volume emitters.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``awayFromCenter`` / ``afc``                                                                         | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Initial velocity multiplier in the direction away from the center point of a cube or sphere volume emitter. Used only with the cube and sphere volume emitters.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cycleEmission`` / ``cye``                                                                          | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Possible values are noneand frame.Cycling emission restarts the random number stream after a specified interval.  This can either be a number of frames or a      |
    |  | number of emitted particles.  In each case the number is specified by the cycleInterval attribute. Setting cycleEmission to frameand cycleInterval to 1 will then |
    |  | re-start the random stream every frame. Setting cycleInterval to values greater than 1 can be used to generate cycles for games work.                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cycleInterval`` / ``cyi``                                                                          | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the number of frames or particles between restarts of the random number stream.  See cycleEmission.  Has no effect if cycleEmission is set to None.     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionX`` / ``dx``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | x-component of emission direction. Used for directional emitters, and for volume emitters with directionalSpeed.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionY`` / ``dy``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | y-component of emission direction. Used for directional emitters, and for volume emitters with directionalSpeed.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionZ`` / ``dz``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | z-component of emission direction. Used for directional emitters, and for volume emitters with directionalSpeed.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionalSpeed`` / ``drs``                                                                       | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | For volume emitters only, adds a component of speed in the direction specified by the directionX, Y, and Z attributes. Applies only to volume emitters. Does not  |
    |  | apply to other types of emitters.                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which emission ends.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minDistance`` / ``mnd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Minimum distance at which emission starts.                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``needParentUV`` / ``nuv``                                                                           | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If aNeedParentUV is true, compute parentUV value from each triangle or each line segment, then send out to the target particle object. You also need to add       |
    |  | parentU and parentV attributes to the particle object to store these values.                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``normalSpeed`` / ``nsp``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Normal speed multiple for point emission. For each emitted particle, multiplies the component of the velocity normal to the surface or curve by this amount.      |
    |  | Surface and curve emitters only.                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Positional emitter at world space location (x,y,z).                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``randomDirection`` / ``rnd``                                                                        | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Magnitude of a random component of the speed from volume emission.                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rate`` / ``r``                                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Rate at which particles emitted (can be non-integer). For point emission this is rate per point per unit time. For surface emission it is rate per square unit of |
    |  | area per unit time.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scaleRateByObjectSize`` / ``sro``                                                                  | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Applies to curve and surface emitters, only. If true, number of particles is determined by object size (area or length) times rate value.  If false, object size  |
    |  | is ignored and the rate value is used without modification. The former is the way Maya behaved prior to version 3.0.                     Flag can have multiple   |
    |  | arguments, passed either as a tuple or a list.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scaleSpeedBySize`` / ``ssz``                                                                       | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Indicates whether the scale of a volume emitter affects its velocity.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``speed`` / ``spd``                                                                                  | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Speed multiple.  Multiplies the velocity of the emitted particles by this amount. Does not apply to volume emitters.  For that emitter type, use directionalSpeed.|
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``speedRandom`` / ``srn``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Identifies a range of random variation for the speed of each generated particle.  If set to a non-zero value, speed becomes the mean value of the generated       |
    |  | particles, whose speeds vary by a random amount up to plus or minus speedRandom/2. For example, speed 5 and speedRandom 2 will make the speeds vary between 4 and |
    |  | 6.                                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``spread`` / ``sp``                                                                                  | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Random spread (0-1), as a fraction of 90 degrees, along specified direction.   Directional emitters only.                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``tangentSpeed`` / ``tsp``                                                                           | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tangent speed multiple for point emission. For each emitted particle, multiplies the component of the velocity tangent to the surface  or curve by this amount.   |
    |  | Surface and curve emitters only.                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``typ``                                                                                   | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Type of emitter. The choices are omni | dir | direction | surf | surface | curve | curv. The default is omni. The full definition of these types are:             |
    |  | omnidirectional point emitter, directional point emitter, surface emitter, or curve emitter.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Volume offset of the emitter.  Volume offset translates the emission volume by the specified amount from the actual emitter location.  This is in the emitter's   |
    |  | local space.                                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Volume shape of the emitter.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than none, determines a 3-D volume within which   |
    |  | particles are generated. Values are: cube,sphere,cylinder,cone,torus.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Volume sweep of the emitter.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.emitter`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.particle( p=((-1, 5, 2), (2, 2, 2), (3, 3, 3)), n='particles' )
        # Result: [nt.Transform(u'particles'), nt.Particle(u'particlesShape')] #
        pm.emitter( 'particles', r=300, mnd=1.5, mxd=2.5, n='emitter' )
        # Result: nt.Transform(u'particles') #
        pm.particle( n='emitted' )
        # Result: [nt.Transform(u'emitted'), nt.Particle(u'emittedShape')] #
        pm.connectDynamic( 'emitted', em='emitter' )
        # Result: [u'emittedShape'] #
        
        # Creates a particle emitter.
        
        pm.emitter( dx=1, dy=0, dz=0, sp=0.33, pos=(1, 1, 1), n='myEmitter' )
        # Result: nt.PointEmitter(u'myEmitter') #
        pm.particle( n='emittedParticles' )
        # Result: [nt.Transform(u'emittedParticles'), nt.Particle(u'emittedParticlesShape')] #
        pm.connectDynamic( 'emittedParticles', em='myEmitter' )
        # Result: [u'emittedParticlesShape'] #
        
        # Creates a point emitter.
    """

    pass


def rigidSolver(*args, **kwargs):
    """
    This command sets the attributes for the rigid solver            In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``autoTolerances`` / ``at``                                                                          | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns the auto tolerance calculation on and off.  The auto tolerances calculation will override the default or user defined values of the step size and collision |
    |  | tolerance value that is calculated based on the objects in the scene. Default: 0 (off)                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``bounciness`` / ``b``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns bounciness on and off for the an the objects in the simulation. Default value: on                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cacheData`` / ``cd``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns the cache on fall all rigid bodies in the system. Default value: off                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``collide`` / ``c``                                                                                  | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Disallows the interpenetration of the two rigid bodies listed. Default: Collide is on for all bodies.                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``collisionTolerance`` / ``ct``                                                                      | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the collision tolerance.  This is the error at which two objects are considered to have collided. Range:   0.0005 - 1.000 Default: 0.02                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``contactData`` / ``ctd``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns the contact data information on/off for all rigid bodies. Default value: off                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``create`` / ``cr``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Creates a new rigid solver.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``current`` / ``cu``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets rigid solver as the current solver.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deleteCache`` / ``deleteCache``                                                                    | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Deletes the cache for all rigid bodies in the system.                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``displayCenterOfMass`` / ``dcm``                                                                    | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Displays the center of mass icon. Default value: on                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``displayConstraint`` / ``dc``                                                                       | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Displays the constraint vectors. Default value: on                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``displayVelocity`` / ``dv``                                                                         | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Displays the velocity vectors. Default value: off                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dynamics`` / ``d``                                                                                 | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns dynamics on and off for the an the objects in the simulation. Default value: on                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``friction`` / ``f``                                                                                 | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns friction on and off for the an the objects in the simulation. Default value: on                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``interpenetrate`` / ``i``                                                                           | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Allows the two rigid bodies listed to interpenetrate. Default: interpenetration is off for all bodies.                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``interpenetrationCheck`` / ``ic``                                                                   | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Checks for interpenetrating rigid bodies in the scene.                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rigidBodies`` / ``rb``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a list of rigid bodies in the solver.                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rigidBodyCount`` / ``rbc``                                                                         | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the number of rigid bodies in the solver.                         Flag can have multiple arguments, passed either as a tuple or a list.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showCollision`` / ``sc``                                                                           | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Displays the colliding objects in a different color.                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``showInterpenetration`` / ``si``                                                                    | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Displays the interpenetrating objects in a different color.                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``solverMethod`` / ``sm``                                                                            | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the solver method.  The choices are 0 | 1 | 2. 0 = Euler (fastest/least acurate), 1 = Runge-Kutta ( slower/more acurate), 2 = adaptive Runge-Kutta           |
    |  | (slowest/most acurate). The default is 2 (adaptive Runge-Kutta)                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``startTime`` / ``stt``                                                                              | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the start time for the solver.                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``state`` / ``st``                                                                                   | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns the rigid solver on or off.                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``statistics`` / ``sta``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns the statistic information on/off for all rigid bodies. Default value: off                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stepSize`` / ``s``                                                                                 | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the solvers step size.  This is the maximum size of a single step the solver will take at one time. Range:   0.0004 - 0.100 Default: 0.0333                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``velocityVectorScale`` / ``vs``                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | scales the velocity vector display. Default value: 1.0                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.rigidSolver`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Set the playback time range to [1, 100]
        pm.playbackOptions(min=1, max=100)
        # Result: 1.0 #
        # Create a poly cube named "floor"
        pm.polyCube(w=10, h=0.10, d=10, sx=10, sy=1, sz=10, ax=(0, 1, 0), name='floor')
        # Result: [nt.Transform(u'floor'), nt.PolyCube(u'polyCube1')] #
        # Create a poly sphere named "ball", then move it to 0 9 0
        pm.polySphere(r=1, sx=20, sy=20, ax=(0, 1, 0), name='ball')
        # Result: [nt.Transform(u'ball'), nt.PolySphere(u'polySphere1')] #
        pm.move(0, 9.0, 0, r=True)
        # Create a new rigid body solver
        pm.rigidSolver(create=True, name='rigidSolver1')
        # Result: nt.RigidSolver(u'rigidSolver1') #
        # Set the floor to passive rigid body
        pm.select('floor')
        pm.rigidBody(passive=True, solver='rigidSolver1', name='passiveRigidBody')
        # Result: nt.RigidBody(u'passiveRigidBody') #
        # Set the ball to active rigid body
        pm.select('ball')
        pm.rigidBody(active=True, solver='rigidSolver1', name='activeRigidBody')
        # Result: nt.RigidBody(u'activeRigidBody') #
        # Add a gravity field, and connect it to ball
        pm.gravity(pos=(0, 0, 0), m=9.8, dx=0, dy=-1, dz=0, name='gravityField')
        # Result: nt.GravityField(u'gravityField') #
        pm.connectDynamic('activeRigidBody', f='gravityField')
        # Result: [u'activeRigidBody'] #
        # Play
        pm.play(w=True)
        
        # Set the rigid solver to allow the ball to interpenetrate the floor, then replay
        pm.currentTime(1, e=True)
        # Result: 1.0 #
        pm.rigidSolver('passiveRigidBody', 'activeRigidBody', 'rigidSolver1', e=True, interpenetrate=True)
        # Result: nt.RigidSolver(u'rigidSolver1') #
        pm.play(w=True)
        
        # Set the rigid solver to disallow the ball to interpenetrate the floor, replay
        pm.currentTime(1, e=True)
        # Result: 1.0 #
        pm.rigidSolver('passiveRigidBody', 'activeRigidBody', 'rigidSolver1', e=True, collide=True)
        # Result: nt.RigidSolver(u'rigidSolver1') #
        pm.play(w=True)
        
        # Set the rigid solver to turn off the bounciness, replay
        pm.currentTime(1, e=True)
        # Result: 1.0 #
        pm.rigidSolver('rigidSolver1', e=True, bounciness=False)
        # Result: nt.RigidSolver(u'rigidSolver1') #
        pm.play(w=True)
    """

    pass


def volumeAxis(*args, **kwargs):
    """
    A volume axis field can push particles in four directions, defined with respect to a volume: along the axis, away from
    the axis or center, around the axis, and in a user-specified direction.  These are analogous to the emission speed
    controls of volume emitters. The volume axis field also contains a wind turbulence model (different from the turbulence
    field) that simulates an evolving flow of liquid or gas. The turbulence has a build in animation that is driven by a
    connection to a time node. The transform is the associated dependency node. Use connectDynamic to cause the field to
    affect a dynamic object. If fields are created, this command returns the names of each of the fields. If a field was
    queried, the results of the query are returned. If a field was edited, the field name is returned. If object names are
    provided or the active selection list is non-empty, the command creates a field for every object in the list and calls
    addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0. Setting the -pos flag with
    objects named on the command line is an error.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``alongAxis`` / ``alx``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Initial velocity multiplier in the direction along the central axis of the volume.  See the diagrams in the documentation.                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``aroundAxis`` / ``arx``                                                                             | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Initial velocity multiplier in the direction around the central axis of the volume.  See the diagrams in the documentation.                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``attenuation`` / ``att``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attentuation rate of field with distance. For sphere volumes, distance is computed from the center of the sphere.  For cone, cylinder, and cube volumes, it is    |
    |  | computed from the vertical axis of the volume.  For torus volumes, it is computed from the ring in the middle of the solid portion of the torus.                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``awayFromAxis`` / ``afx``                                                                           | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Initial velocity multiplier in the direction away from the central axis of the volume.  See the diagrams in the documentation.  Used only with the cylinder, cone,|
    |  | and torus volumes.                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``awayFromCenter`` / ``afc``                                                                         | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Initial velocity multiplier in the direction away from the center point of a cube or sphere volume. Used only with the cube and sphere volumes.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``detailTurbulence`` / ``dtr``                                                                       | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The relative intensity of a second higher frequency turbulence. This can be used to create fine features in large scale flows. Both the speed and the frequency on|
    |  | this second turbulence are higher than the primary turbulence. When the detailTurbulence is non-zero the simulation may run a bit slower, due to the computation  |
    |  | of a second turbulence.                       Flag can have multiple arguments, passed either as a tuple or a list.                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionX`` / ``dx``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | x-component of force direction.  Used with directional speed.                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionY`` / ``dy``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | y-component of force direction.  Used with directional speed.                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionZ`` / ``dz``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | z-component of force direction.  Used with directional speed.                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionalSpeed`` / ``drs``                                                                       | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Adds a component of speed in the direction specified by the directionX, Y, and Z attributes.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``invertAttenuation`` / ``ia``                                                                       | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this attribute is FALSE, the default, then the attenuation makes the field's effect decrease as the affected point is further from the volume's axis and closer|
    |  | to its edge.  If the is set to TRUE, then the effect of the field increases in this case, making the full effect of the field felt at the volume's edge.          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``magnitude`` / ``m``                                                                                | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Strength of field.                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which field is exerted. A zero or negative value will turn off the field effect completely. For sphere volumes, distance is computed from the |
    |  | center of the sphere.  For cone, cylinder, and cube volumes, it is computed from the vertical axis of the volume.  For torus volumes, it is computed from the ring|
    |  | in the middle of the solid portion of the torus.                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of field                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perVertex`` / ``pv``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | No effect for this type of field.                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Position in space where you want to place the volume.                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``turbulence`` / ``trb``                                                                             | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Adds a force simulating a turbulent wind that evolves over time.                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``turbulenceFrequencyX`` / ``tfx``                                                                   | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The repeats of the turbulence function in X.                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``turbulenceFrequencyY`` / ``tfy``                                                                   | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The repeats of the turbulence function in Y.                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``turbulenceFrequencyZ`` / ``tfz``                                                                   | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The repeats of the turbulence function in Z.                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``turbulenceOffsetX`` / ``tox``                                                                      | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The translation of the turbulence function in X.                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``turbulenceOffsetY`` / ``toy``                                                                      | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The translation of the turbulence function in Y.                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``turbulenceOffsetZ`` / ``toz``                                                                      | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The translation of the turbulence function in Z.                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``turbulenceSpeed`` / ``trs``                                                                        | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The rate of change of the turbulence over time. The turbulence loops seamlessly every 1.0/turbulenceSpeed seconds. To animate this rate attach a new time node to |
    |  | the time input on the volumeAxisNode then animate the time value on the time node.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeExclusion`` / ``vex``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.volumeAxis`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.volumeAxis( pos=(0, 0, 0), afc=1.0, afx=2.0, arx=3.0, alx=4.0, drs=6.0 )
        # Result: nt.VolumeAxisField(u'volumeAxisField1') #
        
        # Creates a volume axis field with the following attribute values:
        # awayFromCenter = 1.0, awayFromAxis = 2.0, aroundAxis = 3.0, alongAxis = 4.0,
        # directionalSpeed = 6.0.
    """

    pass


def loadFluid(*args, **kwargs):
    """
    A command to set builtin fluid attributes such as Density, Velocity, etc for all cells in the grid from the initial
    state cache                  In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``currentTime`` / ``ct``                                                                             | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is now obsolete. Move the cache clip in the Trax editor to view different frames of the playback cache.                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``frame`` / ``f``                                                                                    | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is now obsolete. Move the cache clip in the Trax editor to view different frames of the playback cache.                                         Flag can|
    |  | have multiple arguments, passed either as a tuple or a list.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``initialConditions`` / ``ic``                                                                       | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | load initial conditions cache                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.loadFluid`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Load the initial state cache into the fluid
        pm.loadFluid( ic=True )
    """

    pass


def expressionEditorListen(*args, **kwargs):
    """
    Listens for messages for the Expression Editor, at its request, and communicates them to it.  This action is for
    internal use only and should not be called by users.  This action should be called only by the Expression Editor.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``listenFile`` / ``lf``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Listen for changes to the file argument.                          Flag can have multiple arguments, passed either as a tuple or a list.                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listenForAttr`` / ``la``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Listen for changes to the attributes of the node argument.                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listenForExpression`` / ``le``                                                                     | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Listen for changes to the named expression                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listenForName`` / ``ln``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Listen for name changes for the node argument.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stopListenForAttr`` / ``sla``                                                                      | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Stop listening for changes to the attributes of the node argument.                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stopListenForExpression`` / ``sle``                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Stop listening for changes to the named expression                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stopListenForName`` / ``sln``                                                                      | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Stop listening for name changes for the node argument.                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.expressionEditorListen`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.expressionEditorListen()
    """

    pass


def turbulence(*args, **kwargs):
    """
    A turbulence field causes irregularities (also called 'noise' or 'jitter') in the motion of affected objects. Use
    connectDynamic to cause the field to affect a dynamic object. If fields are created, this command returns the names of
    each of the fields. If a field was queried, the results of the query are returned. If a field was edited, the field name
    is returned. If object names are provided or the active selection list is non-empty, the command creates a field for
    every object in the list and calls addDynamic to add it to the object. If the list is empty, the command defaults to
    -pos 0 0 0. Setting the -pos flag with objects named on the command line is an error.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attenuation`` / ``att``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attentuation rate of field                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``frequency`` / ``f``                                                                                | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Frequency of turbulence field. This determines how often motion is disrupted.                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``magnitude`` / ``m``                                                                                | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Strength of field. As this increases, the affected objects will move faster.                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which field is exerted.                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of field                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``noiseLevel`` / ``nsl``                                                                             | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If the noiseLevel parameter is greater than zero, the field will do multiple lookups in the table.  Each additional lookup is weighted using noiseRatio (which    |
    |  | see).  The noiseLevel is the number of additional lookups, so if noiseLevel is 0, there is just one lookup.  A value of 0 (the default) corresponds to the way the|
    |  | field behaved prior to Maya 3.0.                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``noiseRatio`` / ``nsr``                                                                             | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If noiseLevel is greater than zero, then noiseRatio is the relative magnitude for each consecutive noise evaluation. These are cumulative: for example, if        |
    |  | noiseRatio is 0.5, then the first evaluation is weighted 0.5, the second 0.25, and so on. Has no effect if noiseLevel is zero.                         Flag can   |
    |  | have multiple arguments, passed either as a tuple or a list.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perVertex`` / ``pv``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the     |
    |  | force field. If this flag is set to false, then the force is exerted only from the geometric center of the set of points.                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``phase`` / ``p``                                                                                    | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Phase shift of turbulence field. This influences the direction of the disruption.  This flag is obsolete and is retained only for backward compatibility.  It is  |
    |  | replaced by -phaseX, -phaseY, and -phaseZ.  Setting -phase is identical to setting -phaseZ (the phase shift was always in the Z dimension).                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``phaseX`` / ``px``                                                                                  | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | X component of phase shift of turbulence field. This influences the direction of the disruption.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``phaseY`` / ``py``                                                                                  | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Y component of phase shift of turbulence field. This influences the direction of the disruption.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``phaseZ`` / ``pz``                                                                                  | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Z component of phase shift of turbulence field. This influences the direction of the disruption.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Position in space where you want to place a field. The field then emanates from this position in space rather than from an object. Note that you can both use -pos|
    |  | (creating a field at a position) and also provide object names.                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeExclusion`` / ``vex``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.turbulence`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Creates a new field
        pm.turbulence( n='turbulenceF', m=5.0, pos=(0.25, 0, 0) )
        # Result: nt.TurbulenceField(u'turbulenceF') #
        
        # Edits the frequency value of the field named turbulenceF
        pm.turbulence( 'turbulenceF', e=True, f=0.5 )
        # Result: nt.TurbulenceField(u'turbulenceF') #
        
        # Queries turbulenceF for its frequency value
        pm.turbulence( 'turbulenceF', q=True, f=1 )
        # Result: 0.5 #
    """

    pass


def runup(*args, **kwargs):
    """
    runup plays the scene through a frame of frames, forcing dynamic objects to evaluate as it does so.   If no max frame is
    specified, runup runs up to the current time.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``cache`` / ``cch``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Cache the state after the runup.                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fromPreviousFrame`` / ``fpf``                                                                      | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Run up the animation from the previously evaluated frame. If no flag is supplied this is the default.                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fromStartFrame`` / ``fsf``                                                                         | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Run up the animation from the start frame. If no flag is supplied -fromPreviousFrame is the default.                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxFrame`` / ``mxf``                                                                               | *time*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Ending time for runup, in current user time units. The runup will always start at the minimum start frame for all dynamic objects.                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``state`` / ``st``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns runup and cache on/off.                     Flag can have multiple arguments, passed either as a tuple or a list.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.runup`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.runup( mxf=10, cache=True )
        
        # Starts at the minimum start frame of all dynamic objects
        # and plays through to frame 10.  This guarantees that the system
        # is in the same state it would be as if you had rewound and played
        # forward from frame 0.  The state of the dynamic object(s) will be
        # cached after the runup.
    """

    pass


def dynPaintEditor(*args, **kwargs):
    """
    Create a editor window that can be painted into
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``activeOnly`` / ``ao``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | For Scene mode, this determines if only the active strokes will be refreshed.                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``autoSave`` / ``autoSave``                                                                          | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | For Canvas mode, this determines if the buffer will be saved to a disk file after every stroke. Good for painting textures and viewing the results in shaded      |
    |  | display in the model view.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``camera`` / ``cam``                                                                                 | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the name of the camera which the Paint Effects panel looks through.                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``canvasMode`` / ``cm``                                                                              | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the Paint Effects panel into Canvas mode if true.                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``canvasUndo`` / ``cu``                                                                              | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Does a fast undo in Canvas mode. This is a special undo because we are not using any history when we paint in Canvas mode so we provide a single level undo for   |
    |  | the Canvas.                                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``changeCommand`` / ``cc``                                                                           | *unicode, unicode, unicode,   | .. image:: /images/create.gif |
    |                                                                                                      | unicode*                      | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Parameters: First string: commandSecond string: editorNameThird string: editorCmdFourth string: updateFuncCall the command when something changes in the editor   |
    |  | The command should have this prototype :  command(string $editor, string $editorCmd, string $updateFunc, int $reason)  The possible reasons could be : 0: no      |
    |  | particular reason1: scale color2: buffer (single/double)3: axis 4: image displayed5: image saved in memory                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``clear`` / ``cl``                                                                                   | *float, float, float*         | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Clears the buffer (if in Canvas mode) to the floating point values (R,G,B).                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``control`` / ``ctl``                                                                                | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible, at times, for an     |
    |  | editor to exist without a control. This flag returns NONEif no control is present.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``currentCanvasSize`` / ``ccs``                                                                      | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | In Query mode, this returns the (X,Y) resolution of the current canvas.                   Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``defineTemplate`` / ``dt``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Puts a command in a mode where any other flags and args are parsed and added to the command template specified in the argument. They will be used as default      |
    |  | arguments in any subsequent invocations of the command when templateName is set as the current template.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``displayAppearance`` / ``dsa``                                                                      | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the display appearance of the model panel.  Possible values are wireframe, points, boundingBox, smoothShaded, flatShaded.  This flag may be used with the    |
    |  | -interactive and -default flags.  Note that only wireframe, points, and boundingBoxare valid for the interactive mode.                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``displayFog`` / ``dfg``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | For Scene mode, this determines if fog will be displayed in the Paint Effects panel when refreshing the scene. If fog is on, but this is off, fog will only be    |
    |  | drawn on the strokes, not the rest of the scene.                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``displayImage`` / ``di``                                                                            | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set a particular image in the Editor Image Stack as the current Editor Image. Images are added to the Editor Image Stack using the si/saveImageflag.              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``displayLights`` / ``dsl``                                                                          | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the lighting for shaded mode.  Possible values are selected, active, all, default.                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``displayStyle`` / ``dst``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the mode to display the image. Valid values are: colorto display the basic RGB imagemaskto display the mask channellumto display the luminance of the image   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``displayTextures`` / ``dtx``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns on or off display of textures in shaded mode                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``docTag`` / ``dtg``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attaches a tag to the Maya editor.                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``doubleBuffer`` / ``dbf``                                                                           | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the display in double buffer mode                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``drawAxis`` / ``da``                                                                                | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``drawContext`` / ``drc``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the name of the context.                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``exists`` / ``ex``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns true|false depending upon whether the specified object exists.  Other flags are ignored.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fastUpdate`` / ``fu``                                                                              | *int*                         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fileName`` / ``fil``                                                                               | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This sets the file to which the canvas will be saved.                                                                                                             |
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
    | ``iconGrab`` / ``ig``                                                                                | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This puts the Paint Effects panel into Grab Icon mode where the user is expected to drag out a section of the screen to be made into an icon.                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``loadImage`` / ``li``                                                                               | *unicode*                     | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | load an image from disk and set it as the current Editor Image                                                                                                    |
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
    | ``menu`` / ``mn``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the name of the script used to build a menu in the editor. The script takes the editor name as an argument.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``nbImages`` / ``nim``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | returns the number of images                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``newImage`` / ``ni``                                                                                | *int, int, float, float,      | .. image:: /images/query.gif  |
    |                                                                                                      | float*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Starts a new image in edit mode, setting the resolution to the integer values (X,Y) and clearing the buffer to the floating point values (R,G,B). In Query mode,  |
    |  | this returns the (X,Y) resolution of the current Image.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``paintAll`` / ``pa``                                                                                | *float*                       | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Redraws the buffer in current refresh mode.                                                                                                                       |
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
    | ``redrawLast`` / ``rl``                                                                              | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Redraws the last stroke again. Useful when it's brush has just changed. This feature does a fast undo and redraws the stroke again.                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``refresh`` / ``ref``                                                                                | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | requests a refresh of the current Editor Image.                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``refreshMode`` / ``rmd``                                                                            | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the refresh mode to the specified value. 0 - Do not draw strokes on refresh, 1 - Redraw strokes in wireframe mode, 2 - Redraw strokes in final rendered mode.|
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeAllImages`` / ``ra``                                                                         | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | remove all the Editor Images from the Editor Image Stack                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeImage`` / ``ri``                                                                             | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | remove the current Editor Image from the Editor Image Stack                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rollImage`` / ``rig``                                                                              | *float, float*                | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | In Canvas mode, this rolls the image by the floating point values (X,Y). X and Y are between 0 (no roll) and 1 (full roll). A value of .5 rolls the image 50% (ie.|
    |  | the border moves to the center of the screen.                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``saveAlpha`` / ``sa``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | For Canvas mode, this determines if the alpha will be saved when storing the canvas to a disk file.                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``saveBumpmap`` / ``sbm``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Saves the current buffer as a bump map to the specified file.                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``saveImage`` / ``si``                                                                               | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | save the current Editor Image to memory. Saved Editor Images are stored in an Editor Image Stack. The most recently saved image is stored in position 0, the      |
    |  | second most recently saved image in position 1, and so on... To set the current Editor Image to a previously saved image use the di/displayImageflag.             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scaleBlue`` / ``sb``                                                                               | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Define the scaling factor for the blue component in the View. The default value is 1 and can be between -1000 to +1000                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scaleGreen`` / ``sg``                                                                              | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Define the scaling factor for the green component in the View. The default value is 1 and can be between -1000 to +1000                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scaleRed`` / ``sr``                                                                                | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Define the scaling factor for the red component in the View. The default value is 1 and can be between -1000 to +1000                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``selectionConnection`` / ``slc``                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the name of a selectionConnection object which the editor will synchronize with its own selection list.  As the user selects things in this editor, they|
    |  | will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the change.                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``singleBuffer`` / ``sbf``                                                                           | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the display in single buffer mode                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``snapShot`` / ``snp``                                                                               | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Takes a snapshot of the current camera view.                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stateString`` / ``sts``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Query only flag.  Returns the MEL command that will edit an editor to match the current editor state. The returned command string uses the string variable        |
    |  | $editorName in place of a specific name.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``swap`` / ``swp``                                                                                   | *int*                         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``tileSize`` / ``ts``                                                                                | *int*                         | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the size of the tile for the hardware texture redraw of the display buffer.                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``unParent`` / ``up``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies that the editor should be removed from its layout. This cannot be used with query.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``undoCache`` / ``uc``                                                                               | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | By default the last image is cached for undo. If this is set false, then undoing will be disabled in canvas mode and undo in scene mode will force a full refresh.|
    |  | Less memory will be used if this is set false before the first clear or refresh of the current scene.                                                             |
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
    | ``wrap`` / ``wr``                                                                                    | *bool, bool*                  | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | For Canvas mode, should the buffer wrap in U, and V (respectively) when painting.                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``writeImage`` / ``wi``                                                                              | *unicode*                     | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | write the current Editor Image to disk                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``zoom`` / ``zm``                                                                                    | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Zooms the Canvas image by the specified value.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dynPaintEditor`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.dynPaintEditor( 'editor' )
        
        pm.dynPaintEditor( 'editor', e=True, ni=(640, 480, 1.0, 0.5, 0.2) )
    """

    pass


def radial(*args, **kwargs):
    """
    A radial field pushes objects directly towards or directly away from it, like a magnet. The transform is the associated
    dependency node. Use connectDynamic to cause the field to affect a dynamic object. If fields are created, this command
    returns the names of each of the fields. If a field was queried, the results of the query are returned. If a field was
    edited, the field name is returned. If object names are provided or the active selection list is non-empty, the command
    creates a field for every object in the list and calls addDynamic to add it to the object. If the list is empty, the
    command defaults to -pos 0 0 0. Setting the -pos flag with objects named on the command line is an error.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attenuation`` / ``att``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attentuation rate of field                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``magnitude`` / ``m``                                                                                | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Strength of field.                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of field                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perVertex`` / ``pv``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the     |
    |  | force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Position in space where you want to place a field. The field then emanates from this position in space rather than from an object. Note that you can both use -pos|
    |  | (creating a field at a position) and also provide object names.                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``typ``                                                                                   | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Type of radial field (0 - 1).  This controls the algorithm by which the field is attenuated. Type 1, provided for backward compatibility, specifies the same      |
    |  | algorithm as Alias | Wavefront Dynamation. A value between 0 and 1 yields a linear blend.                    Flag can have multiple arguments, passed either as a |
    |  | tuple or a list.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeExclusion`` / ``vex``                                                                        | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.radial`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.radial( 'particle1', m=5.0, mxd=2.0 )
        # Creates a radial field with magnitude 5.0 and maximum distance 2.0,
        # and adds it to the list of fields particle1 owns.
        
        pm.radial( pos=(2, 0, 4 ))
        # Creates a radial field at position (0,2,4) in world coordinates,
        # with default magnitude(1.0), attentuation (1.0),
        # and max distance (5.0).
        
        pm.radial( 'radialField1', e=True, att=0.98 )
        # Edits the attenuation value of the field named radialField1
        
        pm.radial( 'radialField1', q=True, m=True )
        # Queries radialField1 for its magnitude.
        
        pm.radial( 'radialField1', e=True, mxd=10.0 )
        # Changes the maximum distance of the field called
        # "radialField1" to 10.0.
        
        pm.radial( m=2.0 )
        # Creates a radial field with magnitude 2.0 for every active selection.
        # If no there are active
        # selections, creates such a field at world position (0,0,0).
    """

    pass


def nSoft(*args, **kwargs):
    """
    Makes a nSoft body from the object(s) passed on the command line or in the selection list.  The geometry can be a NURBS,
    polygonal, lattice object.  The resulting nSoft body is made up of a hierarchy with a particle shape and a geometry
    shape, thus: T    / \  T   G /      P        Dynamics are applied to the particle shape and the resulting particle
    positions then drive the locations of the geometry's CVs, vertices, or lattice points. With the convert option, the
    particle shape and its transform are simply inserted below the original shape's hierarchy. With the duplicate option,
    the original geometry's transform and shape are duplicated underneath its parent, and the particle shape is placed under
    the duplicate.  Note that any animation on the hierarchy will affect the particle shape as well.  If you do not want
    them, then reparent the structure outside the hierarchy. When duplicating, the nSoft portion (the duplicate) is given
    the name copyOf+ original object name.  The particle portion is always given the name original object name+
    Particles.None of the flags of the nSoft command can be queried.  The nSoft -q command is used only to identify when an
    object is a nSoft body, or when two objects are part of the same nSoft body. See the examples.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``convert`` / ``c``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This tells the command that you want the original object to be the actual deformed object.  The particle shape portion of the nSoft body will be inserted in the  |
    |  | same hierarchy as the original, under the same parent (with one additional intervening transform which is initially the identity).  If no flags are passed, then  |
    |  | this is assumed.  The combination -c -h 1 is not valid; if you have this in your scripts, remove the -h 1.                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``duplicate`` / ``d``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This tells the command that you want to make a copy of the original object and use the copy as the deforming geometry. Input connections to the original object   |
    |  | are duplicated.  You would do this if you wanted to keep the original object in your scene and also have a copy of it that was a nSoft body. This flag and -dh are|
    |  | mutually exclusive.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``duplicateHistory`` / ``dh``                                                                        | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is the same as -d, except that upstream history, is duplicated as well, instead of just input connections. This flag and -d are mutually exclusive.          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``goal`` / ``g``                                                                                     | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is the same as -d, but in addition it tells the command that you want the resulting nSoft body to try to follow the original geometry, using the set goal    |
    |  | weight as the value that controls how strongly it is to follow it.  A value of 1.0 will try to follow exactly, and a value of 0.0 will not follow at all. The     |
    |  | default value is 0.5.  This value must be from 0.0 to 1.0. You could use -d with -g, but it is redundant.  If you want history to be duplicated, you can use -dh  |
    |  | and -g together.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``hideOriginal`` / ``h``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used only when duplicating (-d, -g, or -dh).  If set to true, whichever of the two objects is NOT the nSoft object will be hidden. In other words,   |
    |  | with -d -h true, the original object will be hidden; with -d -c -h 1 the duplicate object will be hidden. You would typically do this if you want to use the non- |
    |  | dynamic object as a goal for the nSoft one (see -g) but you do not want it visible in the scene. The flags -h 1 and -c are mutually exclusive.                    |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.nSoft`
    """

    pass


def nBase(*args, **kwargs):
    """
    Edits one or more nBase objects. Note that nBase objects include nCloth, nRigid and nParticle objects, but the options
    on this command do not currently apply to nParticle objects.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``clearCachedTextureMap`` / ``cct``                                                                  | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Clear the cached texture map for the specified attribute from the nBase.                                          Flag can have multiple arguments, passed either |
    |  | as a tuple or a list.                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``clearStart`` / ``cs``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Indicates that start state should be cleared                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stuffStart`` / ``ss``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Indicates that current state should be stuffed into the start state                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``textureToVertex`` / ``ttv``                                                                        | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Transfer the texture map data for the specified attribute into the related per-vertex attribute.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.nBase`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Stuff the current positions and velocities into nCloth1's startPositions and
        # startVelocities.
        #
        pm.nBase( 'nCloth1', e=True, stuffStart=True )
        # Clear nCloth1's startPositions and startVelocities.
        #
        pm.nBase( 'nCloth1', e=True, clearStart=True )
        # Transfer the texture map data for the thicknessMap attribute into the
        # thicknessPerVertex attribute.
        #
        pm.nBase( 'nCloth1', e=True, textureToVertex='thicknessMap' )
    """

    pass


def dynPref(*args, **kwargs):
    """
    This action modifies and queries the current state of autoCreate rigid bodies, run up to current time, and  run up
    from(previous time or start time). In query mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``autoCreate`` / ``ac``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If on, autoCreate rigid bodies.                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``echoCollision`` / ``ec``                                                                           | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If on, will cause particle systems to echo to the Script Editor the command that they are running for each particle collision event. If off, only the output of   |
    |  | the command will be echoed.                       Flag can have multiple arguments, passed either as a tuple or a list.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``runupFrom`` / ``rf``                                                                               | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If on, run up from previous time; if 2, run up from start time                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``runupToCurrentTime`` / ``rt``                                                                      | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If on, run up the scene to current time                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``saveOnQuit`` / ``sq``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If on, save the current values of preferences to userPrefs file.                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``saveRuntimeState`` / ``sr``                                                                        | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If on, runtime state as well as initial state of all particle objects will be saved to file. If off, only initial state will be saved.                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dynPref`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Sets autoCreate rigid bodies to "on"
        pm.dynPref( autoCreate=1 )
    """

    pass


def nParticle(*args, **kwargs):
    """
    The nParticle command creates a new nParticle object from a list of world space points. If an nParticle object is
    created, the command returns the names of the new particle shape and its associated particle object dependency node. If
    an object was queried, the results of the query are returned. Per particle attributes can be queried using the
    particleId or the order of the particle in the particle array. If an object was edited, nothing is returned.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in per particle attribute query and edit. Specifies the name of the attribute being queried or edited.                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cache`` / ``ch``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns caching on/off for the particle shape.                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``conserve`` / ``c``                                                                                 | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Conservation of momentum control (between 0 and 1).  Specifies the fraction of the particle shape's existing momentum which is conserved from frame to frame. A   |
    |  | value of 1 (the default) corresponds to true Newtonian physics, in which momentum is conserved.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``count`` / ``ct``                                                                                   | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the number of particles in the object.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deleteCache`` / ``dc``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Deletes the particle shapes cache. This command is not undoable.                          Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dynamicAttrList`` / ``dal``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a list of the dynamic attributes in the object.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``floatValue`` / ``fv``                                                                              | *float*                       | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used only in per particle attribute edit.  Specifies that the edit is of a float attribute and must be followed by the new float value.                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``gridSpacing`` / ``grs``                                                                            | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Spacing between particles in the grid.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``inherit`` / ``i``                                                                                  | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Inherit this fraction (0-1) of emitting object's velocity.                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``jitterBasePoint`` / ``jbp``                                                                        | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Base point (center point) for jitters.  The command will create one swatch of jitters for each base point.  It will pair up other flags with base points in the   |
    |  | order they are given in the command line.  If not enough instances of the other flags are availble, the last one on the line with be used for all other instances |
    |  | of -jpb.                                                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``jitterRadius`` / ``jr``                                                                            | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Max radius from the center to place the particle instances.                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lowerLeft`` / ``ll``                                                                               | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Lower left point of grid.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of particle object                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``numJitters`` / ``nj``                                                                              | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Number of jitters (instances) per particle.                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``order`` / ``order``                                                                                | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in per particle attribute query and edit. Specifies the zero-based order (index) of the particle whose attribute is being queried  or edited in the particle |
    |  | array. Querying the value of a per particle attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``particleId`` / ``id``                                                                              | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in per particle attribute query and edit. Specifies the id of the particle whose attribute is being queried or edited. Querying the value of a per particle  |
    |  | attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perParticleDouble`` / ``ppd``                                                                      | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a list of the per-particle double attributes, excluding initial-state, cache, and information-only attributes.                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perParticleVector`` / ``ppv``                                                                      | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a list of the per-particle vector attributes, excluding initial-state, cache, and information-only attributes.                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``p``                                                                                 | *float, float, float*         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | World-space position of each particle.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shapeName`` / ``sn``                                                                               | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify the shape name used for geometry instancing. DO not confuse this with the -n flag which names the particle object.                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``upperRight`` / ``ur``                                                                              | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Upper right point of grid.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``vectorValue`` / ``vv``                                                                             | *float, float, float*         | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used only in per particle attribute edit.  Specifies that the edit is of a vector attribute and must be followed by all three float values for the vector.        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.nParticle`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Creates a particle object with four particles
        pm.nParticle( p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9)] )
        # Result: [nt.Transform(u'nParticle1'), nt.NParticle(u'nParticleShape1')] #
        
        # Returns the age of the particle with id 2 in object particle1
        pm.nParticle( 'particle1', q=True, attribute='age', id=2 )
        
        # Returns the velocity of the 3rd particle in the currently selected
        # particle object
        pm.nParticle( attribute='velocity', q=True, order=3  )
        
        # Edits the velocity of the 7th particle in the currently selected
        # particle object to be 0.0, 1.0, 0.0
        pm.nParticle( e=True, attribute='velocity', order=3, vectorValue=(0.0, 1.0, 0.0) )
        
        # Edits the mass of the particle in "particle1" with id 3 to be 0.7
        pm.nParticle( 'nParticle1', e=True, attribute='mass', id=3, fv=0.7 )
    """

    pass


def setFluidAttr(*args, **kwargs):
    """
    Sets values of built-in fluid attributes such as density, velocity, etc., for individual grid cells or for all cells in
    the grid.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``addValue`` / ``ad``                                                                                | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Add specified value to attribute                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the fluid attribute for which to set values.  Valid attributes are velocity, density, fuel, color, falloff, and temperature.                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``clear`` / ``cl``                                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set this attribute to 0                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``floatRandom`` / ``fr``                                                                             | *float*                       |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this was a scalar (e.g. density) attribute, use a random value in +-VALUE If fv is specified, it is used as the base value and combined with the random value. |
    |  | If the fv flag is not specified, the  base is assumed to be 0.                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``floatValue`` / ``fv``                                                                              | *float*                       |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this was a scalar (e.g. density) attribute, use this value                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lowerFace`` / ``lf``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only valid with -at velocity.  Since velocity values are stored on the edges of each voxel and not at the center, using voxel based indices to set velocity       |
    |  | necessarily affects neighboring voxels.  Use this flag to only set velocity components on the lower left three faces of a voxel, rather than all six.             |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``reset`` / ``re``                                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set this attribute to default value                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``vectorRandom`` / ``vr``                                                                            | *float, float, float*         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this was a vector (e.g. velocity) attribute, use a random value in +-VALUE If vv is specified, it is used as the base value and combined with the random value.|
    |  | If the vv flag is not specified, the  base is assumed to be 0,0,0.                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``vectorValue`` / ``vv``                                                                             | *float, float, float*         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this was a vector (e.g. velocity) attribute, use this value                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``xIndex`` / ``xi``                                                                                  | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only return values for cells with this X index                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``xvalue`` / ``x``                                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only set the first component of the vector-valued attribute specified by the -at/attributeflag.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``yIndex`` / ``yi``                                                                                  | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only return values for cells with this Y index                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``yvalue`` / ``y``                                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only set the second component of the vector-valued attribute specified by the -at/attributeflag.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``zIndex`` / ``zi``                                                                                  | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only return values for cells with this Z index                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``zvalue`` / ``z``                                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only set the third component of the vector-valued attribute specified by the -at/attributeflag.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.setFluidAttr`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # set density for entire fluid
        pm.setFluidAttr( at='density', fv=1.0 )
        # add 3.5 to the density at the cell x=1, y=2, z=3
        pm.setFluidAttr( at='density', ad=True, fv-3.5, xi=1, yi=2, zi=3 )
        # clear the density for the whole fluid
        pm.setFluidAttr( at='density', cl=True )
        # reset the velocity at the cell x=1, y=2, z=3
        pm.setFluidAttr( at='velocity', re=True, xi=1, yi=2, zi=3 )
        # set the velocity at the centers of the voxels on plane y=5
        # to approximately (-1, 0, 0)
        pm.setFluidAttr( at='velocity', vv=(-1, 0, 0), yi=5 )
        # set the Z-component of the velocity at the bottom of cell [0, 0, 0]
        # to exactly 1.3
        pm.setFluidAttr( at='velocity', z=True, xi=0, yi=0, zi=0, fv=1.3 )
        # set the X-component of the velocity at the right of cell [5, 3, 2]
        # (which is also the left of cell [6, 3, 2]) to exactly 4.8
        pm.setFluidAttr( at='velocity', x=True, xi=5, yi=3, zi=2, fv=4.8 )
        # set the density to a random value in the range 0.1 to 0.9
        # the fv flag specfies the base value, and then we add a a
        # random value in the range of -fr to +fr
        pm.setFluidAttr( at='density', fv=0.5, fr=0.4 )
    """

    pass


def soft(*args, **kwargs):
    """
    Makes a soft body from the object(s) passed on the command line or in the selection list.  The geometry can be a NURBS,
    polygonal, lattice object.  The resulting soft body is made up of a hierarchy with a particle shape and a geometry
    shape, thus: T    / \  T   G /      P        Dynamics are applied to the particle shape and the resulting particle
    positions then drive the locations of the geometry's CVs, vertices, or lattice points. With the convert option, the
    particle shape and its transform are simply inserted below the original shape's hierarchy. With the duplicate option,
    the original geometry's transform and shape are duplicated underneath its parent, and the particle shape is placed under
    the duplicate.  Note that any animation on the hierarchy will affect the particle shape as well.  If you do not want
    then, then reparent the structure outside the hierarchy. When duplicating, the soft portion (the duplicate) is given the
    name copyOf+ original object name.  The particle portion is always given the name original object name+ Particles.None
    of the flags of the soft command can be queried.  The soft -q command is used only to identify when an object is a soft
    body, or when two objects are part of the same soft body. See the examples.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``convert`` / ``c``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This tells the command that you want the original object to be the actual deformed object.  The particle shape portion of the soft body will be inserted in the   |
    |  | same hierarchy as the original, under the same parent (with one additional intervening transform which is initially the identity).  If no flags are passed, then  |
    |  | this is assumed.  The combination -c -h 1 is not valid; if you have this in your scripts, remove the -h 1.                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``duplicate`` / ``d``                                                                                | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This tells the command that you want to make a copy of the original object and use the copy as the deforming geometry. Input connections to the original object   |
    |  | are duplicated.  You would do this if you wanted to keep the original object in your scene and also have a copy of it that was a soft body. This flag and -dh are |
    |  | mutually exclusive.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``duplicateHistory`` / ``dh``                                                                        | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is the same as -d, except that upstream history, is duplicated as well, instead of just input connections. This flag and -d are mutually exclusive.          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``goal`` / ``g``                                                                                     | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This is the same as -d, but in addition it tells the command that you want the resulting soft body to try to follow the original geometry, using the set goal     |
    |  | weight as the value that controls how strongly it is to follow it.  A value of 1.0 will try to follow exactly, and a value of 0.0 will not follow at all. The     |
    |  | default value is 0.5.  This value must be from 0.0 to 1.0. You could use -d with -g, but it is redundant.  If you want history to be duplicated, you can use -dh  |
    |  | and -g together.                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``hideOriginal`` / ``h``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used only when duplicating (-d, -g, or -dh).  If set to true, whichever of the two objects is NOT the soft object will be hidden. In other words,    |
    |  | with -d -h true, the original object will be hidden; with -d -c -h 1 the duplicate object will be hidden. You would typically do this if you want to use the non- |
    |  | dynamic object as a goal for the soft one (see -g) but you do not want it visible in the scene. The flags -h 1 and -c are mutually exclusive.                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is obsolete.  If you wish to give your new soft object a name, use the rename command (or from the UI, use the outliner).                       Flag can|
    |  | have multiple arguments, passed either as a tuple or a list.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.soft`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.sphere()
        # Result: [nt.Transform(u'nurbsSphere1'), nt.MakeNurbSphere(u'makeNurbSphere1')] #
        pm.soft( 'nurbsSphere1', c=True )
        # Result: [u'nurbsSphere1Particle'] #
        
        # Creates a sphere named nurbsSphere1 and converts nurbSphere1 into
        # a soft object.  The particle portion of the soft object will
        # be parented (with its own transform) under nurbsSphere1.
        
        pm.sphere()
        # Result: [nt.Transform(u'nurbsSphere2'), nt.MakeNurbSphere(u'makeNurbSphere2')] #
        pm.soft( 'nurbsSphere1', d=True )
        
        # Same as the previous example, except that the soft command will make
        # a duplicate of nurbsSphereShape1.  The resulting soft body will be
        # completely independent of nurbSphere1 and its children.  Input connections
        # to nurbsSphereShape1 will be duplicated, but not any upstream history
        # (in other words, just plain "duplicate").
        
        pm.sphere()
        pm.soft( 'nurbsSphere1', dh=True )
        
        # Same as the previous example, except that upstream history on
        # nurbsSphereShape1 will be duplicated as well (equivalent to
        # "duplicate history").
        
        pm.sphere()
        pm.soft( 'nurbSphere1', g=0.3 )
        
        # This will make a duplicate of the shape under nurbSphere1 (as for -d),
        # and  use it as the shape for the newly created soft object.
        # The original nurbsSphereShape1 will be made a goal for the particles of
        # softy, with a goal weight of 0.3.  This will make those particles try to
        # follow nurbSphere1 loosely as it moves around.
        
        pm.soft( 'foobar', q=True )
        # Returns true if foobar is a soft object.
        
        pm.soft( 'foobar', 'foobarParticles', q=True )
        
        # Returns true if foobar and foobarParticles are parts of the same
        # soft object.  This is useful because when you select a soft body,
        # both the overall transform and the particle transform get put into
        # the selection list.
    """

    pass


def dynGlobals(*args, **kwargs):
    """
    This node edits and queries the attributes of the active dynGlobals node in the scene. There can be only one active node
    of this type. The active dynGlobals node is the first one that was created, either with a createNodecommand or by
    accessing/editing any of the attributes on the node through this command.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``active`` / ``a``                                                                                   | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag returns the name of the active dynGlobals node in the the scene.  Only one dynGlobals node is active. It is the first on created.  Any additional       |
    |  | dynGlobals nodes will be ignored.                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``listAll`` / ``la``                                                                                 | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag will list all of the dynGlobals nodes in the scene.                     Flag can have multiple arguments, passed either as a tuple or a list.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``overSampling`` / ``os``                                                                            | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag will set the current overSampling value for all of the particle in the scene.                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dynGlobals`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.dynGlobals( e=True, os=5 )
        # or
        pm.dynGlobals( os=5 )
        
        # Both of these commands will edit the overSampling attribute of
        # the active dynGlobals node.
    """

    pass


def getFluidAttr(*args, **kwargs):
    """
    Returns values of built-in fluid attributes such as density, velocity, etc., for individual grid cells or for all cells
    in the grid.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the fluid attribute for which to display values.  Valid attributes are force, velocity, density, falloff, fuel, color, and temperature.  (Note that     |
    |  | getting force values is an alternate way of getting velocity values at one time step.)                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lowerFace`` / ``lf``                                                                               | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only valid with -at velocity.  Since velocity values are stored on the edges of each voxel and not at the center, using voxel based indices to set velocity       |
    |  | necessarily affects neighboring voxels.  Use this flag to only set velocity components on the lower left three faces of a voxel, rather than all six.             |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``xIndex`` / ``xi``                                                                                  | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only return values for cells with this X index                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``xvalue`` / ``x``                                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only get the first component of the vector-valued attribute specified by the -at/attributeflag.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``yIndex`` / ``yi``                                                                                  | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only return values for cells with this Y index                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``yvalue`` / ``y``                                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only get the second component of the vector-valued attribute specified by the -at/attributeflag.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``zIndex`` / ``zi``                                                                                  | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only return values for cells with this Z index                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``zvalue`` / ``z``                                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Only get the third component of the vector-valued attribute specified by the -at/attributeflag.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.getFluidAttr`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # get density for entire fluid
        pm.getFluidAttr( at='density' )
        # get density at the cell x=1, y=2, z=3
        pm.getFluidAttr( at='density', xi=1, yi=2, zi=3 )
        # get the velocity at the cell  x=1, y=2, z=3
        pm.getFluidAttr( at='velocity', xi=1, yi=2, zi=3 )
        # get the x-component of the velocity at cell x=1,
        # y=2, z=3
        pm.getFluidAttr( xvalue=True, at='velocity', xi=1, yi=2, zi=3 )
        # get the first component (red) of the rgb vector-valued
        # attribute "color" at the cell x=1, y=2, z=3
        pm.getFluidAttr( xvalue=True, at='color', xi=1, yi=2, zi=3 )
        # get the velocity x component the plane x=5
        pm.getFluidAttr( at='velocity', x=True, xi=5 )
    """

    pass


def particle(*args, **kwargs):
    """
    The particle command creates a new particle object from a list of world space points. If a particle object is created,
    the command returns the names of the new particle shape and its associated particle object dependency node. If an object
    was queried, the results of the query are returned. Per particle attributes can be queried using the particleId or the
    order of the particle in the particle array. If an object was edited, nothing is returned.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in per particle attribute query and edit. Specifies the name of the attribute being queried or edited.                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cache`` / ``ch``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns caching on/off for the particle shape.                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``conserve`` / ``c``                                                                                 | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Conservation of momentum control (between 0 and 1).  Specifies the fraction of the particle shape's existing momentum which is conserved from frame to frame. A   |
    |  | value of 1 (the default) corresponds to true Newtonian physics, in which momentum is conserved.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``count`` / ``ct``                                                                                   | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns the number of particles in the object.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deleteCache`` / ``dc``                                                                             | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Deletes the particle shapes cache. This command is not undoable.                          Flag can have multiple arguments, passed either as a tuple or a list.   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dynamicAttrList`` / ``dal``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a list of the dynamic attributes in the object.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``floatValue`` / ``fv``                                                                              | *float*                       | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used only in per particle attribute edit.  Specifies that the edit is of a float attribute and must be followed by the new float value.                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``gridSpacing`` / ``grs``                                                                            | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Spacing between particles in the grid.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``inherit`` / ``i``                                                                                  | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Inherit this fraction (0-1) of emitting object's velocity.                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``jitterBasePoint`` / ``jbp``                                                                        | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Base point (center point) for jitters.  The command will create one swatch of jitters for each base point.  It will pair up other flags with base points in the   |
    |  | order they are given in the command line.  If not enough instances of the other flags are availble, the last one on the line with be used for all other instances |
    |  | of -jpb.                                                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``jitterRadius`` / ``jr``                                                                            | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Max radius from the center to place the particle instances.                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lowerLeft`` / ``ll``                                                                               | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Lower left point of grid.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of particle object                                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``numJitters`` / ``nj``                                                                              | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Number of jitters (instances) per particle.                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``order`` / ``order``                                                                                | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in per particle attribute query and edit. Specifies the zero-based order (index) of the particle whose attribute is being queried  or edited in the particle |
    |  | array. Querying the value of a per particle attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``particleId`` / ``id``                                                                              | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used in per particle attribute query and edit. Specifies the id of the particle whose attribute is being queried or edited. Querying the value of a per particle  |
    |  | attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perParticleDouble`` / ``ppd``                                                                      | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a list of the per-particle double attributes, excluding initial-state, cache, and information-only attributes.                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perParticleVector`` / ``ppv``                                                                      | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns a list of the per-particle vector attributes, excluding initial-state, cache, and information-only attributes.                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``p``                                                                                 | *float, float, float*         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | World-space position of each particle.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shapeName`` / ``sn``                                                                               | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify the shape name used for geometry instancing. DO not confuse this with the -n flag which names the particle object.                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``upperRight`` / ``ur``                                                                              | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Upper right point of grid.                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``vectorValue`` / ``vv``                                                                             | *float, float, float*         | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used only in per particle attribute edit.  Specifies that the edit is of a vector attribute and must be followed by all three float values for the vector.        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.particle`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Creates a particle object with four particles
        pm.particle( p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9)] )
        # Result: [nt.Transform(u'particle1'), nt.Particle(u'particleShape1')] #
        
        # Returns the age of the particle with id 2 in object particle1
        pm.particle( 'particle1', q=True, attribute='age', id=2 )
        # Result: [0.0] #
        
        # Returns the velocity of the 3rd particle in the currently selected
        # particle object
        pm.particle( attribute='velocity', q=True, order=3  )
        # Result: [0.0, 0.0, 0.0] #
        
        # Edits the velocity of the 7th particle in the currently selected
        # particle object to be 0.0, 1.0, 0.0
        pm.particle( e=True, attribute='velocity', order=3, vectorValue=(0.0, 1.0, 0.0) )
        # Result: [nt.Transform(u'particle1'), nt.Particle(u'particleShape1')] #
        
        # Edits the mass of the particle in "particle1" with id 3 to be 0.7
        pm.particle( 'particle1', e=True, attribute='mass', id=3, fv=0.7 )
        # Result: [nt.Transform(u'particle1'), nt.Particle(u'particleShape1')] #
    """

    pass


def drag(*args, **kwargs):
    """
    Drag exerts a friction, or braking force proportional to the speed of a moving object. If direction is not enabled, the
    drag acts opposite to the current velocity of the object. If direction is enabled, it acts opposite to the component of
    the velocity in the specified direction. The force is independent of the position of the affected object. The transform
    is the associated dependency node. Use connectDynamic to cause the field to affect a dynamic object. If fields are
    created, this command returns the names of each of the fields. If a field was queried, the results of the query are
    returned. If a field was edited, the field name is returned. If object names are provided or the active selection list
    is non-empty, the command creates a field for every object in the list and calls addDynamic to add it to the object. If
    the list is empty, the command defaults to -pos 0 0 0. Setting the -pos flag with objects named on the command line is
    an error.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attenuation`` / ``att``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attentuation rate of field                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionX`` / ``dx``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | X-component of direction.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionY`` / ``dy``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Y-component of direction.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionZ`` / ``dz``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Z-component of direction                                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``magnitude`` / ``m``                                                                                | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Strength of field.                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of field                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perVertex`` / ``pv``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the     |
    |  | force field. If this flag is set to false, then the force is exerted only from the geometric center of the set of points.                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Position in space where you want to place a field. The gravity then emanates from this position in space rather than from an object. Note that you can both use   |
    |  | -pos (creating a field at a position) and also provide object names.                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``useDirection`` / ``ud``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Enable/disable direction. Drag will use -dx/-dy/-dz arguments if and only if this flag is set true.                       Flag can have multiple arguments, passed|
    |  | either as a tuple or a list.                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeExclusion`` / ``vex``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.drag`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Creates a drag field resisting in direction (0,1,0.5).
        pm.drag( name='myDrag', dx=0, dy=1.0, dz=0.5, useDirection=1 )
        # Result: nt.DragField(u'myDrag') #
        
        # Edits the acceleration value of the field myDrag
        pm.drag( 'myDrag', e=True, m=0.75 )
        # Result: nt.DragField(u'myDrag') #
        
        # Queries myDrag for its magnitude
        pm.drag( 'myDrag', q=True, m=True )
        # Result: 0.75 #
    """

    pass


def getDefaultBrush(*args, **kwargs):
    """
    The command returns the name of the default Paint Effects brush.
    
    
    Derived from mel command `maya.cmds.getDefaultBrush`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # get the name of the current brush
        #
        brush = pm.getDefaultBrush()
    """

    pass


def constrain(*args, **kwargs):
    """
    This command constrains rigid bodies to the world or other rigid bodies.                 In query mode, return type is
    based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``barrier`` / ``br``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Creates a barrier constraint.  This command requires one rigid bodies.                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``damping`` / ``d``                                                                                  | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the damping constant. Default value: 0.1 Range: -1000.0 to 1000.0                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionalHinge`` / ``dhi``                                                                       | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Creates a directional hinge constraint.  This command requires two rigid bodies. The directional hinge always maintains the initial direction of its axis.        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``hinge`` / ``hi``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Creates a hinge constraint.  This command requires one or two rigid bodies.                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``interpenetrate`` / ``i``                                                                           | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Allows (or disallows) the rigid bodies defined in the constrain to ipenetrate.                    Flag can have multiple arguments, passed either as a tuple or a |
    |  | list.                                                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``nail`` / ``na``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Creates a nail constraint.  This command requires one rigid body.                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Names the rigid constraint.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``orientation`` / ``o``                                                                              | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set initial orientation of the constraint in world space.  This command is only valid with hinge and barrier constraints Default value: 0.0 0.0 0.0               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``pinConstraint`` / ``pin``                                                                          | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Creates a pin constraint.  This command requires two rigid bodies.                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``p``                                                                                 | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set initial position of the constraint in world space. Default value: 0.0 0.0 0.0 for uni-constraints, midpoint of bodies for deul constraint.                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``restLength`` / ``rl``                                                                              | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the rest length. Default value: 1.0                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``spring`` / ``s``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Creates a spring constraint.  This command requires one or two rigidies.                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``stiffness`` / ``st``                                                                               | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the springs stiffness constant. Default value: 5.0                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.constrain`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # "Nail" a rigid body at position ""0.0, 2.5, 0.0""
        #
        pm.constrain( 'rigidBody1', nail=True, p=(0, 2.5, 0) )
        
        # "Pin" two rigid bodies together at the position ""0.0, 2.5, 0.0"".
        #
        pm.constrain( 'rigidBody1', 'rigidBody2', pin=True, n='pin', p=(0, 2.5, 0) )
        
        # "Hinge" a rigid body at the position ""0.0, 2.5, 0.0"".
        #
        pm.constrain( 'rigidBody1', hinge=True, p=(0, 2.5, 0) )
        
        # Create a barrier for a rigid body which will not allow the rigid body
        # to fall below (in y by default) the plane defined by the
        # barrier point ""0.0, 2.5, 0.0"".
        #
        pm.constrain( 'rigidBody1', barrier=True, p=(0, 2.5, 0) )
        
        # Add a "Spring" to a rigid body at the position ""0.0, 2.5, 0.0""
        # connected on the rigid body at point ""0, 0, 0""
        #
        pm.constrain( 'rigidBody1', spring=True, name='spring', p=(0, 2.5, 0), rl=1.0 )
    """

    pass


def gravity(*args, **kwargs):
    """
    A gravity field simulates the Earth's gravitational force.   It pulls objects in a fixed direction (generally downward)
    entirely independent of their position or mass. The transform is the associated dependency node. Use connectDynamic to
    cause the field to affect a dynamic object. If fields are created, this command returns the names of each of the fields.
    If a field was queried, the results of the query are returned. If a field was edited, the field name is returned. If
    object names are provided or the active selection list is non-empty, the command creates a field for every object in the
    list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0. Setting the
    -pos flag with objects named on the command line is an error. The default for -dx -dy -dz is always the opposite of the
    current up direction. For example, if the current up direction is (0,1,0) (a standard Maya configuration), then the
    gravity default is -dx 0 -dy -1 -dz 0.  The default for -a is 9.8.  9.8 meters per second squared happens to be standard
    Earth gravity, but in fact Maya interprets this value as centimeters per second squared.  If we were to use it as meters
    per second squared then with default Maya units, your particles would vanish almost in the wink of an eye. If you want a
    different value, set it in the gravity option box.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attenuation`` / ``att``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attentuation rate of field                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionX`` / ``dx``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | X-component of direction.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionY`` / ``dy``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Y-component of direction.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionZ`` / ``dz``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Z-component of direction                          Flag can have multiple arguments, passed either as a tuple or a list.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``magnitude`` / ``m``                                                                                | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Strength of field.                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of field                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perVertex`` / ``pv``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the     |
    |  | force field. If this flag is set to false, then the force is exerted only from the geometric center of the set of points.                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Position in space where you want to place a field. The gravity then emanates from this position in space rather than from an object. Note that you can both use   |
    |  | -pos (creating a field at a position) and also provide object names.                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeExclusion`` / ``vex``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.gravity`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.gravity( 'particle1' )
        # Creates a gravity field and adds it to the list of fields
        # owned by particle1.
        
        pm.gravity( pos=(-2, 0, 4) )
        # Creates a gravity field at position (0,2,4) in world coordinates.
        
        pm.gravity( 'MyGravity', e=True, att=10.4 )
        # Changes the gravitational acceleration of the field called
        # "MyGravity" to 10.4.
        
        pm.gravity( dx=0, dy=1.0, dz=0.5 )
        # Creates a gravity field pulling in direction (0,1,0.5) for every
        # active selection. If there is no active selection, it creates this
        # field at world position (0,0,0).
    """

    pass


def uniform(*args, **kwargs):
    """
    A uniform field pushes objects in a fixed direction.  The field strength, but not the field direction, depends on the
    distance from the object to the field location. The transform is the associated dependency node. Use connectDynamic to
    cause the field to affect a dynamic object. If fields are created, this command returns the names of each of the fields.
    If a field was queried, the results of the query are returned. If a field was edited, the field name is returned. If
    object names are provided or the active selection list is non-empty, the command creates a field for every object in the
    list and calls addDynamic to add it to the object. If the list is empty, the command defaults to -pos 0 0 0. Setting the
    -pos flag with objects named on the command line is an error.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attenuation`` / ``att``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Attentuation rate of field                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionX`` / ``dx``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | X-component of direction.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionY`` / ``dy``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Y-component of direction.                                                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``directionZ`` / ``dz``                                                                              | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Z-component of direction                          Flag can have multiple arguments, passed either as a tuple or a list.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``magnitude`` / ``m``                                                                                | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Strength of field.                                                                                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | name of field                                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``perVertex`` / ``pv``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the     |
    |  | force field. If this flag is set to false, then the force is exerted only from the geometric center of the set of points.                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Position in space where you want to place a field. The gravity then emanates from this position in space rather than from an object. Note that you can both use   |
    |  | -pos (creating a field at a position) and also provide object names.                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeExclusion`` / ``vex``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.uniform`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.uniform( dx=0, dy=1.0, dz=0.5 )
        # Result: nt.UniformField(u'uniformField1') #
        # Creates a uniform field pushing in direction (0,1,0.5) for every
        # active selection. If there is no active selection, it creates this
        # field at world position (0,0,0).
        
        pm.uniform( 'uniformF', e=True, att=0.98 )
        # edits the acceleration value of the field uniformF
        pm.uniform( 'uniformF', q=True, att=1 )
        # queries uniformF for its acceleration value
    """

    pass


def connectDynamic(*args, **kwargs):
    """
    Dynamic connection specifies that the force fields, emitters, or collisions of an object affect another dynamic object.
    The dynamic object that is connected to a field, emitter, or collision object is influenced by those fields, emitters
    and collision objects. Connections are made to individual fields, emitters, collisions.  So, if an object owns several
    fields, if the user wants some of the fields to affect an object, s/he can specify each field with a -fflag; but if the
    user wants to connect all the fields owned by an object, s/he can specify the object name with the -fflag. The same is
    true for emitters and collisions. Different connection types (i.e., for fields vs. emitters) between the same pair of
    objects are logically independent. In other words, an object can be influenced by another object's fields without being
    influenced by its emitters or collisions. Each connected object must be a dynamic object. The object connected to can be
    any object that owns fields, emitters, etc.; it need not be dynamic. Objects that can own influences are particles,
    geometry objects (nurbs and polys) and lattices.  You can specify either the shape name or the transform name of the
    object to be influenced.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``addScriptHandler`` / ``ash``                                                                       | *script*                      | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Registers a script that will be given a chance to handle calls to the dynamicConnect command. This flag allows other dynamics systems to override the behaviour of|
    |  | the connectDynamic command. You must pass a Python function as the argument for this flag, and that function must take the following keyword arguments: fields,   |
    |  | emitters, collisionObjects and objects. The python function must return True if it has handled the call to connectDynamic. In the case that the script returns    |
    |  | true, the connectDynamic command will not do anything as it assumes that the work was handled by the script. If all of the callbacks return false, the            |
    |  | connectDynamic command will proceed as normal.  The addScriptHandler flag may not be used with any other flags. When the flag is used, the command will return a  |
    |  | numerical id that can be used to deregister the callback later (see the removeScriptHandler flag)                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``collisions`` / ``c``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Connects each object to the collision models of the given object.                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``delete`` / ``d``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Deletes existing connections.                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``emitters`` / ``em``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Connects each object to the emitters of the given object.                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fields`` / ``f``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Connects each object to the fields of the given object.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeScriptHandler`` / ``rsh``                                                                    | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to remove a callback that was previously registered with the addScriptHandler flag. The argument to this flag is the numerical id returned by   |
    |  | dynamicConnect when the addScriptHandler flag was used. If this flag is called with an invalid id, then the command will do nothing.  This flag may not be used   |
    |  | with any other flag.                      Flag can have multiple arguments, passed either as a tuple or a list.                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.connectDynamic`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.connectDynamic( 'Book', c='Floor' )
        # Connects the dynamic object "Book" to the collision model of the
        # "Floor". This means that the book will collide with and bounce off of
        # the floor.
        
        pm.connectDynamic( 'Moon', 'Spaceship', f='Moon' )
        # Connects dynamic object "Spaceship" to the all fields and emitters
        # owned by "Moon".
        
        pm.connectDynamic( 'Spaceship', f='newtonField1' )
        # Connects dynamic object "Spaceship" to "newtonField1" owned by "Moon".
        
        pm.connectDynamic( 'Moon', f='newtonField1' )
        # If the selection list consists of "Spaceship", connects dynamic object
        # "Spaceship" to "newtonField1" and all emitters owned by "Moon".
        
        pm.connectDynamic( 'Spaceship', d=True, f='Moon' )
        # Deletes the field connection between all the fields owned by "Moon" and
        # "Spaceship". Note that the command establishing the connection need not
        # be in the undo queue.
        
        pm.connectDynamic( 'Spaceship', d=True, f='newtonField1' )
        # Deletes the field connection between "newtonField1" owned by "Moon" and
        # "Spaceship".
    """

    pass


def addPP(*args, **kwargs):
    """
    Adds per-point (per-cv, per-vertex, or per-particle) attribute capability for an attribute of an emitter or field.  The
    -atr flag identifies the attribute.  If no attribute is named, addPP returns a warning and does nothing. The command
    adds any other necessary attributes wherever they are needed, and makes all necessary connections.  If any of the
    attributes already exist, the command simply connects to them.  The command also toggles any relevant attributes in the
    emitter or field to indicate that per-point capability is being used. The command adds a separate per-point attribute to
    the owning object for each emitter/field.  For example, for emission rate, there is a separate ratePP for each emitter.
    These attributes are named according to the convention emitter/field nameattr namePP.  For example, if a particle shape
    owned an emitter smoke, that shape would get attribute smokeRatePP.The name of the object must be the emitter or field
    for which per-point capability is to be added (or the name of its parent transform).  The addPP command adds the per-
    point capability for that emitter or field but not for any others owned by the same object.  If per-point capability is
    not supported for a named object, the command will issue a warning, but will continue executing for any other objects
    which were valid. If no objects are named, addPP uses any objects in the current selection list for which the specified
    attribute is applicable.  (For example, it would add per-point rate for all selected emitters.) If addPP detects that
    the owner object has left-over attributes from a deleted emitter, it will remove those attributes before adding the new
    ones.  Thus, you can delete the emitter, make a new one, and run addPP again, and addPP will clean up after the deleted
    emitter.  This is most commonly used if you have a geometry emitter and then decide to change the geometry.  Likewise,
    if addPP detects that some cvs or vertices have been added to the geometry, then it will expand the corresponding multi-
    attributes as necessary.  However, if it detects that some cvs/vertices have been removed, it will not remove any
    entries from the multi.  See the user manual for more discussion.
    
    Modifications:
      - returns a list of PyNode objects
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``atr``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Name of attribute to which you wish to add PP capability. Currently the only attribute supported is rate (for emitters).                          Flag can have   |
    |  | multiple arguments, passed either as a tuple or a list.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.addPP`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        import maya.cmds as cmds
        
        pm.emitter( n='myEmitter1' )
        # Result: nt.PointEmitter(u'myEmitter1') #
        pm.particle( n='myParticle1' )
        # Result: [nt.Transform(u'myParticle1'), nt.Particle(u'myParticle1Shape')] #
        pm.connectDynamic( 'myParticle1', em='myEmitter1' )
        # Result: [u'myParticle1Shape'] #
        pm.select( 'myParticle1' )
        pm.emitter( n='myEmitter2' )
        # Result: nt.Transform(u'myParticle1') #
        pm.particle( n='myParticle2' )
        # Result: [nt.Transform(u'myParticle2'), nt.Particle(u'myParticle2Shape')] #
        pm.connectDynamic( 'myParticle2', em='myEmitter2' )
        # Result: [u'myParticle2Shape'] #
        
        pm.addPP( 'myEmitter2', atr='rate' )
        # Result: [nt.PointEmitter(u'myEmitter2')] #
        
        # Suppose that myEmitter2 is owned by a particle shape, "myParticle1."
        # addPP will add an attribute "myEmitter2RatePP" to myParticle1, will connect
        # myParticle1.myEmitter2RatePP to myEmitter2.ratePP, and will set myEmitter2.useRatePP
        # to true.
    """

    pass


def rigidBody(*args, **kwargs):
    """
    This command creates a rigid body from a polygonal or nurbs surface.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``active`` / ``act``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Creates a rigid body that is active.  An active rigid body accepts and causes collisions and is effected by dynamic fields.  This is the default.                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``angularVelocity`` / ``av``                                                                         | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Current angular velocity of rigid body.                                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``applyForceAt`` / ``afa``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Determines how forces are applied to the rigid body. The choices are centerOfMass | boundingBox | verticesOrCVs. Default: boundingBox                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``bounciness`` / ``b``                                                                               | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the restitution (or bounciness) of the rigid body. Range:   0.0 - 2.0 Default: 0.6                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cache`` / ``c``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns caching on (1) or off (0) for the rigid body. Default: off                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``centerOfMass`` / ``com``                                                                           | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the center of mass (x,y,z) of the rigid body. Default: actual center of mass.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``collisions`` / ``cl``                                                                              | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Truns collisions on/off for the rigid body.  If the collisions are turned of the rigid body will not collide with any other rigid body. Default: on.              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``contactCount`` / ``cc``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | returns the current contact count for the rigid body.                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``contactName`` / ``cn``                                                                             | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | returns all the rigid body names which are in contact with this shape.  One name for each contact will be returned.                       Flag can have multiple  |
    |  | arguments, passed either as a tuple or a list.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``contactPosition`` / ``cp``                                                                         | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | returns all the contact position.  One position for each contact will be returned.                                                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``damping`` / ``dp``                                                                                 | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the damping value of the rigid body. Range:   -2.0 - 2.0 Default: 0.0                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``deleteCache`` / ``dc``                                                                             | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Deletes the cache (if one exists) of the rigid body.                                                                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dynamicFriction`` / ``df``                                                                         | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the dynamic friction for the rigid body. Range:   0.0 - 1.0 Default: 0.2                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``force`` / ``f``                                                                                    | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Current force on the rigid body.                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``ignore`` / ``ig``                                                                                  | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Causes the rigid body to be ignored in the rigid solver. Default: off                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``impulse`` / ``i``                                                                                  | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Applies an impulse (instantaneous) force on a rigid body. Default: 0.0 0.0 0.0                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``impulsePosition`` / ``imp``                                                                        | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The position at which the impulse is applied. Default: the bodies center of mass.                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``initialAngularVelocity`` / ``iav``                                                                 | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the initial angular velocity of the rigid body. Default: 0.0 0.0 0.0                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``initialVelocity`` / ``iv``                                                                         | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the initial velocity of the rigid body. Default: 0.0 0.0 0.0                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``layer`` / ``l``                                                                                    | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the collision layer of the rigid body.  Only rigid bodies in the same collision layer can collide with each other. Range:   = 0 Default: 0.                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``lockCenterOfMass`` / ``lcm``                                                                       | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Locks the center of mass for the rigid body. Default: off                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mass`` / ``m``                                                                                     | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the mass of the rigid body. Range:   0 Default: 1.0                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Assigns the rigid body the given name.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``orientation`` / ``o``                                                                              | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the initial orientation (x,y,z) of the rigid body. Default: current orientation.                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``particleCollision`` / ``pc``                                                                       | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Turns the ability for a rigid body to collide with particles on and off.  The particles will exert a force on the rigid body. Default: off                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``passive`` / ``pas``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Creates a rigid body that is passive.  A passive rigid body does not react to collisions but active rigid bodies can collide with it. Dynamic Fields will not     |
    |  | effect a passive rigid body.  Only passive rigid bodies can be keyframed.                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``p``                                                                                 | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the initial position (x,y,z) of the rigid body. Default: current position.                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeShape`` / ``rs``                                                                             | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``solver`` / ``slv``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The name of the solver which this rigid node is to resided.  If the solver does not exists then the rigid body will not be created.  If the edit flag is thrown   |
    |  | add the solver exists, the rigid body will be moved to that solver.                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``spinImpulse`` / ``si``                                                                             | *float, float, float*         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Applies an spin impulse (instantaneous rotational) force on a rigid body. Default: 0.0 0.0 0.0                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``standInObject`` / ``sio``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Causes the simulator to use a stand in object for the simulation. The choices are none | cube | sphere. The default is none. Default: none                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``staticFriction`` / ``sf``                                                                          | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the static friction for the rigid body. Range:   0.0 - 1.0 Default: 0.2                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``tesselationFactor`` / ``tf``                                                                       | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the tesselation factor for a rigid body surface. Range:   = 10 Default: 200.                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``velocity`` / ``vel``                                                                               | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Current velocity of rigid body.                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.rigidBody`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # Creates a rigid body with a initial velocity of 10 in the x
        # direction, a bounciness of 0.5 and a static friction coefficent
        # of 0.4.
        #
        pm.rigidBody( n='myRigidBody', active=True, iv=(10, 0, 0), b=0.5, sf=0.4 )
    """

    pass


def dynExpression(*args, **kwargs):
    """
    This command describes an expression that belongs to the specified particle shape.  The expression is a block of code of
    unlimited length with a C-like syntax that can perform conversions, mathematical operations, and logical decision making
    on any numeric attribute(s) or per-particle attribute(s) in the scene.  One expression can read and alter any number of
    these attributes.  Every particle shape in your scene has three expressions, one for the runtimeBeforeDynamics, one for
    the runtimeAfterDynamics and one for creation time.  The create expression gets executed for every particle in the
    object whose age is 0.0.  The runtime expression gets executed for each particle with an age greater then 0.0.  Unlike
    expressions created with the expressioncommand, particle expressions always exist and are a part of the owning particle
    object's shape.  They default to empty strings, but they are always there.  Because of this, there is no need to use the
    '-e' flag.  Every call to the dynExpression command is considered an edit by default.  Per-particle attributes are those
    attributes of a particle shape that have a potentially different value for each particle in the object.  Examples of
    these include positionand velocity. If this command is being sent by the command line or in a script, then the user
    should be sure to embed escaped newlines (\n), tabs (\t) for clarity when reading them in the expression editor.  Also,
    quotes in an expression must be escaped (\) so that they are not confused by the system as the end of your string.  When
    using the expression editor, these characters are escaped for you unless they are already within quotes. This type of
    expression is executed during the evaluation of the dynamics.  If an output of the expression is requested before that,
    then the dynamics will be force to compute at that time.  If dynamics is disabled, then these expressions will have no
    effect.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``creation`` / ``c``                                                                                 | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells the command that the string passed will be a creation expression for the particle shape.  This means that this expression will be executed when a particle  |
    |  | is emitted or at the beginning of the scene for existing particles.                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``runtime`` / ``r``                                                                                  | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``runtimeAfterDynamics`` / ``rad``                                                                   | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells the command that the string passed will be a runtime expression for the particle shape.  This expression will be executed after dynamics whenever a         |
    |  | particle's age is greater then zero (0).                        Flag can have multiple arguments, passed either as a tuple or a list.                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``runtimeBeforeDynamics`` / ``rbd``                                                                  | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Tells the command that the string passed will be a runtime expression for the particle shape.  This expression will be executed before dynamics whenever a        |
    |  | particle's age is greater then zero (0).                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``string`` / ``s``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Set the expression string. This is queriable with the -q/query flag and the -rbd/runtimeBeforeDynamics, the -rab/runtimeAfterDynamics or the -c/creation flag.    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dynExpression`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.dynExpression( 'particleShape1', s='rgbPP = "" 1, 0, 0 ""', c=1 )
        
        # This expression tells particleShape1 that whenever new particles are
        # created for this object, then their color should start out as "" 1, 0, 0 "",
        # which is red.
        
        pm.dynExpression( 'particleShape1', s='rgbPP = rgbPP * .9;', rbd=1 )
        
        # This sets the runtime before dynamics expression for rgbPP.  When a particle is
        # first "born", its color will be red from the previous example.  Every other frame after
        # that, its color is reduced by 10 percent each time the expression is executed.
        
        pm.dynExpression( 'particleShape1', s='rgbPP = rgbPP * .9;', rad=1 )
        
        # This sets the runtime after dynamics expression for rgbPP.  When a particle is
        # first "born", its color will be red from the previous example.  Every other frame after
        # that, its color is reduced by 10 percent each time the expression is executed.
    """

    pass


def event(*args, **kwargs):
    """
    The event command assigns collision events to a particle object. Collision events are stored in multi-attributes in the
    particle shape. The event command returns the event name.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``count`` / ``ct``                                                                                   | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Collision number (for each particle) to which this event applies. Zero (the default) indicates that it applies to all collisions.                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``delete`` / ``d``                                                                                   | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Delete the specified event.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``dieAtCollision`` / ``die``                                                                         | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Particle dies at the collision specified by count.If no count value is given, die at first collision.                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``emit`` / ``em``                                                                                    | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Emit n additional particles into the assigned target object. The original (colliding) particle survives as well, and remains in its original object.  The new     |
    |  | particles have age zero and mass equal to the emitting particle. They use the velocity inheritance parameter of the target object.                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``idNumber`` / ``id``                                                                                | *int*                         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``list`` / ``ls``                                                                                    | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | List all events for the chosen shape, like this: event1Name event2Name ... If no shape identified, list all events for all shapes, like this: shape1Name          |
    |  | event1Name shape2Name event2Name... Returns a string array.                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Assign a name to an event you are creating, or identify an event you wish to edit, query, or delete. See examples.                                                |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``proc`` / ``pr``                                                                                    | *script*                      | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specify a MEL proc to be called each time the event occurs. This must be a global proc with arguments as follows: global proc procName( string obj, int id, string|
    |  | objHit ); Arguments passed in are the name of the particle object, the id of the particle which collided, and the name of the object collided with.  You can use  |
    |  | particle -id -q to get values of the particle's attributes.                   Flag can have multiple arguments, passed either as a tuple or a list.               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``random`` / ``r``                                                                                   | *bool*                        | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Used with -split and -emit flags.  If -random is set true and -split or -emit is set to n, then a random number of particles uniformly distributed between 1 and n|
    |  | will be created at the event.                                                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rename`` / ``re``                                                                                  | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Assign a new name to an event you are editing. See examples.                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``select`` / ``s``                                                                                   | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is obsolete.  See the -name flag.                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``split`` / ``spl``                                                                                  | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Colliding particle splits into specified number of new particles. These new particles become part of the assigned target object. If no target has been assigned,  |
    |  | they become part of the same object.  The new particles inherit the current age of the particle that split.  They use the velocity inheritance parameter of the   |
    |  | target object.  If you set both emit and split, the event will do both: first emit new particles, then split the original one. This is a change from earlier      |
    |  | versions where emit and split were mutually exclusive.                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``spread`` / ``sp``                                                                                  | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Particles created at collision will spread out a random amount from the rebound direction of the colliding particle.  The spread is specified as a fraction (0-1) |
    |  | of 90 degrees.  If spread is set at 0 (the default) all the new particles created may coincide.                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``target`` / ``t``                                                                                   | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Target object for emitting or split particles. New particles created through the -emit or -split flags join this object.                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.event`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.event( em=2, t='newCloud' )
        # At every collision, emit two new particles into the object
        # newCloud. The original colliding particles will survive and
        # remain in their original object. This event will be
        # assigned to the currently selected object.
        
        pm.event( em=2 )
        # At every collision, emit two new particles into the same object.
        
        pm.event( count=1, em=2 )
        # At the first collision for each particle, emit two new particles
        # into the same object.
        # Subsequent collisions for that same particle will not cause any
        # additional particles to be emitted. However, the new particles will
        # each emit two new ones at their first collision, since they also
        # belong to the object for which this event has been assigned.
        
        pm.event( die=1, count=2 )
        # All particles in the selected object will die at their second
        # collision.
        
        pm.event( 'myCloud', name='foo', count=1, q=1 )
        # Return the current value of the count parameter for the event "foo"
        # assigned to particle shape myCloud.  The order of the flags is
        # important.  Thef lag you are querying (in this case, -count) must
        # come before the -q.  The -name flag and the particle object name must
        # come after.
        
        pm.event( 'myCloud', d=True, name='foo' )
        # Delete the event "foo" assigned to particle shape myCloud.
        
        pm.event( 'myCloud', e=True, name='foo', emit=2 )
        # Edit the "emit" value of the event "foo" assigned to
        # particle shape myCloud.
        
        pm.event( 'myCloud', proc='myProc' )
        # Call the MEL proc "myProc(name, id, name) each time a particle
        # of myCloud collides with anything.
        
        pm.event( name='oldName', e=1, rename='newName' )
        # For the selected particle shape, rename the event "oldName" to "newName."
    """

    pass


def fluidEmitter(*args, **kwargs):
    """
    Creates an emitter object. If object names are provided or if objects are selected, applies the emitter to the
    named/selected object(s)in the scene.  Fluid will then be emitted from each. If no objects are named or selected, or if
    the -pos option is specified, creates a positional emitter. If an emitter was created, the command returns the name of
    the object owning the emitter, and the name of emitter shape. If an emitter was queried, the command returns the results
    of the query.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``cycleEmission`` / ``cye``                                                                          | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Possible values are noneand frame.Cycling emission restarts the random number stream after a specified interval.  This can either be a number of frames or a      |
    |  | number of emitted particles.  In each case the number is specified by the cycleInterval attribute. Setting cycleEmission to frameand cycleInterval to 1 will then |
    |  | re-start the random stream every frame. Setting cycleInterval to values greater than 1 can be used to generate cycles for games work.                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cycleInterval`` / ``cyi``                                                                          | *int*                         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the number of frames or particles between restarts of the random number stream.  See cycleEmission.  Has no effect if cycleEmission is set to None.     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``densityEmissionRate`` / ``der``                                                                    | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Rate at which density is emitted.                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fluidDropoff`` / ``fdr``                                                                           | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Fluid Emission Dropoff in volume                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``fuelEmissionRate`` / ``fer``                                                                       | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Rate at which  is emitted.                        Flag can have multiple arguments, passed either as a tuple or a list.                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``heatEmissionRate`` / ``her``                                                                       | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Rate at which density is emitted.                                                                                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxDistance`` / ``mxd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Maximum distance at which emission ends.                                                                                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minDistance`` / ``mnd``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Minimum distance at which emission starts.                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Positional emitter at world space location (x,y,z).                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rate`` / ``r``                                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Rate at which particles emitted (can be non-integer). For point emission this is rate per point per unit time. For surface emission it is rate per square unit of |
    |  | area per unit time.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``torusSectionRadius`` / ``tsr``                                                                     | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``typ``                                                                                   | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Type of emitter. The choices are omni | dir | direction | surf | surface | curve | curv. The default is omni. The full definition of these types are:             |
    |  | omnidirectional point emitter, directional point emitter, surface emitter, or curve emitter.                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeOffset`` / ``vof``                                                                           | *float, float, float*         | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Volume offset of the emitter.  Volume offset translates the emission volume by the specified amount from the actual emitter location.  This is in the emitter's   |
    |  | local space.                                                                                                                                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeShape`` / ``vsh``                                                                            | *unicode*                     | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Volume shape of the emitter.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than none, determines a 3-D volume within which   |
    |  | particles are generated. Values are: cube,sphere,cylinder,cone,torus.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``volumeSweep`` / ``vsw``                                                                            | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Volume sweep of the emitter.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.fluidEmitter`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.fluidEmitter( pos=(0, 0, 0), type='omni', der=1, her=2, fer=3, fdr=1.5, r=100.0, cye='none', cyi=1, mxd=0, mnd=0 )
        # Result: nt.FluidEmitter(u'fluidEmitter1') #
        pm.connectDynamic( 'fluidShape1', em='emitter1' )
        
        # Creates an omni emitter that's emitting density, heat and fuel
        # into fluidShape1
    """

    pass


def particleFill(*args, **kwargs):
    """
    This command generates an nParticle system that fills the selected object with a grid of particles.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``closePacking`` / ``cp``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | If this is on then the particles are positioned as closely as possible in a hexagonal close packing arrangement. Otherwise particles are packed in a uniform grid |
    |  | lattice.                                        Flag can have multiple arguments, passed either as a tuple or a list.                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``doubleWalled`` / ``dw``                                                                            | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag should be used if the thickness of the object to fill has been modeled( for example a mug ). Otherwise the particles will be created inside the wall.   |
    |  | Note that doubleWalled will not handle some cases very well. For example a double walled donut shape may get the center region of the donut filled. In cases like |
    |  | this it may be better to make the internal wall a separate mesh then fill that without using doubleWalled.                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxX`` / ``mxx``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The fill max bounds of the particles in X relative to the X bounds of the object. A value of zero is totally empty and one is totally full. The default value is  |
    |  | 1, or fully filled.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxY`` / ``mxy``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The fill max bounds of the particles in Y relative to the Y bounds of the object. A value of zero is totally empty and one is totally full. The default value is  |
    |  | 1, or fully filled.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``maxZ`` / ``mxz``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The fill max bounds of the particles in Z relative to the Z bounds of the object. A value of zero is totally empty and one is totally full. The default value is  |
    |  | 1, or fully filled.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minX`` / ``mnx``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The fill lower bounds of the particles in X relative to the X bounds of the object. A value of zero is totally full and one is totally empty. The default value is|
    |  | 0, or fully filled.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minY`` / ``mny``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The fill lower bounds of the particles in Y relative to the Y bounds of the object. A value of zero is totally full and one is totally empty. The default value is|
    |  | 0, or fully filled.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``minZ`` / ``mnz``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | The fill lower bounds of the particles in Z relative to the Z bounds of the object. A value of zero is totally full and one is totally empty. The default value is|
    |  | 0, or fully filled.                                                                                                                                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``particleDensity`` / ``pd``                                                                         | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This controls the size of the particles. At a value of 1.0 the particle size will exactly match the grid spacing determined by the resolution parameter and the   |
    |  | object bounds. Particles which overlap the surface will be rejected even if the center of the particle is inside.                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``resolution`` / ``rs``                                                                              | *int*                         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This determines the total number of particles generated. It represent the resolution along the largest axis of the object's bounding box. For a cube shape the    |
    |  | total potential particles will be the cube of the resolution. For other shapes it will be less. The default value for this flag is 10, so 1000 particles could be |
    |  | generated for a cube shape.                                                                                                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.particleFill`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # create a poly torus with particles filling interior
        pm.polyTorus()
        # Result: [nt.Transform(u'pTorus1'), nt.PolyTorus(u'polyTorus1')] #
        pm.particleFill()
    """

    pass


def resampleFluid(*args, **kwargs):
    """
    A command to extend the fluid grid, keeping the voxels the same size, and keeping the existing contents of the fluid in
    the same place. Note that the fluid transform is also modified to make this possible.            In query mode, return
    type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``resampleDepth`` / ``rd``                                                                           | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Change depth resolution to this value                                     Flag can have multiple arguments, passed either as a tuple or a list.                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``resampleHeight`` / ``rh``                                                                          | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Change height resolution to this value                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``resampleWidth`` / ``rw``                                                                           | *int*                         | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Change width resolution to this value                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.resampleFluid`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # set width resolution to 3
        pm.resampleFluid( rw=3 )
        # set height resolution to 12
        pm.resampleFluid( rh=12 )
        # set all  resolutions to 20
        pm.resampleFluid( rw=20, rh=20, rd=20 )
    """

    pass


def arrayMapper(*args, **kwargs):
    """
    Create an arrayMapper node and connect it to a target object. If the -type flag is used, then this command also creates
    an external node used for computing the output values. If the input attribute does not already exist, it will be
    created. The output attribute must exists. If    a flag is omitted, the selection list will be used to supply the needed
    objects. If none are found, that action is omitted.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``destAttr`` / ``da``                                                                                | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the attribute which will be the downstream connection for the output data from the mapper node. The attribute type will be used to determine which      |
    |  | output attribute to use: float array gets outValuePP, vector array gets outColorPP. If the flag is omitted, no output connection is made.                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``inputU`` / ``iu``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the upstream attribute to connect to the mapper's uCoordPP attribute. If the flag is omitted, no input connection is made.                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``inputV`` / ``iv``                                                                                  | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the upstream attribute to connect to the mapper's vCoordPP attribute. If the flag is omitted, no input connection is made.                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``mapTo`` / ``mt``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies an existing node to be used to compute the output values. This node must be of the appropriate type. Currently, only ramp nodes may be used.            |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``target`` / ``t``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the target object to be connected to.                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``type`` / ``ty``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the node type to create which will be used to compute the output values. Currently, only ramp is valid. If the flag is omitted, no connection is made   |
    |  | and the external node is not created.                                                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.arrayMapper`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.arrayMapper( target='particle1', destAttr='rgbPP', inputV='ageNormalized', type='ramp' )
    """

    pass


def collision(*args, **kwargs):
    """
    The collision command causes particles to collide with geometry. It also allows you to specify values for the surface
    properties (friction and resilience) of the collision.  These values are stored in the geoConnector node for the
    geometry object.  Unlike earlier versions of Maya, there is no separate collision node.If a soft object is in the
    selection list, the collision command assumes that you want to make it a collider.  In order to make the soft object
    collide with something use, use connectDynamic -c.  The collision menu option sorts this out using the lead object rule
    and issues the necessary commands. On creation, this command returns a string arrayof the geometry names that were setup
    for particle collision.When the command is used to query information, there are several possible return types. These
    include: If the -resilience or -friction flag is passed on the command line and a single collision geometry is either
    selected or on the command line, then resilience or friction value for that collision geometry is returned as a single
    floatvalue.If the -resilience or -friction flag is passed on the command line and a single collision geometry and a
    single particle object are either selected or on the command line, then two results might occur. If the particle object
    is not set up to collide with the geometry, then an error is displayed stating that.  If the objects are set up to
    collide with each other, then the resilience or friction value that the particle object is using for collisions with the
    geometry is returned as a single floatvalue.  This can be different than the geometry's resilience and friction, because
    the user may break the connection from the geometry's geoConnector node's resilience or friction to the particle, and
    set a different value in the particle's collisionResilience, collisionFriction or collisionOffset attribute that is used
    for that geometry.  This allows the user to make each particle respond to the same surface differently. If neither flag
    is pass on the command line and a single geometry and single particle object are either selected or on the command line,
    then a single integervalue of 1 is returned if the objects are set up to collide with each other, and 0 is returned if
    they are not. Lastly, if no flags are passed on the command line and a single particle object is either selected or on
    the command line, then a string arraywith the names of all geometries that the particle object will collide against and
    the multiIndex that the geometries are connected to is returned.  The array is formatted as follows: pPlaneShape1:0
    pPlaneShape2:2 nurbsSphereShape1:3 ...where the number following the :is the multiIndex.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``friction`` / ``f``                                                                                 | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Friction of the surface.  This is the amount of the colliding particle's velocity parallel to the surface which is removed when the particle collides. A value of |
    |  | 0 will mean that no tangential velocity is lost, while a value of 1 will cause the particle to reflect straight along the normal of the surface.                  |
    |  | Flag can have multiple arguments, passed either as a tuple or a list.                                                                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is obsolete.  In maya 2.0, there is no longer a separate collision node,thus there is nothing to name.  See the collision documentation.  This flag is  |
    |  | included only to allow scripts written with older versions of Maya to run. It will give you a warning message but will not do anything.                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``offset`` / ``o``                                                                                   | *float*                       |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``resilience`` / ``r``                                                                               | *float*                       | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Resilience of the surface.  This is the amount of the colliding particle's velocity reflected along the normal of the surface.  A value of 1 will give perfect    |
    |  | reflection, while a value of 0 will have no reflection along the normal of the surface.                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.collision`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.collision( 'nurbsSphere1', 'particle1', r=.75, f=.1 )
        # Causes particles of particle1 to collide with nurbsSphere1,
        # and sets a resilience value of 0.75 and a friction value of 0.1
        # for the surface.
        
        pm.collision( 'nurbsSphere1', q=True, f=1 )
        # Returns the friction value stored in the geoConnector for nurbsSphere1.
        
        pm.collision( 'particleShape1', 'nurbsSphere1', q=True, f=1 )
        # Returns the friction value that particleShape1 is using for collisions
        # against nurbsSphere1.  This may be the same as the friction stored in
        # nurbsSphere1's geoConnector.  Or, if the user broke that connection,
        # then it is whatever value is in the particleShape1's collisionFriction
        # attribute that is used for collision with nurbsSphere1.
        
        pm.collision( 'nurbsSphere1', 'particleShape1', q=True )
        # Returns whether or not particleShape1 is checking for collisions
        # against nurbsSphere1.
        
        pm.collision( 'particleShape1', q=True )
        # Returns all of the geometries that particleShape1 is colliding with.
    """

    pass


def particleInstancer(*args, **kwargs):
    """
    This command is used to create a particle instancer node and set the proper attributes in the particle shape and in the
    instancer node.  It will also create the connections needed between the particle shape and the instancer node.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``addObject`` / ``a``                                                                                | *bool*                        | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``aimAxis`` / ``aa``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the aim axis of the instanced objects.                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``aimDirection`` / ``ad``                                                                            | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the aim direction of the instanced objects.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``aimPosition`` / ``ap``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the aim position of the instanced objects.                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``aimUpAxis`` / ``aua``                                                                              | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the aim up axis of the instanced objects.                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``aimWorldUp`` / ``awu``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the aim world up of the instanced objects.                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``attributeMapping`` / ``am``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag queries the particle attribute mapping list.                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cycle`` / ``c``                                                                                    | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the cycle attribute for the instancer node.  The options are none, sequential. The default is none.                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cycleStartObject`` / ``sto``                                                                       | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the cycle start object of the instanced objects.                                             |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cycleStep`` / ``cs``                                                                               | *float*                       | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see               |
    |  | cycleStepUnits).                                                                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``cycleStepUnits`` / ``csu``                                                                         | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the cycle step unit attribute for the instancer node. The options are framesor seconds.  The default is frames.                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``index`` / ``i``                                                                                    | *int*                         | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag is used to query the name of the ith instanced object.                                                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``instanceId`` / ``id``                                                                              | *unicode*                     | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag queries the particle attribute name to be used for the id of the instanced objects.                                     Flag can have multiple          |
    |  | arguments, passed either as a tuple or a list.                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``levelOfDetail`` / ``lod``                                                                          | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the level of detail of the instanced objects.  The options are geometry, boundingBoxor boundingBoxes.  The default is geometry.         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the name of the instancer node.                                                                                                         |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``object`` / ``obj``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -addObject and -remove flags.  |
    |  | If neither of these flags is specified on the command line then -addObject is assumed.                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``objectIndex`` / ``oi``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the object index of the instanced objects.                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``particleAge`` / ``age``                                                                            | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the age of the instanced objects.                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``p``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | DEFAULT worldPositionThis flag sets or queries the particle attribute name to be used for the positions of the instanced objects.  By default the attribute is    |
    |  | worldPosition.                                                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``removeObject`` / ``rm``                                                                            | *bool*                        | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag indicates that objects specified by the -object flag will be removed from the instancer node as instanced objects.                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rotation`` / ``r``                                                                                 | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the rotation of the instanced objects.                                                       |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rotationOrder`` / ``ro``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rotationType`` / ``rt``                                                                            | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the rotation type of the instanced objects.                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rotationUnits`` / ``ru``                                                                           | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``scale`` / ``sc``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the scale of the instanced objects.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``shear`` / ``sh``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the shear of the instanced objects.                                                          |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``visibility`` / ``vis``                                                                             | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    |                                                                                                      |                               | .. image:: /images/edit.gif   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag sets or queries the particle attribute name to be used for the visibility of the instanced objects.                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.particleInstancer`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        # create a cube and a particle emitter
        pm.polyCube()
        # Result: [nt.Transform(u'pCube1'), nt.PolyCube(u'polyCube1')] #
        pm.emitter(pos=(0,0,0), type='omni', r=100, sro=0, nuv=0, cye='none', cyi=1, spd=1, srn=0, nsp=1, tsp=0, mxd=0, mnd=0, dx=1, dy=0, dz=0, sp=0)
        # Result: nt.PointEmitter(u'emitter1') #
        pm.particle()
        # Result: [nt.Transform(u'particle1'), nt.Particle(u'particleShape1')] #
        pm.connectDynamic('particle1',em='emitter1')
        # Result: [u'particleShape1'] #
        # instance the cube to each particle emitted
        pm.particleInstancer( 'particleShape1', addObject=True, object='pCube1', cycle='None', cycleStep=1, cycleStepUnits='Frames', levelOfDetail='Geometry', rotationUnits='Degrees', rotationOrder='XYZ', position='worldPosition', age='age')
        # Result: u'instancer1' #
        # query the instancer associated with the particle
        pm.particleInstancer( 'particle1', q=True, name=True )
        # Result: [u'instancer1'] #
        # query the particle attribute name corresponding to the position attribute for the instancer
        pm.particleInstancer( 'particle1', name='instancer1', q=True, position=True )
    """

    pass


def dynControl(*args, **kwargs):
    """
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``autoCreate`` / ``ac``                                                                              | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``oversample`` / ``os``                                                                              | *int*                         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``particleCache`` / ``pc``                                                                           | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``particleLOD`` / ``pld``                                                                            | *float*                       |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``particlesOn`` / ``po``                                                                             | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``rigidOn`` / ``ro``                                                                                 | *bool*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``seed`` / ``sd``                                                                                    | *int*                         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``startTime`` / ``st``                                                                               | *time*                        |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``traceDepth`` / ``td``                                                                              | *int*                         |                               |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  |                                                                                                                                                                   |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.dynControl`
    """

    pass


def particleRenderInfo(*args, **kwargs):
    """
    This action provides information access to the particle render subclasses. These are derived from TdynRenderBase. This
    action is used primarily by the Attribute Editor to gather information about attributes used for rendering. In query
    mode, return type is based on queried flag.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attrList`` / ``al``                                                                                | *int*                         | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the list of attributes used by this render type.                                                                                                           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``attrListAll`` / ``ala``                                                                            | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return a complete list of all render attributes used by the particle object. This also includes the per particle attributes.                                      |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``name`` / ``n``                                                                                     | *int*                         | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the name of the render subclass using the render type.                                                                                                     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``renderTypeCount`` / ``rtc``                                                                        | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Return the count of registered render classes for particle.                       Flag can have multiple arguments, passed either as a tuple or a list.           |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.particleRenderInfo`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        #Return the list of all render attributes
        pm.particleRenderInfo(query=True, ala=True)
        # Result: [u'attributeName:particleId:textfield', u'betterIllumination:false:toggleBtn', u'colorAccum:false:toggleBtn', u'flatShaded:false:toggleBtn', u'incandescence:-:vector', u'incandescencePP:-:vectorArray', u'lineWidth:1:intSlider:1:20', u'multiCount:10:intSlider:1:60', u'multiRadius:0.3:floatSlider:0:10', u'normalDir:2:intSlider:1:3', u'pointSize:2:intSlider:1:60', u'radius0:1:floatSlider:0:10', u'radius1:1:floatSlider:0:10', u'radius:0.5:floatSlider:0:10', u'radiusPP:-:floatArray', u'selectedOnly:false:toggleBtn', u'spriteNum:1:intField', u'spriteNumPP:-:floatArray', u'spriteScaleX:1.0:floatField', u'spriteScaleXPP:-:floatArray', u'spriteScaleY:1.0:floatField', u'spriteScaleYPP:-:floatArray', u'spriteTwist:0.0:floatSlider:-180:180', u'spriteTwistPP:-:floatArray', u'surfaceShading:0:floatSlider:0:1', u'tailFade:0:floatSlider:-1:1', u'tailSize:1:floatSlider:-100:100', u'threshold:0:floatSlider:0:10', u'useLighting:false:toggleBtn'] #
    """

    pass


def goal(*args, **kwargs):
    """
    Specifies the given objects as being goals for the given particle object.  If the goal objects are geometry, each
    particle in the particle object will each try to follow or match its position to that of a certain vertex/CV/lattice
    point of the goal.  If the goal object is another particle object, each particle will try to follow a paricle of the
    goal. In any other case, all the particles will try to follow the current location of the goal object's transform.  You
    can get this latter behavior for a geometry or particle object too by using -utr true. The goal weight can be keyframed.
    It lives on the particle object to which the goal was added and is a multi-attribute.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``goal`` / ``g``                                                                                     | *unicode*                     | .. image:: /images/create.gif |
    |                                                                                                      |                               | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag specifies string to be a goal of the particle object on the command line or the currently selected particle object.  This flag can be used multiple     |
    |  | times to specify multiple goals for a particle object.  Query is for use by the attribute editor.                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``index`` / ``i``                                                                                    | *bool*                        | .. image:: /images/query.gif  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Returns array of multi-attribute indices for the goals. Intended for use by the Attribute Editor.                                                                 |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``useTransformAsGoal`` / ``utr``                                                                     | *bool*                        | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Use transform of specified object instead of the shape. Meaningful only for particle and geometry objects.  Can only be passed once, applies to all objects passed|
    |  | with -g.                       Flag can have multiple arguments, passed either as a tuple or a list.                                                              |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``weight`` / ``w``                                                                                   | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This specifies the goal weight as a value from 0 to 1.  A value of 0 means that the goal's position will have no effect on the particle object, while a weight of |
    |  | 1 will make the particle object try to follow the goal object exactly.  This flag can only be passed once and sets the weight for every goal passed with the      |
    |  | -g/-goal flag.                                                                                                                                                    |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.goal`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.sphere( name='surface1')
        # Result: [nt.Transform(u'surface1'), nt.MakeNurbSphere(u'makeNurbSphere1')] #
        pm.particle( name='Particle')
        # Result: [nt.Transform(u'Particle'), nt.Particle(u'ParticleShape')] #
        
        pm.goal( 'Particle', g='surface1', w=.75 )
        # Result: [u'surface1Shape'] #
        
        # This command assigns surface1 as a goal of Particle with a goal
        # weight of 0.75.
        
        pm.goal( 'Particle', g='surface1', w=.75, utr=1 )
        # Result: [u'surface1'] #
        
        # This command assigns the transform of surface1 as a goal of Particle
        # with a goal weight of 0.75.
        
        pm.goal( 'Particle', g='camera1', w=.75 )
        
        # This command assigns the transform of camera1 as a goal of Particle
        # with a goal weight of 0.75.  The -utr flag is not relevant because
        # only the transform can be used for any object other than geometry
        # or particles.
    """

    pass


def emit(*args, **kwargs):
    '''
    The emitaction allows users to add particles to an existing particle object without the use of an emitter.  At the same
    time, it allows them to set any per-particle attribute for the particles that are created with the action.The particles
    created do not become a part of the initial state for the particle object, and will disappear when the scene is rewound
    unless they are saved into the initial state by the user explicitly.  In addition, a particle object will accept
    particles from an emit action ONLY at frames greater than or equal to its start frame.  For example, if you want to use
    the emit action to create particles at frame -5, you must set startFrame for that particle shape to -5 or less.Unlike
    many commands or actions, the emit action uses the order of its flags as important information as to how it works.  The
    -objectand -positionflags can appear anywhere in the argument list.  The -attributeand the value flags are interpreted
    based on their order.  Any value flags after an -attribute flag and before the next -attribute flag will set the values
    for the attribute specified by the closest -attribute flag before them in the argument list.  See the Examplessection
    below for more detail on how these flags work.Currently, no creation expression is executed for the new particles unless
    they are created from within a particle expression defined with the dynExpressioncommand or the Expression Editor.  If
    you want any particular values put into the particles at the time they are created, then those values should be set
    using the -attribute, -vectorValue, and -floatValueflags.
    
    .. rubric:: Flags:
    
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | Long Name / Short Name                                                                               | Argument Types                | Properties                    |
    +==+===================================================================================================+===============================+===============================+
    | ``attribute`` / ``at``                                                                               | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the attribute on the particle object that any value flags following it and before the next -attribute flag will be associated with.  The same attribute |
    |  | can be specified later in the command to pick up where the first one left off. The attributes used must be per-particle attributes.  This will accept both long   |
    |  | and short names for the attributes. Note the per-particle attribute must already exist on the particle object prior to being specified via this command flag.     |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``floatValue`` / ``fv``                                                                              | *float*                       | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the float value to be used for the currentattribute of the currentparticle.  By current attribute, it is meant the attribute specified by the most recent    |
    |  | -attribute flag.  By current particle, it is meant the particle in the list of -position flags that corresponds to the number of values that  have been set for   |
    |  | the currentattribute.  If the current attribute is a vector-per-particle attribute, then the float value specified will be used for all three components of the   |
    |  | vector.                    Flag can have multiple arguments, passed either as a tuple or a list.                                                                  |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``object`` / ``o``                                                                                   | *unicode*                     | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | This flag takes the name of a particleShape or the transform directly above it in the DAG as its parent.  It specifies which object to add the particles to.  This|
    |  | flag must be passed, as the selection list is ignored for this action.                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``position`` / ``pos``                                                                               | *float, float, float*         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Specifies the positions in the particle object's space (usually world space) where the particles are to be created. One particle is created for each occurence of |
    |  | this flag.                                                                                                                                                        |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    | ``vectorValue`` / ``vv``                                                                             | *float, float, float*         | .. image:: /images/create.gif |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    |  | Sets the vector value to be used for the currentattribute of the currentparticle.  By current attribute, it is meant the attribute specified by the most recent   |
    |  | -attribute flag.  By current particle, it is meant the particle in the list of -position flags that corresponds to the number of values that have been set for the|
    |  | currentattribute.  If the current attribute is a float-per-particle attribute, then the length of the vector described by this flag will be used.  The length is  |
    |  | described as SQR( xVal2+ yVal2+ zVal2.                                                                                                                            |
    +--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+
    
    Derived from mel command `maya.cmds.emit`
    
    
    .. rubric:: Example:
    
    ::
        
        
        import pymel.core as pm
        
        pm.particle()
        pm.emit( object='particle1', position=(1, 1, 1) )
        
        # This will create one particle at position ""1,1,1"" in the
        # already-existing particle object "i"particle1"/i".
        #
        
        pm.particle()
        pm.emit( object='particle1', position=((1, 1, 1), (2, 2, 2)), attribute=('velocity', 'rgbPP'), vectorValue=((1, 2, 3), (2, 3, 4), (.5, 1, 0)), floatValue=.1 )
        
        # This will create two particles at positions ""1,1,1"" and ""2,2,2"" in
        # the already-existing particle object "i"particle1"/i".  Then the velocity
        # attribute of those particles is set to ""1,2,3"" and ""2,3,4"",
        # respectively.  Also, the rgbPP values are set to "".5,1,0"" and
        # "".1,.1,.1"", respectively.  Notice that the rgbPP value for the
        # second particle was set with the -floatValue flag, even though rgbPP
        # is a vector attribute.  The single value was converted into a vector.
        
        pm.particle()
        pm.emit( object='particle1', position=((1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)), attribute=('velocity', 'mass', 'velocity'), vectorValue=((1, 2, 3), (2, 3, 4), (.1, .2, .3), (3, 4, 5)), floatValue=.5)
        
        # This will create five particles in "i"particle1"/i".  The values
        # for their attributes are:
        #
        # Attribute  Particle1   Particle2   Particle3   Particle4   Particle5
        # ----------+-----------+-----------+-----------+-----------+---------
        # position   """"1,1,1""""   """"2,2,2""""   """"3,3,3""""   """"4,4,4""""   """"5,5,5""""
        # velocity   """"1,2,3""""   """"2,3,4""""   """"3,4,5""""   "b"""""3,4,5""""   """"3,4,5"""""/b"
        # mass     .5          .3742       "b".3742       .3742       .3742"/b"
        #
        # Notice that the second value for mass was seet with the -vectorValue
        # flag, even though mass is a float attribute.  The vector was
        # converted into a float by taking its length.  Also, notice the "b"bold"/b"
        # values in the table.  The values for those attribute values were not
        # explicitly set in the command.  If there are fewer values given for
        # an attribute than there are position flags, the remaining unset
        # values are set to the last value set for that attribute.  This
        # allows the user to set many of the values to be the same without
        # having to use multiple value flags.  One last note.  Notice that the
        # attribute flag was passed twice for the attribute velocity.  The value
        # flags for repeated attributes pick up where the previous ones left
        # off.
        
        x = rand(1)
        y = rand(1)
        z = rand(1)
        p = sphrand(5)
        pm.emit( object='particle1', pos=((x, y, z), ('($p.x)', '($p.y)', '($p.z)')) )
        
        # This is a piece of Python code that could be put in a script or
        # even in an expression.  It adds a random number of particles
        # to the already-existing particle object "i"particle1"/i".  Since
        # the number of particles as well as the positions and velocities
        # of the particles are random, it would be impossible to just have
        # the emit action itself in the expression or script.  It must be
        # built as a string and then sent to the command processor with the
        # "b"eval"/b" or "b"evalEcho"/b" commands.  Notice that when appending
        # the vector variables to the string, it is not necessary to append
        # each component of the vectors separately.  When they are converted
        # from a vector to a string, the three components get separated with
        # a space automatically, thus formatting them in the desired way.
        # An example of a possible result from this "script" could be:
        
        pm.emit( object='particle1', pos=((1.899864198, -6.721569708, 0.585203937), (8.103957656, -4.042442985, 2.047724209), (-1.392914569, -0.109724376, 8.62265813), (1.960103537, -3.203145195, -7.6892516), (2.564072614, -6.049536895, 1.334818295), (-5.603376821, 4.33595058, 6.952385447), (-2.478591746, 6.286855715, 6.851659059), (2.424670276, -4.083412217, 6.320538621), (6.440800453, 3.405519296, 5.462135819), (2.445192551, 1.397203422, 3.443755853)), at='velocity', vv=((-2.348796409, 4.022130218, 0.5316172944), (4.149667117, -1.023146404, 1.97965556), (-0.08429132578, -0.5518495233, 1.591812495), (2.597930963, 1.033536331, -1.398351383), (-3.102859272, 3.423569856, 0.7895603241), (-2.519331228, -2.5684916, -1.530779154), (-2.645169119, -0.3186551381, 0.9164776099), (-0.6183816487, -1.060784068, -0.8748223942), (-0.2460372256, 3.567980747, -2.007567372), (1.735044809, -3.660099445, -1.765401859)) )
        
        # The spacing in the string is just for formatting reasons and does
        # not affect how the action executes or compiles.
    '''

    pass



