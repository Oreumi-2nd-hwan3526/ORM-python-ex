# append
a=[1,2,3]
a.append(4)
a.append(5)
print(a)

# append with range
b=[]
for i in range(1,6):
    a.append(i)
print(b)

# remove and pop
a.remove(3)
# a.pop(3)
print(a)

# sort
c=[4,3,2,5,1,6]
c.sort(reverse=True)
print(c)

d=[1,2,3,4,5,6]
print(d[3:4])

d=[i**2 for i in range(1,6)]
print(d)

# extend
a=[1,2,3]
b=[4,5,6]

a.extend(b)
print(a)

a=a*3
print(a)

a.insert(1,"4")
print(a)

a=["1","2","3"]
a.pop(2)
print(a)

# index
idx=a.index("1")
print(idx)
print(len(a))

# reverse
print(a.count("2"))
a.reverse()
print(a)

n=int(input())
a=[1,2,3]
for idx, i in enumerate(a):
    if i==n:
        print(idx)

a=[1,"2","3",[1,2]]
print(a.index([1,2]))

a=(1,2,3,4,5,6)
# exceptions:
# a.append()
# a.remove()
# a.sort()
# a.reverse()
# a.extend()
len(a)
a.index(2)
a.count(2)
