#!/usr/bin/env python3

import os
import time
import platform

def keep_screen_on():
    """
    prevent screen from turning off or idle upon lid closure
    """
    if platform.system() != "Linux":
        print("This script only works on linux kernals")#
        return
    
    # ensure xset is installed
    if os.system("command -v xsset> /dev/null") != 0:
        print("xset is not installed")
        return
    
    try:
        os.system("xset s off") #tuns off screensaver
        os.system("xset -dpms") #disable power management
        os.system("xset s  noblank") #prevent screen blank

        print("Screen will remain on even if lid is closed now.")
        print("Press Ctrl+C to abort")

        while True:
            time.sleep(60) # sleeps for 1 minute and loop
    except KeyboardInterrupt:
        print("\n Restoring orignal power management settings...")
        os.system("xset s on")
        os.system("xset +dpms")
        os.system("xset s blank")

if __name__ == "__main__":
    keep_screen_on()