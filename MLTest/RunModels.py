import MLTest
import WaldoV1


while True:
    userInput = input("\nWhich model would you like to run?\n\t1) Waldo Detection\n\t2) Face Detection\n\tq) Quit\n")
    if (userInput == '1') :
        print("press space to quit model run.")
        WaldoV1.runWald5()
        #WaldoV1.waldoTrain()
        #WaldoV1.runWaldoIMG5()
    elif (userInput == '2') :
        print("press space to quit model run.")
        MLTest.runFaceDetection()
    elif (userInput == 'q') :
        break
    else :
        print ("Enter a valid key, or 'q' to QUIT.")
