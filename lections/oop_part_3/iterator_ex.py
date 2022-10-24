string_ex = 'cat' #iterable
lst = [1, 2, 'hello', 'foo', 'test', 1.4] #iterable

for char in string_ex:
    print(char)

for elem in lst:
    print(elem)

string_ex_iter = iter(string_ex)
try:
    print(next(string_ex_iter))
    print(next(string_ex_iter))
    print(next(string_ex_iter))
    print(next(string_ex_iter))
except StopIteration:
    pass


class Iterator:
    number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        return self.number

class Iterable:
    number = 0

    def __getitem__(self, key):
        self.number += 1
        if self.number == 22:
            raise StopIteration
        return self.number

for i in Iterable():
    print(i)

iterator_ex = Iterator()
print(type(iterator_ex))
print(next(iterator_ex))
print(next(iterator_ex))
print(next(iterator_ex))
print(next(iterator_ex))
print(next(iterator_ex))
print(next(iterator_ex))
print(next(iterator_ex))
print(next(iterator_ex))
print(next(iterator_ex))

from random import random

class RandomIncrease:
    def __init__(self, quantity):
        self.qty = quantity
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty > 0:
            self.number += random()
            self.qty -= 1
            return round(self.number, 2)
        else:
            raise StopIteration

for elem in RandomIncrease(10):
    print(elem)

def check_if_itarable(obj):
    return '__getitem__' in dir(obj)

types_to_check = [int, bool, str, list, dict, tuple, set, float, complex, Iterable()]
for t in types_to_check:
    print(f'{t} Itarable - {check_if_itarable(t)}')