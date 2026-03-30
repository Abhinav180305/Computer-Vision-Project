!pip install opencv-python-headless matplotlib --quiet


import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
image_path = list(uploaded.keys())[0]
img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)

detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(70, 70))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 200, 0), 3)
    cv2.putText(img, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 200, 0), 2)

cv2.putText(img, f"Faces detected: {len(faces)}", (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 200, 255), 2)
print(f"✅ {len(faces)} face(s) detected")

plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title(f"{len(faces)} face(s) detected")
plt.show()

cv2.imwrite("result.jpg", img)
files.download("result.jpg")
