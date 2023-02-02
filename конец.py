import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

name = input('Введите своё имя ')
surname = input("Введите свою фамилию ")
hobby = input("Введите свое хобби ")
age = input("введите свой возраст ")

stroka = "В игру пришел", name, surname, ", любит", hobby,", возраст", age

time.sleep(7)

# mc.postToChat("В игру пришел", name, surname, ", любит", hobby,", возраст", age)
mc.postToChat(stroka)
