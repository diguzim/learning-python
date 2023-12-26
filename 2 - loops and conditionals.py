# Conditional statements
idade = 34

if idade < 18:
    print("Você é maior de idade.")
elif 18 <= idade < 30:
    print("Você é jovem.")
else:
    print("Você é adulto.")

# Loops
    
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

counter = 0
while counter < 5:
    print(counter)
    counter += 1

for i in range(5):
    if i == 3:
        break
    print(i)


idade = 34
status = 'adulto' if idade >= 18 else 'menor de idade'
print(status)

