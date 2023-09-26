import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


def platform(x_p, y_p, z_p, block_p):
    mc.setBlocks(x_p, y_p, z_p, x_p + 20, y_p, z_p + 20, block_p, 1)



def tree(x, y, z, trunk, crown):
    mc.setBlocks(x, y, z, x, y + 7, z, trunk)
    for i in range(3):
        mc.setBlocks(x - 3 + i, y + 8 + i, z - 3 + i, x + 3 - i, y + 8 + i, z + 3 - i, crown)

def  Plof(x, y, z):
    platform(x + 4 , y , z, 1)
    tree(x + 6, y + 1, z + 2,  17, 18)
    tree(x + 14, y + 1, z + 2,  17, 18)
    tree(x + 22, y + 1, z + 2,  17, 18)
    tree(x + 6, y + 1, z + 8,  17, 18 )
    tree(x + 6, y + 1, z + 14,  17, 18 )
    tree(x + 6, y + 1, z + 19,  17, 18 )
    tree(x + 14, y + 1, z + 19,  17, 18)
    tree(x + 22, y + 1, z + 19,  17, 18 )
    tree(x + 22, y + 1, z + 10, + 17, 18, )


def window(x_window, y_window, z_window, block_window=0):  # окна дома
    mc.setBlocks(x_window, y_window + 2, z_window + 3, x_window + 10, y_window + 4, z_window + 4, block_window)

def base(x_base, y_base, z_base, height_base, block_base):  # стены дома
    air = 0
    mc.setBlocks(x_base, y_base, z_base, x_base + height_base, y_base + height_base, z_base + height_base, block_base)
    mc.setBlocks(x_base + 1, y_base + 1, z_base + 1, x_base + height_base - 1, y_base + height_base - 1, z_base + height_base - 1, air)
    mc.setBlock(x_base + 2, y_base, z_base + 2, 91)


def door(x_door, y_door, z_door, block_door=0):  # дверь дома
    mc.setBlocks(x_door, y_door + 1, z_door + 5, x_door + 3, y_door + 4, z_door + 3, block_door)




def hipped_roof(x_roof, y_roof, z_roof, height_roof, block):  # крыша дома
    levels = range(height_roof) # [0, 1, 2, 3, 4], если height_roof = 5
    for level in levels:
        mc.setBlocks(
            x_roof - level,
            y_roof,
            z_roof - level,
            x_roof + level,
            y_roof,
            z_roof + level,
            block
        )
        y_roof -= 1


def house(xx, yy, zz):
    xx = x + 11
    yy = y
    zz = z + 7
    time.sleep(0.5)
    hipped_roof(xx + 3, yy + 10, zz + 3, 5, 5)
    material = random.choice([1, 162, 19, 56, 67, 27, 13, 73, 92])
    base(xx, yy, zz, 6, material)
    door(xx, yy, zz)



def village():
    Plof(x, y, z)
    house(x, y, z)


x, y, z = mc.player.getTilePos()

for i in range(10):  # улица из 10 одинаковых домов
    village()
    x = x + 25