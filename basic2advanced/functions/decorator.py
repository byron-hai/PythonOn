import logging
from functools import wraps


def using_logging(func):
    def wrapper(*args, **kwargs):
        logging.warning("%s is running" % func.__name__)
        logging.warning("Doc: %s" % func.__doc__)
        return func(*args, **kwargs)

    return wrapper

def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)

    return with_logging

#@logged
@using_logging
def my_func(a, b, c = 0):
    """
    Calculate sum value of inputs
    """
    sum_tmp = a + b + c
    print(f"Input: a={a}, b={b}, c={c}, sum={sum_tmp}")


my_func(2, 3, c = 10)
