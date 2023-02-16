import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()


answer = input("создать кратор? y/n")
time.sleep(10)

if answer == "y":

    mc.setBlocks(x + 5, y + 5, z + 5, x -5, y - 60, z - 5, 0)
    mc.postToChat("бу бах")
    print("Crater")
else:
    mc.player.setPos(x + 20, y + 4, z + 20)
    print("teleport")