import bluetooth
import time
import json
import csv
from datetime import datetime


csvLocation = '/home/pi/Desktop/soil-data/received_data.csv'

# List of ESP32 device names
esp32_device_names = ["ESP32-West", "ESP32-South", "ESP32-East", "ESP32-North"]

def find_esp32_mac_address(esp32_device_name):
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

    for device_address, device_name in nearby_devices:
        if device_name == esp32_device_name:
            return device_address

    return None

def connect_to_esp32(esp32_device_name):
    esp32_mac_address = find_esp32_mac_address(esp32_device_name)
    if esp32_mac_address:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        port = 1  # RFCOMM port number

        try:
            sock.connect((esp32_mac_address, port))
            print(f"Connected to {esp32_device_name}")
            return sock
        except Exception as e:
            print(f"Failed to connect to {esp32_device_name}: {e}")
            return None
    else:
        print("ESP32 device not found.")
        return None

def receive_serial_data(sock):
    while True:
        try:
            data = sock.recv(1024)
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
                    with open(csvLocation, "a", newline="") as csvfile:
                        csv_writer = csv.writer(csvfile)
                        csv_writer.writerow(csv_row)

        except Exception as e:
            print(f"Error receiving data: {e}")
            break

if __name__ == '__main__':
    while True:
        for device_name in esp32_device_names:
            # Connect to ESP32
            esp32_socket = connect_to_esp32(device_name)

            if esp32_socket:
                # Start receiving serial data
                receive_serial_data(esp32_socket)
            else:
                print(f"Connection to {device_name} failed.")

            # Wait for a few seconds before trying the next ESP32 device
            time.sleep(2)
