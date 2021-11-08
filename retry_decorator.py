from functools import wraps
from random import randint


def retry(expected_result):
    """decorator that will re-execute function until expected result met"""
    def decorator(func):
        @wraps(func)
        def wrapper():
            for i in range(1, 100):
                result = func()
                print(result)
                if result == expected_result:
                    return result
                else:
                    continue
        return wrapper
    return decorator


@retry(expected_result=5)
def foo():
    return randint(1, 6)
