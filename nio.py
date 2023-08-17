from mcpi.minecraft import Minecraft

mc = Minecraft.create()

import time


class Star:
    def __init__(self, x, y, z, id):
        self.x = x
        self.y = y
        self.z = z
        self.id = id

    def build(self):
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y + 2, self.z, self.id)
        mc.setBlocks(self.x - 1, self.y + 1, self.z, self.x + 1, self.y + 1, self.z, self.id)
        mc.setBlocks(self.x, self.y + 1, self.z - 1, self.x, self.y + 1, self.z + 1, self.id)

    def clean(self):
        mc.setBlocks(self.x - 1, self.y, self.z - 1, self.x + 1, self.y + 2, self.z + 1, 0)


x, y, z = mc.player.getTilePos()
star = Star(x, y, z, 41)
while True:
    star.build()
    time.sleep(0.1)
    star.clean()
    star.x += 1