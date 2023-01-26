from mcpi.minecraft import Minecraft
mc = Minecraft.create()

text = input("введите текст котрый надо отправить: ")
mc.postToChat(text)
