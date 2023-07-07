# Euclidean algorithm
a,b=map(int,input().split())
first_a=a
first_b=b

while b!=0:
    a,b=b,a%b

print(f'GCD is {a}')
print(f'LCM is {(first_a*first_b)/a}')

# Factorization
n=input("Number to factorize: ")

factors=[]

while n%2==0:
    factors.append(2)
    n//=2

i=3
while i*i<=n:
    while n%i==0:
        factors.append(i)
        n//=i
    i+=2

if n>1:
    factors.append(n)

print(factors)