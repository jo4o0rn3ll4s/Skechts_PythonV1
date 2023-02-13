'''
Cria tela de login e senha
File name: login.py
'''

# Importa as bibliotecas
import qrcode
import PySimpleGUI as sg
import sqlite3
import os
import cv2

from Principal import main

#Cria a variavel com o caminho do bando de dados
pastadados = os.path.dirname(os.path.abspath(__file__))+'\Dados\\'
pastaQR = os.path.dirname(os.path.abspath(__file__))+'\QRCodes\\'

#Conecta oa Banco de Dados
conn = sqlite3.connect(pastadados+'Banco.db')
cursor = conn.cursor()

linha = 0
mens = 0

def ch_Entrar():
    linha = 0
    #procura usuario na tabela usuario
    query = (f""" SELECT * FROM Usuario WHERE Nome = '{valores['-usuario-']}' AND '{valores['-senha-']}' """)
    cursor.execute(str(query))

    #verifica se o query retornou alguma linha
    if cursor.fetchone() != None:
        cursor.execute(str(query))
        linha = cursor.fetchone() ## Joga o resultado na variável linha
   
    if linha != 0:
        # valida o nome e a senha
        if valores['-usuario-'] == linha[1] and valores['-senha-'] == linha[2]:
            tela.hide()
            main()
        else:
            if mens == 0:
                sg.Popup('Usuário não cadastrado')


####LER QRCODE####
def ler_qrcode():
    recording = False    # define a video capture object

    vid = cv2.VideoCapture(0)

    detector = cv2.QRCodeDetector()

    while True:
        eventos, valores = windowum.read(timeout=0)
        if eventos == sg.WIN_CLOSED:
            break
            
        recording = True
        linha = 0

        if recording:
            ret, frame = vid.read()
            data, bbox, straight_qrcode = detector.detectAndDecode(frame)

            #update da imagem
            imgbytes = cv2.imencode('.png',frame)[1].tobytes()
            windowum['-image-'].update(data=imgbytes)

            if len(data) > 0:
                #print = data
                try:
                    data = data.split(', ')
                    tela['-usuario-'].update(data[0]) # Limpa o campo
                    tela['-senha-'].update(data[1]) # Limpa o campo

                    usuar = str(data[0])
                    senh = str(data[1])
                    linha = 0
                    #procura usuario na tabela usuario
                    query = (f""" SELECT * FROM Usuario WHERE Nome = '{usuar}' AND '{senh}' """)
                    cursor.execute(str(query))
                except:
                    sg.Popup('Usuário não cadastrado')
                    mens = 1             ##Troca o valor da variável pra não mostrar mensagem acima outra vez
                    windowum.close()
                    tela.close()

                #verifica se o query retornou alguma linha
                if cursor.fetchone() != None:
                    cursor.execute(str(query))
                    linha = cursor.fetchone() ## Joga o resultado na variável linha

                if linha != 0:
                    # valida o nome e a senha
                    if usuar == linha[1] and senh == linha[2]:
                        tela.hide()
                        windowum.hide()
                        main()
                else:
                    if mens == 0:
                        sg.Popup('Usuário não cadastrado')                    

####LER QRCODE####

#layout
sg.theme('Reddit') #Define as cores da tela

layout = [
          [sg.Text ('', size = (6,1)), sg.Text ('Usuário'),sg.Input(key = '-usuario-', size = (20,1))],
          [sg.Text ('', size = (6,1)), sg.Text ('Senha  '), sg.Input(key = '-senha-', password_char='*', size = (20,1))],
          [sg.Text ('', size = (1,1)),
           sg.Button('Entrar', size = (8,1)),
           sg.Button('Sair', size = (8,1)),
           sg.Button('Gerar QRCode', size = (12,1)),
           sg.Button('Ler QRCode', size = (10,1))
          ]
         ]
#cria a janela TELA
tela = sg.Window('Tela de Login', layout)


layout_um = [[sg.Image(key='-image-')]
             ]
#cria a janela
windowum = sg.Window("Ler QRCode", layout_um)

#ler os eventos
while True:
    eventos, valores = tela.read(timeout=0)
    if eventos == sg.WIN_CLOSED or eventos == 'Sair':
        break

    ###GERAR QRCode###    
    if eventos == 'Gerar QRCode':
        if valores['-usuario-'] != '' and valores['-senha-'] != '':
            #procura usuario na tabela usuario
            query = (f""" SELECT * FROM Usuario WHERE Nome = '{valores['-usuario-']}' AND '{valores['-senha-']}' """)
            cursor.execute(str(query))

            #verifica se o query retornou alguma linha
            if cursor.fetchone() != None:
                cursor.execute(str(query))
                linha = cursor.fetchone() ## Joga o resultado na variável linha
                #print(linha)

            if linha != 0:
                # valida o nome e a senha
                if valores['-usuario-'] == linha[1] and valores['-senha-'] == linha[2]:
                    imagem = qrcode.make(f"{valores['-usuario-']}, {valores['-senha-']}")
                    imagem.save(f"{pastaQR}QR-{linha[0]}.jpg")
                    tela['Gerar QRCode'].update(disabled = True) # Coloca o botão desativado            
                else:
                    sg.Popup('Usuário não cadastrado')
    ###GERAR QRCode###

    if eventos == 'Entrar':
        ch_Entrar()

    if eventos == 'Ler QRCode':
        ler_qrcode()        
tela.close()
