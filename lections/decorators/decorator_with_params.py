def smart_divide(func):
    def inner(a, b):
        print(f'I am going to divide {a} and {b}')
        if b == 0:
            print('Whoops, I cannot divide by zero')
        else:
            print(f"Your result: {func(a, b)}")

    return inner


@smart_divide
def divide(a, b):
    return a / b


def customize_data(func):
    def inner(*args, **kwargs):
        print(f'Your new data is: {args}')
        print(f'Your dict data is: {kwargs}')
        func(*args, **kwargs)
    return inner

@customize_data
def print_data(*args, **kwargs):
    print(args, kwargs)

# print_data(1, 'st', 4, 'f', test=5, hello='3')


def tags(tag_name):
    def tag_decorator(func):
        def inner(name):
            return f"<{tag_name}>{func(name)}<\{tag_name}>"
        return inner
    return tag_decorator

@tags('body')
def get_text_name(name):
    return f"Hello, {name}"

result = get_text_name('Mark')

print(result)
