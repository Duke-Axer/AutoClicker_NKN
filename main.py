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
    path = os.getcwd()
    next_ = True
    while next_:
        clearCmd()
        print("Dodawanie, usuwanie i modyfikacja folderów\n"
              "Wybierz folder lub utwórz nowy")
        listDir = os.listdir(path)
        i = 1
        for var in listDir:
            print(str(i) + " --> " + str(var))
            i = i + 1
        print("-1 -> Utwórz nowy\n"
              "-2 -> Zmień nazwę\n"
              "-3 -> Usuń\n"
              "0 --> Cofnij")
        inputMenu = input()
        if not intiger(inputMenu)[1]:
            while not intiger(inputMenu)[1]:
                print("Opcja: " + inputMenu + " nie istnieje, proszę wybrać ponownie\n")
                inputMenu = input()

        # Wybierz folder
        if int(inputMenu) <= len(listDir) and int(inputMenu) > 0:
            print("Wybrano folder: " + str(listDir[int(inputMenu) - 1]))
            modifyFiles(os.chdir(path + chr(92) + str(listDir[int(inputMenu) - 1])))
        # Utwórz nowy
        elif inputMenu == "-1":
            print("Wpisz nazwę folderu:")
            next_ = True
            while next_:
                next_ = False
                inputMenu = input()
                for i in listDir:
                    if inputMenu == i:
                        next_ = True
                        print("Taki folder istnieje")
                        print("Wybierz inną nazwę")
                if not next_:
                    print("Tworzę nowy folder: " + inputMenu)
                    os.mkdir(path + chr(92) + inputMenu)
                    with open(inputMenu + "\obiekty.csv", "w", encoding='utf-8', newline='') as file:
                        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(["ID", "Name", "X", "Y"])

            next_ = True
        # Zmień nazwę
        elif inputMenu == "-2":
            next_ = True
            next_2_ = True
            while next_:
                print("Wybierz który folder ma mieć inną nazwę")
                listDir = os.listdir(path)
                i = 1
                for var in listDir:
                    print(str(i) + " --> " + str(var) + "\n")
                    i = i + 1
                print("0 --> Cofnij")
                inputMenu = input()
                if int(inputMenu) <= len(listDir) and int(inputMenu) > 0:
                    print("Wybrano folder: " + str(listDir[int(inputMenu) - 1]))
                elif inputMenu == "0":
                    next_ = False
                    next_2_ = False
                else:
                    clearCmd()
                    print("Opcja: " + inputMenu + " nie istnieje, proszę wybrać ponownie\n")

            while next_2_:
                print("Wpisz nazwę\n"
                      "0 --> Cofnij")
                next_2_ = False
                inputName = input()
                if inputMenu == "0":
                    return 0

                for i in listDir:
                    if inputMenu == i:
                        print("Taki folder już istnieje")
                        next_2_ = True
                        print("Wybierz inną nazwę")
                if not next_2_:
                    print("Zmieniam nazwę folderu na: " + inputName)
                    os.rename(listDir[int(inputMenu) - 1], inputName)
                    next_2_ = False
            else:
                print("Wybrałeś numer, który nie jest przypisany do folderu\n"
                      "Wybierz folder lub cofnij")
            next_ = True
        # Usuń
        elif inputMenu == "-3":
            clearCmd()
            next_ = True
            while next_:
                print("Wybrano usunięcie folderu\n"
                      "Aby usunąć folder, musi być pusty\n"
                      "Wybierz folder\n")
                listDir = os.listdir(path)
                i = 1
                for var in listDir:
                    print(str(i) + " --> " + str(var) + "\n")
                    i = i + 1
                print("0 --> Cofnij")
                inputMenu = input()
                if int(inputMenu) <= len(listDir) and int(inputMenu) > 0:
                    print("Wybrano foder" + listDir[int(inputMenu) - 1])
                    os.rmdir(os.getcwd() + chr(92) + listDir[int(inputMenu) - 1])
                    next_ = False
                elif inputMenu == "0":
                    next_ = False
                else:
                    clearCmd()
                    print("Opcja: " + inputMenu + " nie istnieje, proszę wybrać ponownie\n")
            next_ = True
        # Cofnij
        elif inputMenu == "0":
            next_ = False


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
        if not intiger(inputMenu)[1]:
            while not intiger(inputMenu)[1]:
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
        for line in list_sek:
            print(line[0] + " --> " + line[1] + " -- " + line[2] + " -- " +
                  line[3] + " -- " + line[4] + " -- " + line[5])

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
    while True:
        list_obiect = listObiects()
        list_sek = listSek(sek)
        print(list_sek)
        # ID --> Name -- Time -- Number -- Speed -- Mouse
        while True:
            for line in list_obiect:
                print(line[0] + " --> " + line[1] + " -- " + line[2] + " -- " + line[3])
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
                    var_input[0] = write_arg_in_item_sek(0)
                    var_input[1] = write_arg_in_item_sek(1)
                    var_input[2] = write_arg_in_item_sek(2)
                    var_input[3] = write_arg_in_item_sek(3)

                    # Zmiana podanych wartości
                    while True:
                        print("1 --> Czas trwania: ", str(var_input[0]), "\n"
                              "2 --> Liczba kliknięć: ", str(var_input[1]), "\n"
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
                                if intiger(var, is_integer=True, min_=1, max_=4)[1]:
                                    var_input[int(var) - 1] = write_arg_in_item_sek(int(var) - 1)
                                elif var == "0":
                                    break
                        break

                        # stworzenie wiersza
                    print(list_sek[-1][0])
                    print(list_obiect[int(obiect_id)][1])
                    print(var_input[0])
                    print(var_input[1])
                    print(var_input[2])
                    print(var_input[3])

                    num = 0
                    for i in list_sek:
                        num = num + 1

                    # Zapisanie danych obiect_id i var_input[0:3] do pliku na ostatnim id
                    list_sek.append([num, list_obiect[int(obiect_id)][1], var_input[0],
                                     var_input[1], var_input[2], var_input[3]])
                    print(list_sek)

                    for i in list_sek:
                        print(i)
                    break


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
            if intiger(var_input, is_integer=False, min_=0)[1]:
                return var_input
        elif var == 1:
            if intiger(var_input, is_integer=True, min_=0)[1]:
                return var_input

        elif var == 3:
            if intiger(var_input, is_integer=True, min_=1, max_=2)[1]:
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
            saveToCSV(obiekty)
            break
        i = i + 1
    else:  # nie ma wolnego
        dodaj_obiekt = dodajObiekt()
        obiekt.append([i, dodaj_obiekt[0], dodaj_obiekt[1], dodaj_obiekt[2]])
        saveToCSV(obiekt)
    print("Zapisanie w lini nr " + str(i))


def saveToCSV(obiekty):
    with open("obiekty.csv", "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in obiekty:
            writer.writerow([i[0], i[1], i[2], i[3]])


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
            saveToCSV(obiekt)
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
            saveToCSV(obiekt)
        elif inputMenu == "0":
            break
        else:
            print("Wybrano złą opcję: ", inputMenu)


def close():
    exit()


def intiger(input_, *, is_integer=True, min_=None, max_=None):
    var = True

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
            var = False

    if max_ is not None:
        if input_ > max_:
            var = False
    return input_, var


if __name__ == "__main__":
    path = os.getcwd()
    firstTest(path)
    menu(path)
