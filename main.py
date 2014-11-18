import pygame
from pygame.locals import *
from gamelib import SimpleGame
 
class SquashGame(SimpleGame):
    def __init__(self,title):
    	self.title = title
    	self.game_over = False

    def init(self):
    	super(SquashGame,self).init()
 
def main():
    game = SquashGame('SquashGame')
    game.run()
 
if __name__ == '__main__':
    main()