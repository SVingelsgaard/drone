#code for controling the dorne based on different inputs
from pyPS4Controller.controller import Controller

class PS4Controller:
    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        controller = Controller(interface="/dev/input/js0", connecting_using_ds4drv=False) 

    def cycle(self):
        pass