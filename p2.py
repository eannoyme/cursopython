#codigo sem mostrar idade

import time
import os
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    n=input("digite seu nome")
    i=int(input("digite sua idade"))
    if i==0:
        exit()
    if i <=12:
        print("voce é criança")
    elif i <=18:
        print("é adolescente")
    elif i <=65:
        print("é adulto")
    elif i >65:
        print("é idoso")

    time.sleep(5) # Sleep for 3 seconds
    