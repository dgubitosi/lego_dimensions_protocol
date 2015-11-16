#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     16/11/2015
# Copyright:   (c) User 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
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
print dev.write(1, [0x55, 0x0f, 0xb0, 0x01, 0x28, 0x63, 0x29, 0x20, 0x4c, 0x45, 0x47, 0x4f, 0x20, 0x32, 0x30, 0x31, 0x34, 0xf7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Startup



# Immediately switch all pads to a value
# Byte 0 is always 0x55
# Byte 3 is a message counter
# Byte 5 is red
# Byte 6 is green
# Byte 7 is blue
# Byte 8 is checksum
# Sniffed
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0xff, 0xff, 0x1a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to light blue (Found via sniffing)
# Mixed colours found by fuzzing
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0x00, 0xff, 0x1b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to Purple (found via fuzzing)
# RGB Monochromatic hex(28) == 0x1c
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0x00, 0x00, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to red
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0xff, 0x00, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to green (found via fuzzing)
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0xff, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to dark blue (found via fuzzing)
# All pads off
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0x00, 29, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch all pads off (Found by fuzzing)




# Fade to value
# Byte 0 is always 0x55
# Byte
##        print dev.write(1, [0x55, 0x14, 0xc6, 0x04, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Fade to dark blue
#[0x55, 0x14, 0xc6, 0x26, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0xfd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All dark Blue
#[0x55, 0x14, 0xc6, 0x27, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0xfb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All pink
#[0x55, 0x14, 0xc6, 0x28, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0xb4, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All red
#[0x55, 0x14, 0xc6, 0x29, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All yellow
#[0x55, 0x14, 0xc6, 0x2a, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All green
#[0x55, 0x14, 0xc6, 0x2b, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x4c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All cyan
#[0x55, 0x14, 0xc6, 0x2c, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All dark blue







def main():
    pass

if __name__ == '__main__':
    main()
