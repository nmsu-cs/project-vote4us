import cvlib as cv
import cv2
import os
import setup_ML
from ultralytics import YOLO
from cvlib.object_detection import draw_bbox

# define waldo percentage global variable
WALDOPERCENT = 0.0    # defaulted 0.0
# define global threshold variable. Best performance currently at 0.395
THRESHOLD = 0.4

# get the model most up to date (currently WaldoV1)
model = YOLO(setup_ML.getCWD() + "\\project-vote4us\\models\\WaldoV4\\weights\\best.pt")

# train model with user specified epochs
def waldoTrain(epic) :
    setup_ML.writeCFG()   # updates traincfg.yaml file, just in case sum stuff changed for some reason
    model = YOLO("yolov8n.yaml")
    results = model.train(data="project-vote4us/MLTest/traincfg.yaml", epochs=epic)

# takes an image path as a string and runs waldo modelS
def runWaldoIMG(image):
    WALDOPERCENT = 0.0
    frame = cv2.imread(image)
    # Predict
    #results = model.predict(image_path, save=True, imgsz=320, conf=0.395)
    results = model(frame)[0]
    print(results)
    # get results list
    resList = results.boxes.data.tolist()
    # define coordinate variables to -1 when no viable waldo box has been found
    x1 = y1 = x2 = y2 = -1.0
    # set global waldoPercent variable based off of score
    for result in resList :
        print("\nfound Waldo!\n")
        score = result[4]
        print(score)
        if (score > THRESHOLD) & (score > WALDOPERCENT) :
            WALDOPERCENT = score
            x1, y1, x2, y2, WALDOPERCENT, dummy = result
    name = "Waldo"
    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
    cv2.putText(frame, name.upper(), (int(x1), int(y1 - 10)),
        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imwrite("frame.jpg", frame)


# video input with waldo model
def runWaldo(device) :
    WALDOPERCENT = 0.0
    x1 = y1 = x2 = y2 = -1.0
    camera = cv2.VideoCapture(device)   # camera hardcoded to 1st camera (0)
    while True :
        ret, frame = camera.read()
        results = model(frame)[0]
        resList = results.boxes.data.tolist()
        for result in resList :
            print("\nfound Waldo!\n")
            score = result[4]
            print(score)
            if (score > THRESHOLD) & (score > WALDOPERCENT) :
                WALDOPERCENT = score
                x1, y1, x2, y2, WALDOPERCENT, dummy = result
        name = "Waldo"
        if WALDOPERCENT != 0.0 :    
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, name.upper(), (int(x1), int(y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imwrite("frame.jpg", frame)
        cv2.imshow("Waldo Detection", frame)
        WALDOPERCENT = 0.0
        if cv2.waitKey(1) & 0xFF == ord(" "):
            camera.release()
            os.remove('frame.jpg')
            cv2.destroyAllWindows()
            break

def displayWaldo(frame, x1, y1, x2, y2) :
    name = "Waldo"
    frame = "D:\\Code\\Whats_Waldo\\WaldoImages\\Waldo1.jpg"
    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
    cv2.putText(frame, name.upper(), (int(x1), int(y1 - 10)),
        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow("Waldo Detection", frame)      # soon to be removed when gui is implemented
    cv2.imwrite("frame.jpg", frame)
    print("test")