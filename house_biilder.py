from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create()


def window(x_window, y_window, z_window, block_window=0):
    mc.setBlocks(x_window, y_window + 2, z_window + 3, x_window + 10, y_window + 4, z_window + 4, block_window)


def hipped_roof(x_roof, y_roof, z_roof, height_roof, block):
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


def fence(x, y, z):
    mc.setBlocks(x - 2, y , z - 2, x + 12, y + 1, z + 12, 85)
    mc.setBlocks(x - 1, y , z - 1, x + 11, y + 1, z + 11, 0)

def tree(x, y, z, trunk, crown):
    mc.setBlocks(x - 1, y, z - 1, x - 1, y + 7, z - 1, trunk)
    for j in range(3):
        mc.setBlocks(x - 3 + j, y + 8 + j, z - 3 + j, x + 3 - j, y + 8 - j, z + 3 - j, crown)



def base(x_base, y_base, z_base, height_base, block_base):
    air = 0
    mc.setBlocks(x_base, y_base, z_base, x_base + height_base, y_base + height_base, z_base + height_base, block_base)
    mc.setBlocks(x_base + 1, y_base + 1, z_base + 1, x_base + height_base - 1, y_base + height_base - 1, z_base + height_base - 1, air)
    mc.setBlock(x_base + 2, y_base, z_base + 2, 91)


def door(x_door, y_door, z_door, block_door=0):
    mc.setBlocks(x_door, y_door + 1, z_door + 5, x_door + 3, y_door + 4, z_door + 3, block_door)


def flower_bed(x, y, z, flower, bed):
    mc.setBlocks(x, y, z, x + 4, y + 4, bed)
    mc.setBlocks(x + 1, y + 1, z + 1, x + 3, y - 1, z + 3, 2)
    mc.setBlocks(x + 1, y + 2, z + 1, x + 3, y, z + 3, flower)


def garden():
    x, y, z = mc.player.getTilePos()
    tree(x - 5, y, z, 17, 18)
    flower_bed(x - 10, y, z - 4, 38, 45)

def house():
    x, y, z = mc.player.getTilePos()
    time.sleep(7)
    fence(x, y, z) # забор нужно делать ДО дома, чтобы воздухом не уничтожить нижний слой дома
    hipped_roof(x + 3, y + 10, z + 3, 5, 5)
    base(x, y, z, 6, 1)
    door(x, y, z)
    window(x, y, z)
    tree(x, y, z, 17, 18)
    #flower_bed(x, y, z)  # // TODO в вызов функции нужно предавать еще два аргумента, flower и bed. Какие значения?

#x, y, z = mc.player.getTilePos()
#mc.setBlocks(x - 10 , y - 10, z - 10, x + 10, y + 10, z + 10, 0)

house()

