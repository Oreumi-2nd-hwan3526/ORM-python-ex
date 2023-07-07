def cat():
    return "Meow"

dog=cat
print(dog())

def apply_operation(func,x,y):
    return func(x,y)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

result=apply_operation(sub,2,3)
print(result)