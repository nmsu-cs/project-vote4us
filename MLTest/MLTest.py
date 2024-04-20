import cv2
import cvlib as cv
import os
from cvlib.object_detection import draw_bbox

# This code's functionality is now implemented by RunModels

# turn off floating-point round-off errors
#TF_ENABLE_ONEDNN_OPTS = 0
DEBUG = 0   # 0 is comments off, 1 is comments on
CAPTURE = 0   # controls capture device


# This is for object detection in video capture
def runObjectDetection() :
    video = cv2.VideoCapture(CAPTURE)   # the argument modifies the capture device, (0 = my webcam)
    # run until space key is pressed
    while True:
        ret, frame  = video.read()
        cv2.imwrite("frame.jpg", frame)
        bbox, label, conf = cv.detect_common_objects(frame)
        # when debug comments are toggled, print the object labels and confidence level
        if (DEBUG == 1) :
            print(label)
            print(conf)

        # for bbox, conf in zip(bbox, conf):
        #     (startX,startY) = bbox[0],bbox[1]
        #     (endX,endY) = bbox[2],bbox[3]
        #     cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)
    
        output_image = draw_bbox(frame, bbox, label, conf)
        cv2.imshow("Object Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord(" ") :
            os.remove('frame.jpg')
            cv2.destroyAllWindows()
            break

        # # TESTING ALLOWING CLICKING THE 'X' TO CLOSE WINDOW
        # # press space or 'X' button to close window
        # if (cv2.waitKey(1) & 0xFF == ord(" ")) | (cv2.waitKey(1) & cv2.getWindowProperty('Object Detection', 0) < 0) :
        #     os.remove('frame.jpg')
        #     cv2.destroyAllWindows()
        #     break
    


# This is for face detection in an image
# im = cv2.imread(r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\S371\What's Waldo\Random Pictures\peopleTest.jpg")   # SPECIFY IMAGE HERE

# while True:
#     faces, conf = cv.detect_face(im)
#     # print the confidence level of the detected faces
#     print(conf)
#     # loop through detected faces
#     for face, conf in zip(faces, conf):
#         (startX,startY) = face[0],face[1]
#         (endX,endY) = face[2],face[3]
#         cv2.rectangle(im, (startX,startY), (endX,endY), (0,255,0), 2)
#     cv2.imshow("Face Detection", im)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break


# This is for object detection in an image
# im = cv2.imread(r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\S371\What's Waldo\Random Pictures\peopleTest.jpg")   # SPECIFY IMAGE HERE

# bbox, label, conf = cv.detect_common_objects(im)
# output_image = draw_bbox(im, bbox, label, conf)
# plt.imshow(output_image)
# plt.show()



# This is for face detection in an image
def runFaceDetection() :
    video = cv2.VideoCapture(CAPTURE)   # the argument modifies the capture device, (0 = my webcam)
    while True:
        ret, frame  = video.read()
        faces, conf = cv.detect_face(frame)
        # when debug comments are toggled, print the object labels and confidence level
        if (DEBUG == 1) :
            print(conf)
        # loop through detected faces
        for face, conf in zip(faces, conf):
            (startX,startY) = face[0],face[1]
            (endX,endY) = face[2],face[3]
            cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)
        cv2.imshow("Face Detection", frame)
        # press space to close window
        if cv2.waitKey(1) & 0xFF == ord(" ") :
            cv2.destroyAllWindows()
            os.remove('frame.jpg')
            break
    
#print("done")
