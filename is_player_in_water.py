from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(8)
x, y, z = mc.player.getTilePos()

block_type = mc.getBlock(x, y, z)

water = 8

if block_type == water:
    mc.postToChat("игрок в воде")
else:
    mc.postToChat("игрок НЕ в воде, он тут: ", block_type)