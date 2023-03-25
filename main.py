import pyautogui
import os
import csv


def menu(path):
    path = path + chr(92) + "Data"
    while True:
        clearCmd()
        print("Menu\n"
              "1 --> Wczytanie\n"
              "2 --> Modyfikacja\n"
              "0 --> Exit")
        inputMenu = input()
        if inputMenu == "1":
            openDict()
        elif inputMenu == "2":
            modifyDict()
        elif inputMenu == "0":
            close()
        else:
            clearCmd()
            print("Opcja: " + inputMenu + " nie istnieje, proszę wybrać ponownie\n")
            print("Menu\n"
                  "1 --> Wczytanie\n"
                  "2 --> Modyfikacja\n"
                  "0 --> Exit")


def clearCmd():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def firstTest(path):
    print(path)
    pathGeneral = path + chr(92) + "Data"
    try:
        os.chdir(pathGeneral)
    except:
        os.mkdir(pathGeneral)
    print(os.getcwd())


# Otwieranie folderów
def openDict():
    clearCmd()
    print("Dodawanie, usuwanie i modyfikacja plików\n"
          "Wybierz folder lub utwórz nowy")
    listDir = os.listdir(os.getcwd())
    i = 1
    for var in listDir:
        print(str(i) + " --> " + str(var) + "\n")
        i = i + 1
    print("-1 -> Utwórz nowy\n"
          "-2 -> Zmień nazwę\n"
          "-3 -> Usuń\n"
          "0 --> Cofnij")
    inputMenu = input()
    pass


# Dodawanie, usuwanie, zmieniane nazwy folderów
def modifyDict():
    path_dir = os.getcwd()

    while True:
        clearCmd()

        # Wyświetlenie menu
        list_dir = os.listdir(path_dir)
        print("Dodawanie, usuwanie i modyfikacja folderów\n"
              "Wybierz folder lub utwórz nowy")
        print_list(first=list_dir, second=["Utwórz nowy", "Zmień nazwę", "Usuń", "Cofnij"], last_as_0=True)

        # Wpisanie poprawnej wartości
        while True:
            inputMenu = integer(input(), min_=-3, max_=len(list_dir))
            if inputMenu[1]:
                inputMenu = inputMenu[0]
                break
            else:
                print("Opcja: " + inputMenu[0] + " nie istnieje, proszę wybrać ponownie")

        # Wybierz folder
        if inputMenu <= len(list_dir) and inputMenu > 0:
            print("Wybrano folder: " + str(list_dir[inputMenu - 1]))
            modifyFiles(os.chdir(path_dir + chr(92) + str(list_dir[inputMenu - 1])))

        # Utwórz nowy
        elif inputMenu == -1:
            while True:
                print("Wpisz nazwę folderu:")
                inputMenu = input()
                for i in list_dir:
                    if inputMenu == i:
                        print("Taki folder istnieje\n Wybierz inną nazwę")
                        break
                else:
                    break

            print("Tworzę nowy folder: " + inputMenu)
            os.mkdir(path_dir + chr(92) + inputMenu)
            with open(inputMenu + "\obiekty.csv", "w", encoding='utf-8', newline='') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(["ID", "Name", "X", "Y"])

        # Zmień nazwę
        elif inputMenu == -2:
            rename_dir(path_dir)

        # Usuń
        elif inputMenu == -3:
            clearCmd()
            while True:
                print("Wybrano usunięcie folderu\n"
                      "Aby usunąć folder, musi być pusty\n"
                      "Wybierz folder\n")
                list_dir = os.listdir(path_dir)
                print_list(list_dir, second=["Cofnij"], last_as_0=True)

                # Wpisanie poprawnej wartości
                while True:
                    inputMenu = integer(input(), min_=0, max_=len(list_dir))
                    if inputMenu[1]:
                        inputMenu = inputMenu[0]
                        break
                    else:
                        print("Opcja: " + inputMenu[0] + " nie istnieje, proszę wybrać ponownie")

                if inputMenu == 0:
                    break
                # Usuwanie folderu
                else:
                    print("Wybrano foder" + list_dir[int(inputMenu) - 1])
                    os.rmdir(os.getcwd() + chr(92) + list_dir[int(inputMenu) - 1])


        # Cofnij
        elif inputMenu == 0:
            break


