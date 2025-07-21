import cv2
import face_recognition

img=cv2.imread("known.jpeg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encoding(rgb_img)[0]

img2 = cv2.imread("image/unknown.jpeg")
rgb_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

cv2.imshow("Img", img)
cv2.waitKey(0)