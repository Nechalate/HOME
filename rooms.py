import random

# Класс комнаты [ включая переменные для спавна призрачной температуры, шкатулки ]
class room():
    def __init__(self):
        self.room_choice = 1
        self.choose_back = 0
        self.choose_next = 0
        self.bg_Count = 0
        self.burn = 0
        self.last_room = 0
        self.ghost_temp = random.randint(0, 1)
        self.box = random.randint(4, 6)
        self.handss = random.randint(4, 6)
        self.spawn = random.randint(200, 600)

# Счетчик явлений
class evidencce():
    def __init__(self):
        self.radInfo = False
        self.handInfo = False
        self.camInfo = False
