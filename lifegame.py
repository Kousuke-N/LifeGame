#!/usr/bin/env python
#coding: utf-8
import pygame
from pygame.locals import *
import os
import math
import random
import sys
import time

SCR_RECT = Rect(0, 0, 800, 500)
SCR = (SCR_RECT.size[1], SCR_RECT.size[0])
CELL = [5, 5]
CELL_NUM = [SCR[0]//CELL[0], SCR[1]//CELL[1]]
WALL, DEAD, ALIVE = (-1, 0, 1)
START_SHAPE = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]
S_SHAPE_XY = [6, 6]

##################################################

class Main():
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode(SCR_RECT.size)
        self.init_game()
        clock=pygame.time.Clock()
        while True:
            # clock.tick(60)
            screen.fill((255, 255, 255))
            
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()
            time.sleep(1)

    def init_game(self):
        self.field = [[DEAD for i in range(CELL_NUM[1])] for j in range(CELL_NUM[0])]
        for i in range(CELL_NUM[0]-2):
            self.field[i+1][0] = WALL
            self.field[i+1][CELL_NUM[1]-1] = WALL

        for i in range(CELL_NUM[1]):
            self.field[0][i] = WALL
            self.field[CELL_NUM[0]-1][i] = WALL

        for i in range(S_SHAPE_XY[0]):
            for j in range(S_SHAPE_XY[1]):
                self.field[CELL_NUM[0]//2 + i][CELL_NUM[1]//2 + j] = START_SHAPE[i][j]

    def update(self):
        self.cc_field = list(self.field)
        for i in range(CELL_NUM[0]-2):
            for j in range(CELL_NUM[1]-2):
                if self.cc_field[i+1][j+1] == ALIVE:
                    if not self.is_alive(i+1, j+1):
                        self.field[i+1][j+1] = DEAD
                if self.cc_field[i+1][j+1] == DEAD:
                    if not self.is_dead(i+1, j+1):
                        self.field[i+1][j+1] = ALIVE


    def draw(self, screen):
        for i in range(CELL_NUM[0]):
            for j in range(CELL_NUM[1]):
                if self.field[i][j] == ALIVE:
                    pygame.draw.rect(screen,(0,80,0),
                        Rect(CELL[0]*j, CELL[1]*i,CELL[0],CELL[1]))
                elif self.field[i][j] == DEAD:
                    pygame.draw.rect(screen,(255,255,255),
                        Rect(CELL[0]*j, CELL[1]*i,CELL[0],CELL[1]))


    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def is_alive(self, a, b):
        cont = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    break
                if self.cc_field[a+i][b+j] == ALIVE:
                    cont += 1
        if cont < 2:
            return False
        elif cont >= 4:
            return False

        return True

    def is_dead(self, a, b):
        cont = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    break
                if self.cc_field[a+i][b+j] == ALIVE:
                    cont += 1

        if cont == 3:
            return False

        return True

if __name__ == "__main__":
    Main()