from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(8)
x, y, z = mc.player.getTilePos()

# block_type = mc.getBlock(x, y, z)

above = mc.getBlock(x, y + 2, z)
water = 8
in_water = above == water


if in_water:
    mc.postToChat("игрок под водой")
# else:
#     mc.postToChat("игрок не в воде, он тут: ")
#     mc.postToChat(above)