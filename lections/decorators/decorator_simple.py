def my_decorator(func):
    def inner():
        print('Something before our function is called')
        func()
        print('Something after our function is called')

    return inner

@my_decorator
def greeting():
    print('Hi there')


# our_function = my_decorator(greeting)
# our_function()

greeting()