import cvlib as cv
import cv2
import os
import setup_ML
from ultralytics import YOLO
from cvlib.object_detection import draw_bbox

# get the model most up to date (currently WaldoV1)
model = YOLO(setup_ML.getCWD() + "\project-vote4us\models\WaldoV1\weights\\best.pt")

# train model with user specified epochs
def waldoTrain(epic) :
    setup_ML.writeCFG()   # updates traincfg.yaml file, just in case sum stuff changed for some reason
    model = YOLO("yolov8n.yaml")
    results = model.train(data="project-vote4us/MLTest/traincfg.yaml", epochs=epic)

# takes an image path as a string and runs waldo modelS
def runWaldoIMG5(image):
    # Image path
    image_path = image
    # Predict
    results = model.predict(image_path, save=True, imgsz=320, conf=0.4)

# video input with waldo modelS
def runWald5() :
    camera = cv2.VideoCapture(0)   # camera hardcoded to 1st camera
    threshold = 0.4
    while True :
        ret, frame = camera.read()
        results = model(frame)[0]
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            #print("score: " + score)              # score contains our certainty percentage
            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow("Waldo Detection", frame)
        #cv2.imwrite("frame.jpg", frame)           # writes to frame.jpg so gui can use it
        if cv2.waitKey(1) & 0xFF == ord(" "):
            os.remove('frame.jpg')
            cv2.destroyAllWindows()
            break
