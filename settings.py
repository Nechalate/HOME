import pygame
pygame.init()

display_width = int(800) # выбор разрешения экрана
display_height = int(500)
# Выставляем разрешение
display = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)# установка разрешения экрана
pygame.display.set_caption("Don't' forget to come home") # установка названия окна

clock = pygame.time.Clock() # отслеживанеи времени, фреймрейт