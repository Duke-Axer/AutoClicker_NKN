import pyautogui
import os
import csv


def menu(path):
    path = path + chr(92) + "Data"
    while True:
        clear_cmd()
        print("MENU")
        print_list(("Wczytanie", "Modyfikacja", "Exit"), last_as_0=True)

        while True:
            input_menu = integer(input(), min_=0, max_=2)
            if input_menu[1]:
                input_menu = input_menu[0]
                break
            else:
                print("Opcja: " + str(input_menu[0]) + " nie istnieje, proszę wybrać ponownie")
        # switcher = {
        #     1: openDict(),
        #     2: modifyDict(),
        #     0: close(),
        # }
        # switcher[input_menu]
        if input_menu == 1:
            openDict()
        elif input_menu == 2:
            modify_dict(path)
        elif input_menu == 0:
            close()


def first_test(path):
    print(path)
    path_general = path + chr(92) + "Data"
    try:
        os.chdir(path_general)
    except:
        os.mkdir(path_general)
    print(os.getcwd())


# Otwieranie folderów; do autoclicker
def openDict():
    clear_cmd()
    print("autoclicker")
    pass


def modify_dict(path_dir):

    while True:
        clear_cmd()

        # Wyświetlenie menu
        list_dir = os.listdir(path_dir)
        print("Dodawanie, usuwanie i modyfikacja folderów\n"
              "Wybierz folder lub utwórz nowy")
        print_list(first=list_dir, second=("Utwórz nowy", "Zmień nazwę", "Usuń", "Cofnij"), last_as_0=True)

        # Wpisanie poprawnej wartości
        while True:
            input_menu = integer(input(), min_=-3, max_=len(list_dir))
            if input_menu[1]:
                input_menu = input_menu[0]
                break
            else:
                print("Opcja: " + str(input_menu[0]) + " nie istnieje, proszę wybrać ponownie")

        # Wybierz folder
        if len(list_dir) >= input_menu > 0:
            print("Wybrano folder: " + str(list_dir[input_menu - 1]))
            modify_files(os.chdir(path_dir + chr(92) + str(list_dir[input_menu - 1])))

        # Utwórz nowy
        elif input_menu == -1:
            make_dir(list_dir, path_dir)
        # Zmień nazwę
        elif input_menu == -2:
            rename_dir(path_dir)
        # Usuń
        elif input_menu == -3:
            remove_dir(path_dir)
        # Cofnij
        elif input_menu == 0:
            break


