resulting_list = [x**2 for x in range(10)]
print(resulting_list)

resulting_dictionary = {x: x**2 for x in range(10)}
print(resulting_dictionary)

resulting_set = {x**2 for x in range(10)}
print(resulting_set)

resulting_pairs = [(x, y) for x in range(3) for y in range(3)]
print(resulting_pairs)