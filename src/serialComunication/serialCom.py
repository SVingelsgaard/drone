#serial comunication with arduino mega for sending the data over usb to mega(that sends radio to drone).
import serial
import time


class SerialCom:
    def __init__(self):

        self.COMPort = ""

        #self.arduino = serial(port="COM4", baudrate=9600, timeout=.1)
        time.sleep(3)#literry dying without this idk.

    def cycle(self):
        self.data = str()#+100 to make sure data uses 3 digits.
        #self.arduino.write(bytes(self.data, 'utf-8'))
        print("ree")

