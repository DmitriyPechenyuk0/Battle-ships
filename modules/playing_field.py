import modules.path_file as path
import pygame
import modules.data_base as data
import modules.effects as effect
import modules.place_player_ships as place
pygame.init()
#Функция игрового поля
def playing_field(screen, x):
    y = 300
    for col in range (10):
        for row in range (10):
            # if data.player_map[col][row] != 2:
            screen.blit(pygame.transform.scale(pygame.image.load(path.path_to_file("images\\another\\cell.png")), (32,32)), (x, y))

            x += 32
        x -= 320 
        y += 32
#Функция цифр на поле
def numbers_on_field(screen, x = 0, y = 270):
    font = pygame.font.Font(path.path_to_file("font\\EightBits.ttf"),32)
    
    for number in range(10):
        # print(number+1)
        text = font.render(str(number+1), True, (0,0,0))
        screen.blit(text, (x, y))
        x += 32
#Функция букв на поле
def letters_on_field(screen, x = 0, y = 295):
    letter_list = ["a","b","c","d","e","f","g","h","i","j"]
    font = pygame.font.Font(path.path_to_file("font\\EightBits.ttf"), 32)
    for number in range(10):
        text = font.render(letter_list[number], True, (0,0,0))
        screen.blit(text, (x, y))
        y += 32
#Функция всех полей
def all_fields(screen,t, repeat):
        screen.fill((255,255,255))
        screen.blit(pygame.image.load(path.path_to_file("images\\another\\back.png")), (0,0))
        screen.blit(pygame.image.load(path.path_to_file("images\\another\\logo.png")), (350, 5))
        letters_on_field(screen, 50)
        letters_on_field(screen, 630)
        numbers_on_field(screen, 70)
        numbers_on_field(screen, 656)
        playing_field(screen, 64)
        playing_field(screen, 650)  
        for ship in data.ship_list:
            if ship.SIDE == "player":
                ship.blit_ship(screen,t)      
        for effect in data.effect_list:
            effect.blit_effect(screen)
        if place.ship_num < 10: data.unplaced_ship.blit_ship(screen)