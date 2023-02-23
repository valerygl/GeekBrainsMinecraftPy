import random
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("получить подарок? y/n")
answer1 = int(input("введите что хотите получить"))




if answer == "y":
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x - 2, y, z + 2, x + 2, y, z + 6, 1)
    mc.setBlocks(x - 1, y + 1, z + 3, x + 1, y + 1, z + 5, 1)
    mc.setBlock(x, y + 2, z + 4, answer1)

    typeTop = mc.getBlock(x, y + 2, z + 4)
    is_good_suprise = typeTop == 56
    time.sleep(5)

    if is_good_suprise:
        mc.postToChat("поздравляем")
    else:
        mc.postToChat("простите другого нет")




else:
    print("не хотите как хотите")
