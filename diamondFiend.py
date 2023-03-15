from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

for block_y in range(y, -64, -1):
    block = mc.getBlock(x, block_y, z)
    print(block)
    if block == 56 or block == 633:
        mc.postToChat(f"алмаз есть?: {block_y}")
        break
    else:
        mc.postToChat("алмаза нет")