class Animal:
    def __init__(self, nickname, poroda):
        self.poroda = poroda
        self.nickname = nickname
        
    def print_poroda(self):
        print(f"у этого животного порода  {self.poroda} ")

    def print_name(self):
        print(f"его/её зовут  {self.nickname}")


catMia = Animal("Mia", "cat")
dogArcan = Animal("Arcan","dog")

catMia.print_poroda()
catMia.print_name()
print()

dogArcan.print_poroda()
dogArcan.print_name()
