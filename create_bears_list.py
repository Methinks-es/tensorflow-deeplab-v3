import os
import random

dir = 'dataset/bearwithus/'
train_split = 0.8

files = [file.split('.')[0] for file in os.listdir(dir)]

random.shuffle(files)

train_num = int(len(files) * 0.8)
train_files = files[:train_num]
validation_files = files[train_num:]

with open('dataset/train_cases.txt', "w") as file:
    for file_name in train_files:
        file.write(file_name + "\n")

with open('dataset/validation_cases.txt', "w") as file:
    for file_name in validation_files:
        file.write(file_name + "\n")