import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
time.sleep(5)

class Tvtower:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def make(self):
        self.stolb1()
        self.restoran()
        self.viewpoint()
        self.room()
        self.stolb2()

    def stolb1(self):
        mc.setBlocks(x-1,y,z-1,x+1,y+20,z+1,1)

    def restoran(self):
        mc.setBlocks(x-3,y+21,z-3,x+3,y+21,z+3,1)

    def viewpoint(self):
        mc.setBlocks(x-4,y+22,z-4,x+4,y+22,z+4,1)

    def room(self):
        mc.setBlocks(x-3,y+23,z-3,x+3,y+23,z+3,1)

    def stolb2(self):
        mc.setBlocks(x,y+24,z,x,y+45,z,1)



tower = Tvtower(x, y, z)
tower.make()