#!/usr/bin/env python
#coding: utf-8
import pygame
from pygame.locals import *
import os
import math
import random
import sys

SCR_RECT = Rect(0, 0, 1600, 1000)

##################################################

class Main():
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode(SCR_RECT.size)
        self.init_game()
        clock=pygame.time.Clock()
        while True:
            clock.tick(60)
            screen.fill((0, 0, 0))
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()

    def init_game(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    Main()