from settings import display
from sounds import click_sound
import pygame

# Класс кнопки
class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.active_color = (255, 0, 0)
        self.inactive_color = (128, 0, 0)
    # Метод рисовки кнопки
    def Draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_color, (x, y, self.width, self.height))
            if click[0] == 1 and action is not None:
                pygame.mixer.Sound.play(click_sound)
                if action == quit:
                    pygame.quit()
                    quit()
                action()
                pygame.time.delay(200)
        else:
            pygame.draw.rect(display, self.inactive_color, (x, y, self.width, self.height))
        print_text(message=message, x=x + 10, y=y + 10, font_size=font_size)

# Функция печати на экран
def print_text(message, x, y, font_color = (0, 0, 0), font_type = 'pixel.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))