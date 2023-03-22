import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

time.sleep(5)

x = 658.5
y = 67
z = 140.5
mc.player.setPos(x, y, z)
# mc.postToChat(f"{x} {y} {z}")
mc.postToChat("пустыня - в ней можно найти пирамиды а также деревни. тебе будут попадаться кактусы с колодцами. тут хорошо,но помни ДЕРЕВЬЕВ ТУТ НЕТ")
time.sleep(13)

x = 293.5
y = 70
z = 928.5
mc.player.setPos(x, y, z)
# mc.postToChat(f"{x} {y} {z}")
mc.postToChat("савана - биом полон извилистых троп, гор, и изогнутых акацевых деревьев, много рек и озер. для выживание так себе но можно на некоторое время. возможно найдешь акакия")
time.sleep(20)

x = 375
y = 233
z = 1167
mc.player.setPos(x, y, z)
# mc.postToChat(f"{x} {y} {z}")
mc.postToChat("это гора. они очень высокие и лучше с них не спрыгивать если нету ведра воды, тотема бессмертия или рыхлого снега с лестницой или паутиной")
time.sleep(20)



x = - 655
y = 63
z = 838
mc.player.setPos(x, y, z)
# mc.postToChat(f"{x} {y} {z}")
mc.postToChat("это океан в нем ооооочень мноогооо воды. также можешь найти подводный храм")
time.sleep(10)



x = -361
y = 71
z = 852
mc.player.setPos(x, y, z)
mc.postToChat(f"{x} {y} {z}")
mc.postToChat("это разрушенный портал - в сундуке можно найти золотые вещи и часы либо обсидиан чтобы достроить портал")
time.sleep(20)
mc.postToChat("иииииииии")
time.sleep(5)


x = -387
y = 68
z = 863
mc.player.setPos(x, y, z)
mc.postToChat(f"{x} {y} {z}")
mc.postToChat("надеюсь понравилось а теперь иди выживай")
