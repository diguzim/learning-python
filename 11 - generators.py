def counter(max):
    i = 0
    while i < max:
        yield i
        i += 1

for i in counter(5):
    print(i)