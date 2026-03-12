"""
14_decorators.py

Topic: decorators, functools.wraps, parameterized decorator
"""
from functools import wraps
import time

def easy():
    print("== Easy: simple decorator ==")
    def announce(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print("calling", f.__name__)
            return f(*args, **kwargs)
        return wrapper

    @announce
    def hello():
        return "hello"
    print(hello())

def intermediate():
    print("\n== Intermediate: timing decorator ==")
    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.time()
            res = func(*args, **kwargs)
            t1 = time.time()
            print(f"{func.__name__} took {t1-t0:.6f}s")
            return res
        return wrapper

    @timeit
    def work(n):
        s = 0
        for i in range(n):
            s += i
        return s
    print("work:", work(100000))

def advanced():
    print("\n== Advanced: parameterized decorator ==")
    def repeat(times):
        def deco(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                result = None
                for _ in range(times):
                    result = f(*args, **kwargs)
                return result
            return wrapper
        return deco

    @repeat(3)
    def greet(name):
        print("hello", name)
    greet("zoheb")

if __name__ == "__main__":
    easy(); intermediate(); advanced()
