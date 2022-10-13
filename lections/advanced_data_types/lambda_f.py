def double(x):
    return x * 2

def test(x, y):
    return x*y+y*x+(x**2 + y**3) / 5

lmb_1 = lambda x: x * 2
lmb_2 = lambda x, y: x*y+y*x+(x**2 + y**3) / 5

print(double(5))
print(lmb_1(5))

print(test(3, 6))
print(lmb_2(3, 6))