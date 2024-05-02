from flask import Flask, request, jsonify, send_file
import cv2
from ultralytics import YOLO
import os

app = Flask(__name__)

# Load the YOLO model
model = YOLO(os.getcwd() + "/models/WaldoV4/weights/best.pt")

# Define global variables
WALDOPERCENT = 0.0
THRESHOLD = 0.2

@app.route('/find_waldo', methods=['POST'])
def find_waldo():
    global WALDOPERCENT
    
    # Get the image file from the request
    image_file = request.files['image']

    # Save the image to disk
    image_path = 'temp_image.jpg'
    image_file.save(image_path)

    WALDOPERCENT = 0.0
    # Process the image
    frame = cv2.imread(image_path)
    results = model(frame)[0]

    resList = results.boxes.data.tolist()

    # Initialize variables
    x1 = y1 = x2 = y2 = -1.0

    # Iterate through results
    for result in resList:
        score = result[4]
        if score > THRESHOLD and score > WALDOPERCENT:
            WALDOPERCENT = score
            x1, y1, x2, y2, _, _ = result

    # Draw rectangle if Waldo found
    if WALDOPERCENT > 0:
        name = "Waldo"
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
        cv2.putText(frame, name.upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        result_image_path = os.path.join(os.getcwd(), 'temp_result.jpg')
        cv2.imwrite(result_image_path, frame)
        return send_file(result_image_path, mimetype='image/jpeg')
    else:
        return jsonify({"message": "Waldo not found."})

@app.route('/live_detect', methods=['POST'])
def live_detect():
    # Initialize webcam
    camera = cv2.VideoCapture(0)  # Use 0 to capture frames from the device's webcam
    if not camera.isOpened():
        return jsonify({"message": "Failed to open webcam."}), 500

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Process the frame for object detection
        annotated_frame = process_frame(frame)
        webcam_image_path = os.path.join(os.getcwd(), 'webcam_image.jpg')
        cv2.imwrite(webcam_image_path ,annotated_frame)
        return send_file(webcam_image_path, mimetype='image/jpeg')

    camera.release()

def process_frame(frame):
    # Preprocess the frame (resize, normalize, etc.) if necessary
    # Process the frame using your YOLO model for object detection
    results = model(frame)[0]

    resList = results.boxes.data.tolist()

    # Initialize variables
    global WALDOPERCENT
    WALDOPERCENT = 0.0
    x1 = y1 = x2 = y2 = -1.0

    # Iterate through results
    for result in resList:
        score = result[4]
        if score > THRESHOLD and score > WALDOPERCENT:
            WALDOPERCENT = score
            x1, y1, x2, y2, _, _ = result

    # Draw rectangle if Waldo found
    if WALDOPERCENT > 0:
        name = "Waldo"
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
        cv2.putText(frame, name.upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    # Always return the frame, whether Waldo is detected or not
    return frame

if __name__ == '__main__':
    app.run(debug=True)


