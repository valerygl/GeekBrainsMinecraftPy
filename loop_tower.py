import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


x, y, z = mc.player.getTilePos()

height = int(input("введи высоту башни"))
height = random.randint(height - 2, height + 2)
height = max(height, 256 - mc.getHeight(x, z))

time.sleep(5)
count = 0

blocks = 84, 28, 29, 16, 37
while count + y < height:
    mc.setBlock(x, y + count, z, random.choice(blocks))
    count += 1

print("count = ", count)


