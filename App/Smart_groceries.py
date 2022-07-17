from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.lang.builder import Builder


class StartScreen(Screen):
    pass


class GroceryList(Screen):
    pass


class ShoppingCart(Screen):
    pass


class Product(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class SmartApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    SmartApp().run()
