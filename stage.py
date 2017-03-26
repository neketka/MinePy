import pygame
import math


class Stage:
    def __init__(self, bg, w, h, window):
        self.window = window
        self.w = w
        self.h = h
        self.aspect = w / h
        self.bg = bg
        self.sprites = []

    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def tick(self, time):
        sur = self.window.window
        w, h = sur.get_size()
        bgw, bgh = self.bg.get_size()
        aspect = w / h
        baspect = bgw / bgh
        dbw = bgw if aspect > baspect else bgh * aspect
        dbh = bgw / aspect if aspect > baspect else bgh
        sur.blit(pygame.transform.scale(self.bg.subsurface(pygame.Rect((bgw - dbw) / 2, (bgh - dbh) / 2, dbw, dbh)),
                                        (w, h)), (0, 0))
        cw = w if aspect < self.aspect else h * self.aspect
        ch = w / self.aspect if aspect < self.aspect else h
        x, y = (w - cw) / 2, (h - ch) / 2
        scaling = cw / self.w
        halfw = self.w / 2
        halfh = self.h / 2
        cw2 = cw / 2
        for spr in self.sprites:
            surface = pygame.transform.rotozoom(spr.getSurface(), -spr.getDirection(),
                                                spr.getScale() * cw2 / spr.getSurface().get_width())
            if spr.tick is not None:
                spr.tick(time)
            sur.blit(surface, (int(x + (spr.pos[0] + halfw) * scaling), int(h - (y + surface.get_height() +
                                                                (spr.pos[1] + halfh) * scaling))))
