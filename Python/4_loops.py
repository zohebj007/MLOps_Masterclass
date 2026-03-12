"""
4_loops.py

Topic: for, while, break, continue, enumerate, iterables
"""
def easy():
    print("== Easy: for and while ==")
    for i in range(3):
        print("for:", i)
    i = 0
    while i < 3:
        print("while:", i)
        i += 1

def intermediate():
    print("\n== Intermediate: iterate list with enumerate & break/continue ==")
    items = ["a", "b", "c", "stop", "d"]
    for idx, val in enumerate(items):
        if val == "stop":
            print("found stop at", idx); break
        if val == "b":
            print("skipping b"); continue
        print(idx, val)

def advanced():
    print("\n== Advanced: generator consumption and else clause on loops ==")
    def gen(n):
        for i in range(n):
            yield i*i
    g = gen(5)
    for v in g:
        print("v:", v)
    else:
        print("generator exhausted, loop else executed")

if __name__ == "__main__":
    easy(); intermediate(); advanced()
