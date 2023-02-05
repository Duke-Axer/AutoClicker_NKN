import pyautogui
import os

print('start program')
print('4label')

menuOpcion = {"openDict": "1",
              "modify": "2"
              }





def menu():
    clearCmd()
    print("Menu\n"
          "1 --> Wczytanie\n"
          "2 --> Modyfikacja\n"
          "0 --> Exit")

    while True:
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
def firstTest():
    print(os.getcwd())
    pathGeneral = os.getcwd() + "/Data"
    try:
        os.chdir(pathGeneral)
    except:
        os.mkdir(pathGeneral)
    print(os.getcwd())

#Otwieranie folderów
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
    next_ = True
    while next_:
        clearCmd()
        print("Dodawanie, usuwanie i modyfikacja plików\n"
              "Wybierz folder lub utwórz nowy")
        listDir = os.listdir(os.getcwd())
        i = 1
        for var in listDir:
            print(str(i) + " --> " + str(var) + "\n")
            i = i+1
        print("-1 -> Utwórz nowy\n"
              "-2 -> Zmień nazwę\n"
              "-3 -> Usuń\n"
              "0 --> Cofnij")
        inputMenu = input()
        try:
            if int(inputMenu) <= len(listDir) and int(inputMenu) > 0:
                print( "Wybrano folder: " + str(listDir[int(inputMenu)]) )

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
                        os.mkdir(os.getcwd() + chr(92) + inputMenu)
                next_ = True

            elif inputMenu == "-2":
                next_ = True
                next_2_ = True
                while next_:
                    print("Wybierz który folder ma mieć inną nazwę")
                    listDir = os.listdir(os.getcwd())
                    i = 1
                    for var in listDir:
                        print(str(i) + " --> " + str(var) + "\n")
                        i = i+1
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

            elif inputMenu == "-3":
                clearCmd()
                next_ = True
                while next_:
                    print("Wybrano usunięcie folderu\n"
                          "Aby usunąć folder, musi być pusty\n"
                          "Wybierz folder\n")
                    listDir = os.listdir(os.getcwd())
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

            elif inputMenu == "0":
                next_ = False
        except ValueError:
            print("Opcja: " + inputMenu + " nie istnieje, proszę wybrać ponownie\n")



def close():
    exit()


def intiger(input_):
    var = True
    try:
        int(input_)
    except ValueError:
        var = False
    return input_, var



if __name__ == "__main__":
    firstTest()
    menu()



