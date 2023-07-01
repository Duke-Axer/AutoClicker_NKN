from support_def import *
from pynput.mouse import Button
from pynput.mouse import Controller
from pynput import keyboard

import time
global listen_var, listen_choice

listen_choice = 0
listen_var = 0
def auto_clicker(path_sek, path_obj):
    list_arg = gen_list_sek(path_sek)[1:]
    list_obj_all = gen_list_sek(path_obj)[1:]
    print(list_arg)
    print(list_obj_all)
    list_obj = []
    for object in list_obj_all:
        for i in list_arg:
            if object[1] == i[1]:
                for var in list_obj:
                    if var[0] == i[1]:
                        break
                else:
                    list_obj.append(object[1:])
    print(list_obj)

    iter = 3
    while iter > 0:
        iter -= iter
        for item in list_arg:
            for obj in list_obj:
                if item[1] == obj[0]:
                    work_clicker(item, obj)
                    break
        else:
            if listen_var == "p":
                break

def work_clicker(item, obj):
    mouse = Controller()
    global listen_var
    start = time.time()
    count = 0
    while count <= int(item[3]) and int(item[2]) > (time.time() - start) \
            and listen_var != "o":
        move_mouse(obj, mouse)
        click(item, mouse)
        print(time.time() - start)

def move_mouse(obj, mouse):
    mouse.position = (obj[1], obj[2])
    print("x", obj[1], "y", obj[2])

def click(item, mouse):
    print(item)
    time.sleep(1 / int(item[4]))
    print("click")
    # if item[5] == "1":
    #     mouse.press(Button.left)
    #     mouse.release(Button.left)
    # else:
    #     mouse.press(Button.right)
    #     mouse.release(Button.right)



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
    with open(os.path.join(input_menu, "obiekty.csv"), "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["ID", "Name", "X", "Y"])


# Dodawanie, usuwanie, zmieniane nazwy folderów
def remove_dir(path_dir):
    """Usuwa folder jeżeli nie zawiera plików z wyjątkiem "obiekty.csv"

        :param path_dir: Ścieżka z folderami
        :return:
        """
    clear_cmd()
    os.chdir(path_dir)

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
        path = os.path.join(path_dir, list_dir[input_menu - 1])
        if "obiekty.csv" in os.listdir(path):
            os.listdir(path).remove("obiekty.csv")

        if not os.listdir(path):
            os.remove(os.path.join(path, "obiekty.csv"))
            print("Wybrano foder: " + list_dir[input_menu - 1])
            os.rmdir(path_dir)
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
    print(len(list_sek) - 1)
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

    list_obiect = objects()
    list_sek = gen_list_sek(sek)
    while True:
        print_two_dimensional_list(list_obiect)
        print("Wybierz obiekt")


        while True:  # Wpisanie poprawnej wartości
            obiect_id = integer(input(), min_=0, max_=len(list_obiect))
            if obiect_id[1]:
                obiect_id = obiect_id[0]
                break
            else:
                print("Opcja: " + str(obiect_id[0]) + " nie istnieje, proszę wybrać ponownie")

        if obiect_id == 0:
            break
        else:
            if list_obiect[obiect_id][1] == "":
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
                    print_two_dimensional_list([["1", "Czas trwania:", var_input[0]],
                                                ["2", "Liczba kliknięć:", var_input[1]],
                                                ["3", "Szybkość:", var_input[2]],
                                                ["4", "Przycisk myszki:", var_input[3]]])
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

# Zwraca listę elementów w sekwencji
def objects():
    # Zapisanie obiektów ID,Name,X,Y
    with open("obiekty.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        list_object = []
        for line in reader:
            list_object.append(line)
    return list_object


def add_object(list_object):
    """Zapisuje obiekt w pierwszym wolnym miejscu

    :param list_object: Lista zapisanych obiektów
    :return:
    """
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
    global listen_var, listen_choice

    while True:
        print("Podaj nazwę")
        input_name = input()
        for name in list_object:
            if name[1] == input_name:
                print("Zła nazwa")
                break
        else:
            if input_name != "":
                break
            else:
                print("Zła nazwa")

    while True:
        listen_var = "0"
        listen_choice = 1
        print("Aby sprawdzić pozycję kursora wciśnij 'w', a następnie \nPodaj x")
        print(listen_var)
        print(listen_choice)
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
    listen_var = "0"
    listen_choice = 0
    return input_name, x, y

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


def on_press(key):

    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    global listen_var
    try:
        if key.char == "p":
            listen_var = "p"
        elif key.char == "o":
            listen_var = "o"
        elif key.char == "q":
            listen_var = "q"
        elif key.char == "w":
            listen_var = "w"
        elif key.char == "e":
            listen_var = "e"
        elif key.char == "]":
            listen_var = "]"
    except AttributeError:
        pass


# Collect events until released

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()

def listener_autoclicker():
    global listen_choice
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        if listen_choice == -1:
            return False

def listener_reply():
    global listen_var, listen_choice
    while True:
        while listen_choice == 1:
            if listen_var == "w":
                print(Controller().position)
                listen_var = ""

        while listen_choice == 0:
            if listen_var == "]":
                print("działa")
                listen_var = ""
        if listen_choice == -1:
            return False

def listener_close():
    global listen_choice
    listen_choice = -1
    return 0