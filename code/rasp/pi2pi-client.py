import socket
import time
import os
import json
import base64


server_ip = ''  # Server IP
server_port = 1235 

directory_path = 'masks' 

csv_file_path = './soil-data/received_data.csv'  
username = ''  # Replace with the desired username


while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    data = {}

    data['username'] = username

    with open(csv_file_path, 'rb') as csv_file:
        csv_data = csv_file.read()
        data['csv'] = base64.b64encode(csv_data).decode()

    images = []
    for file_name in os.listdir(directory_path):
        # Creating the full file path for images - DO NOT CHANGE
        image_path = os.path.join(directory_path, file_name)

        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Encoding with base64
        encoded_image_data = base64.b64encode(image_data).decode()

        # Adding the encoded image data to the list of images - DO NOT CHANGE
        images.append(encoded_image_data)

    # Add the image list to the data
    data['images'] = images

    # Convert the data to JSON
    json_data = json.dumps(data)

    # Send the JSON data to the server
    client_socket.sendall(json_data.encode())
    client_socket.close()

    print("Data Sent")
    print("Sleeping")
    time.sleep(120)
    print("Waking Up")
