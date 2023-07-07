file = open("title2.txt", "r+")
context=file.read()
print(context)
file.close()

file = open("title3.txt", "w+")
file.write("content")
file.close()