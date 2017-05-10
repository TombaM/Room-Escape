import pygame
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

def update():
    gv.window.blit(gv.rooms[gv.index].image, gv.rooms[gv.index].rect)
    gv.rooms[gv.index].drawRoom()
    blit_alpha(gv.window, gv.leftArrow.image, gv.leftArrow.rect)
    blit_alpha(gv.window, gv.rightArrow.image, gv.rightArrow.rect)
    gv.window.blit(gv.invertory.image, gv.invertory.rect)

    if gv.flagInvertory == True:
        print "mamara"
        gv.invBar[0].drawInvertory()
        # ib = invertory("Images/room1.jpg", [600, 350])
        # gv.window.blit(invertoryBar.image, invertoryBar.rect)
        # gv.close.rect = gv.close.image.get_rect()
        # gv.close.rect.center = [1165, 642.5]
        # gv.window.blit(gv.close.image, gv.close.rect)

    if gv.flagPicture == True:
        s = pygame.Surface((1200,700), pygame.SRCALPHA)
        s.fill((0,0,0,180))
        gv.window.blit(s, (0,0))
        pic = LoadImage("Images/picture.png", [600, 350], 300, 150)
        pic.image = pygame.transform.scale(pic.image, (600, 500))
        pic.rect = pic.image.get_rect()
        pic.rect.center = (600, 350)
        gv.window.blit(pic.image, pic.rect)
        gv.close.rect = gv.close.image.get_rect()
        gv.close.rect.center = pic.rect.topright
        gv.window.blit(gv.close.image, gv.close.rect)

    elif gv.flagMessage == True:
        s = pygame.Surface((1200,700), pygame.SRCALPHA)
        s.fill((0,0,0,180))
        gv.window.blit(s, (0,0))
        pic = LoadImage("Images/message-empty.png", [600, 350], 300, 150)
        pic.image = pygame.transform.scale(pic.image, (600, 500))
        pic.rect = pic.image.get_rect()
        pic.rect.center = (600, 350)
        gv.window.blit(pic.image, pic.rect)
        gv.close.rect = gv.close.image.get_rect()
        gv.close.rect.center = pic.rect.topright
        gv.window.blit(gv.close.image, gv.close.rect)

    elif gv.flagPictureSafe == True:
        s = pygame.Surface((1200,700), pygame.SRCALPHA)
        s.fill((0,0,0,180))
        gv.window.blit(s, (0,0))
        pic = LoadImage("Images/pictureSafe.png", [600, 350], 300, 150)
        pic.image = pygame.transform.scale(pic.image, (600, 500))
        pic.rect = pic.image.get_rect()
        pic.rect.center = (600, 350)
        gv.window.blit(pic.image, pic.rect)
        gv.close.rect = gv.close.image.get_rect()
        gv.close.rect.center = pic.rect.topright
        gv.window.blit(gv.close.image, gv.close.rect)

    pygame.display.update()
