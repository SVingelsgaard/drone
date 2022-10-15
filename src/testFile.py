import time
import threading
import serial




class SerialCom():
    def __init__(self):
        self.data = "data"
        self.COMPort = "COM10"
        self.arduino = serial.Serial(port=self.COMPort, baudrate=9600, timeout=.1)
        self.serialThread = threading.Thread(target=self.write)
        self.serialThread.start()
    def write(self):
        for i in range(10):
            self.arduino.write(bytes(str(i), 'utf-8'))
            print(i)
            time.sleep(1)


SerialCom()