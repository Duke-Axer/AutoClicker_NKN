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


def openDict():
    pass

def modifyDict():
    while True:
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

        if int(inputMenu) <= len(listDir) and int(inputMenu) > 0:
            print( "Wybrano folder: " + str(listDir[int(inputMenu)]) )

        elif inputMenu == "-1":
            print("Wpisz nazwę folderu:")
            next_ = 0
            while next_ == 0:
                next_ = 1
                inputMenu = input()
                for i in listDir:
                    if inputMenu == i:
                        print("Taki folder istnieje")
                        next_ = 0
                        print("Wybierz inną nazwę")
                if next_ == 1:
                    print("Tworzę nowy folder: " + inputMenu)
                    os.mkdir(os.getcwd() + chr(92) + inputMenu)

        elif inputMenu == "-2":
            print("Wybierz który folder ma mieć inną nazwę")
            listDir = os.listdir(os.getcwd())
            i = 1
            for var in listDir:
                print(str(i) + " --> " + str(var) + "\n")
            print("0 --> Exit")
            inputMenu = input()
            if int(inputMenu) <= len(listDir) and int(inputMenu) > 0:
                print("Wybrano folder: " + str(listDir[int(inputMenu) - 1]))
                print("Wpisz nazwę")
                next_ = 0
                while next_ == 0:
                    next_ = 1
                    inputName = input()
                    for i in listDir:
                        if inputMenu == i:
                            print("Taki folder już istnieje")
                            next_ = 0
                            print("Wybierz inną nazwę")
                    if next_ == 1:
                        print("Zmieniam nazwę folderu na: " + inputName)
                        os.rename(listDir[int(inputMenu) - 1], inputName)
            else:
                return 0

        elif inputMenu == "-3":
            pass
        elif inputMenu == "0":
            return 0



def close():
    exit()

if __name__ == "__main__":
    firstTest()
    menu()