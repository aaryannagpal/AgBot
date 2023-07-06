#include "BluetoothSerial.h"
#include <ArduinoJson.h>
#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = ""; // Your WiFi SSID
const char* password = ""; // Your WiFi password
const char* host = "";   // IP address of the receiving server
const int port = 8888;  

#define ESP_NAME "ESP32-West"

int sensor_analog;
// int Moisture; // incase you want to map the value
const int sensor_pin = 36;

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to enable it
#endif

WiFiUDP udp;
BluetoothSerial SerialBT;
unsigned long startTime;
bool isConnected = false;

void setup() {
  Serial.begin(115200);
  SerialBT.begin(ESP_NAME); // Bluetooth device name
  Serial.println("The device started, now you can pair it with Bluetooth!");
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  udp.begin(port);
  // pinMode(ecg, INPUT);
}

void loop() {
  if (!isConnected) {
    if (SerialBT.connected()) {
      isConnected = true;
      startTime = millis(); // Record the current time when the connection is established
    }
  } else {
    if (!SerialBT.connected()) {
      isConnected = false;
      Serial.println("Connection lost");
    } else {
      unsigned long elapsedTime = millis() - startTime;
      unsigned long remainingTime = 20000 - elapsedTime; // 20 seconds
      Serial.print("Seconds left: ");
      Serial.println(remainingTime / 1000);
      
      if (elapsedTime >= 20000) {
        SerialBT.disconnect();
        isConnected = false;
        Serial.println("Timer expired. Disconnected.");
      }
    }
  }
  
  if (Serial.available()) {
    SerialBT.write(Serial.read());
  }
  if (SerialBT.available()) {
    Serial.write(SerialBT.read());
  }
  delay(20);
  
  sensor_analog = analogRead(sensor_pin);
  
  // incase you want to map the value
  // Moisture = map(sensor_analog, 0, 4095, 100, 0);
  StaticJsonDocument<128> Data;

  Data["ESP Name"] = ESP_NAME;
  Data["Soil Moisture"] = sensor_analog;
  // Data["current time"] = ctime(&currentTime);
  String jsonString;
  serializeJson(Data, jsonString);
  
  Serial.print("JSON Data = ");
  Serial.println(jsonString);
  SerialBT.println(jsonString);
  Serial.println("Bluetooth Sent");
  
  udp.beginPacket(host, port);
  udp.print(jsonString);
  udp.endPacket();
  Serial.println("WiFi Sent");
  
  delay(1000);
}
