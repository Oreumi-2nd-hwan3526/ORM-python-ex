import os

if os.name=='nt':
    folder_path="C:\\Users\\wlghk"
elif os.name=='posix':
    folder_path="/home/hwan3526/"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"folder {folder_path} is created")
else:
    print(f"folder {folder_path} already exists")