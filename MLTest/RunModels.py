import MLTest
import WaldoV1
import setup_ML

#setup_ML.writeCFG()

while True:
    userInput = input("\nWhich model would you like to run?\n\t1) Waldo Video Detection\n\t2) Waldo Image Detection\n\tt) Train Waldo Model\n\tq) Quit\n")
    if (userInput == '1') :
        print("press space to quit model run.")
        device = 0     # laptop cameras are default 0
        WaldoV1.runWaldo(device)
    elif (userInput == '2') :
        print("press space to quit model run.")
        image = "C:\\Users\\theti\\OneDrive\\Desktop\\School Suff\\S4\\CS371\\Waldo_Project\\WSG_Waldo\\project-vote4us\\data\\V3images\\train\\48.jpg"   # enter path to your image
        WaldoV1.runWaldoIMG(image)
    elif (userInput == 't') :
        runs = input("\nHow many epochs would you like to train Waldo with?\n")
        while (runs.isdigit() == False) :
            runs = input("\nPlease enter an integer number greater than 0\n")
        WaldoV1.waldoTrain(int(runs))
        break
    elif (userInput == 'q') :
        break
    else :
        print ("Enter a valid key, or 'q' to QUIT.")
