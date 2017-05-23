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
opacity_hammer = 255
opacity_lemon = 255
lemon_ind = 0
opacity_picture = 255
opacity_rotated = 0
dragging = False
safe_visible = False
safe_ind = 0

flags = {'picture' : False,
         'paper' : True,
         'message' : False,
         'invertory' : False,
         'pictureSafe' : False,
         'hammer' : True,
         'fridge' : False,
         'lemon' : False,
         'safe' : False}

items = {}

(width, height) = (1200, 700)
window = pygame.display.set_mode((width, height))

leftArrow = LoadImage("Images/left_arrow.png", [60, 350], 100, 100, 0)
rightArrow = LoadImage("Images/right_arrow.png", [1140, 350], 100, 100, 0)
close = LoadImage("Images/close.png", [1150, 50], 50, 50, 0)
invertory = LoadImage("Images/icon-invertory.png", [30, 670], 40, 50, 0)
paper = LoadImage("Images/paper.png", [1800, 645], 75, 75, 0)
candle = LoadImage("Images/candle.png", [1800, 645], 75, 75, 0)
hammer = LoadImage("Images/hammer.png", [1800, 645], 75, 75, 0)
lemon_inv = LoadImage("Images/lemon.png", [1800, 645], 75, 75, 0)
lemon = LoadImage("Images/lemon.png", [705, 420], 80, 70, 0)
rotated = LoadImage("Images/pictureSafe.png", [1005, 515], 250, 175, -40)
#100, 290, 480, 670, 860
