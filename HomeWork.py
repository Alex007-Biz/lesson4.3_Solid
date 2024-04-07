from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self, weapon):
        self.weapon_type = weapon
        pass
class Fighter():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
    def change_weapon(self, weapon):
        print(f"смена оружия на {weapon}")
class Monster():
    pass

class Sword(Weapon):
    def attack(self, weapon):
        print("Атака мечом")

class Bow(Weapon):
    def attack(self, weapon):
        print("Выстрел из лука")

jason = Fighter("Jason", "sword")
jason.change_weapon("sword")

jason.change_weapon("bow")

bob = Bow("bow")
bob.attack("bow")
