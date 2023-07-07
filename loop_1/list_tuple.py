a=[1,"1",True,None,[1,2]] # list
b=(1,"1",True,None,[1,2]) # tuple

a[1]=False
print(a)
# b[1]=False # Error (immutuable)
print(b)

