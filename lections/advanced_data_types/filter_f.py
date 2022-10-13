def even_number(number):
    return number % 2 == 0
    # if number % 2 == 0:
    #     return True
    # return False

filtered = list(filter(even_number, range(10)))
print(filtered)

filtered_2 = list(filter(lambda number: number % 2 == 0, range(10)))
print(filtered_2)


lst = ['test 1', 'hello', 'test 2', 'hi', 'test 3', 'hola']
filtered_3 = list(filter(lambda elem: 'test' in elem, lst))
print(filtered_3)