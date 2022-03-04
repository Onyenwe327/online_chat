import socket
import sys
import threading
from utility import encodeMessage, decodeMessage

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
ip_ad = '127.0.0.1'
PORT = 4444
server.bind((ip_ad, PORT))  # bind the address (host, port) to the socket
server.listen(100)  # start TCP listening
clients = {}  # Mapping of Client Connection with its Client Name


def main():
    print('Waitnig for clients to connect...')
    while True:
        conn, addr = server.accept()
        clients[conn] = ''
        print('{} client connected: {}'.format(len(clients), addr[0]))
        print('{} connected'.format(addr))
        a = threading.Thread(target=newClient, args=(conn, addr,))
        a.start()
    server.close()


def newClient(conn, addr):
    clientName = str(addr[0]) + '.' + str(addr[1])
    conn.send(encodeMessage('Welcome to chat room, enter you name: '))
    clientName = decodeMessage(conn.recv(4096))
    clients[conn] = clientName
    broadcast(encodeMessage('{} connected'.format(clientName)), conn)
    while True:
        try:
            msg = conn.recv(4096)
            if msg:
                msg = clientName + ': ' + decodeMessage(msg)
                print(msg)
                broadcast(encodeMessage(msg), conn)
            else:
                removeClient(conn)
                break
        except:
            continue


def broadcast(msg, conn=None):
    for client in clients:
        if (client == conn):
            continue
        try:
            client.send(msg)
        except:
            removeClient(client)


def removeClient(curClient):
    if curClient in clients:
        broadcast(encodeMessage('{} disconnected'.format(clients[curClient])), curClient)
        clients.pop(curClient)


if __name__ == '__main__':
    main()
