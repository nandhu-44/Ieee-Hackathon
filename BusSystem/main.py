import cv2
import json
import time 
from pyzbar import pyzbar

# Open the camera
camera = cv2.VideoCapture(0)

while True:
    # Capture the frame
    _, frame = camera.read()

    # Decode the QR codes in the frame
    decoded_objects = pyzbar.decode(frame)

    # Loop through the decoded objects
    for obj in decoded_objects:
        # Extract the QR code data
        try: 
          data = obj.data.decode()
          json_data = json.loads(data)
          # Now you can access the data as a dictionary
          print(json_data)
          time.sleep(5)
        except:
            print("Invalid QR code")
            time.sleep(2)

    # Display the frame
    cv2.imshow("QR Code Scanner", frame)

    # Exit if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
camera.release()
cv2.destroyAllWindows()
