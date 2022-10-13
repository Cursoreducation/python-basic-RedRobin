from functools import reduce

lst = [0, 1, 2, 3, 4]

def sum_num(x, y):
    return x + y

sum_of_elem = reduce(lambda x, y: x + y, lst)
print(sum_of_elem)

sum_of_elem = reduce(sum_num, lst)
print(sum_of_elem)

lst2 = [4, 6, 1, 7, 3, 12, 9]
print(sorted(lst2, reverse=True))