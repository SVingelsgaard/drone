#Main code for controling the drone

#variables that needs to be set:
GUIcycletime = .02
mainCycletime = 1

class Drone():
    def __init__(self):
        #system variables
        import threading
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

    def startSerialCom(self):
        print("Serial comunication starting..")

        from serialComunication.serialCom import SerialCom
        self.serialCom = SerialCom()#creating serial comunication
        self.serialCom.master = drone#set master so functions and variables in drone can be run form the serailCom

    def mainCycle(self):
        #self.serialCom.read()#reading data from the radio controller(drone). THIS CRASHES BUT IS NOT NEEDE ATM

        self.LF = self.GUI.controls.manLF
        self.RF = self.GUI.controls.manRF
        self.LB = self.GUI.controls.manLB
        self.RB = self.GUI.controls.manRB

        self.GUI.cycle()#running the gui cycle wich reads user input and presents the real time data from drone(serailCom.read()).
        self.serialCom.write()#writing the data to the radio controller(drone)



drone = Drone()
drone.startSerialCom()#serialcom crashes GUI. need threading i think
drone.startGUI()#has to be the last function to start because it starts the main cycle
