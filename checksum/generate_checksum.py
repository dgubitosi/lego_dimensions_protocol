#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     15/11/2015
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


print dev.write(1, [0x55, 0x0f, 0xb0, 0x01, 0x28, 0x63, 0x29, 0x20, 0x4c, 0x45, 0x47, 0x4f, 0x20, 0x32, 0x30, 0x31, 0x34, 0xf7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Startup





def compute_checksum(byte_list):
    """Compute the checksum byte for the lego portal USB protocol"""
    checksum = 0
    for current_byte in byte_list:
        checksum = checksum ^ current_byte
    print("checksum:"+repr(checksum))
    remainder = checksum % 16
    print("remainder:"+repr(remainder))
    return checksum


def test_expected_checksums():
    packets = [
    [0x55,0x14,0xc6,0x0e,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xe2,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x1a,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xee,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x14,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xe8,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x20,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xf4,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x26,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xfa,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x2c,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x32,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x06,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x38,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x0c,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x3e,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x12,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x04,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xd8,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x0a,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xde,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x10,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xe4,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x16,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xea,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x1c,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xf0,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    [0x55,0x14,0xc6,0x22,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xf6,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    ]

    for original_packet in packets:
        command = original_packet[0:22]
        expected_checksum = original_packet[22]
        generated_checksum = compute_checksum(byte_list=command)
        current_packet = command+[generated_checksum]
        # Pad to 32 bytes
        while ( len(current_packet) < 32):
            current_packet.append(0)
        print("expected_checksum:"+repr(expected_checksum))
        print("generated_checksum: "+repr(generated_checksum))
        assert(expected_checksum == generated_checksum)
        assert(current_packet == original_packet)
    return



def generate_checksum_for_counter():
    original_packet = [0x55,0x14,0xc6,0x0e,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0xe2,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    checksum_and_trailing_zeroes_removed = [0x55,0x14,0xc6,0x0e,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18,0x01,0x1e,0x01,0xff,0x00,0x18]

    counter = -1
    while counter < 256:
        counter += 1
        current_command = checksum_and_trailing_zeroes_removed[:3]+[counter]+checksum_and_trailing_zeroes_removed[4:]
        print("current_command: "+repr(current_command))
        checksum = compute_checksum(byte_list=current_command)
        current_packet = current_command+[checksum]
        # Pad to 32 bytes
        while (len(current_packet) < 32):
            current_packet.append(0)
        print("current_packet: "+repr(current_packet))
        dev.write(1, current_packet)
        time.sleep(2)



def main():
    test_expected_checksums()

if __name__ == '__main__':
    main()
