def salute(name):
    print("Hello, " + name + "!")

salute("Rodrigo")

def my_sum(a, b):
    return a + b

print(my_sum(1, 2))

def personalized_salute(name, salutation="Hello"):
    print(salutation + ", " + name + "!")

personalized_salute("Rodrigo")
personalized_salute("Rodrigo", "Hi")

def average(*numbers):
    return sum(numbers) / len(numbers)

print(average(1, 2, 3, 4, 5))

square = lambda x: x * x
print(square(2))