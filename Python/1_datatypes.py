"""
1_datatypes.py

Topic: basic built-in types
Includes: int, float, str, bool
Three examples: easy / intermediate / advanced
"""
def easy():
    print("== Easy: basic types and type() ==")
    a = 42            # int
    b = 3.14          # float
    s = "mlops"       # str
    flag = False      # bool
    print(a, type(a))
    print(b, type(b))
    print(s, type(s))
    print(flag, type(flag))

def intermediate():
    print("\n== Intermediate: conversions and truthiness ==")
    x = "100"
    xi = int(x) + 5
    xf = float(x) * 1.5
    bools = [bool(""), bool("text"), bool(0), bool(1)]
    print("int:", xi, "float:", xf, "truths:", bools)

def advanced():
    print("\n== Advanced: mixed-type math & type hints ==")
    from typing import Union
    Number = Union[int, float]
    def add(a: Number, b: Number) -> Number:
        return a + b
    print("add(5, 2.3) ->", add(5, 2.3))

if __name__ == "__main__":
    easy(); intermediate(); advanced()
