import module_example

print(module_example.salute("Rodrigo"))
print(module_example.square(5))

# Package

from my_package import module_from_package
from my_package.module_from_package import salute

print(module_from_package.salute("Rodrigo"))
print(salute("Rodrigo"))