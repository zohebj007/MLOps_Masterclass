"""
3_if_else.py

Topic: if / elif / else, ternary, nested branching
"""
def easy():
    print("== Easy: basic if/else ==")
    x = 7
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

def intermediate():
    print("\n== Intermediate: if/elif/else and ternary ==")
    score = 78
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    else:
        grade = "C"
    print("grade:", grade)
    # ternary
    parity = "even" if score % 2 == 0 else "odd"
    print("parity using ternary:", parity)

def advanced():
    print("\n== Advanced: complex nested conditions ==")
    def classify(x, y):
        if x > 0:
            if y > 0:
                return "Q1"
            elif y < 0:
                return "Q4"
            else:
                return "X-axis"
        elif x < 0:
            return "left"
        else:
            return "origin"
    print("classify(2,3):", classify(2,3))

if __name__ == "__main__":
    easy(); intermediate(); advanced()
