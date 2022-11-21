class UppercaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        make_uppercase = self.func().upper()
        return make_uppercase

@UppercaseDecorator
def our_function():
    return "Hello, My name is Mark, and I am 40 years old."

print(our_function())