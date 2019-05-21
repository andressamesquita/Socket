# -*- coding: utf-8 -*-
import socket

# Uso de IPv4(af_inet) + TCP(sock_stream)
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)


sock.connect( ("10.0.13.46", 65432) )
print( ">> Conexão estabelecida!" )

#imagem que será enviada
f = open( "/home/andressa/banguela.jpg", "rb" )

data = ""

data = f.readlines()
for line in data:
    # Envia cada linha para o servidor.
    sock.send( line )


EOF = "\n\r##"
sock.send( EOF )

f.close()
sock.close()