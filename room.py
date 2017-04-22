import pygame
from bookshelf import Bookshelf

class RoomOne(pygame.sprite.Sprite):
  def __init__(self, image, location):
    pygame.sprite.Sprite.__init__(self)
    
    self.image = pygame.image.load(image)    
    self.image = pygame.transform.scale(self.image, (1200, 700))
    
    self.rect = self.image.get_rect()
    self.rect.center = location
    
    self.shelf = Bookshelf("Images/bookshelf.png", [250, 200])
    
  def drawBookshelf(self):
    self.image.blit(self.shelf.image, self.shelf.rect)

  def drawRoom(self):
    self.drawBookshelf()
    
class RoomTwo(pygame.sprite.Sprite):
  def __init__(self, image, location):
    pygame.sprite.Sprite.__init__(self)
    
    self.image = pygame.image.load(image)    
    self.image = pygame.transform.scale(self.image, (1200, 700))
    
    self.rect = self.image.get_rect()
    self.rect.center = location
    
  def drawRoom(self):
    print "Ana"
    
class RoomThree(pygame.sprite.Sprite):
  def __init__(self, image, location):
    pygame.sprite.Sprite.__init__(self)
    
    self.image = pygame.image.load(image)    
    self.image = pygame.transform.scale(self.image, (1200, 700))
    
    self.rect = self.image.get_rect()
    self.rect.center = location
    
  def drawRoom(self):
    print "Ana"