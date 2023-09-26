from mcpi.minecraft import Minecraft

mc = Minecraft.create()


class Flowerbed:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def build(self):
        self.border()
        self.grass()

    def border(self):
        mc.setBlocks(self.x, self.y, self.z, self.x + 5, self.y, self.z + 5, 42)
        mc.setBlocks(self.x + 1, self.y, self.z + 1, self.x + 4, self.y, self.z + 4, 0)

    def grass(self):
        mc.setBlocks(self.x + 1, self.y, self.z + 1, self.x + 4, self.y, self.z + 4, 2)
        mc.setBlock(self.x + 3, self.y + 1, self.z + 3, 38)


x, y, z = mc.player.getTilePos()
flowerbed = Flowerbed(x, y, z)
flowerbed.build()