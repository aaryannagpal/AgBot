import socket
import json
from datetime import datetime
import csv

UDP_IP = "0.0.0.0"  # Listen on all available network interfaces
UDP_PORT = 8888

csv_file = "esp-server-data.csv"

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

connected = False

print("Waiting for device connection...")

while True:
    try:
        # Receive UDP packet
        data, addr = sock.recvfrom(1024)
        if connected:
            print("Device connected")
            connected = True
        if data:
            data_str = data.decode().strip()
            if data_str != '':
                print(f"Received data: {data_str}")
                # Parse the data string as JSON
                data_json = json.loads(data_str)  # Use appropriate JSON parsing method instead

                # Extract the values from the JSON
                esp_name = data_json.get("ESP Name", "")
                soil_moisture = data_json.get("Soil Moisture", "")

                # Get the current timestamp
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Create a CSV row with the timestamp, ESP name, and soil moisture
                csv_row = [timestamp, esp_name, soil_moisture]

                # Append the CSV row to the file
                with open(csv_file, "a", newline="") as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(csv_row)
                print("Written to CSV")
    except Exception as e:
            print(f"Error receiving data: {e}")
            break
