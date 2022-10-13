import keyword

# print("Python keywords: ", keyword.kwlist)

a = None



# незмінні
b = True # boolean
c = False # boolean

d = 5 # integer
e = 5.5 # float
f = complex(5e1) # complex

h = (1, 2, "3", 5.5, True) # tuple
j = 'string' # string

# змінні
g = [1, 2, "3", 5.5, True] # list

i = {1, 2, 3, 4, 'test', 'key'} # set - зберігає унікальні значення
k = {                           # dict
    'name': 'Rostyslav',
    'age': 28,
}

print(k['age'])
print(k.get('name'))