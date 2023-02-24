#import mysql.connector
#from mysql.connector import errorcode
import psycopg2
from flask_bcrypt import generate_password_hash


print("Conectando...")
con = psycopg2.connect(host='localhost', 
                         database='jogoteca',
                         user='postgres', 
                         password='1234')


cursor = con.cursor()


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
     ("Bruno Divino", "BD", generate_password_hash("alohomora").decode('utf-8')),
      ("Camila Ferreira", "Mila", generate_password_hash("paozinho").decode('utf-8')),
      ("Guilherme Louro", "Cake", generate_password_hash("python_eh_vida").decode('utf-8')),
      ("Lucas Ribeiro", "lucas", generate_password_hash("1234").decode('utf-8'))
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

 # inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
      ('Tetris', 'Puzzle', 'Atari'),
      ('God of War', 'Hack n Slash', 'PS2'),
      ('Mortal Kombat', 'Luta', 'PS2'),
      ('Valorant', 'FPS', 'PC'),
      ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
      ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1]) 

# commitando se não nada tem efeito
con.commit()

cursor.close()
con.close()
