import kivy
kivy.require('2.3.1')

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory
from auth import check_credentials

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
    
    def authenticate(self, username, password):
        """
        Authenticate the user with the provided credentials.
        """
        if check_credentials(username, password):
            # Clear the input fields
            login_screen = self.sm.get_screen("login_screen")
            login_screen.ids.username_input.text = ""
            login_screen.ids.password_input.text = ""
            # Navigate to home screen
            self.home_screen()
        else:
            # Show error message (you can enhance this with a popup later)
            print("Invalid username or password")
    
if __name__ == '__main__':
    GolfHandicap().run()