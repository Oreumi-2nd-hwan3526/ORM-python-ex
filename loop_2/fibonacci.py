n1 = 1
n2 = 1
n = 0

num = int(input())

if num == 1 or num == 2:
    print("1")
else:
    for i in range(num - 2):
        n = n1 + n2
        n1 = n2
        n2 = n
    print(n)
