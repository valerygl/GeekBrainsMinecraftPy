from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
time.sleep(5)
wheat = 296
x, y, z = mc.player.getTilePos()
mc.setBlocks(x - 5, y, z - 5, x + 5, y, z + 5, wheat)
mc.postToChat("Psheniza done")

coordinats = "you are here - " + str(x) + ", " + str(y) + ", " + str(z)
mc.postToChat(coordinats)
mc.postToChat("переключись в PyCharm и введи примерно эти Х и Z и точно эту же Y!")



x1 = input("введи x 1")
y1 = input("введи y 1")
z1 = input("введи z 1")
x2 = input("введи x 2")
y2 = input("введи y 2")
z2 = input("введи z 2")

time.sleep(5)
type1 = mc.getBlock(x1, y1, z1)

type2 = mc.getBlock(x2, y2, z2)


if type1 != wheat and type2 != wheat:
    mc.postToChat("тут и там нет пшеницы, надо посадить")
    print("need to plant")
else:
    mc.postToChat("где- то пшеница уже есть")
    print("there is whaet")
