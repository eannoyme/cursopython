#servidor gamer

import sqlite3
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Jogador(BaseModel):
    nome: str
    apelido: str
    email: str
    nascimento: str
    status: str

app = FastAPI()
database = '/Users/Ijovem03/thor/database/game.db'

@app.get("/listar")
def listar():
    c = sqlite3.connect(database)
    cr = c.cursor()
    cr.execute("""select nome, apelido, email, nacimento, status from jogador""")
    listar=cr.fetchall()
    c.close()
    return (listar)

@app.post("/inserir")
def inserir(player: Jogador):
    c = sqlite3.connect(database)
    cr = c.cursor()
    cr.execute(""" insert into jogador (nome, apelido, email, nacimento, status) values (?, ?, ?, ?, ?)""",(player.nome, player.apelido, player.email, player.nascimento, player.status))
    c.commit()
    c.close()
    return 0

@app.delete("/banir/{id}")
def banir(id: str):
    c = sqlite3.connect(database)
    cr = c.cursor()
    cr.execute(""" delete from jogador where id=?""",(id,))
    c.commit()
    c.close()
    return 0

@app.post("/record")
def record(id, pontuacao, data):
    c = sqlite3.connect(database)
    cr = c.cursor()
    cr.execute(""" insert into record (id_jogador, pontuacao, data) values (?, ?, ?)""",(id,pontuacao, data))
    c.commit()
    c.close()
    return 0

@app.put("/suspender")
def suspender(id):
    c = sqlite3.connect(database)
    cr = c.cursor()
    cr.execute(""" update jogador set status='DESATIVADO' where id=? """,(id,))
    c.commit()
    c.close()
    return 0

@app.put("/ativar")
def ativar(id):
    c = sqlite3.connect(database)
    cr = c.cursor()
    cr.execute(""" update jogador set status='ATIVADO' where id=? """, (id,))
    c.commit()
    c.close()
    return 0