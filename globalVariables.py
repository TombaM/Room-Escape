import pygame
from loadImage import LoadImage

rooms = []
invBar = []
index = 0

_opacity = 30

flags = {'picture' : False,
         'paper' : False,
         'message' : False,
         'invertory' : False,
         'pictureSafe' : False}

items = {}

(width, height) = (1200, 700)
window = pygame.display.set_mode((width, height))

leftArrow = LoadImage("Images/left_arrow.png", [60, 350], 100, 100)
rightArrow = LoadImage("Images/right_arrow.png", [1140, 350], 100, 100)
close = LoadImage("Images/close.png", [1150, 50], 50, 50)
invertory = LoadImage("Images/icon-invertory.png", [30, 670], 40, 50)
# paper = LoadImage("Images/paper.png", [360, 580], 25, 25)
