from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(8)
x, y, z = mc.player.getTilePos()

under = mc.getBlock(x, y - 1, z)
above = mc.getBlock(x, y + 2, z)

air = 0

in_air = under == air and above == air
mc.postToChat("Игрок в летат, давай спускайся!!!: " + str(in_air))
