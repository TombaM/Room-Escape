import pygame
from loadImage import LoadImage

rooms = []
invBar = []
index = 0
#index of item to be stored in invertory bar
invIndex = 0
invertoryItems = []

_opacity = 30
opacity_paper = 255

flags = {'picture' : False,
         'paper' : True,
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
paper = LoadImage("Images/paper.png", [1800, 645], 75, 75)
candle = LoadImage("Images/candle.png", [1800, 645], 75, 75)
#100, 290, 480, 670, 860
