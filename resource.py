import os
import pygame


class Music:
    def __init__(self, path):
        self.path = path

    def play(self, loops):
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play(loops)

    def stop(self):
        pygame.mixer.music.stop()


class ResourceLoader:
    def __init__(self):
        self.files = {}
        for dir, unused, files in os.walk("." + os.sep + "resources"):
            name = dir[12:].replace(os.sep, ".")
            for file in files:
                path = os.path.abspath(os.path.join(dir, file))
                ex = os.path.splitext(file)
                extension = ex[1]
                real = name + "." + ex[0]
                if extension == ".png":
                    self.files[real] = pygame.image.load(path)
                elif extension == ".wav":
                    self.files[real] = pygame.mixer.Sound(path)
                elif extension == ".ogg":
                    self.files[real] = Music(path)

    def fetch(self, file):
        return self.files[file]
