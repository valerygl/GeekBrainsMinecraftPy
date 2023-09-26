import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

mc.setBlocks(x+1, y, z+1, x+ 18, y-200, z + 18, 0)