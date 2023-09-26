import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

username = input("напиши имя: ")
while True:
    message = input("введи сообщение или выход: ")
    if message == "выход":
        break
    else:
        mc.postToChat(f"{username}: {message}")