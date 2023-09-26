import pickle
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
def copy_structure(x1, y1, z1, x2, y2, z2):
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    z1, z2 = min(z1, z2), max(z1, z2)
    w = x2 - x1
    h = y2 - y1
    l = z2 - z1

    structure = []
    print("секунду, я думаю.........")
    for column in range(h):
        structure.append([])
        for row in range(w):
            structure[column].append([])
            for depth in range(l):
                block = mc.getBlockWithData(x1 + row, y1 + column, z1 + depth)
                structure[column][row].append(block)
    return structure

input("иди на угол и нажми на ентер")
x1, y1, z1 = mc.player.getTilePos()

input("иди на другой угол и нажми на ентер")
x2, y2, z2 = mc.player.getTilePos()

s = copy_structure(x1, y1, z1, x2, y2, z2)
f = open("strukture.txt", "wb")
pickle.dump(s, f)
f.close()