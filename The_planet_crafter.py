import random
import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
import time


def tree():
    x, y, z = mc.player.getTilePos()
    block_leaves = random.choice(18, 200, 221, 178, 226, 233, 161)
    mc.setBlocks(x, y, z, x, y - 7, z, 17)
    mc.setBlocks(x - 3, y + 8, z - 3, x + 3, y + 8, z + 3, block_leaves)
    mc.setBlocks(x - 2, y + 9, z - 2, x + 2, y + 9, z + 2, block_leaves)


while True:
    tree()
    time.sleep(6)
