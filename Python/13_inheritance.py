"""
13_inheritance.py

Topic: inheritance, overriding, super(), mixins, polymorphism
"""
def easy():
    print("== Easy: single inheritance ==")
    class Animal:
        def speak(self):
            return "..."
    class Dog(Animal):
        def speak(self):
            return "woof"
    d = Dog()
    print("dog:", d.speak())

def intermediate():
    print("\n== Intermediate: override + super() ==")
    class Vehicle:
        def start(self):
            return "vehicle started"
    class Car(Vehicle):
        def start(self):
            return super().start() + " -> car engine"
    c = Car()
    print(c.start())

def advanced():
    print("\n== Advanced: mixin + multiple inheritance ==")
    class LoggerMixin:
        def log(self, msg):
            print("[LOG]", msg)
    class Service(LoggerMixin):
        def start(self):
            self.log("starting")
            return "service started"
    s = Service()
    print(s.start())

if __name__ == "__main__":
    easy(); intermediate(); advanced()
