def double_plus(x):
    return (x + x) * 2


lst = list(map(double_plus, range(10)))
print(lst)

lst_lmb = list(map(lambda x: (x + x) * 2, range(10)))
print(lst_lmb)

lst = ['test 1', 'hello', 'test 2', 'hi', 'test 3', 'hola']
lst_lmb = list(map(lambda elem: f"prefix-{elem}", lst))
print(lst_lmb)