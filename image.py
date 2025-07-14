from tkinter import *
from PIL import ImageTk
from tkinter.ttk import Combobox
from bs4 import BeautifulSoup
import requests
import re
import pyttsx3


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
engine.setProperty('rate',200)

def talk(text):
    engine.say(text)
    engine.runAndWait()


talk("hi would you like to open traffic sign recognition for image and video")
talk("for image type image for video type video")

a=str(input("enter something?"))
if a=="IMAGE":
    
    talk("opening traffic sign recognition for image")
    
    print("opening....")





    # import necessary libraries
    import cv2
    from ultralytics import YOLO
    class image:
        # initialize the detector with weights
        detector = YOLO("C:\\Users\\Parth Mishra\\Desktop\\traffic\\traffic_sign_detector.pt", task="detect")

        # path to the image
        img_path ="C:\\Users\\Parth Mishra\\Desktop\\traffic\\red_light.jpg"

        # to visualize detections

        # reading the image
        image = cv2.imread(img_path)

        # detector.predict returns a list of detection objects
        detections = detector.predict(image)

        for detection in detections:
            # Get class indices and class names
            class_ids = detection.boxes.cls  # cls stores the class IDs
            
            # Iterate over bounding boxes
            for i, bbox in enumerate(detection.boxes):
                # Get the bounding box coordinates
                x1, y1, x2, y2 = bbox.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Draw the bounding box
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
                
                # Get class name using the class ID
                class_id = int(class_ids[i])
                class_name = detection.names[class_id]  # detection.names holds the class names
                
                # Display the class name on the image
                cv2.putText(image, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
                # Show the image with detection
                cv2.imshow("Detected", image)
                
                # Break on 'q' key
                if cv2.waitKey(10000) & 0xFF == ord("q"):
                    break

        # uncomment the following line to detect and save the annotated image without visualizing it
        results = detector(img_path, save=True)
if a=="VIDEO":
    talk("open traffic sign recognition for video")

    print("opening......")
    # import libraries
    from ultralytics import YOLO
    import cv2
    class video:
        # initilaize the detector model
        detector = YOLO("C:\\Users\\Parth Mishra\\Desktop\\traffic\\traffic_sign_detector.pt", task="detect")

        # video path
        video_path = "C:\\Users\\Parth Mishra\\Desktop\\traffic\\traffic_signs.mp4"

        # read the video file
        cap = cv2.VideoCapture(video_path)

        # check for errors
        if not cap.isOpened():
            print("Unable to open the input file")
            exit()

        # processing
        ret = True

        while ret:
            ret, frame = cap.read()
            
            detections = detector(frame)
            
            for detection in detections:
                    for bbox in detection.boxes:
                        x1, y1, x2, y2 = bbox.xyxy[0]  # Get bounding box coordinates
                        
                        # Convert to integers
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        
                        # Draw rectangle
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
                    cv2.imshow("Traffic sign detector", frame)
            
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break

        cap.release()
        cv2.destroyAllWindows()

        # uncomment the following line to detect and save the annotated image without visualizing it
        results = detector(video_path, save=True)

                