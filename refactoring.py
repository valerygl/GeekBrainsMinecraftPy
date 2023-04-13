import random
import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


def random_teleport():
    time.sleep(5)
    x = random.randint(150, 360)
    y = random.randint(65, 80)
    z = random.randint(100, 300)
    mc.player.setTilePos(x, y, z)

def create_home():
    mc.postToChat("ПОДОЖДИ, строю дом")
    mc.setBlocks(x, y, z, x + 5, y + 5, z + 5, 5)
    mc.setBlocks(x, y, z, x + 4, y + 4, z + 4, 0)

random_teleport()
create_home()
