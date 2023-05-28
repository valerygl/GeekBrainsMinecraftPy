from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(2)

def get_wool_state(color):
    if color == "белый":
        return 0
    elif color == "оранжевый":
        return 1
    elif color == "сиреневый":
        return 2
    elif color == "светло-синий":
        return 3
    elif color == "желтый":
        return 4
    elif color == "лаймовый":
        return 5
    elif color == "розовый":
        return 6
    elif color == "серый":
        return 7
    elif color == "светло-серый":
        return 8
    elif color == "бирюзовый":
        return 9
    elif color == "фиолетовый":
        return 10
    elif color == "синий":
        return 11
    elif color == "коричневый":
        return 12
    elif color == "зеленый":
        return 13
    elif color == "красный":
        return 14
    elif color == "черный":
        return 15
color_string = input("напиши цвет ")
state = get_wool_state(color_string)

x, y, z = mc.player.getTilePos()
mc.setBlock(x, y, z, 35, state)
