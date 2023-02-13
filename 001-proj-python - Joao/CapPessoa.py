'''
Cria tela que conta captura as fotos
File name: CapPessoas.py
'''

####Abre a CAM e enquadra o rosto###

## Carregando PySimpleGUI
import PySimpleGUI as sg

## Carregando a OpenCV
import cv2

import numpy as np

import os

#Cria a variavel com o caminho das fotos
pastafotos = os.path.dirname(os.path.abspath(__file__))+'\RecFacial\Fotos\\'

#Cria a variavel com o caminho dos treinos
pastatreino = os.path.dirname(os.path.abspath(__file__))+'\RecFacial\Treino\\'

sg.theme('Reddit') #Define as cores da tela

#Id=input('Enter Your Id:')
Id=0
sampleNum=0
gray = 0

def captura_fotos():
    layout = [[sg.Text("Matric/Nome: "), sg.Input(key = '-matric-', size = (8,1), enable_events=True),
                  sg.Input(key = '-nome-', size = (40,1)),
                ], 
              [sg.Image(key='-image-')],
              [sg.Text(' ', key = '-TEXT-', size=(40, 1), expand_x = True, justification = 'c', font='Helvetica 16')],
              [sg.Text(' ', key = '-TEXT1-', size=(40, 1), expand_x = True, justification = 'c', font='Helvetica 16')],
              [sg.Text ('', size = (5,1)),
               sg.Button('Ligar', size=(8, 1), font='Helvetica 12'),
               sg.Text ('', size = (0,1)),
               sg.Button('Parar', size=(8, 1), font='Helvetica 12', disabled = True), # Cria o botão desabilitado
               sg.Text ('', size = (0,1)),
               sg.Button('Capturar', size=(8, 1), font='Helvetica 12', disabled = True), # Cria o botão desabilitado
               sg.Text ('', size = (0,1)),
               sg.Button('Sair', size=(8, 1), font='Helvetica 12'),]           
             ]

    window = sg.Window("Captura Fotos pra Reconhecer", layout, modal=True)
    choice = None

    # pega o video
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    recording = False
    sampleNum=0

    while True:
        event, values = window.read(timeout=0)
        if event == sg.WIN_CLOSED:
            break
    
        ###Liga a WEBCAM clicando no botão LIGAR###
        elif event == 'Ligar':
            recording = True
            window['Ligar'].update(disabled = True) # Desabilita o botão Capturar
            window['Capturar'].update(disabled = False) # Habilita o botão Capturar
            window['Parar'].update(disabled = False) # Habilita o botão Capturar

        ###Desliga a WEBCAM clicando no botão PARAR###
        elif event == 'Parar':
            recording = False
            img = np.full((480, 640), 255)
            imgbytes = cv2.imencode('.png', img)[1].tobytes()
            window['-image-'].update(data=imgbytes)
            window['-TEXT-'].update(f'Pessoas na imagem: 0') #marca as faces contando-as
            window['Capturar'].update(disabled = True) # Desabilita o botão Capturar
            window['Ligar'].update(disabled = False) # Desabilita o botão Capturar
            window['Parar'].update(disabled = True) # Desabilita o botão Capturar
            


        if recording:
            _, frame = cam.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(
                                                  gray,
                                                  scaleFactor = 1.3,
                                                  minNeighbors = 5)
                                            
            #desenha o retangulo
            if event != 'Capturar': #Linha alterada
                for(x, y, w, h) in faces:
                    cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)

            #update da imagem
            imgbytes = cv2.imencode('.png',frame)[1].tobytes()
            window['-image-'].update(data=imgbytes)

            #update do texto
            window['-TEXT-'].update(f'Pessoas na imagem: {len(faces)}') #marca as faces contando-as

        ###Salva a imagem em um PNG clicando em CAPTURAR###
        if event == 'Capturar': #Botão Capturar clicado
            Id = values['-matric-']
            for sampleNum in range(1,21,1):
                #saving the captured face in the dataset folder
                cv2.imwrite(pastafotos+str(sampleNum)+'.'+Id + ".png", gray[y:y+h,x:x+w])
                if sampleNum == 20:
                    window['-TEXT1-'].update(f'Fotos Capturadas') #altera o texto indicando que a imagem foi capturada
                    try:
                        arquivo = open(pastatreino+('Dados.txt'),'r') ##Abre o arquivo para leitura
                        ##window['-TEXT1-'].update(f'ABRIU') #marca as faces contando-as
                        
                        for linha in arquivo:  ##Varre o arquivo linha a linha
                            aluno = linha.split(',') ##Separa os dados da linha de acordo com a Virgula
                            
                            matric = aluno[1] ## Matric recebe o valor dos dados
                            matric = matric.replace('\n', '') ##dá um replace pra excluir o \n trocando por espaço
                            
                            if matric == values['-matric-']:
                                gravar = 1 ## cria a variável gravar indicando que a MATRIC já existe
                            else:
                                gravar = 2 ## cria a variável gravar indicando que a MATRIC não existe
                        arquivo.close   ##fecha o arquivo     
                    except:
                        arquivo = open(pastatreino+('Dados.txt'),'w') ##Cria o arquivo em branco
                        gravar = 2 ## cria a variável gravar indicando que a MATRIC não existe

                    if gravar == 1:
                        sg.popup_ok('Matricula já cadastrada')
                        arquivo.close ##fecha o arquivo
                    elif gravar == 2:
                        arquivo.close
                        arquivo = open(pastatreino+('Dados.txt'),'a') ##abre o arquivo com opção pra append
                        arquivo.write(values['-nome-']+','+values['-matric-']+ '\n') ##Escreve dados no arquivo
                        arquivo.close ##fecha o arquivo

                        
                        
        ###Sair do sistema clicando no butão SAIR###
        if event == 'Sair' or event == sg.WIN_CLOSED:
            break

    window.close()
