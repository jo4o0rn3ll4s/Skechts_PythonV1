
import PySimpleGUI as sg

import cv2,os

import numpy as np
from PIL import Image

import shutil

pastatreino = os.path.dirname(os.path.abspath(__file__))+'\RecFacial\Treino\\'

recognizer = cv2.face.LBPHFaceRecognizer_create()

detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getfotos():
    layout = [[sg.Text(' ', key = '-TEXT-', size=(40, 1), expand_x = True, justification = 'c', font='Helvetica 16')],
              [sg.Text ('', size = (15,1)),
               sg.Button('Treino', size=(8, 1), font='Helvetica 12'),
               #sg.Text ('', size = (0,1)),
               #sg.Button('Parar', size=(8, 1), font='Helvetica 12', disabled = True), # Cria o botão desabilitado
               #sg.Text ('', size = (0,1)),
               #sg.Button('Capturar', size=(8, 1), font='Helvetica 12', disabled = True), # Cria o botão desabilitado
               sg.Text ('', size = (0,1)),
               sg.Button('Sair', size=(8, 1), font='Helvetica 12'),]           
             ]
    window = sg.Window("Cria o Arquivo de Treino das Faces", layout, modal=True)
    choice = None

    recording = False

    while True:
        event, values = window.read(timeout=0)
        if event == sg.WIN_CLOSED:
            break

        ###Sair do sistema clicando no butão SAIR###
        if event == 'Sair' or event == sg.WIN_CLOSED:
            break

        if event == 'Treino':
            def getImagesAndLabels(path):
                #get the path of all the files in the folder
                imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
                #create empth face list
                faceSamples=[]
                #create empty ID list
                Ids=[]
                #now looping through all the image paths and loading the Ids and the images
                for imagePath in imagePaths:
                    #loading the image and converting it to gray scale
                    pilImage=Image.open(imagePath).convert('L')
                    #Now we are converting the PIL image into numpy array
                    imageNp=np.array(pilImage,'uint8')
                    #getting the Id from the image
                    Id=int(os.path.split(imagePath)[-1].split(".")[1])
                    # extract the face from the training image sample
                    faces=detector.detectMultiScale(imageNp)
                    #If a face is there then append that in the list as well as Id of it]
                    for (x,y,w,h) in faces:
                        faceSamples.append(imageNp[y:y+h,x:x+w])
                        Ids.append(Id)
                return faceSamples,Ids
            
            faces,Ids = getImagesAndLabels('RecFacial\Fotos')

            recognizer.train(faces, np.array(Ids))
            recognizer.save('trainner.yml')

            dest = shutil.move('trainner.yml', pastatreino+'trainner.yml')
            window['-TEXT-'].update(f'Gravado') #marca as faces contando-as

    window.close()

   # print ('Gravado')
