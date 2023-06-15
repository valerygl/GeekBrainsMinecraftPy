class User:
    def __init__(self, name, age, city):
        self.n = name
        self.a = age
        self.c = city
    def print_name(self):
        print(f"меня зовут {self.n}")

    def print_city(self):
        print(f"я из города {self.c}")



petya = User("Petya", 25, "NY")
petya.print_name()
petya.print_city()
