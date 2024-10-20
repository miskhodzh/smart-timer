from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock

from plyer import notification


class MainWidget(Screen):

    timer = StringProperty("00:00:00")
    sec, minute, hour = 0, 0, 0

    sound = SoundLoader.load('assets/1.wav')

    running = False

    def check_points(self):
        data = {
            ...
        }
        if self.hour == 0 and self.minute == 0 and self.sec == 3:
            self.sound.play()
            notification.notify(
                title = "HEADING HERE",
                message=" DESCRIPTION HERE"
            )

    def update_time(self, dt):
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
    
    def start(self):
        if self.running:
            self.running = False
        else:
            self.running = True
    def reset(self):
        self.sec = 0
        self.minute = 0
        self.hour = 0
        self.timer = '00:00:00'
        self.running = False

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
