import os
import ctypes

# Change this to your CANapAPI64.dll path
CANapAPI_dll = os.path.abspath(r"C:\Program Files\Vector CANape 19.0\CANapeAPI\CANapAPI64.dll")
# Load the library and assign it to dll.
dll = ctypes.windll.LoadLibrary(CANapAPI_dll)

class tAsap3Hdl(ctypes.Structure):
    pass
TAsap3Hdl = ctypes.POINTER(tAsap3Hdl)
hdl=TAsap3Hdl()

# Maximum response time (ms)
responseTimeout = 10000 # 10 seconds
# CANape requires absolute path.
workingDir = os.path.abspath(".")
fifoSize = 8192
debugMode = True

# Cast from Python -> ctypes
c_responseTimeout = ctypes.c_ulong()
c_workingDir = ctypes.c_char_p(workingDir.encode("UTF-8"))
c_fifoSize = ctypes.c_ulong(fifoSize)
c_debugMode = ctypes.c_bool(debugMode)

# Define return and argument types
dll.Asap3Init.restype = ctypes.c_bool
dll.Asap3Init.argtypes = (
    ctypes.POINTER(TAsap3Hdl),
    ctypes.c_ulong,
    ctypes.c_char_p,
    ctypes.c_ulong,
    ctypes.c_bool,
)

# Call the DLL function.
dll.Asap3Init(
    ctypes.byref(hdl),
    c_responseTimeout,
    c_workingDir,
    c_fifoSize,
    c_debugMode,
)

### Wait 10 seconds
import time
time.sleep(10)

## Exit CANape
dll.Asap3Exit.argtypes= (TAsap3Hdl, )
dll.Asap3Exit.restype=ctypes.c_bool

result = dll.Asap3Exit(hdl)
result