def caculation(func):
    def wrapper(*args,**kwargs):
        print("caculation start with first decorator")
        func(*args,**kwargs)
        print("caculation finish with first decorator")
    return wrapper

def caculation2(func):
    def wrapper(*args,**kwargs):
        print("caculation start with second decorator")
        func(*args,**kwargs)
        print("caculation finish with second decorator")
    return wrapper

@caculation
@caculation2
def add(a,b):
    print(a+b)

add(3,5)