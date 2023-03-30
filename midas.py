import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

air = 0
flow_water = 8
stand_water = 9
while True:
    x, y, z = mc.player.getTilePos()
    block_below = mc.getBlock(x, y - 1, z)
    if block_below not in (air, flow_water, stand_water):
        mc.setBlock(x, y - 1, z, 41)