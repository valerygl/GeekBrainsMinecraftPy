import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
mc.player.setTilePos(x + 500, y + 100, z + 500)
mc.postToChat('Transfered successful')