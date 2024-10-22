import json


class TimePoint:
    """Класс для управления временными точками"""
    def __init__(self):
        with open('modes.json', 'r') as file:
            data = json.load(file)
        modes = data['modes'] # Список режимов
        current_mode = modes[data['last_mode']] # Текущий режим
        times = current_mode['times'] # Список временных точек
    
    def get_time_points(self, id):
        """Возвращает список временных точек по id режима"""
        