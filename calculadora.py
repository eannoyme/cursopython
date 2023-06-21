#fazer uma calculadora

import os
import time
def calcular(x,y):
    t=(exponencial(x,y))**2
    z=somar(x,y)
    w=dividir(x,y)
    u=multiplicar(x,y)
    resultado = (t/z)*(w/u)

    x =((exponencial(x,y)**2)/somar(x,y))*(dividir(x,y)/multiplicar(x,y))

    return x

def exponencial(x,y):
    resultado = x**y
    return resultado

def multiplicar(x,y):
    resultado = x*y
    return resultado

def dividir(x,y):
    resultado = x/y
    return resultado

def somar(x,y):
    resultado = x+y
    return resultado

def subtrair(x,y):
    resultado = (x-y)
    return resultado

if __name__ == "__main__":
   a=int(input("valor de a : "))
   b=int(input("vlaor de b : "))
   print("soma =",somar(a,b))
   print("dividir =",dividir(a,b))
   print("multiplicar =",multiplicar(a,b))
   print("subtrair =",subtrair(a,b))
   print("exponencial =",exponencial(a,b))
   print("calcular =",calcular(a,b))
   time.sleep(4) # Sleep for 3 seconds
   os.system('cls' if os.name == 'nt' else 'clear')