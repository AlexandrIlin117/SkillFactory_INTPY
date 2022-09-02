#                                              Игра "Морской бой."
#                                 ----- Обозначение полей и формат ввода -----
#                                 '•' - поле доступное для выстрела;
#                                 '@' - вы уже стреляли сюда.
#                                 'X' - поражённая палуба
#                                 '4 3' - строка 4, столбец 3.Подвердите нажав на Enter.

# Для отладки доску CPU можно сделать видимой установив 1 в классе Game для аргумента "self.s_cpu = Board(0)";
# Для отладки этап установки кораблей игроком можно пропустить. Установив при вызове экземпляра класса входной параметр
# класса Game в 1;

# Импортируем модуль random;
import random


# Класс Board отвечает за генерацию положения кораблей на поле, передачу их координат классу Ships.
# Его экземпляры хранят состояние игры необходимое её отображения и обработки;
class Board:

    def __init__(self, display=1):
        self.s_board_filds = []
        self.basic_board_filling()
        self.display = display  # атрибут запоминающий нужна ли видимость доски 1 - нужна, 0 - нет;
        self.flotilla_coordinates = []

    def basic_board_filling(self, s_sym=["R"]):  # заполнение доски при инициализации класса
        self.s_sym = s_sym
        for r in range(7):
            self.s_board_filds.append(s_sym * 7)

    def ship_outline(self, sh_out="*",
                     s_ship_out=[]):  # Устанавливает запрет на установку корабля рядям с установленым;
        for i, j in enumerate(s_ship_out):
            if (int(j[1]) - 1) > 0:
                if self.s_board_filds[j[0]][j[1] - 1] != "▒" and self.s_board_filds[j[0]][j[1] - 1] != "X":
                    self.s_board_filds[j[0]][j[1] - 1] = sh_out  # помечаем контур слева от корабля;
            if (int(j[1]) + 1) < 7:
                if self.s_board_filds[j[0]][j[1] + 1] != "▒" and self.s_board_filds[j[0]][j[1] + 1] != "X":
                    self.s_board_filds[j[0]][j[1] + 1] = sh_out  # помечаем контур слева от корабля;

            if (int(j[0]) - 1) > 0:
                if self.s_board_filds[j[0] - 1][j[1]] != "▒" and self.s_board_filds[j[0] - 1][j[1]] != "X":
                    self.s_board_filds[j[0] - 1][j[1]] = sh_out  # помечаем контур сверху от корабля;
            if (int(j[0]) + 1) < 7:
                if self.s_board_filds[j[0] + 1][j[1]] != "▒" and self.s_board_filds[j[0] + 1][j[1]] != "X":
                    self.s_board_filds[j[0] + 1][j[1]] = sh_out  # помечаем контур снизу от корабля;

            if (int(j[0]) - 1) > 0 and (int(j[1]) + 1) < 7:
                if self.s_board_filds[j[0] - 1][j[1] + 1] != "▒" and self.s_board_filds[j[0] - 1][j[1] + 1] != "X":
                    self.s_board_filds[j[0] - 1][j[1] + 1] = sh_out  # помечаем контур по диагонали справа наверху;
            if (int(j[0]) + 1) < 7 and (int(j[1]) + 1) < 7:
                if self.s_board_filds[j[0] + 1][j[1] + 1] != "▒" and self.s_board_filds[j[0] + 1][j[1] + 1] != "X":
                    self.s_board_filds[j[0] + 1][j[1] + 1] = sh_out  # помечаем контур по диагонали справа внизу;

            if (int(j[0]) - 1) > 0 and (int(j[1]) - 1) > 0:
                if self.s_board_filds[j[0] - 1][j[1] - 1] != "▒" and self.s_board_filds[j[0] - 1][j[1] - 1] != "X":
                    self.s_board_filds[j[0] - 1][j[1] - 1] = sh_out  # помечаем контур по диагонали слева наверху;
            if (int(j[0]) + 1) < 7 and (int(j[1]) - 1) > 0:
                if self.s_board_filds[j[0] + 1][j[1] - 1] != "▒" and self.s_board_filds[j[0] + 1][j[1] - 1] != "X":
                    self.s_board_filds[j[0] + 1][j[1] - 1] = sh_out  # помечаем контур по диагонали слева внизу;

    def random_board_2(self):
        # Найдём все возможные варианты уставновки кораблей согласно последовательности sequence_ships;
        # Количество палуб в обработке опеределяется переменной len_ship ;
        # Для каждого корабля будет формироваться список возможных вариантов
        # "Доступно для выбора" - available_for_selection_ship;
        # Из него случайным образом будем выбирать один при помощи метода choice;
        choice_control = False  # переменная отвечающая за выход из цикла генерации если она успешно завершена;
        while True:  # цикл повторяющий непосредственно цикл генерации если он имеет тупиковое развитие;
            if choice_control == True:
                break
            t = 0  # Счётчик соответствует числу кораблей установленых на доску;
            sequence_ships = [3, 2, 2, 1, 1, 1, 1]  # последовательность кораблей для установки;
            for sq_ships in sequence_ships:  # Цикл генерации положения кораблей из последовательности на доске;
                len_ship = sq_ships
                available_for_selection = []
                available_for_selection_ship = []
                for i in range(1, 7):
                    for j in range(1, 8 - len_ship):
                        check = 0
                        check_2 = 0
                        for z in range(0, len_ship):
                            if self.s_board_filds[i][j + z] != "R":
                                check = 1
                            if self.s_board_filds[j + z][i] != "R":
                                check_2 = 1
                        if check == 0:
                            for z in range(0, len_ship):
                                available_for_selection.append([i, j + z])
                        if check_2 == 0:
                            for z in range(0, len_ship):
                                available_for_selection.append([j + z, i])
                # Блок проверки вариантов для установки корабля. Если список пуст, доска очищается
                # И процесс генерации начинается сначала;
                for i in range(0, len(available_for_selection), len_ship):
                    available_for_selection_ship.append(available_for_selection[i:i + len_ship])
                if len(available_for_selection_ship) == 0:
                    self.s_board_filds.clear()
                    self.basic_board_filling()
                    self.flotilla_coordinates.clear()
                    break
                else:
                    t = t + 1
                # Выбираем случайный набор из возможных вариантов установки корабля с заданным количеством палуб;
                random_position = random.choice(available_for_selection_ship)
                self.flotilla_coordinates.append(random_position)  # вносим координаты корабля в список флотилии;
                # Присваивам полям состояние занятости этих позиций кораблём;
                for i, j in enumerate(random_position):
                    self.s_board_filds[j[0]][j[1]] = "▒"
                # окружаем корабль по внешней линии признаком "Сюда корабли ставить нельзя"
                self.ship_outline("*", random_position)
            if t == len(sequence_ships):
                choice_control = True
        # После заполнения поля корабляит убираем маркеры "*" которые помогали в инициализации и заполнении поля;
        for i in range(1, 7):
            for j in range(1, 7):
                if self.s_board_filds[i][j] == "*" or self.s_board_filds[i][j] == "R":
                    self.s_board_filds[i][j] = "•"
            print()


