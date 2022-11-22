import time


def logger(logfile='out.log'):
    def logger_decorator(func):
        def inner(*args, **kwargs):
            log_string = f'{func.__name__} executes'

            start = time.time()
            res = func(*args, **kwargs)
            stop = time.time()

            execution_time = stop - start
            res_log = f'Result of the function: {res}'
            param_log = f'Function parameters: {args}'
            with open(logfile, 'a') as log_file:
                log_file.write(f"Function: {log_string}\nExecution time: {execution_time}\n"
                               f"{param_log}\n{res_log}\n\n")

        return inner

    return logger_decorator


@logger()
def my_function():
    print('Hello')


@logger()
def test(n):
    return n


@logger()
def test1():
    return 'string'


@logger()
def test2():
    pass


my_function()
test(153)
test1()
test2()
