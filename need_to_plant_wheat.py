from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

wheat = 296

x1 = input("введи x 1")
y1 = input("введи y 1")
z1 = input("введи z 1")
x2 = input("введи x 2")
y2 = input("введи y 2")
z2 = input("введи z 2")

time.sleep(8)
type1 = mc.getBlock(x1, y1, z1)

type2 = mc.getBlock(x2, y2, z2)

if type1 == wheat and type2 == wheat:
    mc.postToChat("тут и там пшеница")


if type1 != wheat and type2 != wheat:
    mc.postToChat("тут и там нет пшеницы, надо посадить")

if type1 == wheat and type2 != wheat:
    mc.postToChat("не нужно сажать пшеницу")



if type1 != wheat and type2 == wheat:
    mc.postToChat("не нужно сажать пшеницу")
