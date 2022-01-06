from kivymd.uix.boxlayout import MDBoxLayout 
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Dashboard(MDBoxLayout):
	pass