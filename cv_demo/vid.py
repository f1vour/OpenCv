import cv2

 # if you have the video, instead of putting the 0, it selects the particular webcam how many you are using

# each image in a video camera has different frames
# the use of an infinite loop cause we dont know how long it will keep running

# All image frames is stored in the variable image and we are getting this from the video field

# We are capturing the video frames of pictures and storing it


capture = cv2.VideoCapture(0)
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    _, image = capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_haar_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)

    cv2.imshow("Video", image)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break


cv2.release()