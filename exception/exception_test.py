import logging

num1=10
num2=0

logging.basicConfig()
try:
    result=num1/num2
except Exception as e:
    logging.error(e)
finally:
    print("execution")

try:
    file=open("abcd.txt","r")
    text=file.read()
except FileNotFoundError as e:
    print(e)

try:
    mylist=[1,2,3]
    value=mylist[3]
    print(value)
except IndexError as e:
    print(e)

try:
    a=input()
    result=a+10
except TypeError as e:
    print(e)

try:
    a="a10"
    int(a)
except ValueError as e:
    print(e)

try:
    mydict={"key1": 1,"key2": 2}
    print(mydict["key3"])
except KeyError as e:
    print(e)

try:
    file=open("abcd","r")
    file.write("ABCD")
except IOError as e:
    print(e)

AttributeError
KeyboardInterrupt