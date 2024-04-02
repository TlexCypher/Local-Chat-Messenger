import logging
import os
import socket

from faker import Faker

server_address = '/tmp/server_socket_file'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

logging.basicConfig(filename="local_chat_messenger_server.log", level=logging.INFO)
logger = logging.getLogger()

try:
    os.unlink(server_address)
    logger.info("Unlink {}".format(server_address))
except FileNotFoundError:
    logger.info("You haven't need to unlink server_address: {}".format(server_address))

sock.bind(server_address)
logger.info("Bind server to {}".format(server_address))

sock.listen(1)

try:
    while True:
        connection, client_address = sock.accept()
        logger.info("Accept connection from {}".format(client_address))
        message_from_client = connection.recv(4096).decode('utf-8')
        print(message_from_client)

        while True:
            if message_from_client:
                logger.info("Had a message (decoded by utf-8): {}".format(message_from_client))
                fake = Faker()
                response = fake.text()
                logger.info("Generate fake response: {}".format(response))
                connection.sendall(response.encode())
                logger.info("Sent back encoded response for client")

            else:
                logger.info("Had a no message from client.")
                break
finally:
    logger.info("Closing connection...")
    sock.close()




