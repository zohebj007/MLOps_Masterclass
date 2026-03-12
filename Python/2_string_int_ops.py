"""
2_string_int_ops.py

Topic: string and integer operations, conversions, formatting, slicing
"""
def easy():
    print("== Easy: concat, convert, format ==")
    s = "hello"
    n = 10
    print(s + " world", "-> length", len(s))
    print("sum:", n + int("5"))
    print(f"formatted: {s}-{n}")

def intermediate():
    print("\n== Intermediate: slicing, replace, split ==")
    s = "mlops_masterclass"
    print("slice:", s[:5])
    print("replace:", s.replace("master", "pro"))
    print("split:", s.split("_"))

def advanced():
    print("\n== Advanced: parsing & safe conversion ==")
    def safe_int(x, default=0):
        try:
            return int(x)
        except (TypeError, ValueError):
            return default
    vals = ["1", "2", "a", None]
    print([safe_int(v, -1) for v in vals])

if __name__ == "__main__":
    easy(); intermediate(); advanced()
