from images import *
from settings import *
from sounds import *
from rooms import *
from buttons import *
import pygame
import random
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
# Класс животного
class animal(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.walkCount = 0
        self.left = False
        self.right = False
        self.last_anim = 0
# Отрисовка
    def draw(self, display):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0
        if self.left:
            display.blit(cat_walkL[self.walkCount//5], (self.x, self.y))
            self.walkCount += 1
            self.last_anim = 1
        elif self.right:
            display.blit(cat_walk[self.walkCount//5], (self.x, self.y))
            self.walkCount += 1
            self.last_anim = 0
        if hero.hide == True:
            if self.last_anim == 1:
                display.blit(cathideL, (self.x, self.y))
                self.left = False
                self.right = False
            else:
                display.blit(cathide, (self.x, self.y))
                self.left = False
                self.right = False
        elif self.x > hero.x_position and self.x > hero.x_position + 100 and hero.hide == False:
            self.left = True
            self.right = False
            self.x -= self.speed
        elif self.x < hero.x_position and self.x < hero.x_position - 100 and hero.hide == False:
            self.left = False
            self.right = True
            self.x += self.speed
        else:
            if self.last_anim == 1:
                display.blit(cat_standL, (self.x, self.y))
                self.left = False
                self.right = False
            else:
                display.blit(cat_stand, (self.x, self.y))
                self.left = False
                self.right = False


# Класс игрока
class player(object):
    def __init__(self, x_position, y_position, width, height):
        self.x_position = x_position # позиция игрока на системе координат
        self.y_position = y_position
        self.width = width # размеры персонажа
        self.height = height
        self.speed = 3 # скорость персонажа
        self.left = False # переменные проверяющие идет ли персонаж вправо или влево
        self.right = False
        self.walkCount = 0 # счетчик для анимации ходьбы
        self.shift = False # проверка бежил ли персонаж в данный момент
        self.ctrl = False
        self.hide = False
        self.last_anim = 0
        self.mind = 0
        self.inventory_choose = 0
        self.inventory_last_choose = 0
        self.flashlight = False
        self.infraredOn = False
        self.set = False
        self.cam = False
        self.rad = False
        self.win = False
        self.cam_point = 1

    def draw(self, display):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0
        if self.left:
            display.blit(walkLeft[self.walkCount//5], (self.x_position, self.y_position))
            self.walkCount += 1
            self.last_anim = 1
        elif self.right:
            display.blit(walkRight[self.walkCount//5], (self.x_position, self.y_position))
            self.walkCount += 1
            self.last_anim = 0
        elif self.shift:
            self.speed += 2
        elif self.ctrl:
            if self.last_anim == 1:
                display.blit(SitL, (self.x_position, self.y_position))
            else:
                display.blit(Sit, (self.x_position, self.y_position))
        else:
            if self.last_anim == 1:
                display.blit(StandL, (self.x_position, self.y_position))
            else:
                display.blit(Stand, (self.x_position, self.y_position))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause()
        clock.tick(40)
        keys = pygame.key.get_pressed()
        # Управление игроком
        if keys[pygame.K_a] and self.x_position > 1:
            self.x_position -= self.speed
            self.left = True
            self.right = False
            self.hide = False
            self.flashlight = False
            self.infraredOn = False
            if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
                self.x_position -= self.speed
                self.left = True
                self.right = False
                self.shift = True
        elif keys[pygame.K_d] and self.x_position < 700:
            self.x_position += self.speed
            self.left = False
            self.right = True
            self.hide = False
            self.flashlight = False
            self.infraredOn = False
            if keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
                self.x_position += self.speed
                self.left = False
                self.right = True
                self.shift = True
        # Подобие инвентаря
        elif keys[pygame.K_f] and self.inventory_last_choose == 0:
            self.flashlight = True
        elif keys[pygame.K_f] and self.inventory_last_choose == 2:
            self.infraredOn = True
        elif keys[pygame.K_f] and self.inventory_last_choose == 3:
            self.cam = True
        elif keys[pygame.K_f] and self.inventory_last_choose == 4:
            self.rad = True
        elif keys[pygame.K_z] and self.cam == True and self.inventory_last_choose == 3 and self.set == False:
            self.cam = False
        elif keys[pygame.K_DOWN] and self.cam == True and self.cam_point == 1:
            self.set = True
            self.cam_point = 0
            room_status.last_room = room_status.room_choice
        elif keys[pygame.K_s]:
            self.left = False
            self.right = False
            self.shift = False
            self.ctrl = True
            self.hide = True
            self.flashlight = False
            self.infraredOn = False
            self.rad = False
        else:
            self.flashlight = False
            self.infraredOn = False
            self.rad = False
            self.right = False
            self.left = False
            self.shift = False
            self.ctrl = False
            self.hide = False
            self.walkCount = 0
        # Проверки для теста
        '''
        if self.flashlight == True:
            print_text('Flashlight on!', 600, 10, (255, 255, 255), font_size=30)
        elif self.flashlight == False:
            print_text('Flashlight off!', 600, 10, (255, 255, 255), font_size=30)
        if self.infraredOn == True:
            print_text('Infrared on!', 600, 30, (255, 255, 255), font_size=30)
        elif self.infraredOn == False:
            print_text('Infrared off!', 600, 30, (255, 255, 255), font_size=30)
        if self.cam == True:
            print_text('Cam on!', 600, 50, (255, 255, 255), font_size=30)
        elif self.cam == False:
            print_text('Cam off!', 600, 50, (255, 255, 255), font_size=30)
        if self.rad == True:
            print_text('Rad on!', 600, 70, (255, 255, 255), font_size=30)
        elif self.rad == False:
            print_text('Rad off!', 600, 70, (255, 255, 255), font_size=30)
        '''
        if keys[pygame.K_i]:
            room_status.room_choice = 6
        # Выбор предмета
        if keys[pygame.K_0]:
            self.inventory_last_choose = 0
        elif keys[pygame.K_1]:
            self.inventory_last_choose = 1
        elif keys[pygame.K_2]:
            self.inventory_last_choose = 2
        elif keys[pygame.K_3]:
            self.inventory_last_choose = 3
        elif keys[pygame.K_4]:
            self.inventory_last_choose = 4
        else:
            pass

# Класс врага
class enemy(object):
    def __init__(self, x_enemy, y_enemy):
        self.x_enemy = x_enemy
        self.y_enemy = y_enemy
        self.x_enemy_kill = 0
        self.y_enemy_kill = 360
        self.x_shape = 300
        self.y_shape = 360
        self.rage = 1
        self.speed = 2
        self.walkCountEnemy = 0
        self.attack_token = True
        self.attack = True
        self.right_enemy = False
        self.left_enemy = False
        self.mind_damage = 1
        self.act = False
        self.chance = 0
        self.find = False
        self.vision = False
        self.time = 0
        self.timer = 0
        self.stay = 0
        self.music_timer = 2000

    # === Враги ===
    # Появляется в [ 0 этаж, генераторная ]
    def jumpscare(self, display):
        self.chance = random.randint(0, 100)
        if self.chance == 100 and self.find == False:
            self.find = True
        elif self.find == True:
            if self.walkCountEnemy + 1 >= 30:
                self.walkCountEnemy = 0
            elif self.attack == True:
                display.blit(StandJumpScare, (self.x_enemy, self.y_enemy))
                self.walkCountEnemy += 1
                self.x_enemy -= self.speed + 28
                heart_attack.play()
                self.act = True
                if self.x_enemy < 0:
                    self.attack = False
                    self.attack_token = False
                if (self.x_enemy + 30 > hero.x_position and self.x_enemy - 30 < hero.x_position and self.attack_token == True and self.attack == True):
                    if hero.hide == True:
                        pass
                    else:
                        mind_attack()
                        self.attack = False
                        self.attack_token = False
                        self.find = False
    # Появляется в [ 0 этаж, 1 комната ]
    def kill_attack(self, display):
        self.chance = random.randint(0, 100)
        if self.chance == 100 and self.find == False:
            self.find = True
        elif self.find == True:
            if self.attack == True:
                if self.walkCountEnemy + 1 >= 30:
                    self.walkCountEnemy = 0
                if self.left_enemy:
                    display.blit(walkLeftObsession[self.walkCountEnemy//5], (self.x_enemy, self.y_enemy))
                    self.walkCountEnemy += 1
                elif self.right_enemy:
                    display.blit(walkRightObsession[self.walkCountEnemy//5], (self.x_enemy, self.y_enemy))
                    self.walkCountEnemy += 1
                if self.x_enemy < hero.x_position:
                    self.left_enemy = False
                    self.right_enemy = True
                    self.x_enemy += self.speed
                elif self.x_enemy > hero.x_position:
                    self.right_enemy = False
                    self.left_enemy = True
                    self.x_enemy -= self.speed
                if self.x_enemy + 30 > hero.x_position and self.x_enemy - 30 < hero.x_position and self.attack_token == True and self.attack == True:
                    mind_attack()
                    self.attack = False
                    self.attack_token = False
                    self.find = False
                    self.act = True
                elif hero.flashlight == True:
                    if self.x_enemy > hero.x_position and self.x_enemy - 110 < hero.x_position and hero.last_anim == 0:
                        self.attack = False
                        self.attack_token = False
                        self.find = False
                        self.act = True
                    elif self.x_enemy < hero.x_position and self.x_enemy + 110 > hero.x_position and hero.last_anim == 1:
                        self.attack = False
                        self.attack_token = False
                        self.find = False
                        self.act = True
    # Появляется в [ 0 этаж, комната с камерами ]
    def shape(self, display):
        self.chance = random.randint(0, 100)
        if self.chance == 100 and self.find == False:
            self.find = True
        elif self.find == True:
            if self.attack == True:
                if self.walkCountEnemy + 1 >= 30:
                    self.walkCountEnemy = 0
                if self.left_enemy:
                    display.blit(walkLeftShape[self.walkCountEnemy // 5], (self.x_enemy, self.y_enemy))
                    self.walkCountEnemy += 1
                elif self.right_enemy:
                    display.blit(walkRightShape[self.walkCountEnemy // 5], (self.x_enemy, self.y_enemy))
                    self.walkCountEnemy += 1
                else:
                    display.blit(StandShape, (self.x_enemy, self.y_enemy))
                if self.x_enemy < hero.x_position:
                    self.left_enemy = False
                    self.right_enemy = True
                    self.x_enemy += self.speed
                elif self.x_enemy > hero.x_position:
                    self.right_enemy = False
                    self.left_enemy = True
                    self.x_enemy -= self.speed
                if self.x_enemy + 60 > hero.x_position and self.x_enemy - 60 < hero.x_position and self.attack_token == True and self.attack == True:
                    self.attack = False
                    self.attack_token = False
                    self.find = False
                    self.act = True
                    if hero.flashlight == True:
                        game_over()
                if hero.flashlight == True:
                    self.speed += 10
                else:
                    self.speed = 2
    # Появляется везде при свете кроме [ начальная локация, трейлер ]
    def eyeless(self, display):
        self.chance = random.randint(0, 100)
        if self.chance == 100 and self.find == False and hero.x_position > 200 and hero.x_position < 400:
            self.find = True
        elif self.find == True and light_status.light == True:
            if self.attack == True:
                if self.left_enemy:
                    display.blit(eyelessL,(self.x_enemy, self.y_enemy))
                elif self.right_enemy:
                    display.blit(eyeless,(self.x_enemy, self.y_enemy))
                if self.x_enemy < hero.x_position:
                    self.left_enemy = False
                    self.right_enemy = True
                elif self.x_enemy > hero.x_position:
                    self.right_enemy = False
                    self.left_enemy = True
                if hero.last_anim == 1 and self.x_enemy < hero.x_position:
                    self.vision = True
                elif hero.last_anim == 0 and self.x_enemy < hero.x_position:
                    self.x_enemy += 8
                    self.vision = False
                    self.timer = 0
                elif hero.last_anim == 1 and self.x_enemy > hero.x_position:
                    self.x_enemy -= 8
                    self.vision = False
                    self.timer = 0
                elif hero.last_anim == 0 and self.x_enemy > hero.x_position:
                    self.vision = True
                if self.x_enemy + 30 > hero.x_position and self.x_enemy - 30 < hero.x_position and self.attack_token == True and self.attack == True:
                    self.attack = False
                    self.attack_token = False
                    mind_attack()
                    self.timer = 0
                    self.vision = False
                    self.find = False
                if self.vision == True:
                    self.timer += 1
                    if self.timer >= 150:
                        self.attack = False
                        self.attack_token = False
                        self.timer = 0
                        self.vision = False
                        self.find = False
                if light_status.light == False:
                    self.attack = False
                    self.attack_token = False
                    self.find = False
    # Появляется везде где есть свет, кроме [ начальная локация, трейлер ]
    def stayalone(self, display):
        self.chance = random.randint(0, 100)
        if self.chance == 100 and self.find == False:
            self.find = True
        elif self.find == True and light_status.light == True:
            if self.attack == True:
                if self.walkCountEnemy + 1 >= 30:
                    self.walkCountEnemy = 0
                if self.left_enemy:
                    display.blit(YelL[self.walkCountEnemy // 5], (self.x_enemy, self.y_enemy))
                    self.walkCountEnemy += 1
                elif self.right_enemy:
                    display.blit(YelR[self.walkCountEnemy // 5], (self.x_enemy, self.y_enemy))
                    self.walkCountEnemy += 1
                if self.x_enemy < hero.x_position:
                    self.left_enemy = False
                    self.right_enemy = True
                elif self.x_enemy > hero.x_position:
                    self.right_enemy = False
                    self.left_enemy = True
                keys = pygame.key.get_pressed()
                if keys[pygame.K_d] or keys[pygame.K_a]:
                    self.timer += 1
                    self.stay = 0
                    if self.timer >= 50:
                        self.timer = 0
                        self.stay = 0
                        mind_attack()
                self.stay += 1
                if self.stay >= 150:
                    self.attack = False
                    self.attack_token = False
                    self.find = False
                    self.timer = 0
                    self.stay = 0
                if light_status.light == False:
                    self.attack = False
                    self.attack_token = False
                    self.find = False
    # Появляется везде, требуется зарядка, шкатулка появляется на 0 этаже в случайной комнате
    def musicbox(self, display):
        if hero.win == False:
            self.music_timer -= 1
        else:
            self.music_timer -= 3
        if self.music_timer <= 0:
            display.blit(creepy, (self.x_enemy, self.y_enemy))
            if self.x_enemy < hero.x_position:
                if hero.win == False:
                    self.x_enemy += 8
                else:
                    self.x_enemy += 16
            elif self.x_enemy > hero.x_position:
                if hero.win == False:
                    self.x_enemy -= 8
                else:
                    self.x_enemy -= 16
            if self.x_enemy + 30 > hero.x_position and self.x_enemy - 30 < hero.x_position:
                mind_attack()
        else:
            pass

# Класс света
class light():
    def __init__(self):
        self.power_off_delay = True
        self.light = True
        self.light_check = 5001
        self.token = 1
    # Метод выключения света
    def light_off(self):
        if self.light == True:
            if (self.light == True and self.power_off_delay == True):
                self.light_check = random.randint(0, 1000)
                if self.light_check == 1000:
                    self.light = False
                    self.light_check = 5001
                    power_off.play()

# === Предметы , спрайты , их местоположение и анимация ===
# Фонарь [ предмет ]
def flash():
    if hero.hide == True:
        if hero.last_anim == 1:
            display.blit(flashlightL, (hero.x_position + 26, hero.y_position + 78))
        else:
            display.blit(flashlight, (hero.x_position + 56, hero.y_position + 78))
    elif hero.flashlight == True:
        if hero.last_anim == 1:
            display.blit(flashlight_onL, (hero.x_position - 50, hero.y_position + 71))
        else:
            display.blit(flashlight_on, (hero.x_position + 56, hero.y_position + 67))
    else:
        if hero.last_anim == 1:
            display.blit(flashlightL, (hero.x_position + 24, hero.y_position + 62))
        else:
            display.blit(flashlight, (hero.x_position + 56, hero.y_position + 62))

# Инфракрасный фонарь [ предмет ]
def infraredd():
    if hero.hide == True:
        if hero.last_anim == 1:
            display.blit(infraredL, (hero.x_position + 26, hero.y_position + 78))
        else:
            display.blit(infrared, (hero.x_position + 56, hero.y_position + 78))
    elif hero.infraredOn == True:
        if hero.last_anim == 1:
            display.blit(infrared_onL, (hero.x_position + 20, hero.y_position + 70))
        else:
            display.blit(infrared_on, (hero.x_position + 56, hero.y_position + 67))
    else:
        if hero.last_anim == 1:
            display.blit(infraredL, (hero.x_position + 24, hero.y_position + 62))
        else:
            display.blit(infrared, (hero.x_position + 56, hero.y_position + 62))

# Камера [ предмет ]
def cameraItem():
    if hero.hide == True:
        if hero.last_anim == 1:
            display.blit(camera_off, (hero.x_position + 26, hero.y_position + 78))
        else:
            display.blit(camera_off, (hero.x_position + 56, hero.y_position + 78))
    elif hero.cam == True:
        if hero.last_anim == 1:
            display.blit(camera_on, (hero.x_position + 26, hero.y_position + 68))
        else:
            display.blit(camera_on, (hero.x_position + 56, hero.y_position + 67))
    else:
        if hero.last_anim == 1:
            display.blit(camera_off, (hero.x_position + 24, hero.y_position + 62))
        else:
            display.blit(camera_off, (hero.x_position + 56, hero.y_position + 62))

# Радио [ предмет ]
def radio():
    if hero.hide == True:
        if hero.last_anim == 1:
            display.blit(rad, (hero.x_position + 26, hero.y_position + 78))
        else:
            display.blit(rad, (hero.x_position + 56, hero.y_position + 78))
    elif hero.rad == True:
        if hero.last_anim == 1:
            display.blit(radon, (hero.x_position + 24, hero.y_position + 62))
        else:
            display.blit(radon, (hero.x_position + 56, hero.y_position + 62))
    else:
        if hero.last_anim == 1:
            display.blit(rad, (hero.x_position + 24, hero.y_position + 62))
        else:
            display.blit(rad, (hero.x_position + 56, hero.y_position + 62))

# Термометр [ предмет ]
def tempitem():
    if hero.hide == True:
        if hero.last_anim == 1:
            display.blit(tempLimg, (hero.x_position + 16, hero.y_position + 78))
        else:
            display.blit(tempimg, (hero.x_position + 66, hero.y_position + 78))
    else:
        if hero.last_anim == 1:
            display.blit(tempLimg, (hero.x_position + 16, hero.y_position + 62))
        else:
            display.blit(tempimg, (hero.x_position + 66, hero.y_position + 62))

# Интерфейс [ включает показатели: время наблюдения, бездействия, шкатулки во время фазы атаки ]
def mind_bar_interface():
    if hero.mind > 3:
        return game_over()
    else:
        display.blit(mind_bar[hero.mind], (10, 30))
    '''
    print_text('mind', 50, 5, (255, 255, 255))
    print_text('Time, {}, Vision {}'.format(eyeblind.timer, eyeblind.vision), 150, 50, (255, 255, 255))
    print_text('Stay, {}, Sound {}'.format(stay.stay, stay.timer), 150, 100, (255, 255, 255))
    '''
    print_text('Music {}'.format(music.music_timer), 150, 30, (255, 255, 255))
    if evi.radInfo == True:
        print_text('Rad Completed'.format(music.music_timer), 150, 170, (255, 255, 255))
    if evi.handInfo == True:
        print_text('Hand Completed'.format(music.music_timer), 150, 190, (255, 255, 255))
    if evi.camInfo == True:
        print_text('Cam Completed'.format(music.music_timer), 150, 210, (255, 255, 255))

# Термометр [ показатели ]
def temp():
    global ghost_room_choice
    if room_status.room_choice == ghost_room_choice:
        temperature = random.randint(1, 10)
    else:
        temperature = random.randint(11, 17)
    print_text('Temperature, {}'.format(temperature), 150, 10, (255, 255, 255))

show = True

# Сцена для наблюдения в камеры
def spirit():
    global ghost_room_choice
    button_exit = Button(75, 40)
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if room_status.last_room == ghost_room_choice:
            if room_status.bg_Count + 1 >= 30:
                room_status.bg_Count = 0
            else:
                display.blit(spirit_on[room_status.bg_Count//5], (0, 0))
                room_status.bg_Count += 1
            evi.camInfo = True
        else:
            display.blit(floor_0_room_1, (0, 0))
        button_exit.Draw(330, 350, 'EXIT', game_run)
        pygame.time.delay(100)
        pygame.display.update()

# Функция для перезарядки шкатулки
def refmus():
    music.music_timer = 2500
    music.x_enemy = 650

# Кнопка рестарта после проигрыша
def restart():
    global show
    room_status.room_choice = 1
    music.music_timer = 1000
    show = False

# Функция прогрыша при нулевом количестве рассудка
def game_over():
    global show
    show = True
    button_exit = Button(75, 40)
    button_restart = Button(75, 40)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill((0, 0, 0))
        print_text('GAME OVER', 220, 100, (255, 0, 0), font_size= 150)
        button_restart.Draw(470, 450, 'RESTART', restart)
        button_exit.Draw(330, 450, 'EXIT', quit)
        pygame.display.update()
        pygame.time.delay(80)

def winn():
    global show
    show = True
    button_exit = Button(75, 40)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill((0, 0, 0))
        print_text('YOU WIN', 220, 100, (0, 255, 0), font_size=150)
        button_exit.Draw(330, 450, 'EXIT', quit)
        pygame.display.update()
        pygame.time.delay(80)

# Функция нанесения урона
def mind_attack():
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(scream, (0, 0))
        pygame.display.update()
        pygame.time.delay(80)
        hero.mind += obsession.mind_damage
        show = False

# Функция паузы
def pause():
    paused = True
    pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('> Press enter to continue.', hero.x_position, 300)
        print_text('> Press B go to menu.', hero.x_position, 320)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False
        if keys[pygame.K_b]:
            paused = False
            show_menu()
        pygame.display.update()
        clock.tick(15)
    pygame.mixer.music.unpause()

# Начальная заставка
def disclaimer():
    global ddd
    button_next = Button(80, 40)
    disc = True
    while disc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill((0, 0, 0))
        print_text('Игра содержит скримеры и резкие звуки.', 230, 100, (255, 255, 255))
        button_next.Draw(350, 150, 'дальше', training)
        pygame.display.update()
        pygame.time.delay(10)

# Обучение
def training():
    button_next = Button(80, 40)
    disc = True
    while disc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill((0, 0, 0))
        print_text('Управление:.', 230, 100, (255, 255, 255))
        print_text('ESC - выйти в меню.', 230, 130, (255, 255, 255))
        print_text('AD - передвижение.', 230, 160, (255, 255, 255))
        print_text('SHIFT - бег.', 230, 190, (255, 255, 255))
        print_text('F - фонарь.', 230, 220, (255, 255, 255))
        print_text('S - присесть.', 230, 250, (255, 255, 255))
        print_text('Взаимодействие с обьектами нажатие левой кнопкой мыши.', 230, 280, (255, 255, 255))
        button_next.Draw(350, 450, 'дальше', show_menu)
        pygame.display.update()
        pygame.time.delay(10)

# Начальное меню
def show_menu():
    pygame.mixer.music.load('Audio\main_menu.mp3')
    pygame.mixer.music.play(-1)
    button_start = Button(75, 40)
    button_settings = Button(75, 40)
    button_exit = Button(75, 40)
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if room_status.bg_Count + 1 >= 30:
            room_status.bg_Count = 0
        else:
            display.blit(main_menu_anim[room_status.bg_Count//5], (0, 0))
            room_status.bg_Count += 1
        button_start.Draw(350, 250, 'start', game_run)
        button_settings.Draw(350, 300, 'settings', mind_attack)
        button_exit.Draw(350, 350, 'exit', quit)
        pygame.display.update()
        pygame.time.delay(10)

# Перезарядка между атаками мобов [ переделать, сделать методом для сокращения кода ]
def attack_delays():
    if killer.attack == False and killer.attack_token == False:
        killer.time += 1
        if killer.time == 500:
            killer.attack = True
            killer.attack_token = True
            killer.time = 0
            killer.x_enemy = random.randint(250, 550)
    elif shapeless.attack == False and shapeless.attack_token == False:
        shapeless.time += 1
        if shapeless.time == 500:
            shapeless.attack = True
            shapeless.attack_token = True
            shapeless.time = 0
            shapeless.x_enemy = 100
    elif obsession.attack == False and obsession.attack_token == False:
        obsession.time += 1
        if obsession.time == 500:
            obsession.attack = True
            obsession.attack_token = True
            obsession.time = 0
            obsession.x_enemy = 600
    elif eyeblind.attack == False and eyeblind.attack_token == False:
        eyeblind.time += 1
        if eyeblind.time == 500:
            eyeblind.attack = True
            eyeblind.attack_token = True
            eyeblind.time = 0
            spawn = random.randint(0, 10)
            if spawn <= 5:
                eyeblind.x_enemy = 50
            elif spawn >= 6:
                eyeblind.x_enemy = 650
    elif stay.attack == False and stay.attack_token == False:
        stay.time += 1
        if stay.time == 500:
            stay.attack = True
            stay.attack_token = True
            stay.time = 0
            stay.x_enemy = random.randint(50, 650)

# Куча функций для перехода между комнатами [ заменить на более удобный вариант ]
def house_room_floor_0_camera():
    room_status.choose_back = 1
    room_status.choose_next = 1
    room_status.room_choice = 6

def house_room_floor_0_room_1():
    room_status.choose_back = 1
    room_status.room_choice = 5
    killer.x_enemy = random.randint(250, 550)

def house_room_floor_1():
    room_status.choose_next = 1
    room_status.room_choice = 3

def house_room_floor_0():
    room_status.choose_back = 1
    room_status.room_choice = 4

def tombstone_scene():
    room_status.choose_next = 1

def forest_rain_scene():
    room_status.choose_next = 1
    room_status.room_choice = 2

def burn_tombstone_scene():
    room_status.burn = 1

# Функция включение генератора на карте
def power_on():
    light_status.token = 1
    light_status.light = True
    light_status.power_off_delay = True
    obsession.attack = True
    shapeless.attack = True
    killer.attack = True
    obsession.attack_token = True
    shapeless.attack_token = True
    eyeblind.attack_token = True
    killer.attack_token = True
    stay.attack_token = True
    obsession.x_enemy = 600
    shapeless.x_enemy = 100

def takeback():
    hero.cam_point = 1

# Функция на проверку призрачной комнаты
ghost_room_choice = random.randint(4, 6)
def ghost_room():
    global ghost_room_choice, ghost_evidence
    if room_status.room_choice == ghost_room_choice:
        #print_text('Ghost room!', 450, 20)
        ghost_evidence = True
    else:
        #print_text('Ghost room undetected!', 400, 20)
        ghost_evidence = False

# Игровой цикл
def game_run():
    global run, ghost_room_choice
    run = True
    pygame.mixer.music.load('Audio\ground_house.mp3')
    pygame.mixer.music.play(-1)
    room_status.choose_next = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # стартовая точка [ магазин ]
        if room_status.room_choice == 1:
            button_next = Button(75, 40)
            if room_status.bg_Count + 1 >= 30:
                room_status.bg_Count = 0
            else:
                display.blit(sleep_forest[room_status.bg_Count // 5], (0, 0))
                room_status.bg_Count += 1
            if (hero.x_position > 650):
                button_next.Draw(350, 450, 'дальше', forest_rain_scene)
            if room_status.choose_next == 1:
                hero.x_position = 20
                hero.y_position = 360
                cat.x = 20
                room_status.choose_next = 0
        # начальная сцена [ появление на карте ]
        elif room_status.room_choice == 2:
            button_next = Button(75, 40)
            if room_status.bg_Count + 1 >= 30:
                room_status.bg_Count = 0
            else:
                display.blit(forest_rain[room_status.bg_Count // 5], (0, 0))
                room_status.bg_Count += 1
            if (hero.x_position > 650):
                button_next.Draw(350, 450, 'дальше', house_room_floor_1)
            if room_status.choose_next == 1:
                hero.x_position = 20
                hero.y_position = 360
                cat.x = 20
                room_status.choose_next = 0
        # первая комната 1 этаж [ комната с лифтом ]
        elif room_status.room_choice == 3:
            button_next = Button(75, 40)
            if room_status.bg_Count + 1 >= 30:
                room_status.bg_Count = 0
            else:
                display.blit(house_rain_anim[room_status.bg_Count // 5], (0, 0))
                room_status.bg_Count += 1
            if (hero.x_position > 650):
                button_next.Draw(350, 450, 'дальше', house_room_floor_0)
            if room_status.choose_next == 1:
                hero.x_position = 20
                hero.y_position = 360
                cat.x = 20
                room_status.choose_next = 0
            elif room_status.choose_back == 1:
                hero.x_position = 680
                hero.y_position = 360
                cat.x = 680
                room_status.choose_back = 0
        # первая комната 0 этаж [ генераторная ]
        elif room_status.room_choice == 4:
            button_next = Button(75, 40)
            button_on = Button(95, 40)
            if light_status.light == True:
                display.blit(floor_0, (0, 0))
            elif light_status.light == False:
                display.blit(floor_0_lightoff, (0, 0))
                obsession.jumpscare(display)
            if (hero.x_position < 50 and light_status.light == True):
                button_next.Draw(350, 450, 'дальше', house_room_floor_0_room_1)
            if (hero.x_position > 450 and hero.x_position < 550 and light_status.light == False):
                button_on.Draw(350, 450, 'включить', power_on)
            if light_status.light == False and light_status.token == 1:
                hero.x_position = 20
                hero.y_position = 360
                cat.x = 20
                light_status.token -= 1
            if room_status.choose_back == 1:
                hero.x_position = 20
                hero.y_position = 360
                cat.x = 20
                room_status.choose_next = 0
        # вторая комната 0 этаж [ коридор ]
        elif room_status.room_choice == 5:
            button_next = Button(75, 40)
            button_back = Button(65, 40)
            light_status.light_off()
            if light_status.light == True:
                display.blit(floor_0_room_1, (0, 0))
            elif light_status.light == False:
                display.blit(floor_0_room_1_lightoff, (0, 0))
                killer.kill_attack(display)
            if light_status.light == True and hero.x_position < 50:
                button_next.Draw(350, 450, 'дальше', house_room_floor_0_camera)
            elif light_status.light == False and light_status.light_check == 5001 and hero.x_position > 650:
                button_back.Draw(350, 450, 'назад', house_room_floor_0)
            if room_status.choose_back == 1:
                hero.x_position = 680
                hero.y_position = 360
                cat.x = 680
                room_status.choose_back = 0
            elif room_status.choose_next == 1:
                hero.x_position = 20
                hero.y_position = 360
                cat.x = 20
                room_status.choose_next = 0
        # наблюдательная [ камеры ]
        elif room_status.room_choice == 6:
            button_next = Button(125, 40)
            button_on = Button(75, 40)
            light_status.light_off()
            if light_status.light == True:
                display.blit(floor_0_room_1_camera, (0, 0))
            elif light_status.light == False:
                display.blit(floor_0_room_1_camera_lightoff, (0, 0))
                shapeless.shape(display)
            if (hero.x_position > 100 and hero.x_position < 150 and light_status.light == True and hero.cam_point == 0):
                button_next.Draw(350, 450, 'просмотреть камеры', spirit)
            if (hero.x_position > 650):
                button_on.Draw(350, 450, 'назад', house_room_floor_0_room_1)
        if hero.set == True and hero.cam_point == 0:
            if room_status.last_room == room_status.room_choice:
                display.blit(camera_on, (600, 150))
        # Рисовка персонажа, перезарядка атак призраков
        attack_delays()
        hero.draw(display)
        # Спаун шкатулки
        if room_status.box == room_status.room_choice:
            button_ref = Button(75, 40)
            if music.music_timer >= 500:
                display.blit(music_box[0], (room_status.spawn, 460))
            else:
                display.blit(music_box[1], (room_status.spawn, 460))
            if room_status.spawn + 60 > hero.x_position and room_status.spawn - 60 < hero.x_position and music.music_timer <= 500:
                button_ref.Draw(350, 450, 'Перезарядить', refmus)
        # Взаимодействие с радио
        if hero.rad == True and ghost_room_choice == room_status.room_choice:
            if random.randint(0, 100) == 100 and light_status.light == False:
                pygame.mixer.Sound.play(voice)
                evi.radInfo = True
        # Взаимодействие с отпечатками
        if obsession.act == True and room_status.room_choice == room_status.handss:
            if hero.infraredOn == True and hero.x_position >= 650:
                display.blit(evidance, (750, 380))
                evi.handInfo = True
        # Выбор предмета
        if hero.inventory_last_choose == 0:
            flash()
        elif hero.inventory_last_choose == 1:
            tempitem()
            temp()
        elif hero.inventory_last_choose == 2:
            infraredd()
        elif hero.inventory_last_choose == 3 and hero.cam_point == 1:
            cameraItem()
        elif hero.inventory_last_choose == 4:
            radio()
        # Создаем останавливающего и безликого, запускаем таймер шкатулки
        music.musicbox(display)
        stay.stayalone(display)
        eyeblind.eyeless(display)
        # Выводим интерфейс, функцию призрачной комнаты
        mind_bar_interface()
        ghost_room()
        if hero.cam_point == 0 and room_status.last_room == room_status.room_choice:
            button_take = Button (75, 40)
            button_take.Draw(590, 190, "Take", takeback)
        # Предупреждение об эвакуации
        if evi.camInfo == True and evi.handInfo == True and evi.radInfo == True:
            print_text('Mission completed, escaped.', 550, 90, font_color=(255, 0, 0))
            hero.win = True
            if room_status.room_choice == 4 and hero.x_position > 650:
                button_win = Button(75, 40)
                button_win.Draw(400, 250, 'ESCAPE', winn)
        cat.draw(display)
        pygame.display.update()

# Задаем координаты спавна персонажа и его размеры
hero = player(-20, 360, 128, 128)
cat = animal(200, 420)
# Создаем врагов и определяем их местоположение
obsession = enemy(600, 360)
killer = enemy(300, 360)
shapeless = enemy(100, 360)
eyeblind = enemy(650, 360)
stay = enemy(350, 360)
music = enemy(650, 360)

evi = evidencce()
# Создаем обьекты свет и комната
light_status = light()
room_status = room()
# Начальные сцены, меню, игровой цикл
disclaimer()
training()
show_menu()
# Запускаем игровой цикл
while game_run():
    pass
pygame.quit()
quit()