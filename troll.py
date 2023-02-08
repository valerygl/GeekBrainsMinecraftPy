from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x, y, z = mc.player.getTilePos()
block_str = input("введи то что появится под тобой")  # в переменную сохраняю инденфикатор блока
block = int(block_str) # преобразуем строку в целое число





time.sleep(8)
mc.setBlock(x, y - 1, z, block)
