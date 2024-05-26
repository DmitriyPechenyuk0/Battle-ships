import pygame, modules.data_base as data, modules.path_file as path, modules.place_player_ships as place, modules.bot as bot, modules.music as music, modules.ship as ship
#Класс кнопки
class Button:
    def __init__(self, x = 0, y = 0, width = 200, height = 66, text = 0, action = None, state = "hidden"):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.TEXT = text
        self.ACTION = action
        self.STATE = state
    #Проверка кликов
    def check_click(self, act):
        if (self.X < pygame.mouse.get_pos()[0] < self.X + self.WIDTH and
            self.Y < pygame.mouse.get_pos()[1] < self.Y + self.HEIGHT):
            if self.STATE != "hidden":
                if act == True:
                    self.STATE = "click"
                    print("click")
                elif act == "Up" and self.STATE == "click":
                    print("act")
                    self.ACTION()
                    self.STATE == "hidden"
                elif act == False:
                    print("hover")
                    self.STATE = "hover"     
                else:
                    print("???")      
    def blit_button(self, screen):
        return_data = False
        font = pygame.font.Font(path.path_to_file("font\\EightBits.ttf"), 50)
        if self.STATE != "hidden": screen.blit(pygame.transform.scale(pygame.image.load(path.path_to_file("images\\another\\button_unpressed.png")), (self.WIDTH, self.HEIGHT)), (self.X, self.Y))
        if self.STATE != "showed" and self.STATE != "hidden": return_data = pygame.SYSTEM_CURSOR_HAND
        if self.STATE != "hidden": screen.blit(font.render(self.TEXT, True,(0, 0, 0)), (self.X + self.WIDTH // 4, self.Y + self.HEIGHT // 7))
        return return_data
#Створення Кнопки "reset"
def reset():
    def create_map():
        map = [[]]
        for col in range(10):
            for row in range(10):
                map[col].append(0)
            map.append([])
        return map
    data.player_map = create_map()
    data.enemy_map = create_map()
    data.effect_list = []
    data.ship_list = []
    bot.place_bot_ships()
    data.unplaced_ship = ship.Ship("four_decker", "player", [0,0,0], None, 0)
    place.ship_num = 0
    music.music_num = 0
    music.music_place = True
    data.winner = None
def ok():
    data.fight_started = True

button_reset = Button(x = 400, y = 600, text = "RESET", action = reset, state = "showed")
button_ok = Button(x = 400, y = 600, text = "OK", action = ok)
button_done = Button(x = 400, y = 317, text = "DONE", action = reset)