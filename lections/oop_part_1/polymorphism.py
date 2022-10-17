num_1 = 1
num_2 = 2
print(num_1 + num_2)

str_1 = 'Python '
str_2 = 'Programming'

print(str_1 + str_2)

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]

print(lst_1 + lst_2)

print(len('Python'))
print(len(lst_1))
print(len({'name': 'Jeff', 'age': 27}))

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a cat. My name is {self.name}. I am {self.age} years old')

    def make_sound(self):
        print('Meow')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a dog. My name is {self.name}. I am {self.age} years old')

    def make_sound(self):
        print('Bark')

kitty = Cat('Kitty', 3)
fluffy = Dog('Fluffy', 4)

for animal in (kitty, fluffy):
    animal.make_sound()
    animal.info()