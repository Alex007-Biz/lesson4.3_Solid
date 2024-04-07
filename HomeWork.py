from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Fighter():
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon
    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"смена оружия на {weapon}")

    def fight(self):
        print(self.weapon.attack())


class Monster():
    pass

class Sword(Weapon):
    def attack(self):
        print("Атака мечом")

class Bow(Weapon):
    def attack(self):
        print("Выстрел из лука")

sword1 = Sword()
bow1 = Bow()
jason = Fighter("Jason", sword1)
jason.change_weapon("sword")

jason.change_weapon("bow")
sword1.attack()

