#GUI using the kivy framework

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.properties import ListProperty, StringProperty
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from gui.static.kivyModules import circularProgressBar
import time
import os

#config
Config.set('kivy','window_icon',os.path.dirname(os.path.realpath(__file__))  + "\static\images\s.png")#window icon

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

kvPath = os.path.dirname(os.path.realpath(__file__))  + "\kivyFrontend.kv"#getting the path this file then adding the actual file


class WindowManager(ScreenManager):
    pass

class StartScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class ControlPanel(FloatLayout):
    pass

class ProcessView(Widget):
    pass

class Controls(Widget):
    manLF = NumericProperty(0)
    manRF = NumericProperty(0)
    manLB = NumericProperty(0)
    manRB = NumericProperty(0)
class GUI(App):
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)
 
        #variables
        self.setCycletime = 0.02#deafault cycletime. this should be set from the master program
        self.readCycletime = 0
        self.runTime = 0
        self.master = None
        self.title = "Drone Controller"
        self.running = False

    def stopApp(self):
        #App.get_running_app().stop()
        Window.close()#only gives me error
        
    def cycle(self):
        self.input()

    def input(self):#input form the GUI
        self.controls.manLF = int(self.root.get_screen('mainScreen').ids.manLF.value)
        self.controls.manRF = int(self.root.get_screen('mainScreen').ids.manRF.value)
        self.controls.manLB = int(self.root.get_screen('mainScreen').ids.manLB.value)
        self.controls.manRB = int(self.root.get_screen('mainScreen').ids.manRB.value)

    def on_start(self):
        #variables for kv file
        self.controls = self.root.get_screen('mainScreen').ids.controls

    def on_stop(self):
        self.master.stopDrone()
    
    def runMainCycle(self, readCycletime):
        self.master.mainCycle()#running the main cycle in the "master" class.  
        self.runTime += readCycletime#runtime
        print(int(self.runTime))

    #runns cycle
    def runApp(self):
        Clock.schedule_interval(self.runMainCycle, self.setCycletime)
        
        print("GUI running")
        self.running = True


    #runs myApp(graphics)
    def build(self):
        self.icon = 'ico/path.ico'
        return Builder.load_file(kvPath)