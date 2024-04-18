import cvlib as cv
import cv2
import os
from ultralytics import YOLO
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor
from cvlib.object_detection import draw_bbox


# test train model
def waldoTrain() :
    model = YOLO("yolov8n.yaml")
    results = model.train(data="project-vote4us/MLTest/testcfg.yaml", epochs=100)
    #print("\n\nRESULTS:\n" + results + "\n\n")

def val2() :
    model = YOLO(r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\Waldo_Project\WSG_Waldo\runs\detect\train2\weights\best.pt")
    results = model.val()

def runWaldoIMG5():
    # Initialize YOLO model
    model = YOLO(r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\Waldo_Project\WSG_Waldo\runs\detect\train5\weights\best.pt")
    
    # Image path
    image_path = r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\What's Waldo\Random Pictures\Waldo 1.jpg"
    
    # Predict
    results = model.predict(image_path, save=True, imgsz=320, conf=0.2)
    #results = model(image_path)
    
    # Check the results
    print(results)

    
    
def runWaldo1() :
    model = YOLO(r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\Waldo_Project\WSG_Waldo\runs\detect\train10\weights\best.pt")
    model.predict(source=r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\What's Waldo\Random Pictures\Waldo 1.jpg", stream=False)
    print("done")

def runWald5() :
    model = YOLO(r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\Waldo_Project\WSG_Waldo\runs\detect\train5\weights\best.pt")
    camera = cv2.VideoCapture(0)   # camera
    threshold = 0.4
    while True :
        ret, frame = camera.read()
        results = model(frame)[0]
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            #print("score: " + score)
            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow("Waldo Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord(" "):
            os.remove('frame.jpg')
            cv2.destroyAllWindows()
            break

def runWaldo3() :
    model = YOLO(r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\Waldo_Project\WSG_Waldo\runs\detect\train10\weights\best.pt")
    VIDEOS_DIR = os.path.join('.', 'video')
    video_path = os.path.join(VIDEOS_DIR, 'wald.mp4')
    video_path_out = '{}_out.mp4'.format(video_path)
    camera = cv2.VideoCapture(video_path)   # camera
    ret, frame = camera.read()
    H, W, _ = frame.shape
    video_path_out = r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\Waldo_Project\WSG_Waldo\video"
    out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(camera.get(cv2.CAP_PROP_FPS)), (W, H))
    threshold = 0.5
    while ret:
        results = model(frame)[0]
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        out.write(frame)
        ret, frame = camera.read()
    camera.release()
    out.release()
    cv2.destroyAllWindows()