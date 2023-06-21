#informar disciplina

import time
import os
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    d=input("disciplina ")
    n1=int(input("nota 1 "))
    n2=int(input("nota 2 "))
    n3=int(input("nota 3 "))
    n4=int(input("nota 4 "))
    nota=(n1+n2+n3+n4)/4
    print("sua nota final é : ",nota)
    if nota <5:
        print("voce esta reprovado")
    elif nota >5:
            print("voce esta aprovado")

    time.sleep(5) # Sleep for 3 seconds
