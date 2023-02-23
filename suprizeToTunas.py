import random
import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

time.sleep(5)

answer = input("получить подарок? y/n")


answer1 = input("введите что хотите получить")




if answer == "y":
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x - 2, y, z + 2, x + 2, y, z + 6, 1)
    mc.setBlocks(x - 1, y + 1, z + 3, x + 1, y + 1, z + 5, 1)
    mc.setBlock(x, y + 2, z + 4, 56)




elif answer1 == "n":
    print("не хотите как хотите")





else:
    print("простите другого нет:(")