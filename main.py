from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ObjectProperty
from kivy.animation import Animation
import math

class ClockCircle(FloatLayout):
    ball = ObjectProperty(None)
    
    def start(self):
        # Анимация перемещения шарика по кругу за заданное время (например, 5 секунд)
        duration = 5  # задайте время выполнения анимации в секундах
        animation = Animation(current_angle= - math.pi / 2 + 2 * math.pi, duration=duration, t='linear')
        
        # Запускаем анимацию с начального угла 0 до угла 2π
        animation.bind(on_progress=self.update_ball_position)
        animation.start(self.ball)

    def update_ball_position(self, animation, widget, progression):
        # Обновляем положение шарика на основе текущего угла
        self.ball.x = self.center_x + math.cos(self.ball.current_angle) * self.ball.radius - self.ball.width / 2
        self.ball.y = self.center_y + math.sin(self.ball.current_angle) * self.ball.radius - self.ball.height / 2

class Ball(Widget):
    current_angle = NumericProperty(math.pi/2)  # Начальный угол
    radius = NumericProperty(130)  # Радиус движения

class SmartTimerApp(App):
    def build(self):
        return ClockCircle()

if __name__ == '__main__':
    SmartTimerApp().run()

