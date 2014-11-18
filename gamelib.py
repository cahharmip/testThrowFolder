import pygame
from pygame import *

class SimpleGame(object):
    def __init__(self,title,window_size=(640,480),fps = 60):
        self.title = title
        self.window_size = window_size
        self.fps = fps
        self.game_over = False

    def init(self):
        self.game_init()

    def game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)

    def run(self):
        # while not self.game_over:
        #     for event in pygame.event.get(): # process events
        #         if (event.type == QUIT) or \
        #             (event.type == KEYDOWN and event.key == K_ESCAPE):
        #             self.game_over = True

        # pass
        pass

    def update(self):
        pass

    def render(self):
        pass

