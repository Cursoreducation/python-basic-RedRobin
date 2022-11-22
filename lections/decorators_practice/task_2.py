from time import time, sleep


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time()
        res = self.func(*args, **kwargs)
        stop = time()
        print(stop - start)
        return res


def decorator(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        stop = time()
        print(stop - start)
        return res

    return wrapper


@decorator
def check_is_prime(number: int) -> bool:
    sleep(2)
    if number > 1:
        d = 2
        while d ** 2 <= number:
            if number % d == 0:
                return False
            d += 1
        return True
    return False


print(check_is_prime(101))
