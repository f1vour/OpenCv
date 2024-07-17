import cv2


face_haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread('demo.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray) This are the colours in BGR and the weight
# cv2.waitKey()

# Classifier is a classification to tell the front of a human face. it detects the face. Cv is used to load the classifier

faces = face_haar_cascade.detectMultiScale(gray, 1.1, 4) # This is our classifier, it detects the faces

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h),(0,255,0), 5)

cv2.imshow("Faces", image)
cv2.waitKey()
