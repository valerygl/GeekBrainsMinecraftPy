import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


count = 0
while count <= 30:
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y, z, 8)
    time.sleep(0.5)
    count += 1