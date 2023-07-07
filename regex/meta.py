import re

# pattern=r"b.t"
# string="bat,bet,bit,but,baat,beet"

# pattern=r"ab+c"
# string="ac,abc,abbc,abbbc,abc,abc"

# pattern=r"ab*c"
# string="ac,abc,abbc,abbbc,abdc"

# pattern=r"(ab)+c"
# string="abc,ababc,abababc,ab,aabbc"

# pattern=r"[aeiou]"
# string="apple,orange,banana"

# pattern=r"[a-z]"
# string="apple,orange,banana"

# pattern=r"[0-9]"
# string="1234567890"

# pattern=r"\d+"
# string="I have 10 apples and 5 bananas"

# pattern=r"\w+"
# string="Hello world 123"

# pattern=r"^Hello"
# pattern=r"^hon!$"
# string="Hello, World! Hello, Python"

# pattern=r"a{1,3}"
# string="ab,abc,aabc,aaabc"

# pattern=r"a|b"
# string="ab,abc,aabc,aaabc"

pattern=r"(ab)+"
string="ab,abab,ababc"

result=re.findall(pattern,string)
print(result)