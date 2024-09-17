import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 1234))

pseudo = input("Entrez votre pseudo: ")

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(data.decode())
        except ConnectionResetError:
            break

# Démarrer un thread pour recevoir les messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input("Entrez votre message: ")
    if message.lower() == "exit":
        break
    
    client_socket.sendall('{pseudo}: {message}'.format(pseudo=pseudo, message=message).encode())

client_socket.close()