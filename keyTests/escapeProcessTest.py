import time
import controllers.keyboardCtrl as kbd
import bindings.bottomLetterRow as blr
from controllers.windowCtrl import WindowCtrl as wctrl

def main():
    print("In app window...")
    w = wctrl()
    w.find_window_wildcard(".*Notepad.*")
    w.set_foreground()
    w.set_active()


