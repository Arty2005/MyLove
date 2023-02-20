import time
from datetime import date
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from random import randint


KV = """
MyBl:
        orientation: "vertical"
        size_hint: (0.95,0.95)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
        Image:
                size: self.texture_size
                source: 'C:/Users/Admin/Desktop/my love/1.jpg'
        Label:
                font_size: "30sp"
                multiline: True
                text_size: self.width*0.98, None
                size_hint_x: 1.0
                size_hint_y: None
                height: self.texture_size[1] + 15
                text: root.data_label
        Button:
                text: root.first
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback()
                
        Button:
                text: root.second
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.new()
                
        Button:
                text: root.third
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.ret()
"""

class MyBl(BoxLayout):
    love_date = date(2021, 5, 5)
    today_date = date.today()
    ress = today_date - love_date
    res = str(ress)
    res = res.split()[0]
    re = "{:.2f}".format(int(res) / 365)
    data_label = StringProperty(f" Мы вместе уже целых {res} дней или {re} лет")
    first = "АНЕКДОТ?"
    second = "ЧТО-ТО ИНТРЕРЕСНОЕ"
    third = "НАЗАД"

    def new(self):
        a = randint(1, 7)
        if a == 1:
            self.data_label = "Ты мое солнышко"

        if a == 2:
            self.data_label = "Я тебя люблю"

        if a == 3:
            self.data_label = "Автор просто хотел сказать, что ты большая умничка и со всем справишься!"

        if a == 4:
            self.data_label = "Самое большое счастье для меня - это когда ты рядом"

        if a == 5:
            self.data_label = "Если честно, то я не представляю, как бы жил без тебя"

        if a == 6:
            self.data_label = "Ты - это то, что заставляет меня двигаться вперед:)"

        if a == 7:
            self.data_label = "Лучший день в моей жизни - день, когда я встретил тебя"



    def ret(self):
        self.data_label = f" Мы вместе уже целых {self.res} дней или {self.re} лет"

    def callback(self):
        a = randint(1, 4)
        b = 0
        if a == 1 and b != 1:
            self.data_label = "Слон извалялся в муке, подошел к зеркалу и говорит: \"Ничего себе - пельмешка!\""
            b = 1
        if a == 2 and b != 2:
            self.data_label = "Принц смотрел на хрустальную туфлю 44-го размера, и постепенно у него внутри холодело…"
            b = 2
        if a == 3 and b != 3:
            self.data_label = "Мальчик, который сходил только на один урок карате, успел лишь поклониться хулиганам"
            b = 3
        if a == 4 and b != 4:
            self.data_label = "Ребенок сотрудников Яндекса, отвечая на уроке, сначала рассказывает две рекламы"
            b = 4


class MyApp(App):

    running = True

    def build(self):
        Window.clearcolor = '#85409c'
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False
MyApp().run()