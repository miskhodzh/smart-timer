from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock


class MainWidget(BoxLayout):

    timer = StringProperty("00:00:00")
    sec, minute, hour = 0, 0, 0

    sound = SoundLoader.load('1.mp3')

    running = False
    def check_points(self):
        if self.hour == 0 and self.minute == 0 and self.sec == 5:
            self.sound.play()

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


class TimerApp(App):
    def build(self):
        return MainWidget()
    
    def on_start(self):
        Clock.schedule_interval(self.root.update_time, 1)

if __name__ == "__main__":
    TimerApp().run()
