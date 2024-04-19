import os

# get the user's current working directory path
CWD = os.getcwd()
output_file_path = CWD + "\\project-vote4us\\MLTest\\test.yaml"

path = "path: " + CWD + "\\project-vote4us\\data"
train = "train: \\images\\train"
val = "val: \\images\\train"     # val = "val: \\images\\val"
names = "names:\n\t0: Waldo"

file = open(output_file_path, "w")

file.write(path + "\n" + train + "\n" + val + "\n\n" + names + "\n")