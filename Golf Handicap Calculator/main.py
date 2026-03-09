import kivy
kivy.require('2.3.1')

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivymd.uix.menu import MDDropdownMenu

from functions import *

class GolfHandicap(MDApp):
    def __init__(self, **kwargs):
        self.title = "Golf Handicap Calculator"
        self.theme_style = "Light"
        self.primary_palette = "Green"
        self.score_popup = None
        self.course_popup = None
        self.course_menu = None
        self.refresh_score_popup_after_course = False
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_file("main.kv")


    def login_screen(self):
        self.root.ids.screen_manager.current = "login_screen"

    def registration_screen(self):
        self.root.ids.screen_manager.current = "registration_screen"

    def home_screen(self):
        self.refresh_home_screen()
        self.root.ids.screen_manager.current = "home_screen"

    def refresh_home_screen(self):
        screen = self.root.ids.screen_manager.get_screen("home_screen")
        screen.ids.handicap_label.text = self.get_user_handicap_index()
        screen.ids.rounds_label.text = self.get_user_rounds_played()
        screen.ids.courses_label.text = self.get_user_courses_played()

    def open_account_drawer(self):
        drawer = self.root.ids.account_drawer
        drawer.set_state("open")

    def courses_screen(self):
        self.root.ids.screen_manager.current = "courses_screen"
        display_courses(self)

    def scorecard_screen(self):
        self.root.ids.screen_manager.current = "scorecard_screen"
        display_scores(self)

    def authenticate(self, username, password):
        if check_credentials(username, password):
            login_screen = self.root.ids.screen_manager.get_screen("login_screen")
            login_screen.ids.username_input.text = ""
            login_screen.ids.password_input.text = ""
            self.home_screen()
        else:
            print("Invalid username or password")

    def get_user_handicap_index(self):
        return str(get_handicap_index())
    
    def get_user_rounds_played(self):
        return str(len(load_scores()))
    
    def get_user_courses_played(self):
        scores = load_scores()
        courses_played = set(name for name, score in scores)
        return str(len(courses_played))

    def show_add_score_popup(self):
        courses = load_courses()

        if not courses:
            popup_content = Factory.NoCoursesPopup()
            self.score_popup = Popup(
                title="Add Score",
                content=popup_content,
                size_hint=(0.9, 0.4),
                auto_dismiss=False,
                background="",
                separator_height=0
            )
        else:
            popup_content = Factory.AddScorePopup()
            self.score_popup = Popup(
                title="Add Score",
                content=popup_content,
                size_hint=(0.9, 0.65),
                auto_dismiss=False,
                background="",
                separator_height=0
            )

            # Build dropdown menu
            self.build_course_menu(popup_content.ids.course_selector, courses)

        self.score_popup.open()

    def build_course_menu(self, caller, courses):
        menu_items = []

        # Add each course
        for course in courses:
            menu_items.append({
                "text": course.name,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=course.name: self.select_course_from_menu(x)
            })

        # Add the "+ Add Course" option
        menu_items.append({
            "text": "+ Add Course",
            "viewclass": "OneLineListItem",
            "on_release": self.open_add_course_from_menu
        })

        self.course_menu = MDDropdownMenu(
            caller=caller,
            items=menu_items,
            width_mult=4
        )

    def open_add_course_from_menu(self):
        if self.course_menu:
            self.course_menu.dismiss()

        self.show_add_course_popup_from_score()


    def select_course_from_menu(self, course_name):
        if self.score_popup:
            popup_content = self.score_popup.content
            popup_content.ids.course_selector.text = course_name

        if self.course_menu:
            self.course_menu.dismiss()

    def close_score_popup(self):
        if self.score_popup:
            self.score_popup.dismiss()
            self.score_popup = None

    def save_score_from_popup(self):
        if self.score_popup:
            popup_content = self.score_popup.content
            course_name = popup_content.ids.course_selector.text
            score_text = popup_content.ids.score_input.text

            validation_error = validate_score_input(course_name, score_text)
            if validation_error:
                print(validation_error)
                return

            score = int(score_text)
            save_score(course_name, score)
            print(f"Score saved: {course_name} - {score}")

            display_scores(self)
            self.close_score_popup()
            self.refresh_home_screen()


    def show_add_course_popup(self):
        popup_content = Factory.AddCoursePopup()
        self.course_popup = Popup(
            title="Add Course",
            content=popup_content,
            size_hint=(0.9, 0.7),
            auto_dismiss=False,
            background="",
            separator_height=0
        )
        self.course_popup.open()

    def show_add_course_popup_from_score(self):
        self.show_add_course_popup()
        self.refresh_score_popup_after_course = True

    def close_course_popup(self):
        if self.course_popup:
            self.course_popup.dismiss()
            self.course_popup = None

    def save_course_from_popup(self):
        if self.course_popup:
            popup_content = self.course_popup.content
            course_name = popup_content.ids.course_name_input.text
            slope_text = popup_content.ids.slope_input.text
            rating_text = popup_content.ids.rating_input.text
            par_text = popup_content.ids.par_input.text

            validation_error = validate_course_input(course_name, slope_text, rating_text, par_text)
            if validation_error:
                print(validation_error)
                return

            try:
                slope = int(slope_text)
                rating = float(rating_text)
                par = int(par_text)

                new_course = golfCourse(course_name, slope, rating, par)
                new_course.save_course()
                print(f"Course saved: {course_name}")

                if self.refresh_score_popup_after_course and self.score_popup:
                    self.refresh_score_popup_after_course = False
                    popup_content_score = self.score_popup.content
                    courses = load_courses()
                    self.build_course_menu(popup_content_score.ids.course_selector, courses)
                    popup_content_score.ids.course_selector.text = course_name

                display_courses(self)
                self.close_course_popup()
                self.refresh_home_screen()

            except ValueError:
                print("Please enter valid values for all fields")

    def delete_all_rounds(self):
        delete_scores(self)
        display_scores(self)
        self.refresh_home_screen()

    def delete_all_data(self):
        delete_courses(self)
        delete_scores(self)
        display_scores(self)
        display_courses(self)
        self.refresh_home_screen()


if __name__ == '__main__':
    GolfHandicap().run()
