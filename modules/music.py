import pygame, modules.path_file as path, modules.data_base as data
pygame.mixer.init()
pygame.init()
music_num = 0
music = pygame.mixer.Sound(path.path_to_file("sounds\\place_ships_theme.mp3"))
music_place = True
#музыка
def play_music(ships_placed):
    global music_place, music, music_num
    if ships_placed:
        if music_place or pygame.mixer.Sound.get_num_channels(music) < 1:
            pygame.mixer.Sound.fadeout(music, 100)
            music = pygame.mixer.Sound(path.path_to_file(f"sounds\\battle_theme_{music_num + 1}.mp3"))
            pygame.mixer.Sound.set_volume(music, 0.3)
            pygame.mixer.Sound.play(music)
            music_num += 1
            music_place = False
            if music_num > 2:
                music_num = 0
    music.set_volume(data.volume * 0.7)

'''
   slider_button - Часть ползунка, за которую мы тянем, в отличии от всех, 
   его координаты указывают на его центр, а не на верхний левый угол
'''

slider_x, slider_y = 650, 35
slider_width, slider_height = 300, 30
slider_button_width, slider_button_height = 40, 40
slider_button_state = 0
slider_button_x, slider_button_y = 650 + data.volume * slider_width, 50
mouse = pygame.SYSTEM_CURSOR_ARROW
def move_slider_button(mouse_pressed):
    global slider_button_state, slider_button_x, slider_button_y, slider_button_width, slider_button_height, slider_x, slider_y, slider_width, slider_height, mouse
    if (slider_x < pygame.mouse.get_pos()[0] < slider_x + slider_width and
        slider_y < pygame.mouse.get_pos()[1] < slider_y + slider_height or
        slider_button_state == "click"):
        # print("in slider")
        if (slider_button_x - slider_button_width // 2  < pygame.mouse.get_pos()[0] < slider_button_x + slider_button_width // 2 and
            slider_button_y - slider_button_height // 2 < pygame.mouse.get_pos()[1] < slider_button_y + slider_button_height // 2 or
            slider_button_state == "click"):
            # print("in slider button")
            if mouse_pressed == True:
                # print("click")
                data.volume = (pygame.mouse.get_pos()[0] - slider_x) // (slider_width // 100) / 100
                slider_button_x = pygame.mouse.get_pos()[0]
                slider_button_state = "click"
                mouse = pygame.SYSTEM_CURSOR_HAND
                if pygame.mouse.get_pos()[0] < slider_x:
                    slider_button_x = slider_x
                    data.volume = 0
                elif pygame.mouse.get_pos()[0] > slider_x + slider_width:
                    slider_button_x = slider_x + slider_width
                    data.volume = 1.0
            else: 
                slider_button_state = "hover"
                mouse = pygame.SYSTEM_CURSOR_HAND
        else:
            slider_button_state = None
            mouse = False
            # print("no slider button")
    else: 
        slider_button_state = None
        mouse = False
        # print("Nope")

def blit_slider(screen):
    global slider_button_state, slider_button_x, slider_button_y, slider_button_width, slider_button_height, slider_x, slider_y, slider_width, slider_height, mouse
    screen.blit(pygame.transform.scale(pygame.image.load(path.path_to_file("images\\another\\slider.png")), (slider_width, slider_height)), (slider_x, slider_y))
    screen.blit(pygame.transform.scale(pygame.image.load(path.path_to_file("images\\another\\slider_button.png")), (slider_button_width, slider_button_height)), (slider_button_x - slider_button_width // 2, slider_button_y - slider_button_height // 2))
    font = pygame.font.Font(path.path_to_file("font\\EightBits.ttf"), 32)
    screen.blit(font.render(f"{int(data.volume*100//1)}%", True, (0, 0, 0)), (slider_x + slider_width / 2, slider_y + slider_height * 1.5))