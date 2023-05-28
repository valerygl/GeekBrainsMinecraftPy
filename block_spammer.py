
import time
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def put(id):
    x, y, z = mc.player.getTilePos()
    mc.setblock(x, y - 1, z, id)
    time.sleep(0.5)

while True:
    block = random.randint(1,150)
    put(block)