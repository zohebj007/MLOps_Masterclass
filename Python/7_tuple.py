"""
7_tuple.py

Topic: tuples, immutability, packing/unpacking, namedtuple
"""
def easy():
    print("== Easy: basic tuple ==")
    t = (1,2,3)
    print(t, "len:", len(t))

def intermediate():
    print("\n== Intermediate: packing/unpacking ==")
    a, b, *rest = (10, 20, 30, 40)
    print("a,b,rest:", a, b, rest)

def advanced():
    print("\n== Advanced: namedtuple / immutability usecase ==")
    from collections import namedtuple
    Point = namedtuple("Point", ["x","y"])
    p = Point(2,3)
    print("point:", p, "x:", p.x)
    # tuples as dict keys
    d = {(1,2): "edge"}
    print("dict with tuple key:", d)

if __name__ == "__main__":
    easy(); intermediate(); advanced()
