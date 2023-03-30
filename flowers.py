from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y - 1, z, 46)
    time.sleep(0.0000000001)