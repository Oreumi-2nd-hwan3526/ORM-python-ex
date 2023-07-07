import glob
import os

current_path=os.path.abspath(__file__)
print(current_path)

pdf_files=glob.glob("/home/hwan3526/**/*.pdf", recursive=True)

for pdf_file in pdf_files:
    print(pdf_file)