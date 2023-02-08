from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x, y, z = mc.player.getTilePos()
block_str = input("введи то что появится под тобой")  # в переменную сохраняю инденфикатор блока
block = int(block_str) # преобразуем строку в целое число

size_str = input("введи размер")  # в переменную сохраняется размер
size = int(size_str) # преобразуем строку в целое число


time.sleep(8)
# mc.setBlock(x - 1,  y - 1 , z, block)
# mc.setBlock(x - 1, y - 1, z - 1, block)
# mc.setBlock(x - 1, y - 1, z + 1, block)
# mc.setBlock(x + 1, y - 1, z, block)
# mc.setBlock(x + 1,  y - 1, z + 1, block)
# mc.setBlock(x + 1, y - 1, z - 1, block)
# mc.setBlock(x, y - 1, z, block)
# mc.setBlock(x, y - 1, z - 1, block)
# mc.setBlock(x, y - 1, z + 1, block)


mc.setBlocks(x - size, y - 1, z - size, x + size, y - 1, z + size, block)
