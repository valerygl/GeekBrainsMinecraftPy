from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create()


r = 46
c = 1
a = 0

pixel_list = [
    [a, c, c, c, a, c, c, c, a],
    [c, r, r, r, c, r, r, r, c],
    [c, r, r, r, r, r, r, r, c],
    [c, r, r, r, r, r, r, r, c],
    [a, c, r, r, r, r, r, c, a],
    [a, a, c, r, r, r, c, a, a],
    [a, a, a, c, r, c, a, a, a],
    [a, a, a, a, c, a, a, a, a]
]




x, y, z = mc.player.getTilePos()
x_start = x

for row in pixel_list:
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    y += 1
    x = x_start

