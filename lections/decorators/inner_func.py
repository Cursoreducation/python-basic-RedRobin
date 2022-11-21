b = 6 # global

def sum_two(number):
    a = 5 # local / non-local

    def check_number(number):
        print(a)
        is_valid = isinstance(number, int)
        return is_valid

    is_valid = check_number(number)
    if is_valid:
        return number + 1
    else:
        return 0


def foo_two(number):
    return f'Your number is {number}'

print(foo_two(sum_two('5')))

check_number()