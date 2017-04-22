import pygame
from arrow import Arrow
from room import *

pygame.init()

rooms = []
index = 0
_opacity = 30

def blit_alpha(target,source,location):
  x = location[0]
  y = location[1]
  temp = pygame.Surface((source.get_width(), source.get_height())).convert()
  temp.blit(target, (-x,-y))
  temp.blit(source, (0,0))
  temp.set_alpha(_opacity)
  target.blit(temp, location)
  
def opacity():
  global _opacity
  if leftArrow.rect.collidepoint(pygame.mouse.get_pos()):
    _opacity = 255  
  elif rightArrow.rect.collidepoint(pygame.mouse.get_pos()):
    _opacity = 255
  else:
    _opacity = 30
    
def changeBackground(side):
    global index
    if side == "left":
      if index == 0:
        index = len(rooms) - 1
      else:
        index = index - 1
    else:
      if index == len(rooms) - 1:
        index = 0
      else:
        index = index + 1

def update():
  global window,rooms,window
  window.blit(rooms[index].image, room.rect)
  rooms[index].drawRoom()
  blit_alpha(window,leftArrow.image,leftArrow.rect)
  blit_alpha(window,rightArrow.image,rightArrow.rect)
  #pygame.display.unlock()
  pygame.display.update()
  
(width, height) = (1200, 700)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Escape room')
room = RoomOne("Images/room1.jpg", [600, 350])
rooms.append(room)
room = RoomTwo("Images/room2.jpg", [600, 350])
rooms.append(room)
room = RoomThree("Images/room3.jpg", [600, 350])
rooms.append(room)
leftArrow = Arrow("Images/left_arrow.png", [60, 350])
rightArrow = Arrow("Images/right_arrow.png", [1140, 350])


update()

pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      running = False
    
    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      
      if rightArrow.rect.collidepoint(pos):
        changeBackground("right")
      elif leftArrow.rect.collidepoint(pos):
        changeBackground("left")
      elif room.shelf.rect.collidepoint(pos):
        print "Iiiiideeeemooooo, tako je mamu ti jebem!"
  opacity()
  update()
  print index