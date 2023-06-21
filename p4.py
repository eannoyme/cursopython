#informae valores
#exibir a soma de a+b
#exibir a subitraçao de a-b
#exibir a multiplicaçao de a*b
#exibir a divisao de a/b

import time
import os
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    a=int(input("informe valor de a "))
    b=int(input("informe valor de b "))
    print("a soma de a+b : ",a+b)
    print("a subtraçao de a+b : ",a-b)
    print("a multiplicaçao de a+b : ",a*b)
    print("a divisao de a+b : ",a/b)
    print("a elevado de a+b : ",a**b)
    time.sleep(4) # Sleep for 3 seconds