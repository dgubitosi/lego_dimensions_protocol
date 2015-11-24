# 0xc8 Immediately switch pad(s) to set of colours
# Byte: use
# 00: Always 0x55
# 01: 0x0e Payload size == 14
# 02: 0xc8 Command
# 03 Message counter
# 04: c:enable - 0x00 disables the command for this pad, other values enable
# 05: c:red
# 06: c:green
# 07: c:blue
# 08: l:enable - 0x00 disables the command for this pad, other values enable
# 09: l:red
# 10: l:green
# 11: l:blue
# 12: r:enable - 0x00 disables the command for this pad, other values enable
# 13: r:red
# 14: r:green
# 15: r:blue
# 16: Checksum
# 17-31: Padding


# left:cyan, center:yellow, right:pink
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x3e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:cyan, center:yellow, right:pink
dev.write(01, [0x55, 0x0e, 0xc8, 0x1b, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x53, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x26, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x26, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x03, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x3b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x2e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x19, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x07, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x3f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x0c, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x44, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x01, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x39, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1a, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x52, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

# Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x23, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x0d, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x20, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x59, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x25, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x37, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1c, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x37, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x0b, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x55, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1e, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x68, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x30, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x7a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x07, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1a, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x14, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x32, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x02, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x4c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x17, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x61, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x33, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x7d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x0d, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x23, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x01, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x4b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

# Fuzzed:
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x18, 184, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# left:off, center:yellow, right:pink
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x00, 160, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off, center:yellow, right:red
# Center
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:red right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0xff, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:green right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0xff, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:blue right:off
# Left
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:red center:off right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:green center:off right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xff, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:blue center:off right: off
# Right
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:off right:red
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:off right:green
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xff, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:off right:blue

# Failed fuzzing:
#[0x55, 0x0e, 0xc8, 0x20, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0xff, 0xff, chk, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# nothing ever tuns on