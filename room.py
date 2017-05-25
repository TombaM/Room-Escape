import pygame
from loadImage import LoadImage
import globalVariables as gv

def blit_alpha(target,source,location,opacity):
  x = location[0]
  y = location[1]
  temp = pygame.Surface((source.get_width(), source.get_height())).convert()
  temp.blit(target, (-x,-y))
  temp.blit(source, (0,0))
  temp.set_alpha(opacity)
  target.blit(temp, location)


class RoomOne(LoadImage):
  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 700, 0)

    #self.shelf = LoadImage("Images/bookshelf.png", [250, 200], 300, 180, 0)
    self.armchair = LoadImage("Images/armchair.png", [250, 500], 350, 300, 0)
    #self.desk = LoadImage("Images/desk.png", [800, 510], 500, 230, 0)
    #self.picture = LoadImage("Images/picture.png", [780, 200], 300, 150, 0)
    self.paper = LoadImage("Images/paper.png", [360, 580], 25, 25, 0)
    self.candle = LoadImage("Images/candleoff.png", [630, 365], 100, 100, 0)
    self.candle2 = LoadImage("Images/candleon.png", [630, 365], 100, 100, 0)

  def drawObject(self, obj):
      self.image.blit(obj.image, obj.rect)

  def drawRoom(self):
    blit_alpha(gv.window, self.paper.image, self.paper.rect,gv.opacity_paper)
    blit_alpha(gv.window, self.armchair.image, self.armchair.rect,255)
    blit_alpha(gv.window, self.candle.image, self.candle.rect,gv.opacity_candle)
    blit_alpha(gv.window, self.candle2.image, self.candle2.rect,gv.opacity_light_candle)
    #self.drawObject(self.shelf)
    #self.drawObject(self.desk)
    #self.drawObject(self.picture)
    self.drawObject(self.candle)

class RoomTwo(LoadImage):
  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 700, 0)

    self.piano = LoadImage("Images/piano.png", [900, 500], 400, 400, 0)
    #self.lamp = LoadImage("Images/lamp.png", [640, 490], 250, 380, 0)
    #self.clock = LoadImage("Images/clock.png", [200, 410], 200, 580, 0)
    self.notebook = LoadImage("Images/notebook.png", [895, 440], 60, 70, 0)
    #self.safe = LoadImage("Images/safe.png", [895, 200], 130, 100, 0)
    self.pictureSafe = LoadImage("Images/pictureSafe.png", [905, 212.5], 250, 175, 0)

  def drawObject(self, obj):
      self.image.blit(obj.image, obj.rect)

  def drawRoom(self):
    blit_alpha(gv.window, self.pictureSafe.image, self.pictureSafe.rect,gv.opacity_picture)
    blit_alpha(gv.window, gv.rotated.image, gv.rotated.rect,gv.opacity_rotated)
    blit_alpha(gv.window, self.piano.image, self.piano.rect,255)
    blit_alpha(gv.window, self.notebook.image, self.notebook.rect,255)
    #self.drawObject(self.lamp)
    #self.drawObject(self.clock)
    #self.drawObject(self.safe)


class RoomThree(LoadImage):
    def __init__(self, image, location):
        LoadImage.__init__(self, image, location, 1200, 700, 0)

    def drawObject(self, obj):
        self.image.blit(obj.image, obj.rect)

    def drawRoom(self):
        return
                #   blit_alpha(gv.window, self.lemon.image, self.lemon.rect,gv.opacity_lemon)

class RoomFour(LoadImage):
  def __init__(self, image, location):
    LoadImage.__init__(self, image, location, 1200, 700, 0)

    #self.barrel = LoadImage("Images/barrel.png", [775, 470], 220, 330, 0)
    self.bucket = LoadImage("Images/bucket.png", [240, 555], 150, 135, 0)
    self.shelf = LoadImage("Images/old_shelf.png", [1020, 370], 350, 670, 0)
    #self.stool = LoadImage("Images/stool.png", [620, 600], 220, 150, 0)
    #self.sack1 = LoadImage("Images/sack.png", [90, 535], 170, 220, 0)
    #self.sack2 = LoadImage("Images/sack.png", [140, 510], 170, 220, 0)
    #self.broom = LoadImage("Images/broom.png", [270, 400], 290, 400, 0)
    #self.chest = LoadImage("Images/chest.png", [495, 510], 350, 190, 0)
    #self.ham = LoadImage("Images/ham.png", [400, 105], 150, 200, 0)
    self.hammer = LoadImage("Images/hammer.png", [250, 540], 90, 90, 0)
    self.matches = LoadImage("Images/matches.png", [1040, 635], 55, 55, 25)
    self.close = LoadImage("Images/close.png", [1170, 30], 50, 50, 0)

  def drawObject(self, obj):
      self.image.blit(obj.image, obj.rect)

  def drawRoom(self):
      blit_alpha(gv.window, self.hammer.image, self.hammer.rect,gv.opacity_hammer)
      blit_alpha(gv.window, self.matches.image, self.matches.rect,gv.opacity_matches)
      #blit_alpha(gv.window, self.broom.image, self.broom.rect,255)
      blit_alpha(gv.window, self.bucket.image, self.bucket.rect,255)
      blit_alpha(gv.window, self.shelf.image, self.shelf.rect,255)
      self.drawObject(self.close)
    #   self.drawObject(self.ham)
    #   self.drawObject(self.chest)
    #   self.drawObject(self.sack2)
    #   self.drawObject(self.sack1)
    # #   self.drawObject(self.shelf)
    #   self.drawObject(self.barrel)
    #   self.drawObject(self.stool)

class RoomDesk(LoadImage):
    def __init__(self, image, location):
        LoadImage.__init__(self, image, location, 1200, 700, 0)
        self.close = LoadImage("Images/close.png", [1170, 30], 50, 50, 0)
        self.candle_on = LoadImage("Images/candle_desk_on.png", [150, 120], 220, 170, 0)
        self.candle_off = LoadImage("Images/candle_desk_off.png", [150, 120], 220, 170, 0)
        self.message_empty = LoadImage("Images/message-empty.png", [600, 320], 400, 370, 0)
        self.message = LoadImage("Images/message.png", [600, 320], 400, 370, 0)

    def drawObject(self, obj):
        self.image.blit(obj.image, obj.rect)

    def drawRoom(self):
        blit_alpha(gv.window, self.candle_off.image, self.candle_off.rect,gv.opacity_candle)
        blit_alpha(gv.window, self.candle_on.image, self.candle_on.rect,gv.opacity_light_candle)
        blit_alpha(gv.window, self.message_empty.image, self.message_empty.rect,gv.opacity_table_paper)
        blit_alpha(gv.window, self.message.image, self.message.rect,gv.opacity_message)
        self.drawObject(self.close)

class RoomStart(LoadImage):
    def __init__(self, image, location):
        LoadImage.__init__(self, image, location, 1200, 700, 0)

    def drawRoom(self):
        return

class RoomEnd(LoadImage):
    def __init__(self, image, location):
        LoadImage.__init__(self, image, location, 1200, 700, 0)

    def drawRoom(self):
        return
