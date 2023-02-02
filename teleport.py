import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

time.sleep(8)

x = 658.5
y = 24.5
z = 140.5
mc.player.setPos(x, y, z)
mc.postToChat(f"{x} {y} {z}")

time.sleep(3)

x = 293.5
y = 293.5
z = 928.5
mc.player.setPos(x, y, z)
mc.postToChat(f"{x} {y} {z}")

time.sleep(3)

x = 928.5
y = 19.5
z = 284.5
mc.player.setPos(x, y, z)
mc.postToChat(f"{x} {y} {z}")

time.sleep(3)

x = 300.5
y = 394.5
z = 155.5
mc.player.setPos(x, y, z)
mc.postToChat(f"{x} {y} {z}")
print('done!')