import kivy
kivy.require('2.3.1')

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory

Builder.load_string("""
#:include kv/login.kv
#:include kv/registration.kv
#:include kv/homepage.kv
                                    
#:import utils kivy.utils
"""
)

class GolfHandicap(MDApp):
    def __init__(self, **kwargs):
        self.title = "Golf Handicap Calculator"
        self.theme_style = "Light"
        self.primary_palette = "Green"
        self.sm = ScreenManager()
        super().__init__(**kwargs)

    def build(self):
        self.sm.add_widget(Factory.LoginScreen())
        self.sm.add_widget(Factory.RegistrationScreen())  
        self.sm.add_widget(Factory.HomeScreen())  
        return self.sm
         
         
    def login_screen(self):
        self.sm.current = "login_screen"

    def registration_screen(self):
        self.sm.current = "registration_screen"

    def home_screen(self):
        self.sm.current = "home_screen"
    
if __name__ == '__main__':
    GolfHandicap().run()