# Класс Game обрабатывает состояние экземпляров других классов реализующих игровой процесс согласно правилам
# описываемым методом loop. Так же отвечает за демонстрацию состояния игры.
class Game:
    def __init__(self, mba=1):
        self.s_man = Board(1)
        self.s_cpu = Board(0)  # Поставьте 1 если нужен режим отладки - поле CPU станет видимым;
        self.s_man.random_board_2()
        self.s_cpu.random_board_2()
        self.p_man = PlayerMan(self.s_cpu.s_board_filds)
        self.p_cpu = PlayerCpu(self.s_man.s_board_filds)
        self.f_man = Ships(self.s_man, self.s_man.s_board_filds, self.s_man.flotilla_coordinates)
        self.f_cpu = Ships(self.s_cpu, self.s_cpu.s_board_filds, self.s_cpu.flotilla_coordinates)
        self.mba = mba  # Выбор будет ли предлагаться установка кораблей игроку. 1 - да, 0 - нет;

    def draw(self, s_man, s_cpu):
        self.game_screen = self.s_cpu.s_board_filds.copy()
        for i in range(1, 7):
            for j in range(1, 7):
                if self.s_cpu.display == 1:
                    self.game_screen[i][j] = self.s_cpu.s_board_filds[i][j]
                else:
                    if self.s_cpu.s_board_filds[i][
                        j] == "*" or self.s_cpu.s_board_filds[i][j] == "▒" or self.s_cpu.s_board_filds[i][j] == "R":
                        self.game_screen[i][j] = "•"

        print("                       --- Игра морской бой ---")

        print("          Поле игрока                          Поле CPU  ")
        print(f"    | 1 | 2 | 3 | 4 | 5 | 6 |          | 1 | 2 | 3 | 4 | 5 | 6 |")
        print(f" 1  | {self.s_man.s_board_filds[1][1]} | {self.s_man.s_board_filds[1][2]} | "
              f"{self.s_man.s_board_filds[1][3]} | {self.s_man.s_board_filds[1][4]} | "
              f"{self.s_man.s_board_filds[1][5]} | {self.s_man.s_board_filds[1][6]} |  "
              f"     1  | {self.game_screen[1][1]} | {self.game_screen[1][2]} | "
              f"{self.game_screen[1][3]} | {self.game_screen[1][4]} | "
              f"{self.game_screen[1][5]} | {self.game_screen[1][6]} |               ----- Обозначение полей и формат ввода -----")
        print(f" 2  | {self.s_man.s_board_filds[2][1]} | {self.s_man.s_board_filds[2][2]} | "
              f"{self.s_man.s_board_filds[2][3]} | {self.s_man.s_board_filds[2][4]} | "
              f"{self.s_man.s_board_filds[2][5]} | {self.s_man.s_board_filds[2][6]} |  "
              f"     2  | {self.game_screen[2][1]} | {self.game_screen[2][2]} | "
              f"{self.game_screen[2][3]} | {self.game_screen[2][4]} | "
              f"{self.game_screen[2][5]} | {self.game_screen[2][6]} |               '•' - поле доступное для выстрела;")
        print(f" 3  | {self.s_man.s_board_filds[3][1]} | {self.s_man.s_board_filds[3][2]} | "
              f"{self.s_man.s_board_filds[3][3]} | {self.s_man.s_board_filds[3][4]} | "
              f"{self.s_man.s_board_filds[3][5]} | {self.s_man.s_board_filds[3][6]} |  "
              f"     3  | {self.game_screen[3][1]} | {self.game_screen[3][2]} | "
              f"{self.game_screen[3][3]} | {self.game_screen[3][4]} | "
              f"{self.game_screen[3][5]} | {self.game_screen[3][6]} |               '@' - вы уже стреляли сюда."
              f" Или рядом утонул корабль;")
        print(f" 4  | {self.s_man.s_board_filds[4][1]} | {self.s_man.s_board_filds[4][2]} | "
              f"{self.s_man.s_board_filds[4][3]} | {self.s_man.s_board_filds[4][4]} | "
              f"{self.s_man.s_board_filds[4][5]} | {self.s_man.s_board_filds[4][6]} |  "
              f"     4  | {self.game_screen[4][1]} | {self.game_screen[4][2]} | "
              f"{self.game_screen[4][3]} | {self.game_screen[4][4]} | "
              f"{self.game_screen[4][5]} | {self.game_screen[4][6]} |               'X' - поражённая палуба"
              f" корабля противника;")
        print(f" 5  | {self.s_man.s_board_filds[5][1]} | {self.s_man.s_board_filds[5][2]} | "
              f"{self.s_man.s_board_filds[5][3]} | {self.s_man.s_board_filds[5][4]} | "
              f"{self.s_man.s_board_filds[5][5]} | {self.s_man.s_board_filds[5][6]} |  "
              f"     5  | {self.game_screen[5][1]} | {self.game_screen[5][2]} | "
              f"{self.game_screen[5][3]} | {self.game_screen[5][4]} | "
              f"{self.game_screen[5][5]} | {self.game_screen[5][6]} |               '4 3' - строка 4, столбец 3."
              f" Подтвердите нажав на Enter.")
        print(f" 6  | {self.s_man.s_board_filds[6][1]} | {self.s_man.s_board_filds[6][2]} | "
              f"{self.s_man.s_board_filds[6][3]} | {self.s_man.s_board_filds[6][4]} | "
              f"{self.s_man.s_board_filds[6][5]} | {self.s_man.s_board_filds[6][6]} |  "
              f"     6  | {self.game_screen[6][1]} | {self.game_screen[6][2]} | "
              f"{self.game_screen[6][3]} | {self.game_screen[6][4]} | "
              f"{self.game_screen[6][5]} | {self.game_screen[6][6]} |")

    def manual_board_acceptance(self):  # позволят игроку установить корабли в ручную;
        process_completed_mba = 0
        while True:
            if process_completed_mba == 1:
                break
            self.s_man.s_board_filds.clear()
            self.s_man.basic_board_filling(["•"])
            self.s_man.flotilla_coordinates.clear()
            sequence_ships_mba = [3, 2, 2, 1, 1, 1, 1]
            reset_mba = 0
            for sq_ships_mba in sequence_ships_mba:  # Цикл генерации положения кораблей из последовательности на доске;
                ship_coordinates_mba = []
                checking_cycle_mba = 0
                while True:
                    if checking_cycle_mba == 1:
                        break
                    self.draw(self.s_man.s_board_filds, self.s_man.s_board_filds)
                    print()
                    len_ship_mba = sq_ships_mba
                    print(f"1_Длинна корабля {len_ship_mba} Укажите через пробел откуда "
                          f" сторить корабль указав сначала строку, а потом столбец.")
                    print(
                        f"  Затем через пробел укажите куда строить корабль: U - вверх, D - вниз, L - влево, R - вправо. ")
                    print(f"  Пример правильного ввода: 5 3 U - из поля строка 5 солбец 3 построить корабль вверх.")
                    print(f"  ВАЖНО !!! Для кораблей с 1 палубой ввод направления не обязателен!")
                    print(f"2_Нельзя ставить корабли рядом символ '*' - запрещённая для установки зона;")
                    print(f"3_Вы можете начать процесс установки заново введя слово - RESET;")
                    target_bild_mba = input(f"Введите через пробел из какого поля сторить корабль "
                                            f"указав сначала строку, а потом столбец ?: ")
                    if len(target_bild_mba) == 3 and len_ship_mba == 1:
                        target_bild_mba = target_bild_mba + ' R'
                    if target_bild_mba == "RESET":
                        reset_mba = 1
                        break

                    if (len(target_bild_mba) == 5 and target_bild_mba[0].isdigit() and target_bild_mba[1] == " "
                        and target_bild_mba[2].isdigit() and target_bild_mba[3] == " "
                        and target_bild_mba[4].isalpha() and (target_bild_mba[4] == "U"
                                                              or target_bild_mba[4] == "D"
                                                              or target_bild_mba[4] == "L"
                                                              or target_bild_mba[4] == "R")) is False:
                        print()
                        print("Ввод осуществлён не по правилам, придётся повторить. ")
                        continue
                    if (target_bild_mba[4] == "R" and int(target_bild_mba[2]) + len_ship_mba > 7) \
                            or (target_bild_mba[4] == "L" and int(target_bild_mba[2]) - len_ship_mba < 0) \
                            or (target_bild_mba[4] == "D" and int(target_bild_mba[0]) + len_ship_mba > 7) \
                            or (target_bild_mba[4] == "U" and int(target_bild_mba[0]) - len_ship_mba < 0)\
                            or int(target_bild_mba[2]) <= 0  or int(target_bild_mba[0]) <= 0\
                            or  int(target_bild_mba[2]) >= 0  or int(target_bild_mba[0]) >= 0:
                        print()
                        print("------------ Нет смысла строить. Корабль выходит за пределы поля. ------------")
                        continue
                    if target_bild_mba[4] == "R":
                        way_ck = 0
                        for i in range(0, len_ship_mba):
                            # print(self.s_man.s_board_filds[int(target_bild_mba[0])][int(target_bild_mba[2]) + i])
                            if self.s_man.s_board_filds[int(target_bild_mba[0])][int(target_bild_mba[2]) + i] == "▒" \
                                    or self.s_man.s_board_filds[int(target_bild_mba[0])][
                                int(target_bild_mba[2]) + i] == "*":
                                print()
                                print(
                                    "-- На пути постройки другой корабль или зона вокруг него. Выберите другое место. --")
                                way_ck = 1
                                break
                    if target_bild_mba[4] == "L":
                        way_ck = 0
                        for i in range(0, len_ship_mba):
                            if self.s_man.s_board_filds[int(target_bild_mba[0])][int(target_bild_mba[2]) - i] == "▒" \
                                    or self.s_man.s_board_filds[int(target_bild_mba[0])][
                                int(target_bild_mba[2]) - i] == "*":
                                print()
                                print(
                                    "-- На пути постройки другой корабль или зона вокруг него. Выберите другое место. --")
                                way_ck = 1
                                break
                    if target_bild_mba[4] == "D":
                        way_ck = 0
                        for i in range(0, len_ship_mba):
                            if self.s_man.s_board_filds[int(target_bild_mba[0]) + i][int(target_bild_mba[2])] == "▒" \
                                    or self.s_man.s_board_filds[int(target_bild_mba[0]) + i][
                                int(target_bild_mba[2])] == "*":
                                print()
                                print(
                                    "-- На пути постройки другой корабль или зона вокруг него. Выберите другое место. --")
                                way_ck = 1
                                break
                    if target_bild_mba[4] == "U":
                        way_ck = 0
                        for i in range(0, len_ship_mba):
                            if self.s_man.s_board_filds[int(target_bild_mba[0]) - i][int(target_bild_mba[2])] == "▒" \
                                    or self.s_man.s_board_filds[int(target_bild_mba[0]) - i][
                                int(target_bild_mba[2])] == "*":
                                print()
                                print(
                                    "-- На пути постройки другой корабль или зона вокруг него. Выберите другое место. --")
                                way_ck = 1
                                break
                    if way_ck == 1:
                        continue
                    else:
                        print("------- Проверка пройдена. Устанавливаем корабль на поле. -------")
                        if target_bild_mba[4] == "R":
                            for i in range(0, len_ship_mba):
                                self.s_man.s_board_filds[int(target_bild_mba[0])][int(target_bild_mba[2]) + i] = "▒"
                                ship_coordinates_mba.append([int(target_bild_mba[0]), int((target_bild_mba[2])) + i])
                            self.s_man.flotilla_coordinates.append(ship_coordinates_mba)
                            self.s_man.ship_outline("*", ship_coordinates_mba)
                            checking_cycle_mba = 1
                        if target_bild_mba[4] == "L":
                            for i in range(0, len_ship_mba):
                                self.s_man.s_board_filds[int(target_bild_mba[0])][int(target_bild_mba[2]) - i] = "▒"
                                ship_coordinates_mba.append([int(target_bild_mba[0]), int((target_bild_mba[2])) - i])
                            self.s_man.flotilla_coordinates.append(ship_coordinates_mba)
                            self.s_man.ship_outline("*", ship_coordinates_mba)
                            checking_cycle_mba = 1
                        if target_bild_mba[4] == "D":
                            for i in range(0, len_ship_mba):
                                self.s_man.s_board_filds[int(target_bild_mba[0]) + i][int(target_bild_mba[2])] = "▒"
                                ship_coordinates_mba.append([int(target_bild_mba[0]) + i, int(target_bild_mba[2])])
                            self.s_man.flotilla_coordinates.append(ship_coordinates_mba)
                            self.s_man.ship_outline("*", ship_coordinates_mba)
                            checking_cycle_mba = 1
                        if target_bild_mba[4] == "U":
                            for i in range(0, len_ship_mba):
                                self.s_man.s_board_filds[int(target_bild_mba[0]) - i][int(target_bild_mba[2])] = "▒"
                                ship_coordinates_mba.append([int(target_bild_mba[0]) - i, int(target_bild_mba[2])])
                            self.s_man.flotilla_coordinates.append(ship_coordinates_mba)
                            self.s_man.ship_outline("*", ship_coordinates_mba)
                            checking_cycle_mba = 1

                if reset_mba == 1:
                    break
            if reset_mba != 1:
                process_completed_mba = 1
        # После заполнения поля корабляит убираем маркеры "*" которые помогали в инициализации и заполнении поля;
        for i in range(1, 7):
            for j in range(1, 7):
                if self.s_man.s_board_filds[i][j] == "*" or self.s_man.s_board_filds[i][j] == "R":
                    self.s_man.s_board_filds[i][j] = "•"
            print()
        print()
        print()
        print("     --- Установка кораблей завершена !!! Начнём игру !!! ---")
        print()

    def loop(self):
        print("     Приветствуем Вас! Сейчас начнётся игра 'Морской бой.'!!! ")
        if self.mba == 1:
            print("       Установите свои корабли следуя инструкции на экране.")
            print()
            self.manual_board_acceptance()
        while True:
            # self.draw(self.s_man.s_board_filds, self.s_cpu.s_board_filds)
            while True:
                self.draw(self.s_man.s_board_filds, self.s_cpu.s_board_filds)
                self.p_man.shot_on_field()
                self.f_cpu.check_flotilla()
                if self.f_cpu.caramba == True:
                    break
                if self.f_cpu.additional_move is False:
                    break
            if self.f_cpu.caramba == True:
                self.draw(self.s_man.s_board_filds, self.s_cpu.s_board_filds)
                print()
                print("Вы победили !!! Поздравляем Вас с победой!!!")
                break
            while True:
                self.draw(self.s_man.s_board_filds, self.s_cpu.s_board_filds)
                print("---------------------------- ХОД CPU ----------------------------")
                self.p_cpu.shot_on_field()
                self.f_man.check_flotilla()
                if self.f_man.caramba == True:
                    break
                if self.f_man.additional_move is False:
                    break
            if self.f_man.caramba == True:
                self.draw(self.s_man.s_board_filds, self.s_cpu.s_board_filds)
                print()
                print("Победу одержал Искуственный Интелект, где далеко улыбнулась SkyNet ...")
                break


