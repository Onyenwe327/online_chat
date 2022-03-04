import socket
import os
import time

flna = input('Please enter the filename you want to send:\n')
fn1, fn2 = os.path.split(flna)  # Separate the file name and path
flsz = str(os.path.getsize(flna))  # To get the file size in bytes
client_addr = ('127.0.0.1',4444)
f = open(flna,'rb')  # Open a file
count = 0
flag = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
#Build connection:
s.connect(('127.0.0.1', 4444))
while True:
    if count == 0:
        s.send(flsz.encode())
        start = time.time()
        s.recv(1024)
        s.send(fn2.encode())
    for line in f:
        s.send(line)
        print('sending please wait...')
    s.send(b'end')
    break

s.close  # Used to close the socket
end = time.time()
print('cost' + str(round(end - start, 2)) + 's')
