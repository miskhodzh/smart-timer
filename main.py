from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        # Изначально фон белый
        Window.clearcolor = (1, 1, 1, 1)

        # Основной контейнер - вертикальная компоновка
        self.layout = BoxLayout(orientation='vertical', padding=20)

        # Текст "Привет, меня зовут Осман!"
        self.label = Label(text="Привет, меня зовут Осман!", font_size='24sp', color=(0, 0, 0, 1))
        self.layout.add_widget(self.label)

        # Кнопка "Нажми на меня!!!"
        self.button = Button(text="Нажми на меня!!!", font_size='24sp', size_hint=(1, 0.2))
        self.button.bind(on_press=self.change_color)  # Привязываем обработчик событий
        self.layout.add_widget(self.button)

        return self.layout

    def change_color(self, instance):
        # Меняем цвет фона и текста при нажатии
        if Window.clearcolor == [1, 1, 1, 1]:  # Если фон белый
            Window.clearcolor = (0, 0, 0, 1)  # Меняем на черный
            self.label.color = (1, 1, 1, 1)   # Текст белый
        else:
            Window.clearcolor = (1, 1, 1, 1)  # Меняем на белый
            self.label.color = (0, 0, 0, 1)   # Текст черный


if __name__ == "__main__":
    MyApp().run()
