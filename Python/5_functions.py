"""
5_functions.py

Topic: def, default args, *args, **kwargs, lambda, closure
"""
def easy():
    print("== Easy: simple function and lambda ==")
    def greet(name="user"):
        return f"hello {name}"
    print(greet("zoheb"))
    add = lambda a,b: a+b
    print("lambda add:", add(2,3))

def intermediate():
    print("\n== Intermediate: varargs and kwargs ==")
    def summarize(*args, **kwargs):
        return {"args": args, "kwargs": kwargs}
    print(summarize(1,2, three=3))

def advanced():
    print("\n== Advanced: closure and decorator-like pattern ==")
    def multiplier(n):
        def mult(x):
            return x * n
        return mult
    dbl = multiplier(2)
    print("dbl(5):", dbl(5))

if __name__ == "__main__":
    easy(); intermediate(); advanced()
