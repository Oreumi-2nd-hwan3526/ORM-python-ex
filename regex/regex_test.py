import re

pattern=r"apple"
string="I have an apple and an orange"

result=re.search(pattern,string)
print(result)

pattern=r"a[bcd]*d"
string="ad,abcd,abbcd,acd"

result=re.findall(pattern,string)
print(result)