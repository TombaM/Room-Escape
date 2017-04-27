import pygame
from arrow import Arrow
from room import *
from close import Close

import functions as f
import globalVariables as gv

pygame.init()
pygame.display.set_caption('Escape room')


room = RoomOne("Images/room1.jpg", [600, 350])
gv.rooms.append(room)
room = RoomTwo("Images/room2.jpg", [600, 350])
gv.rooms.append(room)
room = RoomThree("Images/room3.jpg", [600, 350])
gv.rooms.append(room)


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
            elif gv.rooms[0].picture.rect.collidepoint(pos):
                gv.flag = True
            elif gv.close.rect.collidepoint(pos):
                gv.flag = False

    print gv.flag
    f.opacity()
    f.update()
    print gv.index