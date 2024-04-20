import os

# get the user's current working directory path
CWD = os.getcwd()

# function to return CWD
def getCWD() :
    return CWD

def writeCFG() :
    output_file_path = CWD + "\\project-vote4us\\MLTest\\traincfg.yaml"
    train = "train: " + CWD + "\\project-vote4us\\data\\images\\train"
    val = "val: " + CWD + "\\project-vote4us\\data\\images\\train"     # val = "val: \\images\\val"
    names = "names:\n 0: Waldo"
    file = open(output_file_path, "w")
    file.write(train + "\n" + val + "\n" + names + "\n")