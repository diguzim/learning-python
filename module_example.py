def salute(name):
    return f"Hello, {name}"

def square(number):
    return number * number

# This is executed only when the module is executed directly
if __name__ == "__main__":
    print(salute("Rodrigo"))
    print(square(5))