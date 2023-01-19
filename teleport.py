import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x = 2000
y = 10
z = 2000

time.sleep(15)
mc.player.setTilePos(x, y, z)

a, b, c = mc.player.getPos()
print(a, b, c)

time.sleep(10)


x = 4000
y = 10
z = 4000
mc.player.setTilePos(x, y, z)

a, b, c = mc.player.getPos()
print(a, b, c)