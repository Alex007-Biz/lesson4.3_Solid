class Bird():
    def fly(self):
        print("птица летает")

class Duck():
    def fly(self):
        print("Утка летает быстро")

def fly_in_the_sky(animal):
    animal.fly()

duck = Duck()
bird = Bird()

# bird.fly()
# duck.fly()
fly_in_the_sky(duck)

