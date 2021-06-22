import sys
import os 
import time
import shutil

import tkinter
from tkinter import *

from zipfile import ZipFile


                        ###########################
                        #        Programme        #
                        #      de sauvegarde      #
                        ###########################

def doBackUp():
    backup()

def stop():
    exit()

def backup():
    # On copie colle les fichiers systèmes vers le fichier de sauvegarde sur
    # la NUC

    origine = r"C:\Users\Leo" # Chemin comprenant les fichiers à save

    # Création d'un répertoire permettant de stocker le backup en forme compressée 
    if not os.path.exists(r"C:\Users\Leo\BackUp"):
        os.makedirs(r"C:\Users\Leo\BackUp")

    # Destination de copiage 
    destination = r"C:\Users\Leo\BackUp"

    # Faire l'archivage des dossiers personnels 
    shutil.make_archive(origine, 'zip', origine)

    # Déplacer le fichier backup dans le dossier référencé 
    shutil.move(r"C:\Users\Leo.zip", destination)


def main():    

    # Interface

    app = Tk() 

    app.geometry("720x480")
    app.minsize(720,480)
    app.config(background='white')
    app.title("Back Up")

    frame = Frame(app)

    label_title = Label(app, text = "Back up en cours ...", font = ("Courrier", 20), bg = "white", fg = 'black')
    label_title.pack()

    label_subtitle = Label(app,text = "Voulez-vous continuer la sauvegarde de vos données ?", font =("Courrier", 15), bg = "white", fg ='black')
    label_subtitle.pack()

    label_YesBTN = Button(app, command=doBackUp,text = "OUI")
    label_YesBTN.pack()

    label_NoBTN = Button(app,command=stop,text = "ANNULER")
    label_NoBTN.pack()
    
    frame.pack(expand = tkinter.YES)
    
    app.mainloop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
