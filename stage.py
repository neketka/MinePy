import pygame
import math


class Stage:
    def __init__(self, bg, w, h, window):
        self.window = window
        self.w = w
        self.h = h
        self.bg = bg.convert()
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
        sur.blit(pygame.transform.scale(self.bg.subsurface(pygame.Rect((bgw - dbw)/2, (bgh - dbh)/2, dbw, dbh)),
                                        (w, h)), (0, 0))
        for spr in self.sprites:
            surface = pygame.transform.rotozoom(spr.getSurface(), spr.getDirection(),
                                                spr.getScale())
            if spr.tick is not None:
                spr.tick(time)
            sur.blit(surface, pygame.Rect())
