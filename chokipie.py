class Chocopie:
    def __init__(self, material):
        self.material = material
    def say(self):
        print("I'm made from " + self.material)




food = Chocopie("chocolate")
food.say()