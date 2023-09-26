from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create()

p = 237
m = 12 # желтая кожа
q = 20
l = 4
k = 129
h = 231
o = 234
f = 5 # коричневая кожа
e = 87
d = 39
c = 225
b = 10 # красный динамит
a = 80 # белое

pixel_list = [
    [a, a ,a ,a ,a ,a ,a ,a ,a ,a ,a ,a ,a ,a ,d ,a ,a ,a ,a ,a ,a ,a ,a ,a ,a ,a ,a ,a, a],
    [a, a, a ,a ,a ,a ,a ,a ,a ,a ,a ,a ,d ,d ,o ,d ,d ,a ,a ,a ,a ,a ,a ,a ,a ,a ,a ,a ,a],
    [a, a, a, a, a, a, a, a, a, a, d, d, o, d, d, d, h, d, d, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, d, o, o, d, e, e, e, d, h, h, d, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, d, o, o, d, e, e, e, e, e, d, h, h, d, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, d, o, o, d, e, e, e, e, e, d, h, h, d, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, d, o, o, o, d, l, e, e, e, l, d, h, h, h, d, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, d, o, o, o, h, d, l, q, l, d, h, h, h, h, d, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, d, o, o, o, h, h, d, d, d, h, h, h, h, h, d, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, d, o, o, o, h, h, h, h, h, h, h, h, h, h, h, h, d, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, d, a, a, a, a, a, a],
    [a, a, a, a, a, a, d, p, m, m, m, m, m, p, p, p, m, m, m, m, m, p, d, a, a, a, a, a, a],
    [a, a, a, a, a, a, d, p, m, f, m, m, d, m, p, m, d, m, m, f, m, p, d, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, d, m, f, m, m, d, m, p, m, d, m, m, f, m, d, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, d, m, m, p, p, m, m, p, p, p, m, m, p, p, m, m, d, a, a, a, d, a, a],
    [a, a, d, d, a, a, d, m, m, p, p, p, p, p, p, p, p, p, p, m, m, m, d, d, a, d, f, d, a],
    [a, a, d, f, d, a, a, d, d, m, m, m, m, p, p, p, m, m, m, m, d, d, b, d, d, b, f, d, a],
    [a, d, d, f, d, d, a, a, d, m, m, m, d, d, m, m, d, m, m, m, d, d, d, d, b, b, b, d, a],
    [d, q, b, b, b, d, a, d, d, m, m, m, m, d, b, b, m, m, m, m, d, p, p, d, b, b, b, f, d],
    [a, d, b, b, b, d, d, d, b, d, m, m, m, m, m, m, m, m, m, d, d, p, d, b, b, b, b, d, a],
    [a, d, b, b, b, d, f, d, d, b, d, m, d, d, d, b, b, d, m, d, f, d, d, b, b, b, b, f, d],
    [d, f, b, b, b, d, f, d, p, d, d, b, b, b, b, b, b, b, d, d, f, f, d, b, b, b, b, f, d],
    [d, f, b, b, b, d, f, d, p, p, d, d, d, d, d, d, d, d, d, d, f, f, d, b, b, b, b, d, a],
    [a, d, b, b, b, d, d, d, d, d, f, f, f, d, l, l, d, f, f, d, f, f, d, b, b, b, b, d, a],
    [a, a, d, d, d, d, a, a, a, d, d, d, d, d, d, d, d, d, d, f, f, f, d, d, d, d, d, a, a],
    [a, a, a, a, a, a, a, a, a, a, d, c, c, c, c, c, c, c, c, d, f, f, d, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, d, c, c, d, d, d, c, c, c, d, d, d, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, d, c, c, d, a, a, d, c, c, d, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, d, c, c, c, d, a, a, d, c, c, d, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, d, c, c, c, d, a, a, d, c, c, c, d, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, d, q, q, d, a, a, a, a, d, q, q, d, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, d, d, d, d, a, a, a, a, d, d, d, d, a, a, a, a, a, a, a, a],
]




x, y, z = mc.player.getTilePos()
x_start = x

y = y + 33

for row in pixel_list:
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    y -= 1
    x = x_start