class Player:  # родительский класс. Метод выбор места выбора будет переопределён для человека и CPU;

    def __init__(self, target_board):
        self.target_board = target_board

    def choosing_shot_place(self):
        self.shot_place = [1, 5]
        return self.shot_place

    def shot_on_field(self):
        shot_place_set = self.choosing_shot_place()
        self.target_board[shot_place_set[0]][shot_place_set[1]] = "@"


# Класс PlayerMan отвечает за выбор поля по которому будет наносится удар игроком человеком;
class PlayerMan(Player):

    def choosing_shot_place(self):
        checking_cycle = 0
        test_exceptions = []  # тренировка обработки иключений. Несколько раз выбрать одно и то же поле будет вызвана
        # обработка исключения ValueError;
        test_exceptions_count = 0
        while True:
            if checking_cycle == 1:
                break
            print()
            self.shot_place = input("Игрок, сейчас ваш ход. Через пробел укажите поле по которому будем"
                                    " стрелять. Сначала строку, потом столбец: ")
            if (len(self.shot_place) == 3 and self.shot_place[0].isdigit() and self.shot_place[1] == " " and
                self.shot_place[2].isdigit()) is False:
                print()
                print("Ввод осуществлён не по правилам, придётся повторить. ")
                continue
            else:
                self.shot_place = list(map(int, self.shot_place.split()))
            try:  # часть обрабатывающая вызываемое исключение;
                if test_exceptions_count == 2:
                    raise ValueError
            except ValueError as e:
                print()
                print("СБОЙ !!! Вы несколько раз подряд вводите одно и то же поле "
                      "которое не может быть принято !!! ВНИМАТЕЛЬНЕЙ !!!")
                test_exceptions_count = 0
            if self.shot_place[0] < 1 or self.shot_place[0] > 6 or self.shot_place[1] < 1 or self.shot_place[1] > 6:
                print()
                print(f"Выбранное поле за пределами карты. Цельтесь точнее пожайлуста. Повторите ввод.")
                continue
            if test_exceptions == self.target_board[self.shot_place[0]][self.shot_place[1]]:
                test_exceptions_count = test_exceptions_count + 1
            if self.target_board[self.shot_place[0]][self.shot_place[1]] == "@" or \
                    self.target_board[self.shot_place[0]][self.shot_place[1]] == "X":  # "•" Alt+7
                print()
                print(f"Вы уже стреляли по этому полю. "
                      f"Нет смысла выполнять выстрел в это поле. Повторите ввод.")
                test_exceptions = self.target_board[self.shot_place[0]][self.shot_place[1]]
                continue
            if self.target_board[self.shot_place[0]][self.shot_place[1]] == "*":  # "•" Alt+7
                print(f"Рядом потопленный корабль. "
                      f"Нет смысла делать это ешё раз. Повторите ввод.")
                continue
            checking_cycle = 1
        return self.shot_place


