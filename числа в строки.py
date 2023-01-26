from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = int(input("введи координаты x: "))
y = int(input("введи координаты y: "))
z = int(input("введи координаты z: "))
id = int(input("введите id блока: "))
mc.player.setTilePos(x, y, z, id)
mc.setBlock(x, y, z, id)