def rename_dir(path):
    listDir = os.listdir(path)

    # Wybranie folderu
    while True:
        print("Wybierz który folder ma mieć inną nazwę")
        print_list(listDir, second=["Cofnij"], last_as_0=True)
        inputMenu = input()

        if integer(inputMenu, min_=1, max_=len(listDir))[1]:
            print("Wybrano folder: " + str(listDir[int(inputMenu) - 1]))

            # Wpisanie nowej nazwy
            while True:
                print("Wpisz nazwę\n"
                      "0 --> Cofnij")
                inputName = input()
                if inputMenu == "0":
                    break

                for i in listDir:
                    if inputMenu == i:
                        print("Taki folder już istnieje")
                        print("Wybierz inną nazwę")
                        break
                else:
                    print("Zmieniam nazwę folderu na: " + inputName)
                    os.rename(listDir[int(inputMenu) - 1], inputName)
                break

        elif inputMenu == "0":
            break
        else:
            clearCmd()
            print("Opcja: " + inputMenu + " nie istnieje, proszę wybrać ponownie\n")
            continue
        break


# Dodawanie... plików txt z listą kroków do wykonania i lista wykorzystywanych obiektów
def modifyFiles(path):
    while True:
        clearCmd()
        print("Dodawanie, usuwanie i modyfikacja sekwencji\n"
              "Wybierz plik lub utwórz nowy")
        listDir = os.listdir(path)
        listDir.remove("obiekty.csv")
        i = 1
        for var in listDir:
            print(str(i) + " --> " + str(var))
            i = i + 1
        print("-1 -> Utwórz nowy\n"
              "-2 -> Zmień nazwę\n"
              "-3 -> Usuń\n"
              "-9 -> Obiekty\n"
              "0 --> Cofnij")
        inputMenu = input()
        if not integer(inputMenu)[1]:
            while not integer(inputMenu)[1]:
                print("Opcja: " + inputMenu + " nie istnieje, proszę wybrać ponownie\n")
                inputMenu = input()
        if int(inputMenu) <= 0:

            if inputMenu == "0":
                break
            elif inputMenu == "-1":
                while True:
                    print("Wpisz nazwę sekwencji\n"
                          "0 --> Cofnij")
                    inputMenu = input()
                    if inputMenu == "0":
                        break

                    elif inputMenu != "":
                        for i in listDir:
                            # Czy powtarza się nazwa pliku
                            if i == inputMenu:
                                print("Taka nazwa już istnieje")
                                break
                        else:
                            print("Tworzę nowy folder: " + inputMenu)
                            with open(inputMenu + ".csv", "w", encoding='utf-8', newline='') as file:
                                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                writer.writerow(["ID", "Name", "Time", "Number", "Speed", "Mouse"])
                            break

            elif inputMenu == "-2":
                # Wybranie pliku (pętla)
                while True:
                    print("Wybierz plik")
                    i = 1
                    listDir = os.listdir(path)
                    listDir.remove("obiekty.csv")
                    for var in listDir:
                        print(str(i) + " --> " + str(var))
                        i = i + 1
                    print("0 --> Cofnij")
                    inputMenu = input()
                    if int(inputMenu) <= len(listDir) and int(inputMenu) > 0:
                        print("Wybrano plik: " + str(listDir[int(inputMenu) - 1]))

                        # Wybranie nazwy (pętla)
                        while True:
                            print("Wpisz nazwę\n"
                                  "0 --> Cofnij")
                            inputName = input()

                            if inputMenu == "0":
                                break
                            elif inputName != "":
                                for i in listDir:
                                    if inputMenu == i:
                                        print("Taki plik już istnieje")
                                        print("Wybierz inną nazwę")
                                        break
                                else:
                                    print("Zmieniam nazwę pliku na: " + inputName)
                                    os.rename(listDir[int(inputMenu) - 1], inputName + ".csv")
                                    break
                    elif inputMenu == "0":
                        break

            elif inputMenu == "-3":
                while True:
                    print("Wybierz sekwencje do usunięcia")
                    i = 1
                    listDir = os.listdir(path)
                    listDir.remove("obiekty.csv")
                    for var in listDir:
                        print(str(i) + " --> " + str(var))
                        i = i + 1
                    print("0 --> Cofnij")
                    inputMenu = input()

                    if int(inputMenu) <= len(listDir) and int(inputMenu) > 0:
                        print("Wybrano sekwencje: " + str(listDir[int(inputMenu) - 1]))
                        os.remove(str(listDir[int(inputMenu) - 1]))
                    elif inputMenu == "0":
                        break

            # Powinien istnieć plik obiekty.csv
            elif inputMenu == "-9":
                print("dostępne obiekty")
                obiekty(path)

        elif int(inputMenu) <= len(listDir):
            print("Wybrano sekwencję ", listDir[int(inputMenu) - 1])
            modifySek(listDir[int(inputMenu) - 1])
        else:
            print("Taka opcja nie istnieje: ", inputMenu)


