import random
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
# за 15 сек нужно успеть 3 раза тыкнуть .мечом по блокам правой кнопкой
time.sleep(5)

x = random.randint(1, 1000)
x = random.randint(1, 1000)
y = random.randint(1, 100)



mc.player.setPos(x, y, z)
time.sleep(30)
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


item3_pos = block_hits[3].pos
item3 = mc.getBlock(item3_pos)
my_items.append(item3)


item4_pos = block_hits[4].pos
item4 = mc.getBlock(item4_pos)
my_items.append(item4)


item5_pos = block_hits[5].pos
item5 = mc.getBlock(item5_pos)
my_items.append(item5)


item6_pos = block_hits[6].pos
item6 = mc.getBlock(item6_pos)
my_items.append(item6)

item7_pos = block_hits[7].pos
item7 = mc.getBlock(item7_pos)
my_items.append(item7)



item8_pos = block_hits[8].pos
item8 = mc.getBlock(item8_pos)
my_items.append(item8)

item9_pos = block_hits[9].pos
item9 = mc.getBlock(item8_pos)
my_items.append(item9)

mc.postToChat(f"0: {my_items[0]}, 1: {my_items[1]}, 2: {my_items[2]}, 3: {my_items[3]}, 4: {my_items[4]}, 5: {my_items[5]}, 6: {my_items[6]}, 7: {my_items[7]}, 8: {my_items[8]}, 9: {my_items[9]}")