# "Крестики нолики" - подготовка матрицы для игры;

# Функция отрисовывающая игровую матрицу;
def demonstration_matrix():
    for i in range(0, 4):
        for j in range(0, 4):
            print(game_matrix[i][j], " ", end=" ")
        print()

# Проверка на собраные линии. Аргумент "X" если проверяем крестики, "O" если проверяем нолики;
def matrix_checking(verification_object):
    # Проверяем строки и столбцы на линию из контролируемого объекта;
    cont_line = 0
    cont_column = 0
    cont_diagonal_1 = 0
    cont_diagonal_2 = 0
    for i in range(1, 4):
        for j in range(1, 4):
            if game_matrix[i][j] == verification_object:
                cont_line = cont_line + 1
            if game_matrix[j][i] == verification_object:
                cont_column = cont_column + 1
            if cont_line == 3 or cont_column == 3:
                return verification_object
        cont_line = 0
        cont_column = 0
    # Проверяем диагонали на линию из контролируемого объекта;
    for i in range(1, 4):
        if game_matrix[i][i] == verification_object:
            cont_diagonal_1 = cont_diagonal_1 + 1
        if game_matrix[i][4 - i] == verification_object:
            cont_diagonal_2 = cont_diagonal_2 + 1
        if cont_diagonal_1 == 3 or cont_diagonal_2 == 3:
            return verification_object

# заполнение матрицы 3 на 3 символом "-" он будет обозначать незанятое поле;
game_matrix = []
for i in range(4):
    game_matrix.append(["-"] * 4)
for j in range(0, 4):
    game_matrix[0][j] = game_matrix[j][0] = j

# Инициализируем право хода. Первыми ходят "крестики".
# Если right_of_way = True ходят "крестики, если False "Нолики";
right_of_way = True
# Иницилизация проверки что поле введено и оно корректно;
allowed_field_entered = False
# Иницилизация переменных поля и строки;
line = 0
column = 0
final_status = 0  # Переменная содержащая итоговый результат;
occupied_fields = 0  # Переменная для подсчёта занятых полей;

# Вывод игрового поля и объявление действия;
demonstration_matrix()

while True:  # Основной цикл;
    # Блок ввода значений для очередного хода с проверкой правильности введённых значений.
    # Если значения выходят за диапазон или на это поле уже заполнено предлагается повторить ввод;
    while True:
        if allowed_field_entered is True:
            break
        while True:
            if right_of_way is True:
                s_X = input("Сейчас ходят КРЕСТИКИ."
                            " Введите через пробел номер строки и номер столбца: ")
                if len(s_X) == 3 and s_X[0].isdigit() and s_X[1] == " " and s_X[2].isdigit():
                    line = int(s_X[0])
                    column = int(s_X[2])
                    break
                else:
                    demonstration_matrix()
                    print("Ввод осуществлён не по правилам, придётся повторить. ")

            if right_of_way is False:
                s_O = input("Сейчас ходят НОЛИКИ."
                            " Введите через пробел номер строки и номер столбца: ")
                if len(s_O) == 3 and s_O[0].isdigit() and s_O[1] == " " and s_O[2].isdigit():
                    line = int(s_O[0])
                    column = int(s_O[2])
                    break
                else:
                    demonstration_matrix()
                    print("Ввод осуществлён не по правилам, придётся повторить. ")

        # проверка на вхождение;
        if (3 < line) or (line < 1) or (3 < column) or (column < 1):
            demonstration_matrix()
            print(f"Недопустимое значение!!! Поля {line},{column} не существует. Повторите ввод пожайлуста:")
            line = 0
            column = 0
        # проверка на занятость поля;
        elif game_matrix[line][column] != "-":
            demonstration_matrix()
            print(f"Недопустимое значение!!! Поле {line},{column} Уже занято. Повторите ввод пожайлуста:")
            line = 0
            column = 0
        else:
            allowed_field_entered = True

    # Запись крестика или нолика в игровую матрицу;
    if right_of_way is True:
        game_matrix[line][column] = "X"
    if right_of_way is False:
        game_matrix[line][column] = "O"
    demonstration_matrix()

    # Блок проверки условий завершения игры в случае победы одной из сторон;
    final_status = matrix_checking("X")  # Проверяем матрицу на линию из крестиков;
    if final_status == "X":
        break
    final_status = matrix_checking("O")  # Проверяем матрицу на линию из ноликов;
    if final_status == "O":
        break

    # Блок проверки условий завершения игры в случае заполнения всех полей;
    occupied_fields = 0
    for i in range(1, 4):
        for j in range(1, 4):
            if game_matrix[i][j] != "-":
                occupied_fields = occupied_fields + 1
    if occupied_fields == 9:
        final_status = 3
        break

    # Передача хода. Подготовка для ввода нового поля;
    allowed_field_entered = False
    if right_of_way is True:
        right_of_way = False
    elif right_of_way is False:
        right_of_way = True
    line = 0
    column = 0

# Вывод итогов игры;
if final_status == 3:
    print("Игра завершена!!! Зафиксирована боевая НИЧЬЯ!!!")
elif final_status == "X":
    print("Игра завершена!!! Зафиксирована победа КРЕСТИКОВ!!!")
elif final_status == "O":
    print("Игра завершена!!! Зафиксирована победа НОЛИКОВ!!!")
