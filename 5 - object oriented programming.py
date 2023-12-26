class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def print_details(self):
        print("Model:", self.model)
        print("Color:", self.color)

car = Car("BMW", "red")
print(car.model)
car.print_details()

# Inheritance

class ElectricCar(Car):
    def __init__(self, model, color, battery_size):
        super().__init__(model, color)
        self.battery_size = battery_size

    def print_details(self):
        super().print_details()
        print("Battery size:", self.battery_size)

electric_car = ElectricCar("Tesla", "black", 100)
electric_car.print_details()

# Encapsulation

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self._age)

person = Person("Rodrigo", 30)
person.print_details()

# Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        print("woof!")

class Cat(Animal):
    def make_sound(self):
        print("meow!")

animals = [Dog("Rex"), Cat("Tom")]
for animal in animals:
    animal.make_sound()