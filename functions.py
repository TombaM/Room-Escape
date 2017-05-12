import pygame
import copy
import globalVariables as gv
from loadImage import LoadImage

def blit_alpha(target,source,location):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x,-y))
    temp.blit(source, (0,0))
    temp.set_alpha(gv._opacity)
    target.blit(temp, location)

def opacity():
    if gv.leftArrow.rect.collidepoint(pygame.mouse.get_pos()):
        gv._opacity = 255
    elif gv.rightArrow.rect.collidepoint(pygame.mouse.get_pos()):
        gv._opacity = 255
    else:
        gv._opacity = 30
    if gv.flags['paper']==True:
        gv.opacity_paper=255
    else:
        gv.opacity_paper=0

def changeBackground(side):
    if side == "left":
        if gv.index == 0:
            gv.index = len(gv.rooms) - 1
        else:
            gv.index = gv.index - 1
    else:
        if gv.index == len(gv.rooms) - 1:
            gv.index = 0
        else:
            gv.index = gv.index + 1

def zoomImage(imageSource):
    # drawing of black screen on top of whole screen
    s = pygame.Surface((1200,700), pygame.SRCALPHA)
    s.fill((0,0,0,180))
    gv.window.blit(s, (0,0))

    pic = LoadImage(imageSource, [600, 350], 300, 150)
    pic.image = pygame.transform.scale(pic.image, (600, 500))
    pic.rect = pic.image.get_rect()
    pic.rect.center = (600, 350)
    gv.window.blit(pic.image, pic.rect)

    #drawing of 'x' sign which is used for closing the image
    gv.close.rect = gv.close.image.get_rect()
    gv.close.rect.center = pic.rect.topright
    gv.window.blit(gv.close.image, gv.close.rect)

def update():
    gv.window.blit(gv.rooms[gv.index].image, gv.rooms[gv.index].rect)
    gv.rooms[gv.index].drawRoom()
    
    # blitting arrows with opacity for every room
    blit_alpha(gv.window, gv.leftArrow.image, gv.leftArrow.rect)
    blit_alpha(gv.window, gv.rightArrow.image, gv.rightArrow.rect)


    # drawing invertory icon for every room
    gv.window.blit(gv.invertory.image, gv.invertory.rect)

    if gv.flags["invertory"] == True:
        gv.invBar[0].drawInvertory()

    if gv.flags['picture'] == True:
        zoomImage("Images/picture.png")

    elif gv.flags['message'] == True:
        zoomImage("Images/message-empty.png")

    elif gv.flags['pictureSafe'] == True:
        zoomImage("Images/pictureSafe.png")

    pygame.display.update()
