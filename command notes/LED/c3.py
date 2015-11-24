# 0xc3 - set 1 or all pad(s) to a colour with variable flash rates
# Flashes between old and new colour
# Does not appear to synchronise flashes
# Byte: use
# 00: Always 0x55
# 01: 0x09 Payload size == 9
# 02: 0xc3 Command
# 03: Message counter?
# 04: pad 0:all, 1:center, 2:left 3:right
# 05: On pulse length, higher is longer
# 06: Off pulse length, higher is longer
# 07: Number of pulses, 0xff is forever
# 08: red
# 09: green
# 10: blue
# 11: checksum
# 12-31: padding

[0x55, 0x09, 0xc3, 0x0e, 0x01, 0x02, 0x02, 0x07, 0xff, 0x6e, 0x00, 0xa8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
[0x55, 0x09, 0xc3, 0x3a, 0x03, 0x02, 0x02, 0x07, 0x00, 0x16, 0x04, 0x83, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
[0x55, 0x09, 0xc3, 0x10, 0x02, 0x02, 0x02, 0x07, 0x00, 0x16, 0x04, 0x58, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
[0x55, 0x09, 0xc3, 0x12, 0x02, 0x02, 0x02, 0x07, 0x00, 0x16, 0x04, 0x5a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
send_command([0x55, 0x09, 0xc3, 0x1f, 0x01, 0x02, 0x02, 0x07, 0x00, 0xff, 0x00])# c:green flash qucikly a few times then stay on
send_command([0x55, 0x09, 0xc3, 0x1f, 0x01, 0x02, 0x02, 0x07, 0xff, 0x00, 0x00])# c:red flash qucikly a few times then stay on
send_command([0x55, 0x09, 0xc3, 0x1f, 0x01, 0x02, 0x02, 0x07, 0x00, 0x00, 0xff])# c:blue flash qucikly a few times then stay on
send_command([0x55, 0x09, 0xc3, 0x1f, 0x01, 0x02, 0x02, 0xff, 0x00, 0x00, 0xff])# c:blue flash qucikly forever
send_command([0x55, 0x09, 0xc3, 0x1f, 0x02, 0x02, 0x02, 0xff, 0x00, 0xff, 0x00])# l:green flash qucikly forever