import time
import threading
import serial




class SerialCom():
    def __init__(self):
        self.data = "000000000002"
        self.COMPort = "COM10"
        self.arduino = serial.Serial(port=self.COMPort, baudrate=9600, timeout=.1)
        self.serialThread = threading.Thread(target=self.write)
        self.serialThread.start()
    def write(self):
        while True:
            self.arduino.write(bytes(self.data, 'utf-8'))
            print(self.data)
            time.sleep(1)


s = SerialCom()
while True:
    print("loop")
    time.sleep(0.2)
