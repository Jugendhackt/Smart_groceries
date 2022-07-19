from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
import requests

product_name = ""


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
        global product_name
        product_name = self.product_name.text
        dic_product_name = {"Produktname": product_name}
        # data = requests.post("http://127.0.0.1:8000/Products", dic_product_name)
        # print(data.text)


class ShoppingCart(Screen):
    def on_enter(self, *args):
        global product_name
        dic_product_name = {"Produkt": product_name}
        requests.post("http://127.0.0.1:8000/shoppinglist", dic_product_name)


class Product(Screen):
    # product_name = keys["Produktname"]
    # ean = keys["EAN-Code"]
    # brand = keys["Marke"]
    # price = keys["Preis"]
    # product_weight = keys["Gewicht"]
    # packaging = keys["Verpackung"]
    # print(product_name)
    # print(ean)
    def on_enter(self, *args):
        global product_name
        self.product.text = product_name


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class SmartApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    SmartApp().run()
