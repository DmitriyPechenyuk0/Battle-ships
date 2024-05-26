import pygame
import modules.data_base as data
import modules.path_file as path
#Класс корабль
class Ship:
    def __init__(self, type, side, cell, state, angle):
        self.TYPE = type
        self.SIDE = side
        self.CELL = cell
        self.STATE = state
        self.ANGLE = angle
        self.X = 0
        self.Y = 0
    #расттановка корабля
    def place_ship(self):
        if self.TYPE == "one_decker":
            lenght = 1
        elif self.TYPE == "two_decker":
            lenght = 2
        elif self.TYPE == "three_decker":
            lenght = 3
        elif self.TYPE == "four_decker":
            lenght = 4
            
        if self.ANGLE == 0 or self.ANGLE == -180:
            side = [0, 1]
        if self.ANGLE == -90 or self.ANGLE == -270:
            side = [1, 0]
        print(self.CELL)
        for cell in range(lenght):
            if self.SIDE == "player":
                data.player_map[self.CELL[0] + side[0] * cell][self.CELL[1] + side[1] * cell] = 1
                self.X = 64
            if self.SIDE == "enemy":
                data.enemy_map[self.CELL[0] + side[0] * cell][self.CELL[1] + side[1] * cell] = 1
                self.X = 650
        self.Y = 300 + 32 * self.CELL[0]
        self.X += 32 * self.CELL[1]
    #Отображение корабля
    def blit_ship(self, screen, file=0):
        if self.TYPE == "one_decker":
            lenght = 1
        elif self.TYPE == "two_decker":
            lenght = 2
        elif self.TYPE == "three_decker":
            lenght = 3
        elif self.TYPE == "four_decker":
            lenght = 4
        if file == 0: image = pygame.image.load(path.path_to_file(f"images\\ships\\{self.TYPE}.png"))
        else: image = pygame.image.load(path.path_to_file(f"images\\ships\\tank.png"))
        image = pygame.transform.scale(image, (32 * lenght, 32))
        image = pygame.transform.rotate(image, self.ANGLE)
        screen.blit(image, (self.X, self.Y))