def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

def outer_function():
    x=10

    def inner_function():
        print(x)

    inner_function()

outer_function()