import pygame

class LoadImage(pygame.sprite.Sprite):
    def __init__(self, image, location, width, heigth):
      pygame.sprite.Sprite.__init__(self)

      self.image = pygame.image.load(image)
      self.image = pygame.transform.scale(self.image, (width, heigth))

      self.rect = self.image.get_rect()
      self.rect.center = location

    def setLocation(self,location):
      self.rect.center = location
