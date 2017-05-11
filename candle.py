import pygame

class Candle(pygame.sprite.Sprite):  
  def __init__(self, image, location):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load(image)
    self.image = pygame.transform.scale(self.image, (50, 50))

    self.rect = self.image.get_rect()
    self.rect.center = location
