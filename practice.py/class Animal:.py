class Animal:
    location = "India"
    def __init__(self,name):
        self.name = name

    def speaks(self):
        print("Speaking now..")

class Dog(Animal):
    def speaks(self):
        print("Woof!")



class Cat(Animal):
    def speaks(self):
        super().speaks()
        print("Meow!")


d1 = Dog("Tommy")
d1.speaks()
print(d1.location)

c1 = Cat("Snow")
c1.speaks()