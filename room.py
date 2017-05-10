import pygame
from loadImage import LoadImage
import globalVariables as gv

class RoomOne(LoadImage):
  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 700)

    self.shelf = LoadImage("Images/bookshelf.png", [250, 200], 300, 180)
    self.armchair = LoadImage("Images/armchair.png", [250, 500], 350, 300)
    self.desk = LoadImage("Images/desk.png", [800, 510], 500, 230)
    self.picture = LoadImage("Images/picture.png", [780, 200], 300, 150)
    self.counter = 0

  def drawObject(self, obj):
      self.image.blit(obj.image, obj.rect)

  def drawRoom(self):
    self.drawObject(self.shelf)
    self.counter = self.counter + 1
    print self.counter
    if gv.flagPaper == False:
      self.drawObject(gv.paper)
    self.drawObject(self.armchair)
    self.drawObject(self.desk)
    self.drawObject(self.picture)

class RoomTwo(LoadImage):
  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 700)

    self.piano = LoadImage("Images/piano.png", [900, 540], 400, 300)
    self.lamp = LoadImage("Images/lamp.png", [640, 490], 250, 380)
    self.clock = LoadImage("Images/clock.png", [200, 410], 200, 580)
    self.notebook = LoadImage("Images/notebook.png", [900, 420], 60, 70)
    self.safe = LoadImage("Images/safe.png", [895, 200], 130, 100)
    self.pictureSafe = LoadImage("Images/pictureSafe.png", [905, 212.5], 250, 175)

  def drawObject(self, obj):
      self.image.blit(obj.image, obj.rect)

  def drawRoom(self):
    self.drawObject(self.piano)
    self.drawObject(self.lamp)
    self.drawObject(self.clock)
    self.drawObject(self.notebook)
    self.drawObject(self.safe)
    self.drawObject(self.pictureSafe)

class RoomThree(LoadImage):
  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 700)

    self.barrel = LoadImage("Images/barrel.png", [775, 470], 220, 330)
    self.bucket = LoadImage("Images/bucket.png", [200, 555], 150, 135)
    self.stool = LoadImage("Images/stool.png", [620, 600], 220, 150)
    self.shelf = LoadImage("Images/old_shelf.png", [1020, 370], 350, 670)
    self.sack1 = LoadImage("Images/sack.png", [90, 535], 170, 220)
    self.sack2 = LoadImage("Images/sack.png", [140, 510], 170, 220)
    self.broom = LoadImage("Images/broom.png", [270, 400], 290, 400)
    self.chest = LoadImage("Images/chest.png", [495, 510], 350, 190)
    self.ham = LoadImage("Images/ham.png", [400, 105], 150, 200)

  def drawObject(self, obj):
      self.image.blit(obj.image, obj.rect)
  def drawRoom(self):
      self.drawObject(self.ham)
      self.drawObject(self.chest)
      self.drawObject(self.broom)
      self.drawObject(self.sack2)
      self.drawObject(self.sack1)
      self.drawObject(self.shelf)
      self.drawObject(self.barrel)
      self.drawObject(self.bucket)
      self.drawObject(self.stool)
