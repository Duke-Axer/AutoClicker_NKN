import os
import csv

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

def gen_list_sek(sek):
    # Zapisanie "ID", "Name", "Time", "Number", "Speed", "Mouse"
    with open(sek) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        list_sek = []
        for line in reader:
            list_sek.append(line)
    return list_sek

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

def is_good_number(*, var=None, is_integer=True, min_=None, max_=None):
    if var is None:
        var = input()

    while True:
        var = integer(var, is_integer=is_integer, min_=min_, max_=max_)

        if var[1]:
            return var[0]
        else:
            print(f"Opcja: {var[0]} nie istnieje, proszę wybrać ponownie")

        var = input()


def clear_cmd():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)