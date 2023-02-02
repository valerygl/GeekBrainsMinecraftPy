import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(3)

x, y, z = mc.player.getTilePos()
block = 58  # в переменную сохраняю инденфикатор блока

mc.setBlock(x, y, z, block)
mc.setBlock(x, y + 1, z, block + 1)
mc.setBlock(x, y + 2, z, block + 2)
mc.setBlock(x, y + 3, z, block + 3)
mc.setBlock(x, y + 4, z, block + 4)
mc.setBlock(x, y + 5, z, block + 5)
mc.setBlock(x, y + 6, z, block + 6)
mc.setBlock(x, y + 7, z, block + 7)
mc.setBlock(x, y + 8, z, block + 8)
mc.setBlock(x, y + 9, z, block + 9)