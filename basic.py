import ctypes

user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")
hWnd = None
lpText = "Hello World!"
lpCaption = "Hello Student!"
uType = 0x00000001

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

error = k_handle.GetLastError()

if error != 0:
    print("Error Code: {0}".format(error))
    exit(1)

if response == 1:
    print("User Clicked OK")
elif response == 2:
    print("User Click Cancel")

