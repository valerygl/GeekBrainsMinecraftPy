from mcpi import entity
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
possible_animals = [entity.COW, entity.CREEPER, entity.HORSE]


class AnimalSpawner:
    def spawn_animal(self, pos, animal):

        if animal in possible_animals:
            mc.spawnEntity(pos, animal.id)
        else:
            print("что то не то")


spawner = AnimalSpawner()
while True:
    print("что можем призвать:")
    for i, animal in enumerate(possible_animals):
        print(f"{i + 1}) {animal.name}")
    animal = int(input("введи айди моба:"))
    if animal > len(possible_animals):
        print("такого нет")
        continue
    pos = mc.player.getTilePos()
    spawner.spawn_animal(pos, possible_animals[animal - 1])
