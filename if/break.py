a=int(input())

for i in range(1,101):
    print(i)
    if i==a:
        print("terminated")
        break
print(i)


while True:
    b=int(input())
    if b=="pear":
        print("correct")
        break
    else:
        print("wrong")

answer=5
while True:
    c=int(input())
    if c<answer:
        print("larger")
    elif c>answer:
        print("smaller")
    else:
        print("That's it!")
