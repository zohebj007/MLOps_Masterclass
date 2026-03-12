"""
8_set.py

Topic: sets, uniqueness, union/intersection/difference, comprehension
"""
def easy():
    print("== Easy: create set and uniqueness ==")
    s = set([1,2,2,3])
    print("set:", s)

def intermediate():
    print("\n== Intermediate: set operations ==")
    a = {1,2,3}
    b = {3,4,5}
    print("union:", a|b)
    print("intersection:", a&b)
    print("difference a-b:", a-b)

def advanced():
    print("\n== Advanced: membership & set comprehension ==")
    nums = [1,2,2,3,4,4,5]
    unique = {x for x in nums if x%2==0}
    print("even unique:", unique)
    print("fast membership:", 3 in unique)

if __name__ == "__main__":
    easy(); intermediate(); advanced()
