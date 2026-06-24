import socket
from crypto import encrypt_message

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))

print("Connected to Server")

while True:

    message = input("You: ")

    encrypted = encrypt_message(message)

    client.send(
        encrypted.encode()
    )
