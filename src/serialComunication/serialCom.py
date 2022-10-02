#serial comunication with arduino mega for sending the data over usb to mega(that sends radio to drone).
import serial
import time


class SerialCom:
    def __init__(self):

        self.COMPort = "COM10"#deafault com port. should be set from main.py
        self.arduino = serial.Serial(port=self.COMPort, baudrate=9600, timeout=.1)
        time.sleep(3)#literry dying without this idk.

    def cycle(self):
        self.data = str(111222333444)
        
        
        self.arduino.write(bytes(self.data, 'utf-8'))