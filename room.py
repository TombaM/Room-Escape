import pygame
from loadImage import LoadImage

class RoomOne(LoadImage):
  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 700)

    self.shelf = LoadImage("Images/bookshelf.png", [250, 200], 300, 180)
    self.armchair = LoadImage("Images/armchair.png", [250, 500], 350, 300)
    self.desk = LoadImage("Images/desk.png", [800, 520], 500, 250)
    self.picture = LoadImage("Images/picture.png", [780, 200], 300, 150)

  def drawObject(self, obj):
      self.image.blit(obj.image, obj.rect)

  def drawRoom(self):      
    self.drawObject(self.shelf)
    self.drawObject(self.armchair)
    self.drawObject(self.desk)
    self.drawObject(self.picture)

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