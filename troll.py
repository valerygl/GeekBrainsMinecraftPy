import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(1)

x, y, z = mc.player.getTilePos()
block = 10  # в переменную сохраняю инденфикатор блока иденфикатор лавы

mc.setBlock(x, y - 1, z, block)
