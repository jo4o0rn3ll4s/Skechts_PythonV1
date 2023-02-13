'''
Cria tela de capturar as fotos dos alunos
File name: Capfoto.py
'''


####Abre a CAM e enquadra o rosto###
## Carregando PySimpleGUI
import PySimpleGUI as sg

## Carregando a OpenCV
import cv2

import numpy as np

import sqlite3

#import datetime

import os


#Cria a variavel com o caminho do bando de dados
pastadados = os.path.dirname(os.path.abspath(__file__))+'\Dados\\'
pastafotos = os.path.dirname(os.path.abspath(__file__))+'\FotosAluno\\'


#Conecta oa Banco de Dados
conn = sqlite3.connect(pastadados+'Banco.db')
cursor = conn.cursor()

sg.theme('Reddit') #Define as cores da tela


def captura_window():

    layout_um = [[sg.Text("Matric/Aluno: "), sg.Input(key = '-matric-', size = (8,1), enable_events=True),
                  sg.Input(key = '-aluno-', size = (40,1), readonly=True), 
                  sg.Button('Buscar', size=(7, 1), font='Arial 12', disabled = True),
                ], 
             [sg.Image(key='-image-')],
             [sg.Text(' ', key = '-TEXT-', size=(40, 1), expand_x = True, justification = 'c', font='Helvetica 16')],
             [sg.Text ('', size = (5,1)),
              sg.Button('Ligar', size=(8, 1), font='Arial 12', disabled = True),
              sg.Text ('', size = (0,1)),
              sg.Button('Parar', size=(8, 1), font='Arial 12', disabled = True),
              sg.Text ('', size = (0,1)),
              sg.Button('Capturar', size=(8, 1), font='Arial 12', disabled = True), # Cria o botão desabilitado
              sg.Text ('', size = (0,1)),
              sg.Button('Editar', size=(8, 1), font='Arial 12', disabled = False), # Cria o botão desabilitado
              sg.Text ('', size = (0,1)),
              sg.Button('Sair', size=(8, 1), font='Arial 12'),]           
             ]
    windowum = sg.Window("Capturar Foto", layout_um, modal=True)
    choice = None


    # pega o video
    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    recording = False

    while True:
        eventos, valores = windowum.read(timeout=0)
        if eventos == sg.WIN_CLOSED:
            break
    
        ###Liga a WEBCAM clicando no botão LIGAR###
        elif eventos == 'Ligar':
            recording = True
            windowum['Capturar'].update(disabled = False) # Habilita o botão Capturar

        ###Desliga a WEBCAM clicando no botão PARAR###
        elif eventos == 'Parar':
            recording = False
            img = np.full((480, 640), 255)
            imgbytes = cv2.imencode('.png', img)[1].tobytes()
            windowum['-image-'].update(data=imgbytes)
            windowum['-TEXT-'].update(f'Pessoas na imagem: 0') #marca as faces contando-as
            windowum['Capturar'].update(disabled = True) # Desabilita o botão Capturar


        if recording:
            _, frame = video.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                    gray,
                    scaleFactor = 1.3,
                    minNeighbors = 5,
                    minSize = (70,70),
                    maxSize=(300,300))

            #desenha o retangulo
            if eventos != 'Capturar': #Linha alterada
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x-50, y-50), (x+w+50, y+h+50), (0, 255, 0), 4)

            #update da imagem
            imgbytes = cv2.imencode('.png',frame)[1].tobytes()
            windowum['-image-'].update(data=imgbytes)

            #update do texto
            windowum['-TEXT-'].update(f'Pessoas na imagem: {len(faces)}') #marca as faces contando-as


        # buscar dados na tabela
        if eventos == "Buscar":
            #procura usuario na tabela usuario
            query = (f"""SELECT * FROM Aluno WHERE Matric = '{valores['-matric-']}' """)
            cursor.execute(str(query))

            #verifica se o query retornou alguma linha
            if cursor.fetchone() != None:
                cursor.execute(str(query))
                linha = cursor.fetchone() ## Joga o resultado na variável linha

                if linha != 0:
                    # valida o nome e a senha
                    if valores['-matric-'] == linha[0]:
                        windowum['-aluno-'].update(linha[1]) # Coloca o valor no INPUT -aluno-
                        
                        windowum['Ligar'].update(disabled = False) # Coloca o botão ativado
                        windowum['Parar'].update(disabled = False) # Coloca o botão ativado
                        
            else:
                sg.Popup('Aluno não cadastrado')
                    
                windowum['Ligar'].update(disabled = True) # Coloca o botão desativado
                windowum['Parar'].update(disabled = True) # Coloca o botão desativado


        ###Salva a imagem em um JPG clicando em CAPTURAR###
        if eventos == 'Capturar': #Botão Capturar clicado
            nomeimagem = pastafotos+valores['-matric-']+'.png'
            cv2.imwrite(nomeimagem,frame) #Captura a foto

        ###Edita a imagem em um PNG clicando em EDITAR###
        if eventos == 'Editar': #Botão Editar clicado
            nomeimagem = pastafotos+valores['-matric-']+'.png'
            windowum['-image-'].update(nomeimagem)

            im = cv2.imread(nomeimagem)
            fonte = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(im,'Selecione com o mouse',(5,30), fonte,
            1,(0,0,0),1,cv2.LINE_AA) 

            cv2.putText(im,'Tecle Enter pra salvar',(5,60), fonte,
            1,(0,0,0),1,cv2.LINE_AA)
            
            showCrosshair = False
            fromCenter    = False

            # Select ROI
            myroi = cv2.selectROI("imgName", im, fromCenter, showCrosshair)

            # Crop image
            imCrop = im[int(myroi[1]):int(myroi[1]+myroi[3]), int(myroi[0]):int(myroi[0]+myroi[2])]

            #Redimensiona a Imagem
            largura = imCrop.shape[1]
            altura = imCrop.shape[0]
            proporcao = float(altura/largura)
            largura_nova = 120 #em pixel
            altura_nova = int(largura_nova*proporcao)
            tamanho_novo = (largura_nova, altura_nova)
            imCrop = cv2.resize(imCrop,
                                tamanho_novo, interpolation = cv2.INTER_AREA)

            

            cv2.imwrite(pastafotos+valores['-matric-']+'.png',imCrop) #Captura a foto


            #cv2.imwrite('imagemcorte.png',imCrop) #Captura a foto
            cv2.destroyAllWindows()

        if eventos == "-matric-" and valores['-matric-'] != '':
            windowum['Buscar'].update(disabled = False) # Coloca o botão ativado
        

        ###Sair do sistema clicando no butão SAIR###
        if eventos == 'Sair' or eventos == sg.WIN_CLOSED:
            break

    windowum.close()
