import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import os
import tensorflow as tf

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model", "keras_model.keras")
labels_path = os.path.join(current_dir, "model", "labels.txt")

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

model = tf.keras.models.load_model(model_path)

offset = 20
imgSize = 200

with open(labels_path, 'r') as file:
    labels = [line.strip().upper() for line in file.readlines()]

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        x, y = max(0, x - offset), max(0, y - offset)
        w, h = min(img.shape[1] - x, w + 2 * offset), min(img.shape[0] - y, h + 2 * offset)
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        try:
            imgCrop = img[y:y + h, x:x + w]
            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

            preprocessed_img = imgWhite / 255.0
            preprocessed_img = np.expand_dims(preprocessed_img, axis=0)

            prediction = model.predict(preprocessed_img)[0]
            index = np.argmax(prediction)

            predicted_label = labels[index]
            confidence = prediction[index] * 100
            display_text = predicted_label if predicted_label not in ["DEL", "NOTHING", "SPACE"] else predicted_label.upper()

            cv2.putText(img, f'{display_text} ({confidence:.2f}%)', (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
            cv2.imshow("ImageCrop", imgCrop)
            cv2.imshow("ImageWhite", imgWhite)
        except Exception:
            pass

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
