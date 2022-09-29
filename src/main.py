#Main code for controling the drone
import time

#variables that needs to be set:
GUIcycletime = 0.02

class Drone():
    def __init__(self):
        self.GUIcycletime = GUIcycletime

    def startGUI(self):
        print("GUI starting..")
        from gui.kivyBackend import GUI
        self.GUI = GUI()#crating GUI
        self.GUI.setCycletime = GUIcycletime#setting the cycletime
        self.GUI.master = drone#set master so functions in drone can be run form the GUI
        self.GUI.run()#starting the GUI

    def startSerialCom(self)
        print("Serial comunication starting")

    def mainCycle(self):
        self.GUI.cycle()
        self.

drone = Drone()
drone.startGUI()