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

import time
import os

#config
Config.set('kivy','window_icon',os.path.dirname(os.path.realpath(__file__))  + "\static\images\s.png")#window icon

"""Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'fullscreen', '1')"""

kvPath = os.path.dirname(os.path.realpath(__file__))  + "\kivyFrontend.kv"#getting the path this file then adding the actual file


class WindowManager(ScreenManager):
    pass

class StartScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class Envirement(FloatLayout):
    pass

class GUI(App):
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)
 
        #variables
        self.setCycletime = 0.02#deafault cycletime. this should be set from the master program
        self.readCycletime = 0
        self.runTime = 0
        self.master = None

        self.title = "Drone Controller"
        
    def cycle(self):
        pass

    def on_start(self):

        #variables for kv file
        self.env = self.root.get_screen('mainScreen').ids.env

    def runMainCycle(self, readCycletime):
        self.master.mainCycle()#running the main cycle in the "master" class.  
        self.runTime += readCycletime#runtime

    #runns cycle
    def runApp(self):
        
        Clock.schedule_interval(self.runMainCycle, self.setCycletime)
        print("GUI running")


    #runs myApp(graphics)
    def build(self):
        self.icon = 'ico/path.ico'
        return Builder.load_file(kvPath)