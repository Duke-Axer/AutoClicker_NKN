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
    pathGeneral = os.getcwd()
    try:
        os.chdir(pathGeneral + "/Data")
    except:
        os.mkdir(pathGeneral + "/Data")
    print(os.getcwd())


def openDict():
    pass

def modifyDict():
    pass


def close():
    exit()

if __name__ == "__main__":
    firstTest()
    menu()