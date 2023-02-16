import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()


xd = 960
yd = 75
zd = 181

xc = 979
yc = 69
zc = 274

answer = input("Descert or Cvety?  d\c ")
time.sleep(5)

if answer == "d":
    mc.player.setPos(xd, yd, zd)
    mc.postToChat("you are in Descert")
elif answer == "c":
    mc.player.setPos(xc, yc, zc)
    mc.postToChat("you are in Cvety")
else:
    mc.postToChat("you are wrong")