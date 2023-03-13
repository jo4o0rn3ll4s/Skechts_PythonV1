import PySimpleGUI as sg

USERNAME = 'a'
PASSWORD = '123'


class LoginScreen:
    def __init__(self) -> None:
        self.layout = [[sg.Text('Usuário', size=(10, 1)), sg.InputText(key='login')],
                       [sg.Text('Senha', size=(10, 1)), sg.InputText(
                           key='senha', password_char='*')],
                       [sg.Button('Sair'), sg.Button('Entrar')]]

        self.window = sg.Window('CVTI SYSTEM 2023', self.layout)

    def close(self) -> None:
        self.window.close()
        exit()

    def auth(self, name, password) -> bool:
        if name is None or password is None:  # Validação de campos
            return False

        if name == USERNAME and password == PASSWORD:  # Validação de usuário e senha
            return True

        return False  # Caso não seja nenhum dos casos acima

    def on_login_success(self) -> bool:
        self.window.close()  # Fecha a janela de login
        print("Autenticado com sucesso!")
        return True

    def show(self) -> bool:
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Sair':
                self.close()  # Fecha a janela e encerra o programa

            elif event == 'Entrar':
                # Validação de usuário e senha
                if self.auth(values['login'], values['senha']):
                    return self.on_login_success()
                else:
                    sg.popup('Acesso Negado. Tente Novamente',
                             auto_close=True, auto_close_duration=3)
