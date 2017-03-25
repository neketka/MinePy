from pygame import Surface


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