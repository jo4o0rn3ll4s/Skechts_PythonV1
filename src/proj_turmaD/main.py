import PySimpleGUI as sg
from view import LoginScreen, MainScreen


login = LoginScreen()
authenticated = False


def main():
    authenticated = login.show()
    if authenticated:
        master = MainScreen()
        master.show()


if __name__ == '__main__':
    main()
