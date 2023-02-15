from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

wheat = 296

# делаем площадку, где точно есть пшеница
time.sleep(5)
x, y, z = mc.player.getTilePos()
mc.setBlocks(x - 10, y - 1, z - 10, x + 10, y - 1, z + 10, wheat)

im_here = "Вот твои координаты: Х=" + str(x) + ", У=" + str(y) + ", Z=" + str(z)
mc.postToChat(im_here)  # печатаю в чат
print(im_here)  # печатаю то же самое в консоль
mc.postToChat("в PyCharm и введи _примерно_ эти Х и Z и точно эту же Y!")



x1 = input("введи x 1")
y1 = input("введи y 1")
z1 = input("введи z 1")
x2 = input("введи x 2")
y2 = input("введи y 2")
z2 = input("введи z 2")

time.sleep(8)
type1 = mc.getBlock(x1, y1, z1)

type2 = mc.getBlock(x2, y2, z2)


if type1 != wheat and type2 != wheat:
    mc.postToChat("тут и там нет пшеницы, надо посадить")
else:
    mc.postToChat("где- то пшеница уже есть")
