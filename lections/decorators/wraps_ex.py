from functools import wraps

def uppercase_decorator(func):
    @wraps(func)
    def inner():
        """
        Uppercase
        :return:
        """
        make_uppercase = func().upper()
        return make_uppercase
    return inner

@uppercase_decorator
def hello():
    """
    Hello
    :return:
    """
    return "Hello, My name is Mark, and I am 40 years old."

print(hello())
print(hello.__name__)
print(hello.__doc__)