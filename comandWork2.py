import random

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create(  )




def platform(x_p, y_p, z_p, block_p):  # площадь
    mc.setBlocks(x_p, y_p, z_p, x_p + 5, y_p, x_p + 5, block_p, 1)


def tree(x, y, z, trunk, crown):  # деревья
    mc.setBlocks(x, y, z, x, y + 7, z, trunk)
    for i in range(3):
        mc.setBlocks(x - 3 + i, y + 8 + i, z - 3 + i, x + 3 - i, y + 8 + i, z + 3 - i, crown)

def square(x, y, z): # площадь с деревьями
    platform(x + 4, y, z, 1)
    tree(x - 5, y, z, 17, 18)


def window(x_window, y_window, z_window, block_window=0):  # окна дома
    mc.setBlocks(x_window, y_window + 2, z_window + 3, x_window + 10, y_window + 4, z_window + 4, block_window)


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


def fence(x, y, z):  # забор вокруг дома
    mc.setBlocks(x - 2, y , z - 2, x + 12, y + 1, z + 12, 85)
    mc.setBlocks(x - 1, y , z - 1, x + 11, y + 1, z + 11, 0)


def base(x_base, y_base, z_base, height_base, block_base):  # стены дома
    air = 0
    mc.setBlocks(x_base, y_base, z_base, x_base + height_base, y_base + height_base, z_base + height_base, block_base)
    mc.setBlocks(x_base + 1, y_base + 1, z_base + 1, x_base + height_base - 1, y_base + height_base - 1, z_base + height_base - 1, air)
    mc.setBlock(x_base + 2, y_base, z_base + 2, 91)


def door(x_door, y_door, z_door, block_door=0):  # дверь дома
    mc.setBlocks(x_door, y_door + 1, z_door + 5, x_door + 3, y_door + 4, z_door + 3, block_door)


def flower_bed(x, y, z, flower, bed):  # это что?
    mc.setBlocks(x, y, z, x + 4, y + 4, bed)
    mc.setBlocks(x + 1, y + 1, z + 1, x + 3, y - 1, z + 3, 2)
    mc.setBlocks(x + 1, y + 2, z + 1, x + 3, y, z + 3, flower)


def garden():  # это что?
    x, y, z = mc.player.getTilePos()
    tree(x - 5, y, z, 17, 18)
    flower_bed(x - 10, y, z - 4, 38, 45)

def house():
    time.sleep(0.5)
    fence(x, y, z) # забор нужно делать ДО дома, чтобы воздухом не уничтожить нижний слой дома
    hipped_roof(x + 3, y + 10, z + 3, 5, 5)
    # material = randint(1, 100)
    material = random.choice([1, 162, 19, 56, 67, 27, 13, 73, 92])
    base(x, y, z, 6, material)
    door(x, y, z)
    window(x, y, z)
    tree(x, y, z, 17, 18)
    #flower_bed(x, y, z)  # // TODO в вызов функции нужно предавать еще два аргумента, flower и bed. Какие значения?






x, y, z = mc.player.getTilePos()
xstart = x

time.sleep(7)

square(x, y, z)  # строим площадь с деревьями

for i in range(10):  # улица из 10 одинаковых домов
    house()
    x = x + 15

mc.setBlocks(xstart -10, y, z - 20, x + 10, y, z + 20, 2)   # площадка под домом






