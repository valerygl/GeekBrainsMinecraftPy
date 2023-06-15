
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


class Location:
    def __init__(self, position, name, info):
        self.info = info
        self.p = position
        self.name = name

    def tp(self):
        mc.player.setTilePos(self.p)
        mc.postToChat(f"Welcpme to {self.p}")
        mc.postToChat(f"Info about this location: {self.info}")
ocean = Location(
    position=(-439, 90, 482)
    name="океан",
    "океан это большое озеро"
)

