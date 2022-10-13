# незмінні
m = 15
print(id(m))
print(type(m))
m = 123456
print(id(m))
print(type(m))

# змінні
a = [1, 2, 3, 5, 6]
print(id(a))
a[3] = 4
a.append(7)
print(a)
print(id(a))