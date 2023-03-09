import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

my_items = [15, 12, 13, 14, 123, 232, 121, 212]

height = 0

for item in my_items:
    if item > 80:
        mc.setBlock(x, y + height, z, item)
    height = height + 1
    time.sleep(1)