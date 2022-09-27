#Backend for GUI. Made with the kivy framework
from packages import *

class GUI(App):
    
    def on_start(self): #variables
        pass
    #continus cycle
    def cycle(self, readCYCLETIME):
        pass
    #runns cycle
    def runApp(self):
        Clock.schedule_interval(self.cycle, self.setCYCLETIME)

    #runs myApp(graphics)
    def build(self):
        return Builder.load_file("../frontend/frontend.kv")

#runs program and cycle
if __name__ == '__main__':
    GUI().run()