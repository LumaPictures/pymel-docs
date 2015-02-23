import sys
import os
import maya.mel as mel
import re

from maya.app.general.QUVEditor import *

from random import randint

createMyTextureWindow = '\n                            global proc createMyTextureWindow(string $whichPanel)\n                            {\n                                print(" create "+$whichPanel);\n                                textureWindow -unParent $whichPanel;\n                                print(" end create ");\n                            }\n                            '

removeMyTextureWindow = '\n                            global proc removeMyTextureWindow(string $whichPanel)\n                            {\n                                print(" remove "+$whichPanel);\n                                textureWindow -e -unParent $whichPanel;\n                                print(" end remove ");\n                            }\n                            '

updateMyTextureWindow = '\n                            global proc txtWndUpdateEditor(string $editor, string $editorCmd, string $updatFunc, int $reason)\n                            {\n                            }\n                            '

columnLayout = None

texWinName = []

addMyTextureWindow = '\n                        global proc addMyTextureWindow(string $whichPanel)\n                        {\n                                print(" add "+$whichPanel);\n                                string $formName = `formLayout`;\n                                // Attach the editor to the UI\n                                textureWindow -e -parent $formName $whichPanel;\n                                \n                                //string $textureEditorControl = `textureWindow -query -control $whichPanel`;\n\n                                //\n                                // If any changes goto update\n                                //\n                                //textureWindow -e \n                                //    -cc "txtWndUpdateEditor" $whichPanel\n                                //    "textureWindow" "null"\n                                //    $whichPanel;\n\n                                //txtWndUpdateEditor($whichPanel,"textureWindow","null",101);\n                                \n                                if (`exists performTextureViewGridOptions`)\n                                        performTextureViewGridOptions 0;\n                                \n                                // Change image range\n                                //if (`exists performTextureViewImageRangeOptions`)\n                                //        performTextureViewImageRangeOptions 0;\n\n                                print(" end add ");\n                        }\n                        '

texWidget = None

gMainPane = []


