import pygame
import modules.data_base as data 
import modules.ship as ship
data.unplaced_ship = ship.Ship("four_decker", "player", [0,0,0], None, 0)
data.unplaced_ship.X, data.unplaced_ship.Y = 16, 16
ships = ["three_decker", "three_decker", "two_decker",
         "two_decker","two_decker", "one_decker",
         "one_decker","one_decker", "one_decker"]
ship_num = 0
rotate_press = 0
#Функция выбора кораблей
def choose_ship():
    global ship_num
    if ship_num < 10:
        # print("choose")
        if data.unplaced_ship.TYPE == "one_decker":
            y_max = 32 
        elif data.unplaced_ship.TYPE == "two_decker":
            y_max = 64
        elif data.unplaced_ship.TYPE == "three_decker":
            y_max = 96
        elif data.unplaced_ship.TYPE == "four_decker":
            y_max = 128
        if data.unplaced_ship.ANGLE == 0 or data.unplaced_ship.ANGLE == -180:
            if 16 < pygame.mouse.get_pos()[0] < 16 + y_max and 16  < pygame.mouse.get_pos()[1] < 48:
                data.unplaced_ship.STATE = "hover"
                print(f"choose succeful (horiz), angle = {data.unplaced_ship.ANGLE}")
        elif data.unplaced_ship.ANGLE == -90 or data.unplaced_ship.ANGLE == -270:
            if 16 < pygame.mouse.get_pos()[0] <  48 and 16 < pygame.mouse.get_pos()[1] < y_max:
                data.unplaced_ship.STATE = "hover"
                print(f"choose succeful (vert), angle = {data.unplaced_ship.ANGLE}")
        else:
            print(f'choose failed. More:\n   Angle: {data.unplaced_ship.ANGLE}, \n   X Mouse/X Min/X Max: {pygame.mouse.get_pos()[0]}/16/{16+y_max} or 48,\n   Y Mouse/Y min/Y max: {pygame.mouse.get_pos()[1]}/16/{16 + y_max} or 48')
#Функция поворота кораблей           
def rotate_ship():
    global rotate_press, ship_num
    if ship_num < 10:
        if pygame.key.get_pressed()[pygame.K_r]:
            if rotate_press == False:
                data.unplaced_ship.ANGLE -= 90
                rotate_press = 1
                # print(rotate_press)
                # print(f"Angle: {data.unplaced_ship.ANGLE}")
                if data.unplaced_ship.ANGLE < -270:
                    data.unplaced_ship.ANGLE = 0
        else: rotate_press = 0; #print(pygame.key.get_pressed()[pygame.K_r])
#Функция передвежения кораблей
def move_ship():
    if ship_num < 10:
        
        
        # print(f"placing, STATE = {data.unplaced_ship.STATE}")
        if data.unplaced_ship.STATE == "hover":
            # print("moving hover unplaced ship")
            x = 64
            y = 300
            cell = None
            if (0 < pygame.mouse.get_pos()[0] - 64 < 320 and
                0 < pygame.mouse.get_pos()[1] - 300 < 320):
                cell = [(pygame.mouse.get_pos()[1] - 300) // 32, (pygame.mouse.get_pos()[0] - 64) // 32]
            if cell!=None:
                # print("cont == cell")
                data.unplaced_ship.CELL = cell
                data.unplaced_ship.X = (pygame.mouse.get_pos()[0] - 64) // 32 * 32 + 64
                data.unplaced_ship.Y = (pygame.mouse.get_pos()[1] - 300) // 32 * 32 + 300
                # print("cont != None == True")
            else:
                # print("to mouse")
                # print(f"X Mouse/Y Mouse = {pygame.mouse.get_pos()[0]}/{pygame.mouse.get_pos()[1]}, cont = {cont}")
                data.unplaced_ship.CELL = [0,0,0]
                data.unplaced_ship.X = pygame.mouse.get_pos()[0]
                data.unplaced_ship.Y = pygame.mouse.get_pos()[1]
#Функция проверки клеток
def check_cells():
    if len(data.unplaced_ship.CELL) == 2: 
        if data.unplaced_ship.TYPE == "one_decker":     lenght = 1
        elif data.unplaced_ship.TYPE == "two_decker":   lenght = 2
        elif data.unplaced_ship.TYPE == "three_decker": lenght = 3
        elif data.unplaced_ship.TYPE == "four_decker":  lenght = 4
        if data.unplaced_ship.ANGLE == -90:     side = [0, 1]
        elif data.unplaced_ship.ANGLE == -270:  side = [1, 0]
        elif data.unplaced_ship.ANGLE == 0:     side = [0, 1]
        elif data.unplaced_ship.ANGLE == -180:   side = [1, 0]
        check_list = 0
        for cell in range(lenght):
            if (-1 < data.unplaced_ship.CELL[0] + side[0] * cell < 10 and
                -1 < data.unplaced_ship.CELL[1] + side[1] * cell < 10):  
                    if data.player_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] + side[1] * cell] == 0:
                        check_list += 1
        return check_list == lenght
