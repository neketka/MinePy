from window import GameWindow
from resource import ResourceLoader
from stage import Stage
import pygame


def main():
    pygame.mixer.init()
    pygame.init()
    loader = ResourceLoader()
    window = GameWindow("Tower Defense", 800, 600)
    stage = Stage(loader.fetch("test.test"), 2, 2, window)
    loader.fetch("test.pop").play()
    window.addTickEvent(lambda t: stage.tick(t))
    window.run()

if __name__ == "__main__":
    main()
