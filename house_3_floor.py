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
    mc.setBlocks(x, block_y, z, x + length, block_y, z + width, random.randint(1, 1200))
    mc.postToChat(block_y)
    # air = 0
    # mc.setBlocks(x + 1, y + 1, z + 1, x + length - 1, y + height - 1, z + width - 1, air)