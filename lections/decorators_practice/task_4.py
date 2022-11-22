def convert_to_string(func):
    def inner(number):
        result = func(number)
        str_result = " | ".join([str(elem) for elem in result])
        return str_result
    return inner

@convert_to_string
def print_sequence(number):
    lst = []
    for i in range(1, number + 1):
        x = 0
        while i != x:
            lst.append(i)
            x += 1
    return lst[:number]

print(print_sequence(7))