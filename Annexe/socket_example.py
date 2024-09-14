import socket
import threading

def handle_client(client_socket):
    """
    Fonction pour gérer la communication avec un client.
    """
    print('Connecté par', client_socket)
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data)
        client_socket.sendall(data)
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen()

    print("Serveur en attente de connexion...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()