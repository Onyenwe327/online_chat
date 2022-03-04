import socket
import time

count = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
s.bind(('127.0.0.1', 4444))  # bind the address (host, port) to the socket
s.listen(5)  # start TCP listening
print('Waiting for clients to connect...')

while True:
    sock, addr = s.accept()  # the server passively accept TCP client connections
    print('Accept new connection from %s:%s...' % addr)
    if count == 0:
        data_B = sock.recv(1024)  # receive TCP messages
        print(str(data_B))
        fl_total_sz = int(data_B.decode())  # Decodes obj using the codec registered for encoding.
        rece_sz = 0
        sock.send('received'.encode())  # #Encodes obj using the codec registered for encoding.
        data = sock.recv(1024)
        flpath = str(data.decode())  # Decodes obj using the codec registered for encoding.
        f = open(flpath, 'wb')  # Used to open a file
    while rece_sz < fl_total_sz:
        data = sock.recv(1024)
        f.write(data)  # Used to write the specified string to the file
        rece_sz += len(data)
        print('already received ', rece_sz, ' Byte')
    data = sock.recv(1024)
    if data == b'end':
        break

f.close()  # Used to close the file
s.close()  # Used to close the socket
