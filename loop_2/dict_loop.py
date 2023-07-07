a={"이름": "철수", "나이": 20, "직업": "강사", "일일퀴즈성적": [10,20,20]}
b={"이름": "영희", "나이": 21, "직업": "멘토", "일일퀴즈성적": [9,19,19]}
c={"전화번호": "123456789", "주소": "서울"}

# items
for key,value in a.items():
    print(key,value)

# keys
for key in a.keys():
    print(key)

# values
# c=[]
# for value in a.values():
#     c.append(value)
# print(c)

# update
a.update(c)
print(a)

# update example
gangsa=[{"이름": "철수", "나이": 20, "직업": "강사", "일일퀴즈성적": [10,20,20]},
        {"이름": "영희", "나이": 21, "직업": "멘토", "일일퀴즈성적": [9,19,19]}]
gangsa_info={"전화번호": "123456789", "주소": "서울"}
for i in range(len(gangsa)):
    gangsa[i].update(gangsa_info)
print(gangsa)