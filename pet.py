class Pet:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.happiness = 100
        self.tricks = []

    def get_status(self):
        print(f"Name: {self.name}, Energy: {self.energy}%, Happiness: {self.happiness} %")

    def eat(self):
        self.energy += 10
        print(f"{self.name} is eating. Energy increased to {self.energy}%.")

    def sleep(self):
        self.energy += 20
        print(f"{self.name} is sleeping. Energy increased to {self.energy}%.")

    def play(self):
        if self.energy > 10:
            self.energy -= 10
            self.happiness += 10
            print(f"{self.name} is playing. Energy: {self.energy}%, Happiness: {self.happiness}%.")
        else:
            print(f"{self.name} is too tired to play.")

    def train(self, trick):
        if self.energy > 15:
            self.energy -= 15
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}.")
        else:
            print(f"{self.name} is too tired to train.")

    def show_tricks(self):
        print(f"{self.name} knows the following tricks: {', '.join(self.tricks) if self.tricks else 'No tricks yet.'}")