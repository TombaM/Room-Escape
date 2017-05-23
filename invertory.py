import pygame
from loadImage import LoadImage
import globalVariables as gv

class Invertory(LoadImage):

  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 115, 0)
    # pygame.sprite.Sprite.__init__(self)
    #
    # self.image = pygame.image.load(image)
    # self.image = pygame.transform.scale(self.image, (350, 300))
    #
    # self.rect = self.image.get_rect()
    # self.rect.center = location

  def addItem(self):
    index = index + 1

  def drawObject(self, obj):
    self.image.blit(obj.image, obj.rect)

  def drawInvertory(self):
    gv.window.blit(self.image, self.rect)
    gv.close.rect = gv.close.image.get_rect()
    gv.close.rect.center = [1165, 642.5]
    gv.window.blit(gv.close.image, gv.close.rect)
    i = 0
    while i < gv.invIndex:
        gv.window.blit(gv.invertoryItems[i].image, gv.invertoryItems[i].rect)
        i = i + 1
    # if gv.flagPaper==True:
