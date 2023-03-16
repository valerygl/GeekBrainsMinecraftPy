import random
import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
length = 5
height = 6
width = 5
time.sleep(3)
for block_y in range(y, y + height, 1):
    # mc.setBlock(x, block_y, z, 2)
    mc.setBlocks(x, block_y, z, x + length, block_y, z + width, random.randint(1, 10))
    mc.postToChat(int(block_y))
    time.sleep(1)