def modifySek(sek):
    while True:
        clearCmd()
        print("Dodawanie, usuwanie i modyfikacja sekwencji: ", sek)
        # print("ID --> Name -- Time -- Number -- Speed -- Mouse")
        list_sek = listSek(sek)

        print_two_dimensional_list(list_sek)

        print("0 --> Cofnij\n"
              "-1 -> Utwórz nowy\n"
              "-2 -> modyfikuj\n"
              "-3 -> zmień kolejność\n"
              "-4 -> Usuń\n")
        inputMenu = input()
        if int(inputMenu) <= 0 and int(inputMenu) >= -4:
            if inputMenu == "0":
                break
            elif inputMenu == "-1":
                addItemInSek(sek)


# Dodawanie elementu w sekwencji
def addItemInSek(sek):
    """Pozwala na wpisanie parametrów sekwencji. Wywołuje fukcję zapisu do pliku csv
    parametry: ID, Name, Time, Number, Speed, Mouse

    :param sek: Ścieżka do pliku z sekwencjami
    :return:
    """
    while True:
        list_obiect = listObiects()
        list_sek = listSek(sek)
        while True:
            print_two_dimensional_list(list_obiect)
            print("Wybierz obiekt")

            obiect_id = input()

            if int(obiect_id) >= 1 and int(obiect_id) <= int(list_obiect[-1][0]):
                if list_obiect[-1][1] == "":
                    print("Wybrany obiekt jest usuniety")
                    continue
                else:
                    print("Wybrano obiekt:")
                    print(list_obiect[int(obiect_id)][0] + " --> " + list_obiect[int(obiect_id)][1] + " -- " +
                          list_obiect[int(obiect_id)][2] + " -- " + list_obiect[int(obiect_id)][3])
                while True:
                    print("Określ czas trwania, liczbę kliknięć, szybkość, przycisk myszki"
                          "\n0 Dla czasu trwania oznacza zakończenie po x kliknięciach"
                          "\n0 Dla liczby kliknięć oznacza zakończenie po x czasie")
                    var_input = [None, None, None, None]
                    for i in range(4):
                        var_input[i] = write_arg_in_item_sek(i)

                    # Zmiana podanych wartości
                    while True:
                        print("1 --> Czas trwania: ", str(var_input[0]), "\n"
                                                                         "2 --> Liczba kliknięć: ", str(var_input[1]),
                              "\n"
                              "3 --> Szybkość: ", str(var_input[2]), "\n"
                                                                     "4 --> Przycisk myszki: ", str(var_input[3]), "\n")
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
                    list_sek.append([str(len(list_sek)), list_obiect[int(obiect_id)][1], var_input[0],
                                     var_input[1], var_input[2], var_input[3]])
                    save_to_csv(sek, list_sek)

                    break
            break
        break


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
                len_arg.append(len(arg))
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
    :param second: lista do wyświetlenia, zlicza od -inf do -1
    :param add: Dodanie n razy znaku -
    :param last_as_0: Ostatnia wartość wyświetla się jako 0 dla second,jeżeli second nie istnieje, to dla first
    :return:
    """

    if second is None:
        second = []
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
                  "1 --> Lewy"
                  "2 --> Prawy")
        var_input = input()
        if var == 0 or var == 2:
            if integer(var_input, is_integer=False, min_=0)[1]:
                return var_input
        elif var == 1:
            if integer(var_input, is_integer=True, min_=0)[1]:
                return var_input

        elif var == 3:
            if integer(var_input, is_integer=True, min_=1, max_=2)[1]:
                return var_input
        else:
            print("Bład: ", var_input)


# Zwraca listę elementów w sekwencji
def listSek(sek):
    # Zapisanie "ID", "Name", "Time", "Number", "Speed", "Mouse"
    with open(sek) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        list_sek = []
        for line in reader:
            list_sek.append(line)
    return list_sek


# Zwraca listę obiektków
def listObiects():
    # Zapisanie obiektów ID,Name,X,Y
    with open("obiekty.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        list_obiekt = []
        for line in reader:
            list_obiekt.append(line)
    return list_obiekt


def obiekty(path):
    # Czy plik obiekty.csv istnieje
    listDir = os.listdir(path)
    i = 1
    for var in listDir:
        if var == "obiekty.csv":
            break
        i = i + 1
    else:
        print("Brak pliku csv, Dodawanie pliku obiekty.csv")
        with open("obiekty.csv", "w", encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["ID", "Name", "X", "Y"])

    # Wyświetenie obiektów ID,Name,X,Y
    while True:
        list_obiekt = listObiects()
        for line in list_obiekt:
            print(line[0] + " --> " + line[1] + " -- " + line[2] + " -- " + line[3])

        print("0 --> Cofnij\n"
              "-1 -> Utwórz nowy\n"
              "-2 -> modyfikuj\n"
              "-3 -> Usuń\n")
        inputMenu = input()

        if int(inputMenu) <= 0 and int(inputMenu) >= -3:
            if inputMenu == "0":
                break
            elif inputMenu == "-1":
                # Dodaje obiekt na pierwszym wolnym ID liczącz od 1
                print("tworzenie nowego obiektu")
                addObiect(list_obiekt)

            elif inputMenu == "-2":
                # zmienia Name, x lub y
                print("modyfikacja")
                modifyObiekt()

            elif inputMenu == "-3":
                # powinno sprawdzić czy jakieś sekwencje wykorzystują dany obiekt (teraz nie sprawdza)
                print("usuwanie obiektu")
                delObiekt()
            else:
                print("bład")


def addObiect(obiekt):
    i = 1
    # Sprawdzenie czy jest wolne miejsce
    while i < obiekt[-1][0]:
        if obiekt[i][1] == "":  # jest wolne
            obiekty = []
            for var in obiekt:
                if var[0] != str(i):
                    obiekty.append(var)
                else:
                    dodaj_obiekt = dodajObiekt()
                    obiekty.append([i, dodaj_obiekt[0], dodaj_obiekt[1], dodaj_obiekt[2]])
            save_to_csv("obiekty.csv", obiekty)
            break
        i = i + 1
    else:  # nie ma wolnego
        dodaj_obiekt = dodajObiekt()
        obiekt.append([i, dodaj_obiekt[0], dodaj_obiekt[1], dodaj_obiekt[2]])
        save_to_csv("obiekty.csv", obiekt)
    print("Zapisanie w lini nr " + str(i))


def dodajObiekt():
    while True:
        print("Podaj nazwę")
        Name = input()
        if Name != "":
            break
        else:
            print("Zła nazwa")

    while True:
        print("Podaj x")
        x = input()
        if int(x) >= 0:
            break
        else:
            print("Zła wielkość x")

    while True:
        print("Podaj y")
        y = input()
        if int(y) >= 0:
            break
        else:
            print("Zła wielkość y")
    return Name, x, y


def modifyObiekt():
    while True:
        with open("obiekty.csv") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            obiekt = []
            for line in reader:
                try:
                    print(line[0] + " --> " + line[1] + " -- " + line[2] + " -- " + line[3])
                    obiekt.append(line)
                except IndexError:
                    continue

            print("0 --> Cofnij\n"
                  "Wybierz obiekt do modyfikacji\n")
        inputMenu = input()

        if int(inputMenu) > 0 and int(inputMenu) <= int(obiekt[-1][0]):
            dodaj_obiekt = dodajObiekt()
            obiekt[int(inputMenu)] = [int(inputMenu), dodaj_obiekt[0], dodaj_obiekt[1], dodaj_obiekt[2]]
            save_to_csv("obiekty.csv", obiekt)
        elif inputMenu == "0":
            break


def delObiekt():
    while True:
        with open("obiekty.csv") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            obiekt = []
            for line in reader:
                try:
                    print(line[0] + " --> " + line[1] + " -- " + line[2] + " -- " + line[3])
                    obiekt.append(line)
                except IndexError:
                    continue

            print("0 --> Cofnij\n"
                  "Wybierz obiekt do usunięcia\n")
        inputMenu = input()

        if int(inputMenu) > 0 and int(inputMenu) <= int(obiekt[-1][0]):
            obiekt[int(inputMenu)] = [int(inputMenu), "", "", ""]
            save_to_csv("obiekty.csv", obiekt)
        elif inputMenu == "0":
            break
        else:
            print("Wybrano złą opcję: ", inputMenu)


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


if __name__ == "__main__":
    path = os.getcwd()
    firstTest(path)
    menu(path)
