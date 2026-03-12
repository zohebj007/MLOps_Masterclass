"""
12_classes.py

Topic: class basics, instance methods, properties, __repr__, dataclass example
"""
def easy():
    print("== Easy: simple class ==")
    class Greeter:
        def __init__(self, name):
            self.name = name
        def greet(self):
            return f"hello {self.name}"
    g = Greeter("zoheb")
    print(g.greet())

def intermediate():
    print("\n== Intermediate: properties & __repr__ ==")
    class User:
        def __init__(self, name, age):
            self._name = name
            self.age = age
        @property
        def name(self):
            return self._name
        def __repr__(self):
            return f"User(name={self._name!r}, age={self.age})"
    u = User("asha", 30)
    print(u, "name prop:", u.name)

def advanced():
    print("\n== Advanced: dataclass for simple records ==")
    from dataclasses import dataclass
    @dataclass
    class ModelMeta:
        name: str
        version: int
    m = ModelMeta("resnet", 1)
    print(m)

if __name__ == "__main__":
    easy(); intermediate(); advanced()
