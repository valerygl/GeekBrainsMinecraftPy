import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
def put_arbis():
    arbis = 46
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y, z, arbis)
    time.sleep(0.0001)

while True:
    put_arbis()