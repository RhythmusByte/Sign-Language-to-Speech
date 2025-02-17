import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import os
import tensorflow as tf

# Get absolute paths
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model", "keras_model.keras")
labels_path = os.path.join(current_dir, "model", "labels.txt")

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

# Load the Keras model
model = tf.keras.models.load_model(model_path)

offset = 20
imgSize = 200  # Changed to match the training data size (200x200)

# Read labels from file
with open(labels_path, 'r') as file:
    labels = [line.strip() for line in file.readlines()]
print("Available labels:", labels)

# Check if we have all 29 classes
if len(labels) != 29:
    print(f"Warning: Expected 29 classes (A-Z, SPACE, DELETE, NOTHING), but found {len(labels)}")

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        try:
            imgCrop = img[y - offset: y + h + offset, x - offset: x + w + offset]
            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil(((imgSize - wCal) / 2))
                imgWhite[:, wGap:wCal + wGap] = imgResize
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil(((imgSize - hCal) / 2))
                imgWhite[hGap:hCal + hGap, :] = imgResize

            # Preprocess the image for TensorFlow - using 200x200 dimensions
            preprocessed_img = imgWhite.copy()
            preprocessed_img = preprocessed_img / 255.0  # Normalize pixel values
            preprocessed_img = np.expand_dims(preprocessed_img, axis=0)  # Add batch dimension

            # Get prediction
            prediction = model.predict(preprocessed_img)[0]
            index = np.argmax(prediction)

            predicted_label = labels[index]
            confidence = prediction[index] * 100  # Convert to percentage
            
            # Display special messages for non-letter classes
            if predicted_label == "SPACE":
                display_text = "SPACE"
            elif predicted_label == "DELETE":
                display_text = "DELETE"
            elif predicted_label == "NOTHING":
                display_text = "NOTHING"
            else:
                display_text = predicted_label
                
            cv2.putText(img, f'{display_text} ({confidence:.2f}%)',
                        (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

            cv2.imshow("ImageCrop", imgCrop)
            cv2.imshow("ImageWhite", imgWhite)

        except Exception as e:
            print(f"Error processing image: {e}")

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()