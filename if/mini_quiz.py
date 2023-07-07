with open("file_1.txt","r") as f:
    color_list=[]
    for i in f.readlines():
        color_list.append(i.replace("]n",""))

    color_list.sort()
    print(len(color_list))
    print(color_list)
    print(len(set(color_list)))