import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
class Object:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

        def info(self):
            mc.postToChat('Щбъект ' + self.name + str(self.x) + str(self.y) + str(self.z))


class Forest(Object):
    def tree(self):
        height_trunk = random.randint(3, 6)
        height_leaves = random.randint(1, 3)

        mc.setBlocks(self.x, self.y - 1, self.z,
                     self.x, self.y + height_trunk, self.z, 17)

        mc.setBlocks(self.x - 3, self.y + height_trunk, self.z - 3,
                     self.x + 3, self.y + height_trunk + height_leaves, self.z + 3, 161)

        mc.setBlocks(self.x - 2, self.y + height_trunk + height_leaves, self.z - 2,
                     self.x + 2, self.y + height_trunk + height_leaves * 2, self.z + 2, 161)


    def row_trees(self, count):
        for i in range(count):
            self.tree()
            self.x += 7

x, y, z = mc.player.getTilePos()
x += 10

forest1 = Forest('лесополоса слеваааааа', x, y, z - 5)
forest2 = Forest('лесополоса справаааааааа', x, y, z + 25)

forest1.row_trees(10)
forest2.row_trees(10)

ЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁЁