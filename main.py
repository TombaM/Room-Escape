import pygame
from room import *
from invertory import *
import copy

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
room = RoomFour("Images/room4.jpg", [600, 350])
gv.rooms.append(room)


invertoryBar = Invertory("Images/invertory.png", [600, 642.5])
gv.invBar.append(invertoryBar)

f.update()
pygame.display.flip()

mx,my=pygame.mouse.get_pos()
running = True
while running:
    if gv.safe_visible == True:
        gv.safe_ind = 2

    for event in pygame.event.get():
        mx,my=pygame.mouse.get_pos()
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        #dragging hammer
        if gv.dragging == True:
            gv.hammer.setLocation([mx,my])
            if event.type == pygame.MOUSEBUTTONUP:
                gv.dragging=False
                if mx>=800 and mx<=1010 and my>=135 and my<=275 and gv.index==1:
                    gv.flags['pictureSafe']=False
                    gv.opacity_picture=0
                    gv.opacity_rotated=255
                    gv.safe_visible=True

                gv.hammer.setLocation([100+(gv.invIndex-1)*190,645])
        # Cheking if picture is "pressed" so it should be zoomed
        elif gv.rooms[1].pictureSafe.rect.collidepoint(pos) and gv.index==1 and event.type == pygame.MOUSEBUTTONUP:
            #only if it is visible we should zoom
            if gv.opacity_picture==255:
                gv.flags['pictureSafe'] = True

        if event.type == pygame.MOUSEBUTTONUP:

            if gv.rightArrow.rect.collidepoint(pos):
                f.changeBackground("right")
            elif gv.leftArrow.rect.collidepoint(pos):
                f.changeBackground("left")
            #bird picture
            elif gv.rooms[0].picture.rect.collidepoint(pos) and gv.index == 0:
                gv.flags['picture'] = True
            #safe pressed
            elif gv.rooms[1].safe.rect.collidepoint(pos) and gv.index == 1 and gv.safe_visible == True:
                if gv.safe_ind == 2:
                    gv.flags['safe'] = True
            #hammer taken
            elif gv.rooms[3].hammer.rect.collidepoint(pos) and gv.index == 3:
                gv.flags['hammer'] = False
                gv.hammer.setLocation([100+gv.invIndex*190,645])
                gv.invertoryItems.append(gv.hammer)
                gv.invIndex = gv.invIndex + 1
            #paper taken
            elif gv.rooms[0].paper.rect.collidepoint(pos) and gv.index == 0:
                gv.flags['paper'] = False
                gv.paper.setLocation([100+gv.invIndex*190,645])
                gv.invertoryItems.append(gv.paper)
                gv.invIndex = gv.invIndex + 1
            #paper pressed after storage
            elif gv.paper.rect.collidepoint(pos):
                gv.flags['message'] = True
            #trying to check inventory
            elif gv.invertory.rect.collidepoint(pos):
                gv.flags['invertory'] = True
            #start to drag hammer
            elif gv.hammer.rect.collidepoint(pos) and pygame.MOUSEBUTTONUP:
                gv.dragging = True
            #'X' pressed
            elif gv.close.rect.collidepoint(pos):
                gv.flags['lemon']=False
                gv.flags['fridge']=False
                gv.flags['picture'] = False
                gv.flags['invertory'] = False
                gv.flags['message'] = False
                gv.flags['pictureSafe'] = False
                gv.flags['safe'] = False
            #opening fridge
            elif gv.index==2 and event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # hardcoded part, if we think of something better, will be implemented
                if pos[0]>=230 and pos[0]<=300 and pos[1]>=220 and pos[1]<=330:
                    gv.flags['fridge']=True
                    #drawing lemon before it is taken
                    if gv.lemon_ind == 0:
                        gv.flags['lemon'] = True
                #taking lemon, first and only time
                if gv.lemon.rect.collidepoint(pos) and gv.index==2:
                    gv.flags['lemon']=False
                    gv.lemon_ind = 1
                    gv.lemon.setLocation([100+gv.invIndex*190,645])
                    gv.invertoryItems.append(gv.lemon)
                    gv.invIndex = gv.invIndex + 1
    f.opacity()
    f.update()
    gv.window.fill((255, 255, 255))
    # print gv.index
