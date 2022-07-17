from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
import requests


class StartScreen(Screen):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)

    def btn(self):
        print("Name:", self.first_name.text, "Last Name:", self.last_name.text)
        name = self.first_name.text
        last_name = self.last_name.text
        dic = {"Namen": name, "Nachname": last_name}
        requests.post("http://127.0.0.1:8000/Name_hinzu", dic)


class GroceryList(Screen):
    product_name = ObjectProperty(None)

    def btn(self):
        print("Product Name:", self.product_name.text)


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
