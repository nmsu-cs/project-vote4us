import os

# get the user's current working directory path
CWD = os.getcwd()

# function to return CWD
def getCWD() :
    return CWD

def writeCFG() :
    output_file_path = CWD + "\\MLTest\\traincfg.yaml"
    train = "train: " + CWD + "\\data\\images\\train"
    val = "val: " + CWD + "\\data\\images\\train"     # val = "val: \\images\\val"
    names = "names:\n 0: Waldo"
    file = open(output_file_path, "w")
    file.write(train + "\n" + val + "\n" + names + "\n")