#Функция расстановки кораблей по клеткам
def place_stop_cells():
    if data.unplaced_ship.TYPE == "one_decker":     lenght = 1
    elif data.unplaced_ship.TYPE == "two_decker":   lenght = 2
    elif data.unplaced_ship.TYPE == "three_decker": lenght = 3     #    Влево,Вправо
    elif data.unplaced_ship.TYPE == "four_decker":  lenght = 4     # Вверх, Вниз
    if data.unplaced_ship.ANGLE == 0:      side = [0, 1]; side_cells = [1, 0, 1, 0]
    elif data.unplaced_ship.ANGLE == -90:  side = [1, 0]; side_cells = [0, 1, 0, 1]
    elif data.unplaced_ship.ANGLE == -180: side = [0, 1]; side_cells = [1, 0, 1, 0]
    elif data.unplaced_ship.ANGLE == -270: side = [1, 0]; side_cells = [0, 1, 0, 1]
    for cell in range(lenght + 2):
        cell -= 1
        if (-1 < data.unplaced_ship.CELL[0] + side[0] * cell < 10 and
             -1 < data.unplaced_ship.CELL[1] + side[1] * cell < 10):
            if side_cells[0] and data.unplaced_ship.CELL[0] + 1 < 10:
                data.player_map[data.unplaced_ship.CELL[0] + 1][data.unplaced_ship.CELL[1] + side[1] * cell] = 2
            if side_cells[2] and data.unplaced_ship.CELL[0] - 1 > -1:
                data.player_map[data.unplaced_ship.CELL[0] - 1][data.unplaced_ship.CELL[1] + side[1] * cell] = 2
            if side_cells[1] and data.unplaced_ship.CELL[1] + 1 < 10:
                data.player_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] + 1] = 2
            if side_cells[3] and data.unplaced_ship.CELL[1] - 1 > -1:
                data.player_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] - 1] = 2
            data.player_map[data.unplaced_ship.CELL[0] + side[0] * cell][data.unplaced_ship.CELL[1] + side[1] * cell] = 2
#Заверщать расттановку
def end_place():
    global ship_num
    global ships
    data.ship_list.append(data.unplaced_ship)
    data.ship_list[-1].place_ship()
    if ship_num < 9:
        data.unplaced_ship = ship.Ship(ships[ship_num], "player", [0,0,0], None, 0)
        data.unplaced_ship.X =  16
        data.unplaced_ship.Y = 16
    ship_num += 1
#Расттановка кораблей
def place_ship():
    print(f"Placing... Cell: {data.unplaced_ship.CELL}")
    approval_to_place = check_cells()
    if approval_to_place:
        place_stop_cells()
        end_place()
    else: data.unplaced_ship.X, data.unplaced_ship.Y = 16, 16; data.unplaced_ship.CELL = [0,0,0]; data.unplaced_ship.STATE = None
