# Project AgBot
## Description
Created while working as a Teaching Assistant for the Young Technology Scholar Program, 2023 at Plaksha University.<br><br>
AgBot is an advanced robot equipped with wheels using Raspberry Pi and Arduino Uno boards. Designed for data collection, it can traverse various terrains to gather valuable information. With its sensors, AgBot captures ground data, which it efficiently transmits to a central server for analysis and further decision-making. It also has a camera that can be used to capture images and videos of the surroundings.

## Components Used
- Arduino Uno (and cable)
- Raspberry Pi 3B+
- 12V Battery
- Power Bank (any source to power the Raspberry Pi)
- 4 Wheels
- Jumper Wires
- LogiTech WebCam
- 2 IBT-2 H-Bridge
- 4 Motor (model ask)
- Soldering Equipment
- 4 Acrylic Chassis (more info)

  .
  .
  .
_It is not necessary to use the exact same components_
## Pre-requisites (optional)
- Arduino IDE
- VS Studio Code

## Building the AgBot
### Assembling the Chasis
For this project, we created the frame of our robot using Acrylic Chassis. In total, we used laser cutter to create four of them to create the body, with several openings for the motor axes and screws. The ```CAD``` file is attached in the repository.

The chassis looks like this: <br>
<center>
<img src="./components/chassis.jpeg" width="300" height="250">
</center>

Two of them has their length side bent 90 degrees to create the side chassis. It was bent at a distance of 54 mm from each ends of the breadth. The side chassis look like:
<center>
<img src="./components/side-chassis.jpeg" width="300" height="250">
</center>

### Creating the Motor Ciruit
### Creating the H-Bridge Circuit
### Motor Code on Uno
#### Writing the Code
#### Configuration
### Setting up Raspberry Pi
#### Flashing 
#### Connecting to Local Network
#### Setting up SSH
### Serial Control Code on Raspberry Pi
#### Writing the Code
#### Configuration
### Accessing camera from Raspberry Pi
### Image Masking on the Server
#### Writing the Code
#### Sending to Raspberry Pi
### Setting up soil sensor
#### Soil data collection
#### Bluetooth connection with Client AgBots
##### Setting up on the ESP32
##### Setting up on the Raspberry Pi (Client)
### Setting up the Server AgBot
#### From Client AgBots
#### From ESP32


## Final Look
## References


