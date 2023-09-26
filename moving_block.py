from mcpi.minecraft import Minecraft

mc = Minecraft.create()

import time

x, y, z = mc.player.getTilePos()
while True:
    mc. setBlock(x, y, z, 41)
    time.sleep(0.5)
    mc.setBlock(x, y, z, 0)
    x += 1
    z += 1