
from mcpi.minecraft import Minecraft

mc = Minecraft.create()


class Building:
    def __init__(self, width, height, lenght, pos):
        self.width = width
        self.height = height
        self.lenght = lenght
        self.pos = pos
        self.blocktype = randomint(100)

    def build(self):
        x, y, z = self.pos
        mc.setBlocks(x, y, z, x + self.width, y + self.height, z + self.lenght, self.blocktype)
        mc.setBlocks(x + 1, y + 1, z + 1, x + self.width - 1, y + self.height - 1, z + self.lenght - 1, 0)

    def clean(self):
        x, y, z = self.pos
        mc.setBlocks(x, y, z, x + self.width, y + self.height, z + self.lenght, 0)

pos = mc.player.getTilePos()
house = Building(10, 10, 10, pos)
house.build()


