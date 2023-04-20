import time
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x, y, z = mc.player.getPos()
def symbol_m(x, y, z, block_type):
mc.setBlocks(x, y, z, x, y + 5, z, block_type)
for i in range(3):

def symbol_i(x, y, z, block_type):
        mc.setBlocks(x, y, z, x, y + 5, z, block_type)
def symbol_s(x, y, z, block_type):
mc.setBlocks(x, y, z, x, y + 5, z, block_type)
mc.setBlocks(x, y, z, x + 4, y, z, block_type)
mc.setBlocks(x, y + 5, z, x + 4, y + 5, z, block_type)

def symbol_h(x, y, z, block_type):
for i in range(6):
mc.setBlock(x + i, y + i, z, block_type)
mc.setBlock(x + 6 - i, y + i, z, block_type)

def symbol_a(x, y, z, block_type):
mc.setBlocks(x, y, z, x, y + 5, z, block_type)
mc.setBlocks(x + 4, y, z, x + 4, y + 5, z, block_type)
mc.setBlocks(x, y + 5, z, x + 3, y + 5, z, block_type)
mc.setBlocks(x, y + 3, z, x + 3, y + 3, z, block_type)

x, y, z = mc.player.getPos()
symbol_m(x, y, z )
symbol_i(x + 10, y, z, 1)
symbol_s(x + 20 ,y, z, 1)
symbol_h(x + 30 ,y, z, 1)
symbol_a(x + 40 ,y, z, 1)