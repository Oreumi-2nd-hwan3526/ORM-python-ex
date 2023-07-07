class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Animal sounds")

class Dog(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
    
    def speak(self):
        super().speak()
        print("Dog barks")

    def speak2(self):
        print("Dog barks2")

my_dog=Dog()
my_dog.speak()