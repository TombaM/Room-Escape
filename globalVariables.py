import pygame
from arrow import Arrow
from close import Close

rooms = []
index = 0

_opacity = 30
flag = False

(width, height) = (1200, 700)
window = pygame.display.set_mode((width, height))


leftArrow = Arrow("Images/left_arrow.png", [60, 350])
rightArrow = Arrow("Images/right_arrow.png", [1140, 350])
close = Close("Images/close.png", [1150, 50])
