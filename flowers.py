from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y - 1, z, 1)
    time.sleep(3)