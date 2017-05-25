import pygame
from room import *
from invertory import *

import functions as f
import globalVariables as gv

pygame.init()
pygame.display.set_caption('Escape room')

music = "Music/backgroundMusic.mp3"
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

#pravi se objekat za zvuk i ovo .play() se poziva kad se klikne na vrata

def item_taken():
    pickUp = pygame.mixer.Sound('Music/pick_up.ogg')
    pickUp.set_volume(1)
    pickUp.play()

room = RoomStart("Images/room_start.jpg", [600, 350])
gv.rooms.append(room)
room = RoomTwo("Images/room2.jpg", [600, 350])
gv.rooms.append(room)
room = RoomThree("Images/room3.jpg", [600, 350])
gv.rooms.append(room)
room = RoomEnd("Images/room5.jpg", [600, 350])
gv.rooms.append(room)
room = RoomFour("Images/room4shelf.jpg", [600, 350])
gv.rooms.append(room)
room = RoomDesk("Images/desk_room.png", [600, 350])
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
        # print mx,my
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYDOWN:
            gv.key=event.key
        if event.type == pygame.MOUSEBUTTONUP and gv.game_started == False:
            if mx >= 140 and mx <= 680 and my >= 555 and my <= 625:
                gv.game_started = True
                room = RoomOne("Images/room1.jpg", [600, 350])
                gv.rooms[0] = room
        #dragging hammer
        if gv.dragging_hammer == True:
            gv.hammer.setLocation([mx,my])
            if event.type == pygame.MOUSEBUTTONUP:
                gv.dragging_hammer=False
                if mx>=800 and mx<=1010 and my>=135 and my<=275 and gv.index==1:
                    gv.flags['pictureSafe']=False
                    gv.opacity_picture=0
                    gv.opacity_rotated=255
                    gv.safe_visible=True

                gv.hammer.setLocation([100+(gv.hammer_index)*190,645])

        elif gv.dragging_match == True:
            gv.match.setLocation([mx,my])
            if event.type == pygame.MOUSEBUTTONUP:
                gv.dragging_match=False
                if mx>=635 and mx<=645 and my>=318 and my<=335 and gv.index==0:
                    gv.opacity_candle=0
                    gv.opacity_light_candle=255

                gv.matches.setLocation([100+(gv.matches_index)*190,645])

        elif gv.dragging_paper == True:
            gv.table_paper.setLocation([mx,my])
            if event.type == pygame.MOUSEBUTTONUP:
                gv.dragging_paper=False
                if mx>=280 and mx<=940 and my>=60 and my<=500 and gv.index==5:
                    gv.opacity_table_paper = 255

                gv.paper.setLocation([100+(gv.paper_index)*190,645])

        elif gv.dragging_lemon == True:
            gv.lemon_inv.setLocation([mx,my])
            if event.type == pygame.MOUSEBUTTONUP:
                gv.dragging_lemon=False
                if mx>=380 and mx<=920 and my>=70 and my<=490 and gv.index==5 and gv.opacity_table_paper==255:
                    gv.message_lemoned = True
                    if gv.opacity_candle==0:
                        gv.opacity_table_paper = 0

                gv.lemon_inv.setLocation([100+(gv.lemon_index)*190,645])

        elif gv.dragging_key == True:
            gv.key_inv.setLocation([mx,my])
            if event.type == pygame.MOUSEBUTTONUP:
                # gv.dragging_key=False
                if mx>=310 and mx<=330 and my>=285 and my<=340 and gv.index==3:
                    unlockingDoor = pygame.mixer.Sound('Music/unlock_door.ogg')
                    unlockingDoor.play()

                gv.matches.setLocation([100+(gv.matches_index)*190,645])
        # Cheking if picture is "pressed" so it should be zoomed
        elif gv.rooms[1].pictureSafe.rect.collidepoint(pos) and gv.index==1 and event.type == pygame.MOUSEBUTTONUP:
            #only if it is visible we should zoom
            if gv.opacity_picture==255:
                gv.flags['pictureSafe'] = True

        if event.type == pygame.MOUSEBUTTONUP and gv.game_started == True:
            if mx>=310 and mx<=340 and my>=285 and my<=340 and gv.index==3 and gv.dragging_key == False:
                lockedDoorSound = pygame.mixer.Sound('Music/door_locked.ogg')
                lockedDoorSound.play()

            if gv.rightArrow.rect.collidepoint(pos) and gv.index != len(gv.rooms) - 2:
                f.changeBackground("right")
            elif gv.leftArrow.rect.collidepoint(pos) and gv.index != len(gv.rooms) - 2:
                f.changeBackground("left")
            #bird picture
            elif mx>=730 and mx<=945 and my>=120 and my<=280 and gv.index == 0:
                gv.flags['picture'] = True
            #safe pressed
            elif mx>=890 and mx<=980 and my>=195 and my<=265 and gv.index == 1 and gv.safe_visible == True:
                if gv.safe_ind == 2:
                    gv.flags['safe'] = True
            #hammer taken
            elif gv.rooms[4].hammer.rect.collidepoint(pos) and gv.index == 4:
                gv.flags['hammer'] = False
                gv.hammer.setLocation([100+gv.invIndex*190,645])
                gv.invertoryItems.append(gv.hammer)
                gv.hammer_index=gv.invIndex
                gv.invIndex = gv.invIndex + 1
                item_taken()
            #matches taken
            elif gv.rooms[4].matches.rect.collidepoint(pos) and gv.index == 4:
                gv.flags['matches'] = False
                gv.matches.setLocation([100+gv.invIndex*190,645])
                gv.invertoryItems.append(gv.matches)
                gv.matches_index=gv.invIndex
                gv.invIndex = gv.invIndex + 1
                item_taken()
            #paper taken
            elif gv.rooms[0].paper.rect.collidepoint(pos) and gv.index == 0:
                gv.flags['paper'] = False
                gv.paper.setLocation([100+gv.invIndex*190,645])
                gv.invertoryItems.append(gv.paper)
                gv.paper_index=gv.invIndex
                gv.invIndex = gv.invIndex + 1
                item_taken()
            #close desk_room
            elif gv.rooms[5].close.rect.collidepoint(pos) and gv.index == 5:
                gv.index = 0
            elif gv.rooms[4].close.rect.collidepoint(pos) and gv.index == 4:
                gv.index = 3
            #enter desk room
            elif mx>=595 and mx<=1075 and my>=400 and my<=420 and gv.index == 0:
                gv.index = len(gv.rooms) - 1
            #enter basement
            elif mx>=820 and mx<=1015 and my>=65 and my<=545 and gv.index == 3:
                gv.index = len(gv.rooms) - 2
            #paper pressed after storage
            elif gv.paper.rect.collidepoint(pos):
                # gv.flags['message'] = True
                gv.dragging_paper = True
            elif gv.key_inv.rect.collidepoint(pos):
                # gv.flags['message'] = True
                gv.dragging_key = True
            #trying to check inventory
            elif gv.invertory.rect.collidepoint(pos):
                gv.flags['invertory'] = True
            #start to drag hammer
            elif gv.hammer.rect.collidepoint(pos) and pygame.MOUSEBUTTONUP:
                gv.dragging_hammer = True
            #start to drag match
            elif gv.matches.rect.collidepoint(pos) and pygame.MOUSEBUTTONUP:
                gv.dragging_match = True
                #dragging lemon
            elif gv.lemon_inv.rect.collidepoint(pos) and pygame.MOUSEBUTTONUP:
                gv.dragging_lemon = True
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
                # pos = pygame.mouse.get_pos()
                # hardcoded part, if we think of something better, will be implemented
                if mx>=1040 and pos[0]<=1100 and pos[1]>=125 and pos[1]<=340:
                    gv.flags['fridge']=True
                    #drawing lemon before it is taken
                    if gv.lemon_ind == 0:
                        gv.flags['lemon'] = True
                #taking lemon, first and only time
                if gv.lemon.rect.collidepoint(pos) and gv.index==2:
                    gv.flags['lemon']=False
                    gv.lemon_ind = 1
                    gv.lemon_inv.setLocation([100+gv.invIndex*190,645])
                    gv.invertoryItems.append(gv.lemon_inv)
                    gv.lemon_index = gv.invIndex
                    gv.invIndex = gv.invIndex + 1
                    item_taken()
            elif gv.index == 1 and event.type == pygame.MOUSEBUTTONUP:
                if gv.key_pic.rect.collidepoint(pos) and gv.index==1 and gv.safe_open == True:
                    gv.flags['key'] = False
                    gv.key_inv.setLocation([100+gv.invIndex*190,645])
                    gv.invertoryItems.append(gv.key_inv)
                    gv.key_index = gv.invIndex
                    gv.invIndex = gv.invIndex + 1
                    item_taken()
        f.opacity()
        f.update()
        gv.window.fill((255, 255, 255))
        # print gv.index
