"""
6_list.py

Topic: lists, methods, slicing, comprehension, nested lists
"""
def easy():
    print("== Easy: create and basic methods ==")
    l = [1,2,3]
    l.append(4)
    print(l, "len:", len(l))

def intermediate():
    print("\n== Intermediate: slicing & comprehension ==")
    l = list(range(10))
    print("slice 2:7:", l[2:7:2])
    evens = [x for x in l if x%2==0]
    print("evens:", evens)

def advanced():
    print("\n== Advanced: nested lists and flattening ==")
    nested = [[1,2],[3,4],[5]]
    flat = [x for sub in nested for x in sub]
    print("flat:", flat)
    # in-place modifications
    nested[0][0] = 100
    print("modified nested:", nested)

if __name__ == "__main__":
    easy(); intermediate(); advanced()
