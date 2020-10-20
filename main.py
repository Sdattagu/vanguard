# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
import time

import controllers.windowCtrl as wctrl
import character.classScripts.kanna.kishinScript as kishScript
import character.classScripts.phantom.buffScript as buffScript

if __name__ == '__main__':
    w = wctrl.WindowCtrl()
    w.find_window_wildcard(".*MapleStory.*")
    w.set_foreground()
    w.set_active()
    time.sleep(2)
    buffScript.main()

