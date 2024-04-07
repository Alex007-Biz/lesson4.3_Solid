class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("птица летает")

class Ping(Bird):
    pass

p = Ping("Сара")

p.fly()
