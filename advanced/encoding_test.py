encoded_text=b"\xbc\xd3\xd3\xcd" # 加油

with open("codecs_list.txt","r") as f:
    codecs_list=f.read().replace(",","").replace("\n"," ").replace("  "," ").split(" ")
print(codecs_list)

for codec in codecs_list:
    try:
        print(encoded_text.decode(codec),codec)
    except:
        pass