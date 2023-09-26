from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
height = 0
time.sleep(5)

for _ in range(3):
    for _ in range(5):
        mc.setBlock(x, y + height, z, 56)
        height += 1
        time.sleep(0.1)
    mc.postToChat("шаг внешнего цикла")
    mc.setBlock(x, y, z + 1, 11)
