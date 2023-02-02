
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(8)

x, y, z = mc.player.getTilePos()

length = 5
height = 6
width = 7
block = 4

mc.setBlocks(x, y, z, x + length, y + height, z + width, block)

air = 0
mc.setBlocks(x+1, y+1, z+1, x + length-1, y + height-1, z + width-1, air)