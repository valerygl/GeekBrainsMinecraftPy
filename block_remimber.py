from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(2)

def remind_block(name):
    if name == "камень":
        return 1
    if name == "песок":
        return 12
    if name == "динамит":
        return 49
block_name = input("напиши название блока: ")
block_id = remid_block(block_name)
if block_id is None:
    print("Eror 404")
else:
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y, z, block_id)
