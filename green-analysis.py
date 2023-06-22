import numpy as np
import cv2

def green_percentage(image):
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    cv2.imshow('Processed image', green_mask)
    green_pixels = np.sum(green_mask == 255)
    total_pixels = green_mask.size
    greenPercentage = green_pixels/total_pixels*100


    print(greenPercentage)

stream= "http://10.1.45.82:8081"
vid= cv2.VideoCapture(stream)
while vid.isOpened():
    ret,frame=vid.read()
    if ret:
        cv2.imshow('frame',frame)
        green_percentage(frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()



