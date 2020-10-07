# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ctypes, time

import win32con
import win32gui, re
import win32api

user32 = ctypes.windll.user32

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actual Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def KeyPress(key):
    PressKey(key) # press Q
    time.sleep(.1)
    ReleaseKey(key) #release Q

def KeyHold(key,duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        PressKey(key)
        time.sleep(0.2)
    ReleaseKey(key)

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__(self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)
        print("done")
        if self._handle:
            print(self._handle)

    def set_foreground(self):
        """put the window in the foreground"""
        print(self._handle)
        win32gui.SetForegroundWindow(self._handle)

    def set_active(self):
        print(self._handle)
        win32gui.BringWindowToTop(self._handle)

def send_input():
    keycode = int("41", 16)
    win32api.keybd_event(keycode, 0, 0, 0)  # holds the "F" key down
    time.sleep(2)  # waits 2 seconds
    win32api.keybd_event(keycode, 0, win32con.KEYEVENTF_KEYUP, 0)  # releases the key


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    q = 0x10
    rightArrow = 0xCD
    leftArrow = 0xCB
    w = WindowMgr()
    w.find_window_wildcard(".*MapleStory.*")
    w.set_foreground()
    w.set_active()
    time.sleep(1)
    KeyHold(rightArrow, 2)
    PressKey(q)
    KeyHold(leftArrow, 2)
    PressKey(q)

