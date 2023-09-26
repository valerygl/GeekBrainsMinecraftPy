import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

file = open("pushkin.txt", "r")
for line in file:
    mc.postToChat(line)
    time.sleep(0.1)
file.close()