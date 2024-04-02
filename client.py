import logging
import os
import socket
import sys

client_address = '/tmp/client_socket_file'
server_address = '/tmp/server_socket_file'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

logging.basicConfig(filename="local_chat_messenger_client.log", level=logging.INFO)
logger = logging.getLogger()

try:
    os.unlink(client_address)
    logger.info("Unlink {}".format(client_address))
except FileNotFoundError:
    logger.info("You haven't need to unlink client_address: {}".format(client_address))

sock.bind(client_address)
logger.info("Bind client to {}".format(client_address))

try:
    sock.connect(server_address)
except socket.error as error:
    logger.error("Failed to connect with server.")
    sys.exit(1)

try:
    while True:
        print("Please input something...!")
        client_input = input()
        encoded_client_input = client_input.encode()
        sock.sendall(encoded_client_input)
        # sock.settimeout(2)

        try:
            client_response = sock.recv(4096).decode('utf-8')
            if client_response:
                logger.info("Server response: {}".format(client_response))
                print("Server response: {}".format(client_response))
                print("Try again...!")
            else:
                break
        except TimeoutError:
            logger.error("Timeout error occurs.")
            break
finally:
    print("Closing connection...")
    logger.info("Closed socket.")
    sock.close()