# Класс PlayerCpu отвечает за выбор поля по которому будет наносится удар игроком CPU;
class PlayerCpu(Player):

    def choosing_shot_place(self):
        list_goals = []
        # СPU составляет список полей по которым он не стрелял;
        for i in range(1, 7):
            for j in range(1, 7):
                if self.target_board[i][j] != "X" and self.target_board[i][j] != "@":
                    list_goals.append([i, j])
        # СPU выбирает их списка случайную цель;
        self.shot_place = random.choice(list_goals)
        return self.shot_place


# Класс Ships хранит список всех кораблей игрока, обрабатывает выстрел сделаный противником и меняет статус поля
# на доске. Возвращает классу Game информацию и необходимости произвести выстрел при попадани в кораль.
# А так же о том что все корабли флотилии уничтожены.
class Ships:

    def __init__(self, board, board_flotilla, list_flotilla):
        self.board = board  # аргумент дающий доступ к методам класса доска
        self.board_flotilla = board_flotilla  # двумерный список доски на которой распологается флотилия;
        self.list_flotilla = list_flotilla  # список координат флотилии;
        self.caramba = False
        self.additional_move = True  # признак получения дополнительного хода в случае попадания;

    # метод класса проверяющий аргумент класса "Корабли" и возвращающий True если она вся потоплена;
    # Кроме того метод проверяет был ли произведённый выстрел по доске "@" попаданием в корабль, если да
    # палуба помечается на доске как поражённая "X". Если корабль потоплен полностью. Вызывается метод доски
    # заполняющий контур вокруг корабля;
    def check_flotilla(self):
        # Проверяем координаты палуб корабля на предмет попадания Если в эту коррдинату был произведён выстрел "@"
        # помечаем это поле на доске как подбитую палубу "X";
        self.additional_move = False
        for z in range(0, len(self.list_flotilla)):
            for i, j in enumerate(self.list_flotilla[z]):
                if self.board_flotilla[j[0]][j[1]] == "@":
                    self.board_flotilla[j[0]][j[1]] = "X"
                    self.additional_move = True
        # Проверяем корабли флотилии на уничтожение, если все палубы поражены вызываем метод доски для заполнения
        # контура вокруг потопленного корабля. Одновременно с этим подсчитываем потопленные корабли. Если все
        # уничтожены устанавливаем статус "КАРАМБА!!!" :) - self.caramba = True;
        ch_caramba = 0
        for z in range(0, len(self.list_flotilla)):
            check_flooding = 0
            for i, j in enumerate(self.list_flotilla[z]):
                if self.board_flotilla[j[0]][j[1]] == "X":
                    check_flooding = check_flooding + 1
                if check_flooding == len(self.list_flotilla[z]):
                    self.board.ship_outline("@", self.list_flotilla[z])
                    ch_caramba = ch_caramba + 1
        if ch_caramba == len(self.list_flotilla):
            self.caramba = True


a = Game(1)  # Выбор будет ли предлагаться установка кораблей игроку. 1 - да, 0 - нет;
a.loop()
