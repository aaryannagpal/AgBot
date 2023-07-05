import socket
import time
import sys
import os
import base64
import json
from threading import Thread

host = '0.0.0.0' 
port = 1235

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(15)
print('Server listening on {}:{}'.format(host, port))

base_dir = '/home/pi/Desktop/received-server-files'

def handle_client(client_socket):
    try:
        json_data = b''
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            json_data += chunk

      
        data = json.loads(json_data.decode())

        username = data['username']

        # Create a directory for the username if it doesn't exist
        user_dir = os.path.join(base_dir, username)
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)

        # Create separate directories for masks and soil-data
        masks_dir = os.path.join(user_dir, 'masks')
        soil_data_dir = os.path.join(user_dir, 'soil-data')
        if not os.path.exists(masks_dir):
            os.makedirs(masks_dir)
        if not os.path.exists(soil_data_dir):
            os.makedirs(soil_data_dir)

        # Save the CSV file
        csv_data = base64.b64decode(data['csv'])
        csv_file_path = os.path.join(soil_data_dir, 'received_data.csv')
        with open(csv_file_path, 'wb') as csv_file:
            csv_file.write(csv_data)
        print('CSV file saved:', csv_file_path)

        # Save the images
        images = data['images']
        for idx, image_data in enumerate(images):
            image_data = base64.b64decode(image_data)
            image_path = os.path.join(masks_dir, 	'received_image_{}_{}.jpg'.format(int(time.time()), idx))
            with open(image_path, 'wb') as image_file:
                image_file.write(image_data)
            print('Image saved:', image_path)

        # Send acknowledgment to the client
        client_socket.sendall(b'ACK')

    except Exception as e:
        print(e)

    finally:
        # Close the connection
        client_socket.close()

# Function to start accepting connections
def start_server():
    while True:
        try:
            # Accept a connection
            client_socket, client_address = server_socket.accept()
            print('Client connected: {}'.format(client_address))

            # Start a new thread to handle the client connection
            client_thread = Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

        except KeyboardInterrupt:
            print('Closing the server')
            server_socket.close()
            sys.exit(0)

        except Exception as e:
            print(e)
            continue

# Start the server
start_server()
