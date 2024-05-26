# 0 - Пустота
# 1 - Корабль
# 2 - Занято
# 3 - Промах
# 4 - Взрыв
# 5 - Наведение
# 6 - Наведено, корабль
# 7 - Нажато
# 8 - Нажато, корабль

def create_map():
    map = [[]]
    for col in range(10):
        for row in range(10):
            map[col].append(0)
        map.append([])
    return map
   
winner = None
player_map = create_map()
fight_started = False
volume = 0.7
enemy_map = create_map()
effect_list = []
ship_list = []
unplaced_ship = ""