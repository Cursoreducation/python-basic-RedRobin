class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        print(f'I am going to divide {a} and {b}')
        if b == 0:
            print('Whoops, I cannot divide by zero')
        else:
            print(f"Your result: {self.func(a, b)}")

@MyDecorator
def divide(a, b):
    return a / b

divide(5, 0)