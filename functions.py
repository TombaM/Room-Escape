import pygame
import copy
import globalVariables as gv
from loadImage import LoadImage
import room

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

    if gv.flags['hammer']==True:
        gv.opacity_hammer=255
    else:
        gv.opacity_hammer=0

    if gv.flags['lemon']==True:
        gv.opacity_lemon=255
    else:
        gv.opacity_lemon=0

    if gv.flags['matches']==True:
        gv.opacity_matches=255
    else:
        gv.opacity_matches=0

    if gv.message_lemoned==True and gv.opacity_candle==0:
        gv.opacity_message=255
    else:
        gv.opacity_message=0

def changeBackground(side):
    if side == "left":
        if gv.index == 0:
            gv.index = len(gv.rooms) - 2
        else:
            gv.index = gv.index - 1
    else:
        if gv.index == len(gv.rooms) - 2:
            gv.index = 0
        else:
            gv.index = gv.index + 1

def zoomImage(imageSource):
    # drawing of black screen on top of whole screen
    s = pygame.Surface((1200,700), pygame.SRCALPHA)
    s.fill((0,0,0,180))
    gv.window.blit(s, (0,0))

    pic = LoadImage(imageSource, [600, 350], 300, 150, 0)
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

    if gv.dragging_match == True:
        gv.window.blit(gv.match.image, gv.match.rect)

    if gv.dragging_paper == True:
        gv.window.blit(gv.table_paper.image, gv.table_paper.rect)

    if gv.flags['picture'] == True:
        zoomImage("Images/picture.png")

    elif gv.flags['message'] == True:
        zoomImage("Images/message-empty.png")

    elif gv.flags['pictureSafe'] == True:
        zoomImage("Images/pictureSafe.png")

    elif gv.flags['fridge'] == True:
        zoomImage("Images/fridge.png")
        room.blit_alpha(gv.window, gv.lemon.image, gv.lemon.rect,gv.opacity_lemon)

    elif gv.flags['safe'] == True:
        zoomImage("Images/safe.png")

    pygame.display.update()
