import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Load Known faces
tapon_image = face_recognition.load_image_file("C:/Users/ASUS/Dropbox/PC/Documents/OOP2_Poject/faces/tapon.jpg")
tapon_encoding = face_recognition.face_encodings(tapon_image)[0]

osman_image = face_recognition.load_image_file("C:/Users/ASUS/Dropbox/PC/Documents/OOP2_Poject/faces/osman.jpg")
osman_encoding = face_recognition.face_encodings(osman_image)[0]

mahin_image = face_recognition.load_image_file("C:/Users/ASUS/Dropbox/PC/Documents/OOP2_Poject/faces/mahin.jpg")
mahin_encoding = face_recognition.face_encodings(mahin_image)[0]

shaon_image = face_recognition.load_image_file("C:/Users/ASUS/Dropbox/PC/Documents/OOP2_Poject/faces/shaon.jpg")
shaon_encoding = face_recognition.face_encodings(shaon_image)[0]

# Add both known face encodings and names
known_face_encodings = [tapon_encoding, osman_encoding, mahin_encoding, shaon_encoding]
known_face_names = ["Tapon", "Osman", "Mahin", "Shaon"]

# List of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Open CSV file for adding
filename = "attendance.csv"
f = open(filename, "a+", newline="")
lnwriter = csv.writer(f)

while True:
    # Capture a single frame of video
    ret, frame = video_capture.read()
    if not ret:
        break

    # Resize frame to 1/4 size for faster face recognition
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        else:
            name = "Unknown"

        # Add the text if a person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2

            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                now = datetime.now()
                current_date = now.strftime("%Y-%m-%d")
                current_time = now.strftime("%I:%M:%S %p")  # Change to AM/PM format
                lnwriter.writerow([name, current_date, current_time])

    # Display the resulting frame
    cv2.imshow("Attendance", frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam and close CSV file
video_capture.release()
cv2.destroyAllWindows()
f.close()
