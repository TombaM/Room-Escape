import pygame
from loadImage import LoadImage

class RoomOne(LoadImage):
  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 700)

    self.shelf = LoadImage("Images/bookshelf.png", [250, 200], 300, 180)
    self.armchair = LoadImage("Images/armchair.png", [250, 500], 350, 300)
    self.desk = LoadImage("Images/desk.png", [800, 520], 500, 250)
    self.picture = LoadImage("Images/picture.png", [780, 200], 300, 150)

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

class RoomTwo(LoadImage):
  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 700)

  def drawRoom(self):
    return

class RoomThree(LoadImage):
  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 700)

  def drawRoom(self):
    return