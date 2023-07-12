# boj_2439

num=int(input())

for i in range(1,num+1):
    for x in range(1,num-i+1):
        print(" ",end="")
    for y in range(1,i+1):
        print("*",end="")
    print("")
