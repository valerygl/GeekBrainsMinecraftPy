import random
import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()


answer = input("создать кратор? y/n ")
time.sleep(10)

if answer == "y":

    mc.setBlocks(x + 5, y + 5, z + 5, x -5, y - 60, z - 5, 0)
    mc.postToChat("бу бах")
    print("Crater")
else:
    x += random.randint(-100, 100)
    z += random.randint(-100, 100)
    mc.player.setPos(x , y + 10, z )
    print("teleport")