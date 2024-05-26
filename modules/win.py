import modules.data_base as data, pygame, modules.path_file as path, random
player_ship_cells = 100
enemy_ship_cells = 100
scan_finished = 0
win_sound_played = 0
#Сканирование кораблей ячеек
def scan_ship_cells():
    global scan_finished, enemy_ship_cells, player_ship_cells
    if scan_finished + 1 == True:
        player_ship_cells = 0
        enemy_ship_cells = 0
        for row in data.player_map:
            for cell in row:
                if cell == 1:
                    player_ship_cells += 1
        for row in data.enemy_map:
            for cell in row:
                if cell == 1:
                    enemy_ship_cells += 1
        scan_finished = 1
#Сканирование победы
def scan_victory(frame):
    if frame % 20 == 0:
        global enemy_ship_cells, player_ship_cells
        player_exploded_ship_cells = 0
        enemy_exploded_ship_cells = 0
        for row in data.player_map:
            for cell in row:
                if cell == 4:
                    player_exploded_ship_cells += 1
        for row1 in data.enemy_map:
            for cell1 in row1:
                if cell1 == 3:
                    enemy_exploded_ship_cells += 1  
                    print("one enemy done")
        print(f"Player exploded/ships: {player_exploded_ship_cells}/{player_ship_cells}; \nEnemy exploded/ship: {enemy_exploded_ship_cells}/{enemy_ship_cells}")
        if enemy_ship_cells <= enemy_exploded_ship_cells:
            return "player"
        elif player_exploded_ship_cells >= player_ship_cells:
            return "enemy"
#Победный экран
def win_screen(winner, screen):
    global win_sound_played
    if winner == "enemy":
        sound = pygame.mixer.Sound(path.path_to_file("sounds\\lose_sound.mp3"))
        win_image = pygame.image.load(path.path_to_file("images\\another\\lose_screen.png"))
    elif winner == "player":
        sound = pygame.mixer.Sound(path.path_to_file(f"sounds\\win_sound-{random.randint(1,2)}.mp3"))
        win_image = pygame.image.load(path.path_to_file("images\\another\\victory_screen.png"))
    if win_sound_played + 1 == True:
        sound.set_volume(data.volume)
        sound.play()

        win_sound_played = 1
    screen.blit(pygame.transform.scale(win_image, pygame.display.get_window_size()), (0,0))