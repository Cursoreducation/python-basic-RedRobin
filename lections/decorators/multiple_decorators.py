def uppercase_decorator(func):
    def inner():
        """
        Uppercase
        :return:
        """
        make_uppercase = func().upper()
        return make_uppercase
    return inner

def split_data(func):
    def inner():
        """
        Split data
        :return:
        """
        splitted_data = func().split()
        return splitted_data
    return inner

def join_data(func):
    def inner():
        """Join Data"""
        joined_data = ", ".join(func())
        return joined_data
    return inner


@join_data
@split_data
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