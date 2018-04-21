from window import GameWindow
from resource import ResourceLoader
from stage import Stage
from sprite import Sprite
import pygame

#hello world
def main():
    pygame.mixer.init()
    pygame.init()
    window = GameWindow("Tower Defense", 800, 600)
    loader = ResourceLoader()
    stage = Stage(loader.fetch("test.test"), 2, 2, window)
    sprite = Sprite([loader.fetch("test.test")])
    sprite.setPosition((0, 0))
    sprite2 = Sprite([loader.fetch("test.test")])
    sprite2.setPosition((-1, -1))
    sprite.lookToward(sprite2)
    stage.addSprite(sprite)
    stage.addSprite(sprite2)
    loader.fetch("test.pop").play()
    window.addTickEvent(lambda t: stage.tick(t))
    window.run()

if __name__ == "__main__":
    main()
