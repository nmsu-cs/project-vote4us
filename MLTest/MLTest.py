import cv2
import cvlib as cv
import os
from cvlib.object_detection import draw_bbox


# HOW TO USE:
# PRESS 'q' KEY TO QUIT PROGRAM


# turn off floating-point round-off errors
#TF_ENABLE_ONEDNN_OPTS = 0


# This is for object detection in video capture

# video = cv2.VideoCapture(0)   # the argument modifies the capture device, (0 = my webcam)
# while True:
#     ret, frame  = video.read()
#     cv2.imwrite("frame.jpg", frame)
#     bbox, label, conf = cv.detect_common_objects(frame)
#     # print the labels of the objects being detected
#     print(label)
#     # print the confidence level of the detected objects
#     print(conf)
#     print(bbox)
#     output_image = draw_bbox(frame, bbox, label, conf)
#     cv2.imshow("Object Detection", frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         os.remove('frame.jpg')
#         break


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

video = cv2.VideoCapture(0)   # the argument modifies the capture device, (0 = my webcam)
while True:
    ret, frame  = video.read()
    cv2.imwrite("frame.jpg", frame)
    faces, conf = cv.detect_face(frame)
    # print the confidence level of the detected faces
    print(conf)

    # loop through detected faces
    for face, conf in zip(faces, conf):
        (startX,startY) = face[0],face[1]
        (endX,endY) = face[2],face[3]
        cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)

    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        os.remove('frame.jpg')
        break


print("done")