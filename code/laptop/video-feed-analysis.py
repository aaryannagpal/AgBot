import cv2
import numpy as np
import paramiko
import datetime
import io

# url = 'http://<ip>:<port>' to visit the feed from the web
capture = cv2.VideoCapture(0)

username = ' ' # WRITE YOUR SSH USERNAME
password = ' ' # WRITE YOUR SSH PASSWORD

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(username, username='pi', password=password)

start_time = datetime.datetime.now()
while True:
    ret, frame = capture.read()
    if not ret: 
        break
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)
    green_pixels = np.sum(green_mask == 255)
    total_pixels = green_mask.size
    percentage_green_hsv = green_pixels/total_pixels*100

    print(f"Percentage of hsv green pixels: {percentage_green_hsv:.1f}%")
    
    cv2.imshow('Mask', green_mask)
    cv2.imshow('Video', frame)

    current_time = datetime.datetime.now()
    elapsed_time = current_time - start_time

    if elapsed_time.total_seconds() >= 1.0:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        remote_filename = f'frame-{percentage_green_hsv:.1f}%_{timestamp}.jpg'

        frame_bytes = cv2.imencode('.jpg', green_mask)[1].tobytes()
        frame_file = io.BytesIO(frame_bytes)

        remote_directory = '/home/pi/Desktop/masks'
        sftp = ssh.open_sftp()
        sftp.putfo(frame_file, remote_directory + '/' + remote_filename)
        sftp.close()
        start_time = current_time

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
ssh.close()
