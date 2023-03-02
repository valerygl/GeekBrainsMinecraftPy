import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
# за 15 сек нужно успеть 3 раза тыкнуть .мечом по блокам правой кнопкой

time.sleep(15)
block_hits = mc.events.pollBlockHits()
my_items = []

mc.postToChat("lets go")

item0_pos = block_hits[0].pos
item0 = mc.getBlock(item0_pos)
my_items.append(item0)

item1_pos = block_hits[1].pos
item1 = mc.getBlock(item1_pos)
my_items.append(item1)

item2_pos = block_hits[2].pos
item2 = mc.getBlock(item2_pos)
my_items.append(item2)


mc.postToChat(f"0: {my_items[0]}, 1: {my_items[1]}, 2: {my_items[2]}")






