import serial
import curses

arduino = serial.Serial('/dev/ttyUSB0', 9600) # write /dev/ttyACM0 for older version of arduino
#COM for windows

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
  while True:
    char = screen.getch()
    if char == ord('q'):
      break
    elif char == curses.KEY_UP:
      arduino.write(b'F') #this sends 'F' to arduino. Use whatever convention/key you hve decided for each direction
    elif char == curses.KEY_DOWN:
      arduino.write(b'B')
    elif char == curses.KEY_LEFT:
      arduino.write(b'L')
    elif char == curses.KEY_RIGHT:
      arduino.write(b'R')
    elif char == ord(' '):
      arduino.write(b'S')
      
     
finally:
  curses.nobreak()
  screen.keypad(False)
  curses.echo()
  curses.endwin()
  arduino.close()
