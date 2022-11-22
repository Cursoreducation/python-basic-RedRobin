def number_verification(func):
    def inner(number):
        if number > 0 and isinstance(number, int):
            print(f"My number: {number} and temp result: {func(number)}")
            return func(number)
        else:
            raise Exception(f'You have negative or not integer number: {number}')
    return inner

@number_verification
def recursive_factorial(number):
    return number * recursive_factorial(number - 1) if number > 1 else 1


print(recursive_factorial(7))