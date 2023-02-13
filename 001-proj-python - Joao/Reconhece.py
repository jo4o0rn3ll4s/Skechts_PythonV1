'''
Cria tela que conta captura as fotos
File name: Reconhece.py
'''

####Abre a CAM e enquadra o rosto###

## Carregando PySimpleGUI
import PySimpleGUI as sg

## Carregando a OpenCV
import cv2

import numpy as np

import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
#Direciona para a pasta dos treinos
pastatreino = os.path.dirname(os.path.abspath(__file__))+'\RecFacial\Treino\\'

recognizer.read(pastatreino+'trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
Id=0
gray = 0
font = cv2.FONT_HERSHEY_SIMPLEX

sg.theme('Reddit') #Define as cores da tela

def reconhece_pessoas():
    layout = [[sg.Image(key='-image-')],
              [sg.Text(' ', key = '-TEXT-', size=(40, 1), expand_x = True, justification = 'c', font='Helvetica 16')],
              [sg.Text(' ', key = '-TEXT1-', size=(40, 1), expand_x = True, justification = 'c', font='Helvetica 16')],
              [sg.Text ('', size = (10,1)),
               sg.Button('Ligar', size=(8, 1), font='Helvetica 12'),
               sg.Text ('', size = (0,1)),
               sg.Button('Parar', size=(8, 1), font='Helvetica 12', disabled = True), # Cria o botão desabilitado
               sg.Text ('', size = (0,1)),
               sg.Button('Sair', size=(8, 1), font='Helvetica 12'),]           
             ]

    window = sg.Window("Reconhece Pessoa", layout, modal=True)
    choice = None

    # pega o video
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    recording = False
    sampleNum=0

    while True:
        event, values = window.read(timeout=0)
        nome = ''
        if event == sg.WIN_CLOSED:
            break
        
        ###Liga a WEBCAM clicando no botão LIGAR###
        elif event == 'Ligar':
            recording = True
            window['Ligar'].update(disabled = True) # Desabilita o botão Capturar
            window['Parar'].update(disabled = False) # Habilita o botão Capturar

        ###Desliga a WEBCAM clicando no botão PARAR###
        elif event == 'Parar':
            recording = False
            img = np.full((480, 640), 255)
            imgbytes = cv2.imencode('.png', img)[1].tobytes()
            window['-image-'].update(data=imgbytes)
            window['-TEXT-'].update(f'Pessoas na imagem: 0') #marca as faces contando-as
            window['Ligar'].update(disabled = False) # Desabilita o botão Capturar
            window['Parar'].update(disabled = True) # Desabilita o botão Capturar
            
        if recording:
            #_, frame = cam.read()
            ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)
                                            
            #desenha o retangulo
            for(x, y, w, h) in faces:
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0, 255, 0),2)
                    Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
                    
                    if(conf<70):
                        arquivo = open(pastatreino+('Dados.txt'),'r') ##Abre o arquivo para leitura
                        for linha in arquivo:  ##Varre o arquivo linha a linha
                            aluno = linha.split(',') ##Separa os dados da linha de acordo com a Virgula
                            matric = aluno[1] ## Matric recebe o valor dos dados
                            matric = matric.replace('\n', '') ##dá um replace pra excluir o \n trocando por espaço

                            if matric == str(Id):
                                 nome=aluno[0] ## Nome recebe o valor vindo do arquivo
  
                    else:
                        nome="Nao Encontrado"

                    cv2.putText(im,(nome),(x+5,y-15), font, 1,(255,255,255),2,cv2.LINE_AA)
                       
                    #update da imagem
                    imgbytes = cv2.imencode('.png',im)[1].tobytes()
                    window['-image-'].update(data=imgbytes)

            #update do texto
            window['-TEXT-'].update(f'Pessoas na imagem: {len(faces)}') #marca as faces contando-as

        ###Sair do sistema clicando no butão SAIR###
        if event == 'Sair' or event == sg.WIN_CLOSED:
            break

    window.close()
