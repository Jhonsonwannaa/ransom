import os
from cryptography.fernet import Fernet

os.chdir('/home/jhonson/')


x = open('calm.txt', 'r') # remplace par un fichier crypté soit cree un fichier et met tout les fichier crypté a l'interieur'
for xx in x :
        xa = xx.strip()
        xv = str(os.path.isfile(xa))
        car = xa+' '+xv
        if 'True' in car :
                caca = car.split()
                ca = str(caca[0])
                dada = open(ca, 'r')
                for xd in dada :
                        xxd = xd
                        
                        f = Fernet(cle) # met la clés
                        token = f.decrypt(xd)
                        file =open(ca,'w')
                        file.write(token)
