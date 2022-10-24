def test():
    return 'Hello'

def simple_generator(value):
    while value > 0:
        value -= 1
        yield value

gen = simple_generator(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

from random import randint

def random_increase(quantity):
    number = 0
    while quantity > 0:
        number += randint(1, 50)
        quantity -= 1
        yield round(number, 2)

gen_1 = random_increase(10)
for elem in gen_1:
    print(elem)

g = (round(randint(1, 50)+number, 2) for number in range(10))
for elem in g:
    print(elem)