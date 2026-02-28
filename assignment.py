class Car:
    def drive():
        print("Car is moving")


c1 = Car.drive()


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"Person's name: {self.name} and age is {self.age}")

p1 = Person("Yash", 28)
p1.get_info()


class Animal:
    def sound():
        print("Some Sound")

class Dog(Animal):
    def sound():
        print("Bark!")

d1 = Dog.sound()


class Test:
    def show(self):
        return "Hello"

t1 = Test()
print(t1.show())