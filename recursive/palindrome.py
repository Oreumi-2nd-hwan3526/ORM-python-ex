# boj_25501

import sys

def recursion(string,left,right,count):
    if left>=right:
        return 1,count
    elif(string[left] != string[right]):
        return 0,count
    else:
        return recursion(string, left+1, right-1,count+1)

test=int(input())

for i in range(test):
    string=sys.stdin.readline()
    res,cnt=recursion(string,0,len(string)-2,1)
    print(res,cnt)
