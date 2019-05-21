# -*- coding: utf-8 -*-
import socket
import threading
import os, re

# Uso de IPv4(af_inet) + TCP(sock_stream)
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

ip = "0.0.0.0"
porta = 65432

sock.bind( (ip, porta) )


#socket escutando...
sock.listen( 5 )
print("Ouvindo em %s:%d"  %(ip, porta))



client, addr = sock.accept()
print("Conexao recebida por %s:%d " % (addr[0], addr[1]))

# Variavel onde vai ser guardada a informacao recebida
data = ""

while ( data[-4:] != "\n\r##" ):    
    data += client.recv( 1024 )
   
#Protocolo ICMP
cmd = "ping -c4 " + ip
r = "".join(os.popen(cmd).readlines())
print (r)


data = data.replace( "\n\r##", "" )

f = open( "/home/andressa/socket_img/minions.jpg", "wb" )
f.write( data )
f.close()

#Fechar os sockets criados. 
sock.close()
client.close()
print( ">> Recepcao terminada!" )
#exit(0)
