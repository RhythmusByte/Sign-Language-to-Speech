import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import os

# Get absolute paths
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model", "keras_model.h5")
labels_path = os.path.join(current_dir, "model", "labels.txt")

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier(model_path, labels_path)

offset = 20
imgSize = 300

# Read labels from file
with open(labels_path, 'r') as file:
    labels = [line.strip() for line in file.readlines()]
print("Available labels:", labels)

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

                # Convert to grayscale
                imgWhiteGray = cv2.cvtColor(imgWhite, cv2.COLOR_BGR2GRAY)
                imgWhiteGray = cv2.cvtColor(imgWhiteGray, cv2.COLOR_GRAY2BGR)

                prediction, index = classifier.getPrediction(imgWhiteGray)

                # Print all prediction probabilities
                print("\nPrediction probabilities:")
                for i, (label, prob) in enumerate(zip(labels, prediction)):
                    print(f"{label}: {prob:.2f}%")

                predicted_label = labels[index]
                confidence = prediction[index]
                cv2.putText(img, f'{predicted_label} ({confidence:.2f}%)',
                            (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil(((imgSize - hCal) / 2))
                imgWhite[hGap:hCal + hGap, :] = imgResize

            cv2.imshow("ImageCrop", imgCrop)
            cv2.imshow("ImageWhite", imgWhiteGray)

        except Exception as e:
            print(f"Error processing image: {e}")

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()