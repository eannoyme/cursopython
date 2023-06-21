#construir uma funçao para exibir numero

import random

def exibir_numero(qtd_jogos):
    for j in range(qtd_jogos):
        print("jogo : ",j+1)
        x = 1
        numeros = ""
        for x in range(6):
            numeros = numeros + " " + str(random.randrange(1, 60, 1))
        print(numeros)

if __name__ == "__main__":
    q=int(input("quantos jogos? : "))
    exibir_numero(q)
