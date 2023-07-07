fruits=["apple","melon","pear"]
fruit="melon"

if fruit in fruits:
    print("like")
else:
    print("unlike")

fruits_main=["apple","melon","pear"]
fruits_sub=["apple","melon"]

eat_list=[]
for f in fruits_main:
    if f in fruits_sub: # not in
        print("eat")
        eat_list.append(f)
    else:
        print("no eat")

print(eat_list)