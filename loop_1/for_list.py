fruits = ["apple","melon","pear"]
for fruit in fruits:
    print(fruit)

# range
for i in range(1,101):
    print(i)

# enumerate
fruits = ["apple","melon","pear"]
prices = [2500,15000,5000]
for idx, i in enumerate(fruits):
    print(idx+1, i)

# zip
fruits = ["apple","melon","pear"]
prices = [2500,15000,5000]
amounts = [5,6,3]
for fruit, price, amount in zip(fruits,prices,amounts):
    profit = price*amount
    print(fruit, price, amount, profit)

# break
for i in range(0,10):
    if i==5:
        break
    print(i)

# reversed
for i in reversed(range(0,10)):
    print(i)

# example
with open("test.txt",'r',encoding="utf-8") as f:
    # print(f.read())
    # for i in f.readlines():
    #     print(i)
    
    text=f.read().split('\n')
    for idx, line in enumerate(text):
        name, score = line.split(" ")
        print(f'{idx+1}번째 학생: {name}, 점수: {score}')