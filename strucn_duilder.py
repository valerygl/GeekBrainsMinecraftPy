import pickle
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def build_structure(x, y, z, structure):
    x_start = x
    z_start = z
    for row in structure:
        for column in row:
            for block in column:
                mc.setBlock(x, y, z, block.id, block.data)
                z += 1
            x += 1
            z = x_start
        y += 1
        x = x_start

f = open("strukture.txt", "rb")
structure = pickle.load(f)
f.close()

x, y, z = mc.player.getTilePos()
build_structure(x, y, z, structure)