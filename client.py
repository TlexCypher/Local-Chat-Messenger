import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = './server_file'
client_address = './client_file'

print('try to have connection to {}'.format(client_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

while True:
    try:
        while True:
            message = input()
            sock.sendall(message.encode())
            sock.settimeout(2)
            data = str(sock.recv(32))
            if data:
                print('Server response: ' + data)
            else:
                break

    except socket.timeout:
        print('Socket timeout, ending listening for server messages')

    finally:
        print('Close socket.')
        sock.close()
        break

