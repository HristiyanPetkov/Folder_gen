import os
import random

num_of_folders = int(input("Enter number of folders: "))

if os.path.exists("folders"): 
    print("Dir already exists")
else:
    os.mkdir("folders")

    for i in range(num_of_folders):
        os.mkdir(f"folders/folder{i + 1}")
        random_num = random.randint(0, 10)
        print(random_num)
        for j in range(random_num):
            with open(f"folders/folder{i + 1}/file{j + 1}.txt", 'w') as file:
                file.write(f"{j + 1}")