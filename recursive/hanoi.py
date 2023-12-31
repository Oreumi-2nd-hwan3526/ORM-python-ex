# boj_11729

n = int(input())
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
        return
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)

sum = 2 ** n - 1
print(sum)
hanoi(n, 1, 2, 3)