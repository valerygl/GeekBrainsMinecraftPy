import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()


time.sleep(2)


x, y, z = mc.player.getTilePos()

mc.setBlock(x - 6, y, z, 5)
mc.setBlock(x - 6, y + 1, z, 5)
mc.setBlock(x - 6, y + 2, z, 5)
mc.setBlock(x - 6, y + 3, z, 5)
mc.setBlock(x - 6, y + 4, z, 9)


mc.setBlock(x - 5, y, z - 3, 5)
mc.setBlock(x - 6, y, z - 3, 5)
mc.setBlock(x - 7, y, z - 3, 5)
mc.setBlock(x - 4, y, z - 3, 5)
mc.setBlock(x - 8, y, z - 3, 5)

mc.setBlock(x - 3, y, z - 2, 5)
mc.setBlock(x - 3, y, z - 1, 5)
mc.setBlock(x - 3, y, z, 5)
mc.setBlock(x - 3, y, z + 1, 5)
mc.setBlock(x - 3, y, z + 2, 5)

mc.setBlock(x - 5, y, z + 3, 5)
mc.setBlock(x - 6, y, z + 3, 5)
mc.setBlock(x - 7, y, z + 3, 5)
mc.setBlock(x - 4, y, z + 3, 5)
mc.setBlock(x - 8, y, z + 3, 5)

mc.setBlock(x - 9, y, z - 2, 5)
mc.setBlock(x - 9, y, z - 1, 5)
mc.setBlock(x - 9, y, z, 5)
mc.setBlock(x - 9, y, z + 1, 5)
mc.setBlock(x - 9, y, z + 2, 5)

mc.setBlock(x - 4, y - 1, z - 1, 5)
mc.setBlock(x - 5, y - 1, z - 1, 5)
mc.setBlock(x - 6, y - 1, z - 1, 5)
mc.setBlock(x - 7, y - 1, z - 1, 5)
mc.setBlock(x - 8, y - 1, z - 1, 5)
mc.setBlock(x - 4, y - 1, z - 2, 5)
mc.setBlock(x - 5, y - 1, z - 2, 5)
mc.setBlock(x - 6, y - 1, z - 2, 5)
mc.setBlock(x - 7, y - 1, z - 2, 5)
mc.setBlock(x - 8, y - 1, z - 2, 5)
mc.setBlock(x - 4, y - 1,  z + 1, 5)
mc.setBlock(x - 5, y - 1, z + 1, 5)
mc.setBlock(x - 6, y - 1, z + 1, 5)
mc.setBlock(x - 7, y - 1, z + 1, 5)
mc.setBlock(x - 8, y - 1, z + 1, 5)
mc.setBlock(x - 4, y - 1, z + 2, 5)
mc.setBlock(x - 5, y - 1, z + 2, 5)
mc.setBlock(x - 6, y - 1, z + 2, 5)
mc.setBlock(x - 7, y - 1, z + 2, 5)
mc.setBlock(x - 8, y - 1, z + 2, 5)
mc.setBlock(x - 4, y - 1, z, 5)
mc.setBlock(x - 5, y - 1, z, 5)
mc.setBlock(x - 6, y - 1, z, 5)
mc.setBlock(x - 7, y - 1, z, 5)
mc.setBlock(x - 8, y - 1, z, 5)
