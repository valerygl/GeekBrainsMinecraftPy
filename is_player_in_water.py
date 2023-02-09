from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(8)
x, y, z = mc.player.getTilePos()

block_type = mc.getBlock(x, y, z)

water = 8
in_water = block_type == water


if in_water:
    mc.postToChat("игрок в воде")
else:
    mc.postToChat("игрок не в воде, он тут: ")
    mc.postToChat(block_type)