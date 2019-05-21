# -*- coding: utf-8 -*-
import socket

host = "10.0.13.46" #ip do servidor
porta = 65432

# Uso de IPv4(af_inet) + TCP(sock_stream)
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

sock.connect( (host, porta) )
sock.send('Cliente conectado')

resposta = sock.recv(4096)
print(resposta)
print( ">> Conexão estabelecida!" )

#imagem que será enviada
f = open( "/home/andressa/banguela.jpg", "rb" )

data = "" # Variável para onde vai ser carregado o f.


data = f.readlines() # Carrega para a variável 'data' cada linha do ficheiro.
for line in data:
    # Envia cada linha para o servidor.
    print (line)
    sock.send( line )

# imagem foi enviada na totalidade.
EOF = "\n\r##"
sock.send( EOF )

f.close()
sock.close() 