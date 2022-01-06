import os
import kivy
from kaki.app import App
from kivymd.app import MDApp
from kivy.factory import Factory 
from kivy.core.window import Window
Window.size = (400, 700)

class MainApp(App, MDApp):

    DEBUG = 1
    KV_FILES = {
        os.path.join(os.getcwd(), "view/dashboard.kv"),

        os.path.join(os.getcwd(), "view/login_screen/login_screen.kv"),

        os.path.join(os.getcwd(), "view/home_screen/home_screen.kv"),

        os.path.join(os.getcwd(), "view/screen_one/screen_one.kv"),

        os.path.join(os.getcwd(), "view/screen_two/screen_two.kv"),

        os.path.join(os.getcwd(), "view/screen_three/screen_three.kv"),

    }
    CLASSES = {
        "Dashboard": "view.dashboard",

        "LoginThree": "view.login_screen.login_screen",

        "HomeScreen": "view.home_screen.home_screen",

        "ScreenOne": "view.screen_one.screen_one",

        "ScreenTwo": "view.screen_two.screen_two",

        "ScreenThree": "view.screen_three.screen_three",

    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True})
    ]

    def build_app(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.primary_hue = "900"
        return Factory.Dashboard()

MainApp().run()