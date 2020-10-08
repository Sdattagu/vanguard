import time
import controllers.keyboardCtrl as kbd
import bindings.bottomLetterRow as blr
from controllers.windowCtrl import WindowCtrl as wctrl
import signal

def handler(signum, frame):
    print("Signal handled called with signal", signum)

def main():
    print("In app window...")
    signal.signal(signal.SIGINT, handler)
    w = wctrl()
    w.find_window_wildcard(".*Notepad.*")
    w.set_foreground()
    w.set_active()
    while True:
        print("Waiting...")
        time.sleep(1)
