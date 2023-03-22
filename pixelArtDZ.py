from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create()

p = 2
a = 0
b = 1
o = 86


pixel_list = [
[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
[a, a, a, a, b, b, b, b, a, a, a, a, a, a, a, a, a, a, a, b, b, b, b, a, a, a, a, a, a],
[a, a, a, b, o, o, o, o, b, a, a, a, a, a, a, a, a, a, b, o, o, o, o, b, a, a, a, a, a],
[a, a, b, p, b, b, o, o, o, b, a, a, a, a, a, a, a, b, o, o, o, b, b, p, b, a, a, a, a],
[a, a, b, p, p, p, b, o, o, b, b, b, b, b, b, b, b, b, o, o, b, p, p, p, b, a, a, a, a],
[a, a, b, p, p, p, b, o, o, o, o, o, o, o, o, o, o, o, o, o, b, p, p, p, b, a, a, a, a],
[a, a, b, p, p, b, o, o, o, o, o, o, o, o, o, o, o, a, a, a, a, b, p, p, b, a, a, a, a],
[a, a, a, b, b, o, o, o, o, o, o, o, o, o, a, a, a, a, a, a, a, a, b, b, a, a, a, a, a],
[a, a, a, a, b, o, o, b, b, b, o, o, a, a, a, a, a, b, b, b, a, a, b, a, a, a, a, a, a],
[a, a, a, a, b, o, b, b, a, a, b, a, a, a, a, a, b, a, a, b, b, a, b, a, a, a, a, a, a],
[a, a, a, b, o, o, b, b, a, a, b, a, a, a, a, a, b, a, a, b, b, a, a, b, a, a, a, a, a],
[a, a, a, b, a, a, b, a, b, b, b, a, a, a, a, a, b, b, b, a, b, a, a, b, a, a, a, a, a],
[a, a, a, b, b, a, a, b, b, b, a, a, a, a, a, a, a, b, b, b, a, a, b, b, a, a, a, a, a],
[a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a, a, a],
[a, a, a, b, b, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, b, b, a, a, a, a, a],
[a, a, a, b, a, a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a, a, b, a, a, a, a, a],
[a, a, a, a, b, a, a, a, a, a, a, b, b, a, b, b, a, a, a, a, a, a, b, a, a, a, a, a, a],
[a, a, a, a, b, b, o, o, a, a, a, a, a, a, a, a, a, a, o, o, b, b, b, a, a, a, a, a, a],
[a, a, a, a, b, o, o, a, a, b, a, a, a, a, a, a, a, b, a, a, o, o, b, a, a, a, a, a, a],
[a, a, a, a, b, o, o, a, p, p, b, a, a, a, a, a, b, p, p, a, o, o, b, a, a, a, a, a, a],
[a, a, a, a, b, o, a, b, p, p, b, a, a, a, a, a, b, p, p, b, a, o, b, a, a, a, a, a, a],
[a, a, a, a, b, a, a, a, b, b, a, a, a, a, a, a, a, b, b, a, a, a, b, a, a, a, a, a, a],
[a, a, a, a, a, b, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, b, a, a, a, a, a, a, a],
[a, a, a, a, a, a, b, a, a, a, b, b, b, b, b, b, b, a, a, a, b, a, a, a, a, a, a, a, a],
[a, a, a, a, a, b, p, p, b, b, a, a, a, a, a, a, a, b, b, p, p, b, a, a, a, a, a, a, a],
[a, a, a, a, a, a, b, b, a, a, a, a, a, a, a, a, a, a, a, b, b, a, a, a, a, a, a, a, a],
[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]
]




x, y, z = mc.player.getTilePos()
x_start = x

for row in pixel_list:
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    y += 1
    x = x_start
