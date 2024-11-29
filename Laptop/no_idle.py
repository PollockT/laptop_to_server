#!/usr/bin/env python3

import time
from gi.repository import Gio, GLib

def inhibit_sleep():
    """
    Prevent the system from sleeping or going idle.
    """
    try:
        # Create an interface to communicate with the Power Management service
        bus = Gio.bus_get_sync(Gio.BusType.SYSTEM, None)
        proxy = Gio.DBusProxy.new_sync(
            bus,
            Gio.DBusProxyFlags.NONE,
            None,
            "org.freedesktop.login1",
            "/org/freedesktop/login1", #test
            "org.freedesktop.login1.Manager",
            None
        )

        # Call the Inhibit method to block sleep and idle
        fd = proxy.call_sync(
            "Inhibit",
            GLib.Variant("(ssss)", ("sleep", "keep_awake.py", "Preventing sleep", "block")),
            Gio.DBusCallFlags.NONE,
            -1,
            None
        )

        print("Sleep inhibited. The system will stay awake.")
        return fd
    except Exception as e:
        print(f"Failed to inhibit sleep: {e}")
        return None

def main():
    # Inhibit sleep
    inhibit_fd = inhibit_sleep()

    # Keep the script running
    try:
        while True:
            time.sleep(60)  # Sleep for 1 minute intervals
    except KeyboardInterrupt:
        print("Exiting. Sleep inhibition will be removed.")

if __name__ == "__main__":
    main()

