lst = []
for num in range(21):
    lst.append(str(num))
print(lst)

lst_1 = [str(num) for num in range(21)]
print(lst_1)

lst_2 = []
for even_number in range(21):
    if even_number % 2 == 0:
        lst_2.append(even_number)
print(lst_2)

lst_3 = [even_number for even_number in range(21) if even_number % 2 == 0]
print(lst_3)

lst_4 = []
for number in range(21):
    if number % 2 == 0:
        lst_4.append(number)
    else:
        lst_4.append(number * 2)

print(lst_4)

lst_5 = [number if number % 2 == 0 else number * 2 for number in range(21)]
print(lst_5)