from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock

from plyer import notification

from kivy.core.window import Window
Window.size = (393, 852)

import json


class MainWidget(Screen):
    def __init__(self, **kw):
        super(MainWidget, self).__init__(**kw)
        self.load_btns()

    timer = StringProperty("00:00:00")
    sec, minute, hour = 0, 0, 0
    mes = StringProperty("")
    sound = SoundLoader.load('assets/1.wav')
    running = False

    # Загрузка режима работы
    with open('modes.json', 'r') as file:
        data = json.load(file)
    modes = data['modes']
    current_mode_id = data['last_mode']
    mode_name = StringProperty(modes[current_mode_id]['name'])

    def load_btns(self):
        button_layout = self.ids.modes
        for mode in self.modes:
            btn = Button(text=mode['name'])
            btn.id = mode['id']
            btn.bind(on_press=self.choose_mode)
            button_layout.add_widget(btn)

    def choose_mode(self, instance):
        self.current_mode_id = instance.id
        self.mode_name = self.modes[self.current_mode_id]['name']


    def check_points(self):
        """Функция для проверки временных точек"""
        points = self.modes[self.current_mode_id]['points']
        # point = points[0]
        for point in points:
            if self.hour == point[0] and self.minute == point[1] and self.sec == point[2]:
                self.sound.play()
        

    def update_time(self, dt):
        """Ядро таймера"""

        if self.running:
            self.sec += 1
            if self.sec == 60:
                self.sec = 0
                self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1

            tsec = f'{self.sec}' if self.sec >= 10 else f'{self.sec:02}'
            tmin = f'{self.minute}' if self.minute >= 10 else f'{self.minute:02}'
            thour = f'{self.hour}' if self.hour >= 10 else f'{self.hour:02}'

            self.timer = f'{thour}:{tmin}:{tsec}'
            self.check_points()

            if [self.hour, self.minute, self.sec] == self.modes[self.current_mode_id]['points'][-1]:
                self.running = False
                self.mes = 'Программа заверщена'
    
    def start(self):
        """Старт таймера"""

        if self.running:
            self.running = False
        else:
            self.running = True

    def reset(self):
        """Перезагрузка таймера"""

        self.sec = 0
        self.minute = 0
        self.hour = 0
        self.timer = '00:00:00'
        self.running = False
        self.mes = ''

class AddMode(Screen):
    ...




class TimerApp(App):
    def build(self):
        screen_manager = ScreenManager(transition=SlideTransition())

        screen_manager.add_widget(MainWidget(name='main_widget'))
        screen_manager.add_widget(AddMode(name='add_mode'))     
        return screen_manager
    
    def on_start(self):
        Clock.schedule_interval(self.root.get_screen('main_widget').update_time, 1)

if __name__ == "__main__":
    TimerApp().run()
