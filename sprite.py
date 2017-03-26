from pygame import Surface
import math


class Sprite:
    def __init__(self, constumes, tick=None):
        self.imgs = constumes
        self.costumeid = 0
        self.tick = tick
        self.pos = (0, 0)
        self.dir = 0
        self.scale = 1

    def getSurface(self):
        return self.imgs[self.costumeid]

    def setScale(self, scale):
        self.scale = scale

    def getScale(self):
        return self.scale

    def setCostume(self, id):
        self.costumeid = id

    def setPosition(self, pos):
        self.pos = pos

    def getPosition(self):
        return self.pos

    def setDirection(self, direction):
        self.dir = direction

    def getDirection(self):
        return self.dir

    def lookToward(self, sprite):
        self.dir = math.degrees(math.atan2(sprite.pos[1] - self.pos[1], sprite.pos[0] - self.pos[0]))

    def intesects(self, sprite):
        a = self.getSurface().get_size()
        b = sprite.getSurface().get_size()
        xa, ya = self.pos
        xb, yb = sprite.pos
        wa, ha = self.scale * a[0] + xa, self.scale * a[1] + ya
        wb, hb = sprite.scale * b[0] + xb, sprite.scale * b[1] + yb
        return ((xb <= xa <= wb) and (yb <= ya <= hb)) or \
               ((xb <= wa <= wb) and (yb <= ha <= hb))
