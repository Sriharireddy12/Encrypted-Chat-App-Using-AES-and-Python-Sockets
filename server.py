import socket
import threading
from crypto import decrypt_message

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server Started...")

clients = []

def handle_client(client):
    while True:
        try:
            msg = client.recv(4096).decode()

            if not msg:
                break

            text = decrypt_message(msg)

            print(f"[MESSAGE] {text}")

            # Save messages to chat.log
            with open("chat.log", "a") as log:
                log.write(text + "\n")

        except:
            break

    client.close()

while True:
    client, addr = server.accept()

    print(f"Connected: {addr}")

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()
