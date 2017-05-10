import pygame
from room import *
from invertory import *


import functions as f
import globalVariables as gv

pygame.init()
pygame.display.set_caption('Escape room')


room = RoomTwo("Images/room2.jpg", [600, 350])
gv.rooms.append(room)
room = RoomOne("Images/room1.jpg", [600, 350])
gv.rooms.append(room)
room = RoomThree("Images/room3.jpg", [600, 350])
gv.rooms.append(room)


invertoryBar = Invertory("Images/invertory.png", [600, 642.5])
gv.invBar.append(invertoryBar)

f.update()
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if gv.rightArrow.rect.collidepoint(pos):
                f.changeBackground("right")
            elif gv.leftArrow.rect.collidepoint(pos):
                f.changeBackground("left")
            elif gv.rooms[1].picture.rect.collidepoint(pos):
                gv.flagPicture = True
            elif gv.rooms[0].pictureSafe.rect.collidepoint(pos):
                gv.flagPictureSafe = True
            elif gv.paper.rect.collidepoint(pos):
                # gv.invBar[0].addItem(paper)
                # gv.flagPaper = True
                gv.flagMessage = True
                print gv.flagPaper
            elif gv.invertory.rect.collidepoint(pos):
                gv.flagInvertory = True
            elif gv.close.rect.collidepoint(pos):
                gv.flagPicture = False
                gv.flagMessage = False
                gv.flagInvertory = False


    f.opacity()
    f.update()
    gv.window.fill((255, 255, 255))
    # print gv.index
