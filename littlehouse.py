from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create()


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



def house():
    x, y, z = mc.player.getTilePos()
    time.sleep(7)
    # fence(x, y, z) # забор нужно делать ДО дома, чтобы воздухом не уничтожить нижний слой дома
    hipped_roof(x + 3, y + 10, z + 3, 4, 5)
    # base(x, y, z, 6, 1)
    # door(x, y, z)
    # window(x, y, z)
    # tree(x, y, z, 17, 18)
    #flower_bed(x, y, z)  # // TODO в вызов функции нужно предавать еще два аргумента, flower и bed. Какие значения?

#x, y, z = mc.player.getTilePos()
#mc.setBlocks(x - 10 , y - 10, z - 10, x + 10, y + 10, z + 10, 0)

house()

