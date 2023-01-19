import cv2
import json
import time 
from pyzbar import pyzbar
from tkinter import *

def open_camera():
    global camera
    camera = cv2.VideoCapture(0)
    scan_qr()

def scan_qr():
    global camera
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
                print(json_data)
                close_camera()
                time.sleep(5)
            except:
                print("Invalid QR code")
                time.sleep(2)

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Exit if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            close_camera()
            break

def close_camera():
    global camera
    camera.release()
    cv2.destroyAllWindows()

root = Tk()
root.geometry("500x500")
root.title("QR Code Scanner")

scan_button = Button(root, text="Scan QR Code", command=open_camera)
scan_button.pack(pady=20)

root.mainloop()
