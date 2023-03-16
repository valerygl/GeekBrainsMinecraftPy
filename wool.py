from mcpi.minecraft import Minecraft


mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

rainbow = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4],
    [5, 5, 5],
]
start_x = x
for row in rainbow:
    for color in row:
        mc.setBlock(x, y, z, 35, color)
        x += 1
    y += 1
    x = start_x
