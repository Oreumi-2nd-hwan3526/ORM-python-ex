def greet(name):
    print("Welcome, {} everyone".format(name))

greet("oreumi")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b=2):
    return a*b

def sum(*args): # variable parameter
    total=0
    for i in args:
        total+=i
    return total

result=sub(3,5)
print(result)

def character_info(name,age):
    print("name: ",name)
    print("age: ",age)

def database_login(addr,ip,database):
    pass

database_login(ip="127.0.0.1", database="") # keyword parameter