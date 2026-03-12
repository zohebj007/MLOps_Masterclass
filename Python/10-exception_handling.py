"""
10_exception_handling.py

Topic: try/except/finally/else, raising custom exceptions, chaining
"""
def easy():
    print("== Easy: try/except/finally ==")
    try:
        int("a")
    except ValueError as e:
        print("caught ValueError:", e)
    finally:
        print("always runs")

def intermediate():
    print("\n== Intermediate: custom exception and raise ==")
    class ConfigError(Exception):
        pass
    def load(cfg):
        if "required" not in cfg:
            raise ConfigError("required missing")
    try:
        load({})
    except ConfigError as e:
        print("handled ConfigError:", e)

def advanced():
    print("\n== Advanced: exception chaining and context ==")
    def outer():
        try:
            int("x")
        except ValueError as e:
            raise RuntimeError("parsing failed") from e
    try:
        outer()
    except RuntimeError as e:
        print("caught chained exception:", e)
        print("original:", e.__cause__)

if __name__ == "__main__":
    easy(); intermediate(); advanced()
