import pygame
from pygame import *

class SimpleGame(object):
    def __init__(self,title,window_size=(640,480),fps = 60):
        self.title = title
        self.window_size = window_size
        self.fps = fps
        self.game_over = False

    def init(self):
        self.__game_init()

    def __game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)

    def run(self):
        self.init()
        while True:
            self.update()
            self.render()
            self.clock.tick(self.fps)


    def update(self):
        pass

    def render(self):
        pass

