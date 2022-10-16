# drone
code for drone. sending the speed reference for the 4 motors to a arduino over serial comunictaion. the the arduino sends it via radio to another arduino inside the drone.

# stuff to do for it to work on a new machine
-add a "local.py" file. that has a variable "COMPort" whitch is set to the comport your arduino is conected to. for examle: "COMPort = "COM10""

-install the RF24 module made by TMRh20,avmander from the arduino liberary manager.