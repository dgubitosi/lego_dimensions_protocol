import usb.core
import usb.util
import time

# find our device
dev = usb.core.find(idVendor=0x0e6f)# 0x0e6f Logic3 (made lego dimensions portal hardware)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# Initialise portal
print "Initialising portal"
dev.write(1, [0x55, 0x0f, 0xb0, 0x01, 0x28, 0x63, 0x29, 0x20, 0x4c, 0x45, 0x47, 0x4f, 0x20, 0x32, 0x30, 0x31, 0x34, 0xf7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Startup

def cycle_fade():
    """Cycle through fade colours"""
    commands = [
        [0x55, 0x14, 0xc6, 0x26, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0xfd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All dark Blue
        [0x55, 0x14, 0xc6, 0x27, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0xfb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All pink
        [0x55, 0x14, 0xc6, 0x28, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0xb4, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All red
        [0x55, 0x14, 0xc6, 0x29, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All yellow
        [0x55, 0x14, 0xc6, 0x2a, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All green
        [0x55, 0x14, 0xc6, 0x2b, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x4c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All cyan
        [0x55, 0x14, 0xc6, 0x2c, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All dark blue
        ]
    print "cycle_fade"
    for command in commands:
        print command
        dev.write(1, command)
        time.sleep(2)
    return


def cycle_immediate_all():
    """Cycle through immediate switch of all pad colours"""
    commands = [
        [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0x00, 0x00, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# Switch to red
        [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0xff, 0x00, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# Switch to green (found via fuzzing)
        [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0xff, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# Switch to dark blue (found via fuzzing)
        [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0x00, 29, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# Switch all pads off (Found by fuzzing)
        ]
    print "cycle_immediate_all"
    for command in commands:
        print command
        dev.write(1, command)
        time.sleep(2)
    return


def demo():
    """Show off cycle functions"""
    print "Running demo"
    while True:
        cycle_fade()
        dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0x00, 29, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch all pads off (Found by fuzzing)
        cycle_immediate_all()
        dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0x00, 29, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch all pads off (Found by fuzzing)
