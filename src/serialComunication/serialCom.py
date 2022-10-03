#serial comunication with arduino mega for sending the data over usb to mega(that sends radio to drone).
import serial
import time
import local

class SerialCom:
    def __init__(self):

        self.COMPort = local.COMPort #COM10"#deafault com port. should be set from main.py
        self.arduino = serial.Serial(port=self.COMPort, baudrate=9600, timeout=.1)
        self.dataIn = ""
        self.dataOut = [1,2,3,4]


    def read(self):
        self.dataIn = (self.arduino.readline().decode("utf-8"))#read data from arduino. an emoji is atached to the end of the message to indicate it is a string. idk y. ignore it.

        print(self.dataIn)
        
        
    def write(self):
        
        
        self.arduino.write(bytes(str(self.dataOut), 'utf-8'))#write data to arduino

    def parseData(self):
        pass#self.dataOut = ()#data out is a 12 letter string where each motor speed have 3 letters