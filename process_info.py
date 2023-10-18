import ctypes

from ctypes.wintypes import HANDLE, DWORD


class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD)
    ]


p_handle = PROCESS_INFORMATION()