import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()


class Ufo:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def build(self):
        mc.setBlocks(self.x - 1, self.y - 4, self.z - 1, self.x + 2, self.y - 4, self.z + 2, 22)
        mc.setBlocks(self.x - 2, self.y - 3, self.z - 2, self.x + 3, self.y - 3, self.z + 3, 22)
        mc.setBlocks(self.x - 2, self.y - 2, self.z - 2, self.x + 4, self.y - 2, self.z + 3, 20)
        mc.setBlocks(self.x - 2, self.y - 1, self.z - 2, self.x + 3, self.y - 1, self.z + 3, 22)
        mc.setBlocks(self.x - 1, self.y, self.z - 1, self.x + 2, self.y, self.z + 2, 22)
        mc.setBlocks(self.x, self.y + 1, self.z, self.x + 1, self.y + 1, self.z + 1, 41)
    def clean(self):
        mc.setBlocks(self.x - 4, self.y - 4, self.z - 4, self.x + 4, self.y + 1, self.z + 4, 0)


x, y, z = mc.player.getTilePos()
ufo = Ufo(x, y, z)
while True:
    ufo.build()
    time.sleep(0.5)
    ufo.clean()
    ufo.x += 1
