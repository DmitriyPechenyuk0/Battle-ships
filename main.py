import pygame
import modules.data_base as data
import modules.playing_field as m_field
import modules.path_file as path
import modules.ship as ship
import modules.place_player_ships as place
import modules.shoot as sh
import modules.bot as bot
import modules.music as music
import modules.win as win
import modules.button as button

pygame.init()

bot.place_bot_ships()
print("end place")
screen = pygame.display.set_mode((1000, 700))
data.unplaced_ship = ship.Ship("four_decker", "player", [0,0,0], None, 0)

pygame.display.set_caption("Морський бій")
pygame.display.set_icon(pygame.image.load(path.path_to_file("images\\another\\icon.png")))

FPS = 60
step = "player"
clock = pygame.time.Clock()
# data.ship_list.append(ship.Ship("four_decker", "player", [0,0], "Calm", 0))
t=0
repeat = 0
main = True
mouse_press = False
mouse_click = False
mouse = False
cursor = pygame.SYSTEM_CURSOR_ARROW
while main:
    if data.winner == None:
        music.play_music(place.ship_num < 10)
        m_field.all_fields(screen, t, repeat)
    mouse_press = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            main = False 
        if   pygame.key.get_pressed()[pygame.K_MINUS]==1 and t==0: t=1
        elif pygame.key.get_pressed()[pygame.K_MINUS]==1 and t==1: t=0
        if event.type == pygame.MOUSEBUTTONDOWN: 
            place.choose_ship()
            mouse_click = True
            mouse_press = True
        elif event.type == pygame.MOUSEBUTTONUP: 
            if place.ship_num < 10: place.place_ship()
            mouse_press = "Up"
            mouse_click = False
        # print(f"Mouse Button Down: {event.type==pygame.MOUSEBUTTONDOWN}; \nMouse Button Up: {event.type==pygame.MOUSEBUTTONUP}")
        place.rotate_ship()
        place.move_ship()
    # Часть кнопок - Начало
    if repeat % 10 == 0:
        if place.ship_num >= 10 and data.fight_started == False:
            button.button_ok.STATE = "showed"
            button.button_reset.STATE = "hidden"
        else:
            button.button_reset.STATE = "showed"
            button.button_ok.STATE = "hidden"
        if data.winner == None:
            if place.ship_num < 10 or data.fight_started != False:
                button.button_reset.STATE = "showed"
            button.button_done.STATE = "hidden"
        else:
            button.button_reset.STATE = "hidden"
            button.button_done.STATE = "showed"
        
    if data.winner == None:
        if place.ship_num >= 10:
            win.scan_ship_cells()
        data.winner = win.scan_victory(repeat)
        cursor = pygame.SYSTEM_CURSOR_ARROW
    if data.winner != None:
        win.win_screen(data.winner, screen)
    button_ok_data    = button.button_ok.blit_button(screen)
    button_done_data  = button.button_done.blit_button(screen)
    button_reset_data = button.button_reset.blit_button(screen)

    if button_ok_data != False:    cursor = button_ok_data   
    if button_done_data != False:  cursor = button_done_data 
    if button_reset_data != False: cursor = button_reset_data
    button.button_ok.check_click(mouse_press)
    button.button_done.check_click(mouse_press)
    button.button_reset.check_click(mouse_press)
    music.blit_slider(screen)
    # sh.hover_and_shoot(mouse_press)
    clock.tick(FPS)
    if data.winner == None and data.fight_started == True:
        if place.ship_num >= 10:
            pl_data = sh.hover_and_shoot(mouse_press)
            if pl_data[1] != False: cursor = pl_data[1]
            if step == "player" and pl_data[0] == True:
                step = "enemy"
            elif step == "enemy" and bot.bot_shoot(repeat):
                step = "player"
    
        # ship.place_ship()
    music.move_slider_button(mouse_click)
    if music.mouse != False: cursor = music.mouse
    # print(cursor)
    if cursor != None: pygame.mouse.set_cursor(cursor)
    pygame.display.flip()
    repeat += 1