import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

time.sleep(10)

answer = input("создать кратор? y/n")
if answer == "y":
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x + 5, y + 5, z + 5, x -5, y - 60, z - 5, 0)
    mc.postToChat("бу бах")