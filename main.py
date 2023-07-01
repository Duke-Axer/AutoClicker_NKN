import pyautogui
import threading

from back_functions import *


def menu(path):
    path = os.path.join(path, "Data")
    while True:
        clear_cmd()
        print("MENU")
        print_list(("Wczytanie", "Modyfikacja", "Exit"), last_as_0=True)

        input_menu = is_good_number(min_=0, max_=2)
        # while True:
        #     input_menu = integer(input(), min_=0, max_=2)
        #     if input_menu[1]:
        #         input_menu = input_menu[0]
        #         break
        #     else:
        #         print("Opcja: " + str(input_menu[0]) + " nie istnieje, proszę wybrać ponownie")
        # switcher = {
        #     1: openDict(),
        #     2: modifyDict(),
        #     0: close(),
        # }
        # switcher[input_menu]
        if input_menu == 1:
            open_dict(path)
        elif input_menu == 2:
            modify_dict(path)
        elif input_menu == 0:
            close()


def first_test(path):
    print(path)
    path_general = os.path.join(path, "Data")
    try:
        os.chdir(path_general)
    except:
        os.mkdir(path_general)
    for i in os.listdir(path_general):
        if not "obiekty.csv" in os.listdir(os.path.join(path_general, i)):
            print(f"Brak pliku obiekty.csv w folderze {i}, Utworzenie pliku")
            with open(os.path.join(os.path.join(path_general, i), "obiekty.csv"),
                      "w", encoding='utf-8', newline='') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(["ID", "Name", "X", "Y"])

# Otwieranie folderów; do autoclicker
def open_dict(path_dir):
    clear_cmd()
    list_dir = os.listdir(path_dir)
    while True:
        print("autoclicker")
        print("Wybierz folder")
        print_list(first=list_dir, second=["Cofnij"], last_as_0=True)

        # Wpisanie poprawnej wartości
        input_menu = is_good_number(min_=0, max_=len(list_dir))

        if input_menu == 0:
            return 0
        else:
            path_sek = os.path.join(path_dir, list_dir[input_menu - 1])
            print(path_sek)
            open_sek(path_sek)


def open_sek(path_sek):
    list_sek = os.listdir(path_sek)
    list_sek.remove("obiekty.csv")

    while True:
        print("Wybierz sekwencję\n")
        print_list(first=list_sek, second=["Cofnij"], last_as_0=True)

        input_menu = is_good_number(min_=0, max_=len(list_sek))

        if input_menu == 0:
            return 0
        else:
            path_obj = os.path.join(path_sek, "obiekty.csv")
            path_sek_one = os.path.join(path_sek, list_sek[input_menu - 1])
            print(path_sek_one)
            auto_clicker(path_sek_one, path_obj)


def modify_dict(path_dir):
    while True:
        clear_cmd()

        # Wyświetlenie menu
        list_dir = os.listdir(path_dir)
        print("Dodawanie, usuwanie i modyfikacja folderów\n"
              "Wybierz folder lub utwórz nowy")
        print_list(first=list_dir, second=("Utwórz nowy", "Zmień nazwę", "Usuń", "Cofnij"), last_as_0=True)

        # Wpisanie poprawnej wartości
        input_menu = is_good_number(min_=-3, max_=len(list_dir))
        # Wybierz folder
        if len(list_dir) >= input_menu > 0:
            print("Wybrano folder: " + str(list_dir[input_menu - 1]))
            modify_files(os.chdir(os.path.join(path_dir, str(list_dir[input_menu - 1]))))

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


def modify_files(path):
    while True:
        clear_cmd()
        list_dir = os.listdir(path)
        list_dir.remove("obiekty.csv")
        print("Dodawanie, usuwanie i modyfikacja sekwencji\n"
              "Wybierz plik lub utwórz nowy")
        print_list(list_dir, second=("Utwórz nowy", "Zmień nazwę", "Usuń", "Obiekty", "Cofnij"), last_as_0=True)

        # Wpisanie poprawnej wartości
        input_menu = is_good_number(min_=-4, max_=len(list_dir))

        if input_menu <= 0:

            if input_menu == 0:
                return

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

        # Wpisanie poprawnej wartości
        input_menu = is_good_number(min_=-4, max_=0)
        if input_menu == 0:
            break
        elif input_menu == -1:
            add_item_in_sek(sek)
        elif input_menu == -2:
            order_sek(sek)
        elif input_menu == -3:
            remove_item_in_sek(list_sek, sek)


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

        # Wpisanie poprawnej wartości
        input_menu = is_good_number(min_=-3, max_=0)
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


def close():
    listener_close()
    print("Koniec!")
    exit()


if __name__ == "__main__":
    path = os.getcwd()
    first_test(path)

    l_listener = threading.Thread(target=listener_autoclicker)
    l_listener.start()
    l_reply = threading.Thread(target=listener_reply)
    l_reply.start()

    menu(path)
