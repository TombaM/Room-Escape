import pygame
from bookshelf import Bookshelf
from armchair import Armchair
from desk import Desk
from picture import Picture

class RoomOne(pygame.sprite.Sprite):
  def __init__(self, image, location):
    pygame.sprite.Sprite.__init__(self)
    
    self.image = pygame.image.load(image)    
    self.image = pygame.transform.scale(self.image, (1200, 700))
    
    self.rect = self.image.get_rect()
    self.rect.center = location
    
    self.shelf = Bookshelf("Images/bookshelf.png", [250, 200])
    self.armchair = Armchair("Images/armchair.png", [250, 500])
    self.desk = Desk("Images/desk.png", [800, 520])
    self.picture = Picture("Images/picture.png", [780, 200])
    
  def drawBookshelf(self):
    self.image.blit(self.shelf.image, self.shelf.rect)

  def drawArmchair(self):
    self.image.blit(self.armchair.image, self.armchair.rect)
    
  def drawDesk(self):
    self.image.blit(self.desk.image, self.desk.rect)

  def drawPicture(self):
    self.image.blit(self.picture.image, self.picture.rect)


  def drawRoom(self):
    self.drawBookshelf()
    self.drawArmchair()
    self.drawDesk()
    self.drawPicture()
    
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