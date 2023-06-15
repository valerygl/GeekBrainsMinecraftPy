
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

class Location:
    def __init__(self, position, name, info):
        self.info = info
        self.p = position
        self.name = name

    def tp(self):
        mc.player.setTilePos(self.p)
        mc.postToChat(f"Welcpme to {self.p}")
        mc.postToChat(f"Info about this location: {self.info}")



ocean = Location((-212, 83, 60), "океан", "океан это большое озеро")

ocean.tp()
time.sleep(8)


boloto = Location((0, 72, 0), "болото", "болото как море, только болотное :з")

boloto.tp()
time.sleep(8)


les = Location((-439, 90, -482), "лес", "в лесу много деревьев и пчеееееел")

les.tp()
time.sleep(10)


