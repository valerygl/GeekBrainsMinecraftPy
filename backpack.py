import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

my_items = [15, 121, 57, 65, 2]
x, y, z = mc.player.getTilePos()

time.sleep(3)
mc.setBlock(x, y, z, my_items[0])
mc.postToChat(my_items[0])
mc.setBlock(x, y+1, z, my_items[1])
mc.postToChat(my_items[1])
mc.setBlock(x, y+2, z, my_items[2])
mc.postToChat(my_items[2])
mc.setBlock(x, y+3, z, my_items[3])
mc.postToChat(my_items[3])
mc.setBlock(x, y+4, z, my_items[4])
mc.postToChat(my_items[4])






