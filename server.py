import os
import time
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
address = './server_file'

try:
    os.unlink(address)
except FileNotFoundError:
    pass

sock.bind(address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(16)
            decoded = data.decode('utf-8')
            print('Recieved: ' + decoded)
            if data:
                decoded = 'ServerProcessing' + decoded
                
                connection.sendall(decoded.encode())
            else:
                print('no data was sent.')
                break
    finally:
        print('Close connection.')
        connection.close()
        break





