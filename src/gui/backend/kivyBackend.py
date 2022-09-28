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

kv = Builder.load_file("C:\\Users\\Sigur\\Desktop\\cs\\drone\\src\\gui\\frontend\\kivyFrontend.kv")

#window settings
"""Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'fullscreen', '1')"""


class WindowManager(ScreenManager):
    pass

class StartScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class Envirement(FloatLayout):
    pass

class GUI(App):
    def on_start(self): #variables
        #system variables
        self.setCYCLETIME = 0.02
        self.readCYCLETIME = 0
        self.runTime = 0
        self.env = self.root.get_screen('mainScreen').ids.env

    def cycle(self, readCYCLETIME):
        self.readCYCLETIME = readCYCLETIME
        if self.runTime != 0 and self.runTime < .03:
            time.sleep(1)

    



        #runtime
        self.runTime += readCYCLETIME 

    #runns cycle
    def runApp(self):
        Clock.schedule_interval(self.cycle, self.setCYCLETIME)

    #runs myApp(graphics)
    def build(self):
        return kv
