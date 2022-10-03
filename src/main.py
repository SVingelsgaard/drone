#Main code for controling the drone

#variables that needs to be set:
GUIcycletime = 0.02
#COMPort = "COM10"

class Drone():
    def __init__(self):
        self.GUIcycletime = GUIcycletime

    def startGUI(self):
        print("GUI starting..")
        #import stuff
        from gui.kivyBackend import GUI
        self.GUI = GUI()#crating GUI
        self.GUI.setCycletime = GUIcycletime#setting the cycletime
        self.GUI.master = drone#set master so functions in drone can be run form the GUI
        self.GUI.run()#starting the GUI

    def startSerialCom(self):
        print("Serial comunication starting..")
        #import stuff
        from serialComunication.serialCom import SerialCom
        import local
        self.serialCom = SerialCom()#creating serial comunication
        self.serialCom.COMPort = local.COMPort#setting arduino com port

    def mainCycle(self):
        self.GUI.cycle()
        self.serialCom.cycle()

drone = Drone()
drone.startSerialCom()
drone.startGUI()#has to be the last function to start because it starts the main cycle
