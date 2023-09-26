from mcpi.minecraft import Minecraft
mc = Minecraft.create()

r = 152
c = 41
a = 0
v = 58
o = 49

pixel_list = [
    [a, a, a, a, o, o, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, o, o, o, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, o, c, c, o, a, a, a, o, o, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, o, c, c, c, o, o, o, o, o, o, o, o, o, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, o, c, c, o, v, v, v, v, o, v, v, v, o, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, o, c, o, v, v, v, o, v, v, o, v, v, v, o, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, o, o, v, v, o, v, v, v, v, o, v, v, o, o, o, o, o, o, o, o, a, a, a, a, a, a, a],
    [a, a, a, a, a, o, v, v, o, o, o, v, v, v, v, o, o, o, c, c, c, c, c, c, o, o, a, a, a, a, a, a, a],
    [a, a, a, a, a, o, v, v, v, v, v, o, o, o, o, c, c, c, c, o, c, c, c, o, o, a, a, a, a, a, a, a, a],
    [a, a, a, a, o, c, o, o, o, o, o, c, c, c, c, c, c, c, c, c, o, o, o, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, o, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, o, a, a, a, o, o, o, o, o, a, a, a, a],
    [a, a, a, a, o, c, o, o, c, c, c, c, c, c, o, o, c, c, c, c, o, a, o, o, c, c, c, c, o, a, a, a, a],
    [a, a, a, a, o, c, o, o, c, c, c, c, c, c, o, o, c, c, c, c, o, a, o, c, c, c, c, c, o, a, a, a, a],
    [a, a, a, a, o, r, c, c, c, c, o, c, c, c, c, c, r, r, c, c, o, a, o, c, c, c, c, c, o, a, a, a, a],
    [a, a, a, a, o, r, c, c, c, o, c, o, c, c, c, c, r, r, c, o, a, a, o, c, c, c, o, o, o, a, a, a, a],
    [a, a, a, a, a, o, c, c, c, c, c, c, c, c, c, c, c, c, o, o, a, a, o, c, c, o, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, o, c, c, c, c, c, c, c, c, c, o, o, c, c, o, a, o, c, c, o, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, o, c, c, o, o, o, o, c, c, c, c, c, c, c, c, o, a, o, c, c, o, a, a, a, a, a, a],
    [a, a, a, a, a, o, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, o, a, a, o, c, o, a, a, a, a, a, a],
    [a, a, a, a, a, o, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, o, a, a, o, c, o, a, a, a, a, a, a],
    [a, a, a, a, a, o, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, o, o, c, c, o, a, a, a, a, a, a],
    [a, a, a, a, a, o, c, c, c, c, o, c, c, c, o, c, c, c, c, o, c, c, o, c, c, o, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, o, c, c, c, c, o, c, o, c, c, c, c, o, c, c, c, o, o, o, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, o, c, o, c, c, c, o, c, o, c, c, c, o, c, c, c, c, o, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, o, c, c, o, o, o, c, c, c, o, o, o, c, c, c, c, o, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, o, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, o, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, o, c, c, c, c, c, c, c, c, c, c, c, c, c, o, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, o, c, c, o, o, o, o, o, o, c, c, c, o, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, o, o, o, a, a, a, a, o, o, o, o, a, a, a, a, a, a, a, a, a, a, a, a, a, a]
]
x, y, z = mc.player.getTilePos()
y = y + len(pixel_list)
x_start = x

for row in pixel_list:
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    y -= 1
    x = x_start