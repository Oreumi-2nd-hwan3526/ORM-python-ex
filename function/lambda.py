def add(a,b):
    return a+b

add=lambda a,b: a+b
result=add(2,3)
print(result)

numbers=[1,2,3,4,5]
squared=list(map(lambda x: x**2, numbers))
data=list(map(int,input().split()))

print(squared)

students=[
    {"name": "A","age":23},
    {"name": "B","age":17},
    {"name": "C","age":25}
]

students.sort(key=lambda x:x["age"])
print(students)