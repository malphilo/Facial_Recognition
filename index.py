"""
this is sample for comparing two images
import cv2
import face_recognition

# Load and encode known image
img = cv2.imread("known.jpeg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

# Load and encode unknown image
img2 = cv2.imread("image/unknown.jpeg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2_encoding = face_recognition.face_encodings(rgb_img2)[0]

# Compare faces
result = face_recognition.compare_faces([img_encoding], img2_encoding)
print("Match Found:" if result[0] else "No Match")

# Show images
cv2.imshow("Known", img)
cv2.imshow("Unknown", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""