'''
Cria tela que conta as pessoas em uma imagem
File name: ContaPessoas.py
'''

####Abre a CAM e enquadra o rosto###

## Carregando PySimpleGUI
import PySimpleGUI as sg

## Carregando a OpenCV
import cv2

import numpy as np

sg.theme('Reddit') #Define as cores da tela


def conta_pessoas_window():
    layout = [
              [sg.Image(key='-image-')],
              [sg.Text(' ', key = '-TEXT-', size=(40, 1), expand_x = True, justification = 'c', font='Helvetica 16')],
              [sg.Text ('', size = (5,1)),
               sg.Button('Ligar', size=(8, 1), font='Helvetica 12'),
               sg.Text ('', size = (0,1)),
               sg.Button('Parar', size=(8, 1), font='Any 12'),
               sg.Text ('', size = (0,1)),
               sg.Button('Capturar', size=(8, 1), font='Helvetica 12', disabled = True), # Cria o botão desabilitado
               sg.Text ('', size = (0,1)),
               sg.Button('Sair', size=(8, 1), font='Helvetica 12'),]           
             ]


    window = sg.Window("Detector da Face", layout, modal=True)
    choice = None

    # pega o video
    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    recording = False

    while True:
        event, values = window.read(timeout=0)
        if event == sg.WIN_CLOSED:
            break
    
        ###Liga a WEBCAM clicando no botão LIGAR###
        elif event == 'Ligar':
            recording = True
            window['Capturar'].update(disabled = False) # Habilita o botão Capturar

        ###Desliga a WEBCAM clicando no botão PARAR###
        elif event == 'Parar':
            recording = False
            img = np.full((480, 640), 255)
            imgbytes = cv2.imencode('.png', img)[1].tobytes()
            window['-image-'].update(data=imgbytes)
            window['-TEXT-'].update(f'Pessoas na imagem: 0') #marca as faces contando-as
            window['Capturar'].update(disabled = True) # Desabilita o botão Capturar


        if recording:
            _, frame = video.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                                                  gray,
                                                  scaleFactor = 1.3,
                                                  minNeighbors = 5,
                                                  minSize = (70,70))

            #desenha o retangulo
            if event != 'Capturar': #Linha alterada
                for(x, y, w, h) in faces:
                    cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)

            #update da imagem
            imgbytes = cv2.imencode('.png',frame)[1].tobytes()
            window['-image-'].update(data=imgbytes)

            #update do texto
            window['-TEXT-'].update(f'Pessoas na imagem: {len(faces)}') #marca as faces contando-as

        ###Salva a imagem em um JPG clicando em CAPTURAR###
        if event == 'Capturar': #Botão Capturar clicado
            cv2.imwrite(nomeimagem,frame) #Captura a foto
        

        ###Sair do sistema clicando no butão SAIR###
        if event == 'Sair' or event == sg.WIN_CLOSED:
            break

    window.close()    

