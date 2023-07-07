from functools import reduce

# map(func,list or tuple)

# numbers=[1,2,3,4,5]
# sum=reduce(lambda x,y: x+y, numbers)
# print(sum)

# numbers=[1,2,3,4,5]
# even_num=list(filter(lambda x: x%2==0, numbers))
# print(even_num)

# numbers=[1,2,3,4,5]
# print(sum(numbers))

numbers = ["letter","bigger"]

numbers = list(map(lambda x: x.upper(), numbers))
print(numbers)