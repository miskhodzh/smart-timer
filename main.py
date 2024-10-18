from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty


class MainWidget(BoxLayout):

    input_text = ObjectProperty(None)
    label_text = StringProperty("")

    def save_text_input(self):
        text = self.input_text.text
        with open("output.txt", 'w') as f:
            f.write(text)
    
    def show_text(self):
        with open("output.txt", "r") as f:
            self.label_text = f.read()

class TimerApp(App):
    def build(self):
        return MainWidget()

if __name__ == "__main__":
    TimerApp().run()
