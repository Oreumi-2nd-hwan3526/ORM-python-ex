global_var=100

def my_func(global_var):

    # global global_var

    local_var=50
    global_var+=50
    print("global_var: ",global_var)
    print("local_var: ",local_var)

    return global_var

# my_func()
global_var=my_func(global_var)
print("global_var: ",global_var)
# print("local_var: ",local_var)

def get_person():
    return "abcd", 20, "id@naver.com"

name, age, email=get_person()
print(f"name: {name}, age: {age}, email: {email}")