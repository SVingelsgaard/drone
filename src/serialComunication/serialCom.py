#serial comunication with arduino mega for sending the data over usb to mega(that sends radio to drone).
from concurrent.futures import thread
import local
import serial
import threading
import time

class SerialCom():
    def __init__(self, **kwargs):
        super(SerialCom, self).__init__(**kwargs)

        self.COMPort = local.COMPort #setting com port from the local vaiable file
        try:
            self.arduino = serial.Serial(port=self.COMPort, baudrate=9600, timeout=.1)
            self.offline = False
        except:
            print('Arduino disconected. running in "offline" mode')
            self.offline = True
        self.master = None
        self.run = False
        self.dataIn = ""
        self.dataOut = "000000000000"
        
        self.LFString = "000"
        self.RFString = "000"
        self.LBString = "000"
        self.RBString = "000"
        
        self.serialThread = threading.Thread(target=self.threadLoop)        

    def start(self):
        self.run = True
        self.serialThread.start()#this needs to be after self.run is set to true for shit to work

    def stop(self):
        self.run = False
        self.write()#data is reset in main function. writing one last time so motors stop

    def threadLoop(self):
        time.sleep(2)#wait for gui to start
        print("Serial comunication running")
        while True:
            if (not self.run):
                print("Serial comunication stoping")
                break
            self.write()
            time.sleep(.1)


    def read(self):
        if not self.offline:
            self.dataIn = (self.arduino.readline().decode("utf-8"))#read data from arduino. an emoji is atached to the end of the message to indicate it is a string. idk y. ignore it.
        
        
    def write(self):
        self.parseData()
        if not self.offline:
            self.arduino.write(bytes(str(self.dataOut), 'utf-8'))#write data to arduino

    def parseData(self):#gathering data from the master and saving in a format for writing to arduino
        self.LFString = str(self.master.LF).rjust(3,"0")
        self.RFString = str(self.master.RF).rjust(3,"0")
        self.LBString = str(self.master.LB).rjust(3,"0")
        self.RBString = str(self.master.RB).rjust(3,"0")
        self.dataOut = (self.LFString + self.RFString + self.LBString + self.RBString)#data out is a 12 letter string where each motor speed have 3 letters

