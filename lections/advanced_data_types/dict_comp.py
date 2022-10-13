dict_basic = {f'Number_{x}': x for x in range(5)}
print(dict_basic)
print(dict_basic['Number_3'])

dc_with_if = {f"{x}**3": x**3 for x in range(10) if x % 2 == 0}
print(dc_with_if)

dc_with_elif = {f"Number_{x}": x**3 if x % 2 == 0 else x**2 for x in range(10)}
print(dc_with_elif)