
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
file = open("position.txt", "a")
file.write(str(x) + '\n' + str(y) + "\n" + str(z) + "\n" + "\n")

file.close()