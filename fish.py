import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
time.sleep(5)


class aukvariym:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



    def build(self):
        self.glass()
        self.water()
        self.stone()
        self.criper()

    def glass(self):
        mc.setBlocks(self.x, self.y - 1, self.z, self.x + 4, self.y + 3, self.z + 9, 102)

    def water(self):
        mc.setBlocks(self.x + 1, self.y, self.z + 1, self.x + 3, self.y + 3, self.z + 8, 9)

    def stone(self):
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y + 3, self.z, 1)
        mc.setBlocks(self.x + 4, self.y, self.z, self.x + 4, self.y + 3, self.z, 1)
        mc.setBlocks(self.x, self.y, self.z + 9, self.x, self.y + 3, self.z + 9, 1)
        mc.setBlocks(self.x + 4, self.y, self.z + 9, self.x + 4, self.y + 3, self.z + 9, 1)


    def criper(self):
        entity_id = 50

        for i in range(10):
            mc.spawnEntity(x + 4, y + 20, z + 5, entity_id)

aq1 = aukvariym(x, y, z)
aq1.build()