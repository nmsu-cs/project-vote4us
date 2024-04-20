import MLTest
import WaldoV1


while True:
    userInput = input("\nWhich model would you like to run?\n\t1) Waldo Detection\n\t2) Face Detection\n\tt) Train Waldo Model\n\tq) Quit\n")
    if (userInput == '1') :
        print("press space to quit model run.")
        WaldoV1.runWald5()
        #WaldoV1.runWaldoIMG5()
    elif (userInput == '2') :
        print("press space to quit model run.")
        MLTest.runFaceDetection()
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
