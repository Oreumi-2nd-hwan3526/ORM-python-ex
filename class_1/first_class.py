class Car:
    wheel=4
    window=2

    def __init__(self,people):
        self.people=people
        self.wheel=4
        self.window=2

    def brake(self):
        print(f"{self.people} brake")

    def accelerate(self):
        print("accelerate")

my_car=Car("A")
my_car.brake()