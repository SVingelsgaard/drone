#Main code for controling the drone

#variables that needs to be set:
GUIcycletime = .02
mainCycletime = 1

class Drone():
    def __init__(self):
        #system variables
        
        #self.mainThread = threading.Thread(target=self.cycle)
        
        self.GUIcycletime = GUIcycletime

        #drone variables(global)
        #motor speeds. have to be int for making it easyer to send data aswell as the motors taking an int as speedreference.
        self.LF = 0
        self.RF = 0
        self.LB = 0
        self.RB = 0

    def startGUI(self):
        print("GUI starting..")

        from gui.kivyBackend import GUI
        self.GUI = GUI()#crating GUI
        self.GUI.setCycletime = GUIcycletime#setting the cycletime
        self.GUI.master = drone#set master so functions in drone can be run form the GUI
        self.GUI.run()#starting the GUI

    def stopGUI(self):
        self.GUI.stopApp()

    def startSerialCom(self):
        print("Serial comunication starting..")

        from serialComunication.serialCom import SerialCom
        self.serialCom = SerialCom()#creating serial comunication
        self.serialCom.master = drone#set master so functions and variables in drone can be run form the serailCom
        self.serialCom.start()

    def stopSerialCom(self):
        self.serialCom.stop()

    def mainCycle(self):
        self.LF = self.GUI.controls.manLF
        self.RF = self.LF#self.GUI.controls.manRF
        self.LB = self.LF#self.GUI.controls.manLB
        self.RB = self.LF#self.GUI.controls.manRB

        self.GUI.cycle()#running the gui cycle wich reads user input and presents the real time data from drone(serailCom.read()).

    def stopDrone(self):
        self.LF = 0
        self.RF = 0
        self.LB = 0
        self.RB = 0

        self.stopSerialCom()
        self.stopGUI()

drone = Drone()
drone.startSerialCom()#serialcom crashes GUI. need threading i think
drone.startGUI()#has to be the last function to start because it starts the main cycle
