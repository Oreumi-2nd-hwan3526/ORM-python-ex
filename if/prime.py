n=int(input())

is_prime=True
for i in range(2, int(n**0.5)+1):
    if n%i==0:
        print("Not prime number")
        is_prime=False
        break

if is_prime:
    print("Prime number")