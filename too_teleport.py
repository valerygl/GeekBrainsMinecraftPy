import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(3)

mc.create()
count = 0

while count <= 5:
    x = random.randint(-127, 127)
    z = random.randint(-127, 127)
    y = mc.getHeight(x, z) + 1
    mc.player.setTilePos(x, y, z)
    count += 1
    time.sleep(1)
mc.postToChat("game over")