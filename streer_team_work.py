from mcpi.minecraft import Minecraft
mc = Minecraft.create()



def platform(x_p, y_p, z_p, block_p):
    mc.setBlocks(x_p, y_p, z_p, z_p + 5, y_p, x_p + 5, block_p, 1)



def tree(x, y, z, trunk, crown):
    mc.setBlocks(x, y, z, x, y + 7, z, trunk)
    for i in range(3):
        mc.setBlocks(x - 3 + i, y + 8 + i, z - 3 + i, x + 3 - i, y + 8 + i, z + 3 - i, crown)

def  Plof(x,y, z):
    platform(x + 4, y, z, 1)
    tree(x - 5, y, z, 17, 18,)

x, y, z = mc.player.getTilePos()
Plof(x, y, z)