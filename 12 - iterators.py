something_iterable = [4, 8, 15]
# something_iterable = ("apple", "banana", "cherry")

my_iterator = iter(something_iterable)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

for item in something_iterable:
    print(item)

class MyIterableClass:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        x = self.x
        self.x += 1
        return x
    
my_iterable_object = MyIterableClass()
my_iterator = iter(my_iterable_object)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# This would cause an infinite loop
# for item in my_iterable_object:
#     print(item)

class MyIterableClass:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        if self.x < 4:
            x = self.x
            self.x += 1
            return x
        else:
            raise StopIteration

my_iterable_object = MyIterableClass()
my_iterator = iter(my_iterable_object)

# But not this, as we raise StopIteration
for item in my_iterable_object:
    print(item)