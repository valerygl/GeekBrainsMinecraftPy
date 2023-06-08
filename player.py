class Player:
    def __init__(self, hp, armor, nickname, satiety):
        self.health_points = hp
        self.armor = armor
        self.nickname = nickname
        self.satiety = satiety

    def print_hp(self):
        print(f"У меня {self.health_points} здоровья!")

    def print_name(self):
        print(f"Меня зовут {self.nickname}!")

    def death(self):
        print("грусть, печаль, обида...")

    def fall(self):
        print("Я упал....")
        self.health_points -= 50
        if self.health_points <= 0:
            self.death()


steve = Player(100, 10, "Steve", 10)
steve.print_name()
steve.print_hp()
steve.fall()
steve.print_hp()
steve.fall()