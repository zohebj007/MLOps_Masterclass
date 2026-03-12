"""
9_dictionary.py

Topic: dict creation, access, items(), comprehension, merging
"""
def easy():
    print("== Easy: dict create & access ==")
    d = {"a":1, "b":2}
    print(d["a"], d.get("c", "missing"))

def intermediate():
    print("\n== Intermediate: iterate & comprehension ==")
    d = {str(i): i*i for i in range(5)}
    for k,v in d.items():
        print(k, "->", v)

def advanced():
    print("\n== Advanced: merging & nested dicts ==")
    d1 = {"x":1}
    d2 = {"y":2}
    merged = {**d1, **d2}
    nested = {"config": {"host":"localhost", "port":8000}}
    print("merged:", merged, "nested host:", nested["config"]["host"])

if __name__ == "__main__":
    easy(); intermediate(); advanced()
