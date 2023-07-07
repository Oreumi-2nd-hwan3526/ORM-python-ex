file = open("byte.txt", "rb")
context=file.read()
print(context)
file.close()

file = open("byte.txt", "rw")
file.write(b"content")
file.close()