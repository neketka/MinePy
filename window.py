import pygame
import time
from stage import *


class GameWindow:
    def __init__(self, title, w, h):
        self.window = pygame.display.set_mode((w, h), pygame.RESIZABLE)  # Creates a window
        pygame.display.set_caption(title)
        self.running = False
        self.ticking = []  # Events that get run every frame
        self.fps = 60

    def addTickEvent(self, event):
        self.ticking.append(event)  # Takes a parameter for the time passed since last frame

    def getFps(self):
        return self.fps

    def getMousePos(self):
        return pygame.mouse.get_pos()

    def getMouseButton(self, button):
        return pygame.mouse.get_pressed()[button]

    def getKey(self, key):
        return pygame.key.get_pressed()[key]

    def run(self):
        self.running = True
        last_time = time.time()
        while self.running:
            start_time = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.VIDEORESIZE:
                    self.window = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
            self.window.fill((0, 0, 0))
            for tick in self.ticking:
                tick(last_time - start_time)
            pygame.display.update()
            last_time = time.time()
            self.fps = int(1 / max(0.001, last_time - start_time))
            print(self.fps)

    def stop(self):
        self.running = False
