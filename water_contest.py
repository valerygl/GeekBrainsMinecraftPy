import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


score = 0
x, y, z =mc.player.getTilePos()
block_up = mc.getBlock(x, y + 2, z)
while block_up == 8 or block_up == 9:
    time.sleep(1)
    x, y, z = mc.player.getTilePos()
    block_up = mc.getBlock(x, y + 2, z)
    score += 1
    mc.postToChat(f"ваш результат: {score}")
mc.postToChat(f"окончательный счет: {score}")
if score > 15:
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x-15,y-10,z-5,x+5,y+10,z+5,38)