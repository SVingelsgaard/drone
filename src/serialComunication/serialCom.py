#serial comunication with arduino mega for sending the data over usb to mega(that sends radio to drone).
import string
import serial
import time
import local

class SerialCom:
    def __init__(self, **kwargs):
        super(SerialCom, self).__init__(**kwargs)

        self.COMPort = local.COMPort #setting com port from the local vaiable file
        self.arduino = serial.Serial(port=self.COMPort, baudrate=9600, timeout=.1)
        self.master = None
        self.dataIn = ""
        self.dataOut = "000000000000"
        
        self.LFString = "000"
        self.RFString = "000"
        self.LBString = "000"
        self.RBString = "000"


    def read(self):
        self.dataIn = (self.arduino.readline().decode("utf-8"))#read data from arduino. an emoji is atached to the end of the message to indicate it is a string. idk y. ignore it.

        print(self.dataIn)
        
        
    def write(self):
        
        self.parseData()
        self.arduino.write(bytes(str(self.dataOut), 'utf-8'))#write data to arduino

    def parseData(self):#gathering data from the master and saving in a format for writing to arduino
        self.LFString = str(self.master.LF).rjust(3,"0")
        self.RFString = str(self.master.RF).rjust(3,"0")
        self.LBString = str(self.master.LB).rjust(3,"0")
        self.RBString = str(self.master.RB).rjust(3,"0")
        self.dataOut = (self.LFString + self.RFString + self.LBString + self.RBString)#data out is a 12 letter string where each motor speed have 3 letters