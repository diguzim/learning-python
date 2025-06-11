name = 'Rodrigo'

print(f'Hello {name}')
def greet(name):
    print(f'Hello {name}')
greet(name)
def farewell(name):
    print(f'Goodbye {name}')
farewell(name)
def ask_name():
    name = input('What is your name? ')
    return name
if __name__ == '__main__':
    name = ask_name()
    greet(name)
    farewell(name)
    print('Goodbye!')
def main():
    name = ask_name()
    greet(name)
    farewell(name)
    print('Goodbye!')
if __name__ == '__main__':
    main()
    print('This is the end of the program.')