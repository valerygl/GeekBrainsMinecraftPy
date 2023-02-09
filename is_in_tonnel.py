from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(8)
x, y, z = mc.player.getTilePos()

under = mc.getBlock(x, y - 1, z)
above = mc.getBlock(x, y + 2, z)


# if under == above:
    # mc.postToChat("in tonnel")

in_tonnel = under != 0 and above != 0
mc.postToChat("Игрок в тоннеле: " + str(in_tonnel))
