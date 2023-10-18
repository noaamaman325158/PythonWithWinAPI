import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll")

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

dwDesiredAccess = PROCESS_ALL_ACCESS
bInheriHandle = False
# dwProcessId = 0x00005D70 -> Access Denied Errror
dwProcessId = 0x0000448C
# PID_TASKMGR.EXE = 23920(10) = 5D70(16)
# PID_Notepad++.exe = 17548(10) = 448C(16)
response = k_handle.OpenProcess(dwDesiredAccess, bInheriHandle, dwProcessId)

error = k_handle.GetLastError()

if error != 0:
    print("Error Code: {0}".format(error))
    exit(1)

if response <= 0:
    print("Handle was not created")
else:
    print("Handle was Created")
