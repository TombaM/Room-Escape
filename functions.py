import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import globalVariables as gv
from loadImage import LoadImage

def blit_alpha(target,source,location,opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x,-y))
    temp.blit(source, (0,0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

# def get_key():
#   while 1:
#     event = pygame.event.poll()
#     if event.type == KEYDOWN:
#       return event.key
#     else:
#       pass

def display_box(message,password):
    fontobject = pygame.font.Font(None,22)
    fontobjectpass = pygame.font.Font(None,25)

    pygame.draw.rect(gv.window, (0,0,0),
                   ((gv.window.get_width() / 2) - 175,
                    (gv.window.get_height() / 2) - 10,
                    350,50), 0)
    pygame.draw.rect(gv.window, (255,255,255),
                   ((gv.window.get_width() / 2) - 177,
                    (gv.window.get_height() / 2) - 12,
                    354,54), 1)
    if len(message) != 0:
        gv.window.blit(fontobject.render(message, 1, (255,255,255)),
        ((gv.window.get_width() / 2) - 175, (gv.window.get_height() / 2) - 10))
        gv.window.blit(fontobjectpass.render(password, 1, (255,255,255)),
        ((gv.window.get_width() / 2) - 175, (gv.window.get_height() / 2) + 15))

def ask(question):
#   "ask(screen, question) -> answer"
  pygame.font.init()
  display_box(question + ":",''.join(gv.password))
  inkey = gv.key
  if inkey == K_BACKSPACE:
      gv.password = gv.password[0:-1]
      gv.key=-1
  elif inkey == pygame.K_RETURN:
    #   gv.key=-1
      pom=gv.password
      gv.password=[]
      return string.join(pom,"")
  elif inkey <= 127 and inkey > 0:
      gv.password.append(chr(inkey))
      gv.key=-1


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

    if gv.flags['key']==True:
        gv.opacity_key=255
    else:
        gv.opacity_key=0

def changeBackground(side):
    if side == "left":
        if gv.index == 0:
            gv.index = len(gv.rooms) - 3
        else:
            gv.index = gv.index - 1
    else:
        if gv.index == len(gv.rooms) - 3:
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

    if gv.end_game == True:
        gv.window.blit(gv.end.image, gv.end.rect)

    if gv.game_started == True:
        # blitting arrows with opacity for every room
        if gv.index != 4 and gv.index != 5:
            blit_alpha(gv.window, gv.leftArrow.image, gv.leftArrow.rect,gv._opacity)
            blit_alpha(gv.window, gv.rightArrow.image, gv.rightArrow.rect,gv._opacity)


        # drawing invertory icon for every room
        gv.window.blit(gv.invertory.image, gv.invertory.rect)

    if gv.flags["invertory"] == True:
        gv.invBar[0].drawInvertory()

    if gv.dragging_match == True:
        gv.window.blit(gv.match.image, gv.match.rect)

    if gv.dragging_key == True and gv.end_game == False:
        gv.window.blit(gv.small_key.image, gv.small_key.rect)

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
        blit_alpha(gv.window, gv.lemon.image, gv.lemon.rect,gv.opacity_lemon)

    elif gv.flags['safe'] == True:
        if gv.safe_open == False:
            zoomImage("Images/safe.png")
            pom=ask("Type safe password and press enter")
            if gv.key == K_RETURN:
                if pom=="4295" or pom=="4 2 9 5":
                    gv.safe_open = True
                gv.key=-1
        else:
            zoomImage("Images/safe_inside.png")
            blit_alpha(gv.window, gv.key_pic.image, gv.key_pic.rect,gv.opacity_key)
            gv.window.blit(gv.nail.image, gv.nail.rect)
    pygame.display.update()
