# -*- coding: utf-8 -*-
import socket, os, re, sys
from pkg_resources import load_entry_point

# Uso de IPv4(af_inet) + TCP(sock_stream)
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

sock.bind( ("0.0.0.0", 65432) )

#socket escutando...
sock.listen( 5 )

s, clientSock = sock.accept()

print( ">> Conexao recebida" )
print ( "IP Remoto: %s" % clientSock[0] )
print ( "Porta Remota: %d" % clientSock[1] )

# Variavel onde vai ser guardada a informacao recebida
data = ""
while ( data[-4:] != "\n\r##" ):    
    data += s.recv( 1024 )

#Protocolo ICMP
cmd = "ping -c4 " + clientSock[0]
r = "".join(os.popen(cmd).readlines())
print (r)

data = data.replace( "\n\r##", "" )

f = open( "/home/ok.jpg", "wb" )
f.write( data )
f.close()

#Fechar os sockets criados. 
sock.close()
s.close()
print( ">> Recepcao terminada!" )


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyspeedtest==1.2.7', 'console_scripts', 'pyspeedtest')()
    )
