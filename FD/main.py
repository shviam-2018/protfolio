import threading
import cv2
from deepface import DeepFace

# Initialize Video Capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize Variables
counter = 0
face_match = False
Reference_img = "reference.jpg"

def check_face(frame):
    global face_match
    try:
        temp_file = "temp_frame.jpg"
        cv2.imwrite(temp_file, frame)
        result = DeepFace.verify(temp_file, Reference_img)
        face_match = result['verified']
    except Exception as e:
        print(f"Error in check_face: {e}")
        face_match = False

while True:
    ret, frame = cap.read()
    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except Exception as e:
                print(f"Threading Error: {e}")
        counter += 1

        # Display Match Status
        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        # Show Video Frame
        cv2.imshow("video", frame)

    # Exit on 'q'
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
