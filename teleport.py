import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x = 2000
y = 10
z = 2000

time.sleep(15)  # пауза на 15 секунд, чтобы успеть переключиться в майнкрафт
mc.player.setTilePos(x, y, z)  # телепорт в координаты x, y, z

a, b, c = mc.player.getPos()  # записываем в переменные a, b, c текущее положение игрока.
# интересно, совпадут ли эти координаты с теми, в которые игрок был телепортирован и с теми, которые на экране майнкрафта?

print(a, b, c)

time.sleep(10)  # пауза на 10 секунд и еще раз то же самое


x = 4000
y = 10
z = 4000
mc.player.setTilePos(x, y, z)

a, b, c = mc.player.getPos()
print(a, b, c)