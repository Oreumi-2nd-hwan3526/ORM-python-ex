a=[1,2,3,3]
a=list(set(a))
print(a)

a=list(tuple(a))
print(a)

a=set(tuple(a))
print(a)