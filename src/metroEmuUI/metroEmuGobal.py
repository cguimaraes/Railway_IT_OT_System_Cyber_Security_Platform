#-----------------------------------------------------------------------------
# Name:        metroEmuGlobal.py
#
# Purpose:     This module is used as a local config file to set constants, 
#              global parameters which will be used in the other modules.
#              
# Author:      Yuancheng Liu
#
# Created:     2010/08/26
# Copyright:   
# License:     
#-----------------------------------------------------------------------------
"""
For good coding practice, follow the following naming convention:
    1) Global variables should be defined with initial character 'g'
    2) Global instances should be defined with initial character 'i'
    2) Global CONSTANTS should be defined with UPPER_CASE letters
"""

import os, sys
from collections import OrderedDict

print("Current working directory is : %s" % os.getcwd())
DIR_PATH = dirpath = os.path.dirname(__file__)
print("Current source code location : %s" % dirpath)
APP_NAME = ('MetroEmu', 'UI')

TOPDIR = 'src'
LIBDIR = 'lib'

#-----------------------------------------------------------------------------
# Init the logger:
idx = dirpath.find(TOPDIR)
gTopDir = dirpath[:idx + len(TOPDIR)] if idx != -1 else dirpath   # found it - truncate right after TOPDIR
# Config the lib folder 
gLibDir = os.path.join(gTopDir, LIBDIR)
if os.path.exists(gLibDir):
    sys.path.insert(0, gLibDir)
import Log
Log.initLogger(gTopDir, 'Logs', APP_NAME[0], APP_NAME[1], historyCnt=100, fPutLogsUnderDate=True)

#-----------------------------------------------------------------------------
# Init the configure file loader.
import ConfigLoader
CONFIG_FILE_NAME = 'metroConfig.txt'
gGonfigPath = os.path.join(dirpath, CONFIG_FILE_NAME)
iConfigLoader = ConfigLoader.ConfigLoader(gGonfigPath, mode='r')
if iConfigLoader is None:
    print("Error: The config file %s is not exist.Program exit!" %str(gGonfigPath))
    exit()

CONFIG_DICT = iConfigLoader.getJson()


#------<IMAGES PATH>-------------------------------------------------------------
IMG_FD = os.path.join(dirpath, 'img')
ICO_PATH = os.path.join(IMG_FD, "metro.ico")

# Init the agent object type
RAILWAY_TYPE_LINE   = 'RL'
RAILWAY_TYPE_CYCLE  = 'RC'
TRAIN_TYPE          = 'TR'
LABEL_TYPE          = 'LB'
SENSOR_TYPE         = 'SS'
SINGAL_TYPE         = "SG"
STATION_TYPE        = 'ST'
ENV_TYPE            = 'EV'
JUNCTION_TYPE       = 'JC'

PERIODIC = 300      # update the main in every 300ms
UDP_PORT = 3001

# Init the log type parameters.
DEBUG_FLG   = False
LOG_INFO    = 0
LOG_WARN    = 1
LOG_ERR     = 2
LOG_EXCEPT  = 3

# Init the UI layout flags
LAY_U = 0   # layout at up position  
LAY_D = 1   # layout at down position 
LAY_L = 2   # layout at left position
LAY_R = 3   # layout at right position
LAY_C = 4   # layout at center 
LAY_H = 5   # horizontal layout
LAY_V = 6   # vertical layout

# gTrainImgB = os.path.join(dirpath, IMG_FD, "train.png")
# gTrainImgH = os.path.join(dirpath, IMG_FD, "trainhead2.png")

#-------<GLOBAL VARIABLES (start with "g")>------------------------------------
# VARIABLES are the built in data type.
gTestMD = CONFIG_DICT['TEST_MD']      # test mode flag, True: the simulator will operate with control logic itself. 
# False: The simultor will connect to the PLC, PLC will implement the control logic.
gTranspPct = 70     # Windows transparent percentage.
# main frame update rate 0.5 sec.
gUpdateRate = float(CONFIG_DICT['TEST_MD']) if float(CONFIG_DICT['TEST_MD'])>0 else 0.5
gSensorCount = 0    # number of sensors.
gMinTrainDist = 80  # min distance between each trains by refresh rate
gTrackConfig = OrderedDict()
gCollsionTestFlg = CONFIG_DICT['TEST_JC_COLLISION'] # flag used to enable test the train collision at the junction.
gTrainDistTestFlag = CONFIG_DICT['TEST_TR_DISTANCE'] # flag used to see if the minimum distance between trains are observed

def gDebugPrint(msg, prt=True, logType=None):
    if prt: print(msg)
    if logType == LOG_WARN:
        Log.warning(msg)
    elif logType == LOG_ERR:
        Log.error(msg)
    elif logType == LOG_EXCEPT:
        Log.exception(msg)
    elif logType == LOG_INFO or DEBUG_FLG:
        Log.info(msg)

#-------<GLOBAL PARAMTERS>-----------------------------------------------------
iMainFrame = None   # UI MainFrame.
iCtrlPanel = None   # UI function control panel.
iMapPanel = None    # UI map display panel
iMapMgr = None      # map manager.
iDataMgr = None     # data manager to handling data fetch and set requirment.
