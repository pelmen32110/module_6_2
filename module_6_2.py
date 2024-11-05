class Vehicle:
    __color_variants = ['red', 'blue', 'green', 'black', 'white']

    def __init__(self,owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color


    def get_model(self):
        return print(f'Модель {self._Vehicle__model}')

    def get_horsepower(self):
        return print(f'Мощность двигателя {self._Vehicle__engine_power}')

    def get_color(self):
        return print(f'Цвет {self._Vehicle__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец {self.owner}')

    def set_color(self,new_color):
        if new_color.lower() in self._Vehicle__color_variants:
            self._Vehicle__color = new_color
        else:
            print('Нельзя сменить цвет на ', new_color)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()