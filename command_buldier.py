from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:
    command = input("что хочешь сделать? (куб, пирамида, башня) или выход: ")
    if command == "выход":
        break
    elif command == "куб":
        block_id = int(input("введи айди блока: "))
        x, y, z = mc.player.getTilePos()
        mc.setBlocks(x, y, z, x + 10, y + 10, z + 10, block_id)
        print("куб готов")
    elif command == "пирамида":
        block_id = int(input("введи айди блока: "))
        x, y, z = mc.player.getTilePos()
        for i in range(10):
            mc.setBlocks(x - i, y, z - i, x + i, y, z + i, block_id)
            y -= 1
        print("пирамида готова")
    elif command == "башня":
        block_id = int(input("введи айди блока: "))
        x, y, z = mc.player.getTilePos()
        for i in range(20):
            mc.setBlock(x + 10, y + i, z, block_id)
        print("башня готова")
    else:
        print("404, element not found")
print("до свидания")