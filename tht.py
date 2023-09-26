from mcpi import entity
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
blockid = 46

time.sleep(3)
mc.player.setPos(x - 5, y, z - 5)
time.sleep(2)

mc.setBlocks(x, y, z, x + 49, y + 49, z + 49, blockid)