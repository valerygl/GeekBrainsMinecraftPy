import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

my_items = [15, 12, 13, 14, 42, 56, 48]

height = 0

for item in my_items:
    mc.setBlock(x, y + height, z, item)
    height = height + 1
    time.sleep(1)