def make_dir(list_dir, path_dir):
    """Tworzy folder,

    :param list_dir: lista utworzonych folderów
    :param path_dir: ścieżka to folderów
    :return:
    """
    while True:
        print("Wpisz nazwę folderu:\n 0 --> Cofnij")
        input_menu = input()

        for i in list_dir:
            if input_menu == i:
                print("Taki folder istnieje\n Wybierz inną nazwę")
        if input_menu == 0:
            return
        break

    print("Tworzę nowy folder: " + input_menu)
    os.mkdir(os.path.join(path_dir, input_menu))
    with open(input_menu + chr(92) + "obiekty.csv", "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["ID", "Name", "X", "Y"])


# Dodawanie, usuwanie, zmieniane nazwy folderów
def remove_dir(path_dir):
    """Usuwa folder jeżeli nie zawiera plików z wyjątkiem "obiekty.csv"

        :param path_dir: Ścieżka z folderami
        :return:
        """
    clear_cmd()

    print("Wybrano usunięcie folderu\n"
          "Aby usunąć folder, musi być pusty\n"
          "Wybierz folder\n")
    list_dir = os.listdir(path_dir)
    print_list(list_dir, second=["Cofnij"], last_as_0=True)

    # Wpisanie poprawnej wartości
    while True:
        input_menu = integer(input(), min_=0, max_=len(list_dir))
        if input_menu[1]:
            input_menu = input_menu[0]
            break
        else:
            print("Opcja: " + input_menu[0] + " nie istnieje, proszę wybrać ponownie")

    if input_menu == 0:
        return
    # Usuwanie folderu
    else:
        list_dir = os.listdir(path_dir + chr(92) + list_dir[input_menu - 1])
        list_dir.remove("obiekty.csv")

        if not list_dir:
            os.remove(os.path.join(path_dir + chr(92) + list_dir[input_menu - 1], "obiekty.csv"))
            print("Wybrano foder" + list_dir[int(input_menu) - 1])
            os.rmdir(os.getcwd() + chr(92) + list_dir[int(input_menu) - 1])
        else:
            print("Folder zawiera pliki!")


def rename_dir(path):
    """Zmienia nazwę folderu

    :param path: Ścieżka z folderami
    :return:
    """
    list_dir = os.listdir(path)

    while True:  # Wybranie folderu
        print("Wybierz który folder ma mieć inną nazwę")
        print_list(list_dir, second=["Cofnij"], last_as_0=True)

        while True:  # Wpisanie poprawnej wartości
            input_menu = integer(input(), min_=0, max_=len(list_dir))
            if input_menu[1]:
                input_menu = input_menu[0]
                break
            else:
                print("Opcja: " + input_menu[0] + " nie istnieje, proszę wybrać ponownie")

        if input_menu == 0:
            break

        else:
            print("Wybrano folder: " + str(list_dir[input_menu - 1]))

            while True:  # Wpisanie nowej nazwy
                print("Wpisz nazwę\n0 --> Cofnij")
                input_name = input()
                if input_name == "0":
                    break

                for i in list_dir:
                    if input_menu == i:
                        print("Taki folder już istnieje")
                        print("Wybierz inną nazwę")
                        continue
                else:
                    print("Zmieniam nazwę folderu na: " + input_name)
                    os.rename(list_dir[input_menu - 1], input_name)
                    break
        break


def rename_sek(path):
    """Zmienia nazwę pliku csv z sekwencją

    :param path: Ścieżka z plikami csv (sekwencjami)
    :return:
    """
    # Wybranie pliku (pętla)
    while True:
        list_dir = os.listdir(path)
        list_dir.remove("obiekty.csv")
        print_list(list_dir, second=["Cofnij"], last_as_0=True)
        print("Wybierz plik")

        while True:  # Wpisanie poprawnej wartości
            input_menu = integer(input(), min_=0, max_=len(list_dir))
            if input_menu[1]:
                input_menu = input_menu[0]
                break
            else:
                print("Opcja: " + input_menu[0] + " nie istnieje, proszę wybrać ponownie")

        if input_menu == 0:
            break

        else:
            print("Wybrano plik: " + str(list_dir[input_menu - 1]))

            # Wybranie nazwy (pętla)
            while True:
                print("Wpisz nazwę\n0 --> Cofnij")
                input_name = input()

                if input_name == 0:
                    break
                elif input_name != "":
                    for i in list_dir:
                        if input_menu == i:
                            print("Taki plik już istnieje, Wybierz inną nazwę!")
                            continue
                    else:
                        print("Zmieniam nazwę pliku na: " + input_name)
                        os.rename(list_dir[input_menu - 1], input_name + ".csv")
                        break


def make_sek(list_dir):
    """Tworzy nową sekwencję

    :param list_dir: lista dostępnych sekwencji (pliki csv)
    :return:
    """
    while True:
        print("Wpisz nazwę sekwencji\n"
              "0 --> Cofnij")
        input_menu = input()
        if input_menu == "0":
            break

        elif input_menu != "":
            for i in list_dir:
                # Czy powtarza się nazwa pliku
                if i == input_menu:
                    print("Taka nazwa już istnieje")
                    continue
            else:
                with open(input_menu + ".csv", "w", encoding='utf-8', newline='') as file:
                    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(["ID", "Name", "Time", "Number", "Speed", "Mouse"])
                break


def remove_sek(path):
    """Usuwa plik csv (sekwencję)

    :param path: Ścieżka z plikami csv (sekwencjami)
    :return:
    """
    list_dir = os.listdir(path)
    list_dir.remove("obiekty.csv")

    print("Wybierz sekwencje do usunięcia")
    print_list(list_dir, second=["Cofnij"], last_as_0=True)

    while True:  # Wpisanie poprawnej wartości
        input_menu = integer(input(), min_=0, max_=len(list_dir))
        if input_menu[1]:
            input_menu = input_menu[0]
            break
        else:
            print("Opcja: " + str(input_menu[0]) + " nie istnieje, proszę wybrać ponownie")

    if input_menu == 0:
        return
    else:
        print("Wybrano sekwencje: " + str(list_dir[input_menu - 1]))
        os.remove(str(list_dir[input_menu - 1]))
        return


def modify_files(path):
    while True:
        clear_cmd()
        list_dir = os.listdir(path)
        list_dir.remove("obiekty.csv")
        print("Dodawanie, usuwanie i modyfikacja sekwencji\n"
              "Wybierz plik lub utwórz nowy")
        print_list(list_dir, second=("Utwórz nowy", "Zmień nazwę", "Usuń", "Obiekty", "Cofnij"), last_as_0=True)

        while True:  # Wpisanie poprawnej wartości
            input_menu = integer(input(), min_=-4, max_=len(list_dir))
            if input_menu[1]:
                input_menu = input_menu[0]
                break
            else:
                print("Opcja: " + str(input_menu[0]) + " nie istnieje, proszę wybrać ponownie")

        if input_menu <= 0:

            if input_menu == 0:
                break

            elif input_menu == -1:
                make_sek(list_dir)

            elif input_menu == -2:
                rename_sek(path)

            elif input_menu == -3:
                remove_sek(path)

            elif input_menu == -4:
                print("dostępne obiekty")
                obiekty(path)

        else:
            print("Wybrano sekwencję ", list_dir[input_menu - 1])
            modify_sek(list_dir[input_menu - 1])


# Dodawanie... plików txt z listą kroków do wykonania i lista wykorzystywanych obiektów
def modify_sek(sek):
    while True:
        clear_cmd()
        print("Dodawanie, usuwanie i modyfikacja sekwencji: ", sek)
        # print("ID --> Name -- Time -- Number -- Speed -- Mouse")
        list_sek = gen_list_sek(sek)

        print_two_dimensional_list(list_sek)
        print_list([], second=("Utwórz nowy", "zmień kolejność", "Usuń", "Cofnij"), last_as_0=True)

        while True:  # Wpisanie poprawnej wartości
            input_menu = integer(input(), min_=-4, max_=0)
            if input_menu[1]:
                input_menu = input_menu[0]
                break
            else:
                print("Opcja: " + str(input_menu[0]) + " nie istnieje, proszę wybrać ponownie")

        if input_menu == 0:
            break
        elif input_menu == -1:
            add_item_in_sek(sek)
        elif input_menu == -2:
            order_sek(sek)
        elif input_menu == -3:
            remove_item_in_sek(list_sek, sek)


def order_sek(sek):
    """Zmienia kolejność wierszy w pliku csv

    :param sek: Ścieżka z plikami csv (sekwencjami)
    :return: Zapisuje zmieniony plik
    """
    while True:
        list_sek = gen_list_sek(sek)
        print_two_dimensional_list(list_sek)
        print_list([], second=["Cofnij"], last_as_0=True)

        print("Wybierz numer")
        while True:  # Wpisanie poprawnej wartości
            first = integer(input(), min_=0, max_=len(list_sek) - 1)
            if first[1]:
                first = first[0]
                break
            else:
                print("Opcja: " + str(first[0]) + " nie istnieje, proszę wybrać ponownie")
        if first == 0:
            break

        print("Wybierz numer")
        while True:  # Wpisanie poprawnej wartości
            second = integer(input(), min_=0, max_=len(list_sek) - 1)
            if second[1]:
                second = second[0]
                break
            else:
                print("Opcja: " + str(second[0]) + " nie istnieje, proszę wybrać ponownie")

        if second == 0:
            break

        for item in list_sek:
            if item[0] == str(first):
                first = list(item)
                break
        for item in list_sek:
            if item[0] == str(second):
                list_sek[int(first[0])][1:] = item[1:]
                list_sek[int(item[0])][1:] = first[1:]
                break

        save_to_csv(sek, list_sek)


def remove_item_in_sek(list_sek, sek):
    """Usuwa wiersz w pliku csv

    :param list_sek: lista dwuwymiarowa sekwencji
    :param sek: Ścieżka z plikami csv (sekwencjami)
    :return: Zapisuje zmieniony plik
    """
    print_two_dimensional_list(list_sek)
    print_list([], second=["Cofnij"], last_as_0=True)

    print("Wybierz wiersz do usunięcia")
    while True:  # Wpisanie poprawnej wartości
        del_item = integer(input(), min_=0, max_=len(list_sek) - 1)
        if del_item[1]:
            del_item = del_item[0]
            break
        else:
            print("Opcja: " + str(del_item[0]) + " nie istnieje, proszę wybrać ponownie")
    if del_item == 0:
        return
    new_list_sek = []
    decrement = 0
    for item in list_sek:
        if item[0] == "ID":
            new_list_sek.append(item)
            continue
        if item[0] == str(del_item):
            decrement = -1
            continue

        new_list_sek.append([str(int(item[0]) + decrement), item[1], item[2], item[3], item[4], item[5]])

        save_to_csv(sek, new_list_sek)


def add_item_in_sek(sek):
    """Pozwala na wpisanie parametrów sekwencji. Wywołuje fukcję zapisu do pliku csv
    parametry: ID, Name, Time, Number, Speed, Mouse

    :param sek: Ścieżka do pliku z sekwencjami
    :return:
    """
    while True:
        list_obiect = objects()
        list_sek = gen_list_sek(sek)
        while True:
            print_two_dimensional_list(list_obiect)
            print("Wybierz obiekt")

            obiect_id = int(input())

            if 1 <= obiect_id <= int(list_obiect[-1][0]):
                if list_obiect[-1][1] == "":
                    print("Wybrany obiekt jest usuniety")
                    continue
                else:
                    print("Wybrano obiekt:")
                    print(list_obiect[obiect_id][0] + " --> " + list_obiect[obiect_id][1] + " -- " +
                          list_obiect[obiect_id][2] + " -- " + list_obiect[obiect_id][3])
                while True:
                    print("Określ czas trwania, liczbę kliknięć, szybkość, przycisk myszki"
                          "\n0 Dla czasu trwania oznacza zakończenie po x kliknięciach"
                          "\n0 Dla liczby kliknięć oznacza zakończenie po x czasie")
                    var_input = [None, None, None, None]
                    for i in range(4):
                        var_input[i] = write_arg_in_item_sek(i)

                    # Zmiana podanych wartości
                    while True:
                        print_two_dimensional_list([[1, "Czas trwania:", var_input[0]],
                                                    [2, "Liczba kliknięć:", var_input[1]],
                                                    [3, "Szybkość:", var_input[2]],
                                                    [4, "Przycisk myszki:", var_input[3]]])
                        if var_input[0] == "0" and var_input[1] == "0":
                            print("Czas trwania i liczba kliknięć nie mogą mieć oba 0\n"
                                  "Wybierz co zmienić: ")
                            var = input()
                            var_input[int(var) - 1] = write_arg_in_item_sek(int(var) - 1)
                        else:
                            print("0 --> Zapisz\n")
                            while True:
                                var = input()
                                if integer(var, is_integer=True, min_=1, max_=4)[1]:
                                    var_input[int(var) - 1] = write_arg_in_item_sek(int(var) - 1)
                                elif var == "0":
                                    break
                        break

                    # Zapisanie danych obiect_id i var_input[0:3] do pliku na ostatnim id
                    list_sek.append([str(len(list_sek)), list_obiect[obiect_id][1], var_input[0],
                                     var_input[1], var_input[2], var_input[3]])
                    save_to_csv(sek, list_sek)
                    break
            break
        break


# Dodawanie elementu w sekwencji
def print_two_dimensional_list(list_2d):
    """Wyświetla tabelę stworzoną z 2-wymiarowej listy

    :param list_2d: lista do wyświetlenia
    """
    # Określenie długości argumentów
    len_arg = []
    for line in list_2d:
        value_number = 0

        for arg in line:
            try:
                if len(arg) > len_arg[value_number]:
                    len_arg[value_number] = len(arg)
            except:
                len_arg.append(len(str(arg)))
            finally:
                value_number += 1

    # Wyświetlenie
    curret_line = str()
    for line in list_2d:
        value_number = 0
        len_last_arg = int()

        for arg in line:
            if value_number == 0:
                curret_line = arg

            elif value_number == 1:
                curret_line = curret_line + " -" + "-" * (len_arg[value_number - 1] - len_last_arg) + ">" + " " + arg
            else:
                curret_line = curret_line + "-" * (len_arg[value_number - 1] - len_last_arg) + " " + arg
            len_last_arg = len(arg)
            value_number += 1
        print(curret_line)


def print_list(first, *, second=None, add=0, last_as_0=False):
    """Wyświetla w czytelny sposób listy

    :param first: lista do wyświetlenia, zlicza od 1 do inf
    :param second: lista do wyświetlenia, zlicza od -1 do -inf
    :param add: Dodanie n razy znaku -
    :param last_as_0: Ostatnia wartość wyświetla się jako 0 dla second,jeżeli second nie istnieje, to dla first
    :return:
    """

    if second is None:
        second = ()
    # Określenie maksymalnej długości 1 argumentu
    if len(str(len(second))) + 1 > len(str(len(first))):
        len_list = len(str(len(second) - 1)) + add if last_as_0 else len(str(len(second))) + add
        len_list += 1
    else:
        len_list = len(str(len(first) - 1)) + add if last_as_0 else len(str(len(first))) + add

    # Wyświetlenie
    i = 1
    if first:
        for arg in first[0:-1]:
            line = str(i) + " -" + "-" * (len_list - len(str(i))) + "> " + arg
            i += 1
            print(line)
        i = 0 if last_as_0 and not second else i
        print(str(i) + " " + "-" * (len_list + 1 - len(str(i))) + "> " + str(first[-1]))
    i = 1
    if second:
        for arg in second[0:-1]:
            line = "-" + str(i) + " -" + "-" * (len_list - len(str(i)) - 1) + "> " + arg
            i += 1
            print(line)
        i = str(0) + " -" if last_as_0 else str(-i) + " "
        print(i + "-" * (len_list + 2 - len(str(i))) + "> " + str(second[-1]))


def save_to_csv(csv_file, lines):
    """Zapisuje listę do pliku csv

    :param csv_file: Ścieżka pliku csv
    :param lines: lista dwuwymiarowa określająca numer wiersza i numer kolumny
    """
    with open(csv_file, "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in lines:
            writer.writerow(line)


def write_arg_in_item_sek(var):
    while True:
        if var == 0:
            print("Określ czas trwania")
        elif var == 1:
            print("Określ liczbę kliknięć")
        elif var == 2:
            print("Określ szybkość")
        elif var == 3:
            print("Określ przycisk myszki\n"
                  "1 --> Lewy\n"
                  "2 --> Prawy")
        var_input = input()
        if var == 0:
            if integer(var_input, is_integer=False, min_=0)[1]:
                return var_input
        elif var == 1:
            if integer(var_input, is_integer=True, min_=0)[1]:
                return var_input

        if var == 2:
            if integer(var_input, is_integer=False, min_=0.1)[1]:
                return var_input

        elif var == 3:
            if integer(var_input, is_integer=True, min_=1, max_=2)[1]:
                return var_input
        else:
            print("Bład: ", var_input)


def gen_list_sek(sek):
    # Zapisanie "ID", "Name", "Time", "Number", "Speed", "Mouse"
    with open(sek) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        list_sek = []
        for line in reader:
            list_sek.append(line)
    return list_sek


# Zwraca listę elementów w sekwencji
def objects():
    # Zapisanie obiektów ID,Name,X,Y
    with open("obiekty.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        list_object = []
        for line in reader:
            list_object.append(line)
    return list_object


# Zwraca listę obiektków
def obiekty(path):
    # Czy plik obiekty.csv istnieje
    list_dir = os.listdir(path)
    i = 1
    for var in list_dir:
        if var == "obiekty.csv":
            break
        i = i + 1
    else:
        print("Brak pliku csv, Tworzenie pliku obiekty.csv")
        with open("obiekty.csv", "w", encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["ID", "Name", "X", "Y"])

    # Wyświetenie obiektów ID,Name,X,Y
    while True:
        list_object = objects()

        print_two_dimensional_list(list_object)
        print_list([], second=("Utwórz nowy", "modyfikuj", "Usuń", "Cofnij"), last_as_0=True)

        while True:  # Wpisanie poprawnej wartości
            input_menu = integer(input(), min_=-3, max_=0)
            if input_menu[1]:
                input_menu = input_menu[0]
                break
            else:
                print("Opcja: " + str(input_menu[0]) + " nie istnieje, proszę wybrać ponownie")

        if input_menu == 0:
            break
        else:
            if input_menu == -1:
                # Dodaje obiekt na pierwszym wolnym ID licząc od 1
                add_object(list_object)

            elif input_menu == -2:
                # zmienia Name, x lub y
                modify_object(list_object)

            else:  # input_menu == -3
                # powinno sprawdzić czy jakieś sekwencje wykorzystują dany obiekt (teraz nie sprawdza)
                del_object(list_object)


def add_object(list_object):
    i = 1
    dodaj_obiekt = input_object(list_object)
    # Sprawdzenie czy jest wolne miejsce
    while i < len(list_object):
        if list_object[i][1] == "":  # jest wolne
            list_object[i] = [i, dodaj_obiekt[0], dodaj_obiekt[1], dodaj_obiekt[2]]
            break
        i += 1
    else:
        list_object.append([i, dodaj_obiekt[0], dodaj_obiekt[1], dodaj_obiekt[2]])

    print("Zapisanie w lini nr " + str(i))
    save_to_csv("obiekty.csv", list_object)
    return


def input_object(list_object):
    """Funkcja pyta o parametry: Nazwa, x, y.

    :return: Zwraca: Nazwa, x, y
    """
    while True:
        print("Podaj nazwę")
        input_name = input()
        for name in list_object:
            print(name[1])
            if name[1] == input_name:
                print("Zła nazwa")
                break
        else:
            if input_name != "":
                break
            else:
                print("Zła nazwa")

    while True:
        print("Podaj x")
        while True:  # Wpisanie poprawnej wartości
            x = integer(input(), min_=0)
            if x[1]:
                x = x[0]
                break
            else:
                print("Zła wielkość x: " + str(x[0]))
        break

    while True:
        print("Podaj y")
        while True:  # Wpisanie poprawnej wartości
            y = integer(input(), min_=0)
            if y[1]:
                y = y[0]
                break
            else:
                print("Zła wielkość y: " + str(y[0]))
        break
    return input_name, x, y


def modify_object(list_object):
    """Modyfikacja zapisanych obiektów

    :param list_object: Lista obiektów
    :return:
    """
    print_two_dimensional_list(list_object)
    print_list([], second=["Cofnij"], last_as_0=True)
    print("Wybierz obiekt do modyfikacji")

    while True:  # Wpisanie poprawnej wartości
        input_menu = integer(input(), min_=0, max_=len(list_object))
        if input_menu[1]:
            input_menu = input_menu[0]
            break
        else:
            print("Opcja: " + str(input_menu[0]) + " nie istnieje, proszę wybrać ponownie")

    if input_menu == 0:
        return
    else:
        dodaj_obiekt = input_object(list_object)
        list_object[input_menu] = [input_menu, dodaj_obiekt[0], dodaj_obiekt[1], dodaj_obiekt[2]]
        save_to_csv("obiekty.csv", list_object)
        return


def del_object(list_object):
    """Usuwanie obiektu

    :param list_object: Lista dostępnych obiektów
    :return:
    """
    print_two_dimensional_list(list_object)
    print_list([], second=["Cofnij"], last_as_0=True)
    print("Wybierz obiekt do usunięcia")

    while True:  # Wpisanie poprawnej wartości
        input_menu = integer(input(), min_=0, max_=len(list_object))
        if input_menu[1]:
            input_menu = input_menu[0]
            break
        else:
            print("Opcja: " + str(input_menu[0]) + " nie istnieje, proszę wybrać ponownie")

    if input_menu == 0:
        return
    else:
        list_object[input_menu] = [input_menu, "", "", ""]
        save_to_csv("obiekty.csv", list_object)
        return


def close():
    exit()


def integer(input_, *, is_integer=True, min_=None, max_=None):
    """Określa czy argument spełnia wymagania

    :param input_: Sprawdzany input
    :param is_integer: Czy ma być liczbą całkowitą, jeżeli float ma po przecinku wyłącznie zera, to jest również
        przyjmowany za int
    :param min_: dopuszczalna najmniejsza wartość
    :param max_: dopuszczalna największa wartość
    :return: lista[1,2], 1 - input w typie int/float lub str jeśli to nie liczba, 2 - wynik sprawdzenia
    """
    result = True

    try:
        input_ = float(input_)
    except ValueError:
        return input_, False

    if is_integer:
        if input_ != int(input_):
            return input_, False
        else:
            input_ = int(input_)

    if min_ is not None:
        if input_ < min_:
            result = False

    if max_ is not None:
        if input_ > max_:
            result = False
    return input_, result


def clear_cmd():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


if __name__ == "__main__":
    path = os.getcwd()
    first_test(path)
    menu(path)
