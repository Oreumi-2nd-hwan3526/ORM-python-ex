a=int(input())

num_list=list(map(int,input().split()))
max=num_list[0]
min=num_list[0]

num=int(input())

for i in range(0,a):
    if max<num:
        max=num
    if min>num:
        min=num

print(min, max)