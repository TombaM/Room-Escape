import pygame

class Picture(pygame.sprite.Sprite):  
  def __init__(self, image, location):
    pygame.sprite.Sprite.__init__(self)
    
    self.image = pygame.image.load(image)    
    self.image = pygame.transform.scale(self.image, (300, 150))
    
    self.rect = self.image.get_rect()
    self.rect.center = location