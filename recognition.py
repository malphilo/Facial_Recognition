import cv2 #opencv 
import face_recognition 

# Load a known image and encode it
known_image = face_recognition.load_image_file("known.jpeg") #loading the image
known_encoding = face_recognition.face_encodings(known_image)[0] #encoding the image
known_name = "Elon musk" #name of the loaded image


video_capture = cv2.VideoCapture(0) # Start webcam

while True:
    ret, frame = video_capture.read() #reading camera
    if not ret: #if any error opening the camera
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) 
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB) # changing BGR to RGB

    # Find all faces and face encodings in current frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        match = face_recognition.compare_faces([known_encoding], face_encoding)[0]

        name = known_name if match else "Unknown"

        # Scale back up face locations since the frame was resized
        top = top * 4
        right = right * 4
        bottom = bottom * 4
        left = left * 4

        # Draw a box and name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 0), 1)

    
    cv2.imshow('Webcam Face Recognition', frame) # Show the frame

    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to quit (indication for exiting )
        break

video_capture.release()
cv2.destroyAllWindows()
