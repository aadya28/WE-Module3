import pygame

import ui

SYSTEM_SCREEN_WIDTH, SYSTEM_SCREEN_HEIGHT = ui.get_screen_size()
SCREEN_W = SYSTEM_SCREEN_WIDTH * 0.8
SCREEN_H = SYSTEM_SCREEN_HEIGHT * 0.8

# Fonts
FONT_SMALL = pygame.font.Font(None, 35)
FONT_MEDIUM = pygame.font.Font(None, 45)
FONT_LARGE = pygame.font.Font(None, 55)

# Colours
GREEN = (0, 153, 90)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (96, 96, 96)
GOLDEN = (218, 165, 32)
