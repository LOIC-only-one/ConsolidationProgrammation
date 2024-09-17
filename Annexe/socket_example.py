import socket
import threading

clients = []

def broadcast(message, sender_socket):
    """
    Fonction pour envoyer un message à tous les clients sauf l'expéditeur.
    """
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message)
            except BrokenPipeError:
                clients.remove(client)

def handle_client(client_socket):
    """
    Fonction pour gérer la communication avec un client.
    """
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            broadcast(data, client_socket)
        except ConnectionResetError:
            break
    client_socket.close()
    clients.remove(client_socket)



def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen()

    print("Serveur en attente de connexion...")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection from {addr} has been established!")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()