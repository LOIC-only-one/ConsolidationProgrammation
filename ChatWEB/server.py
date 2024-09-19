import socket

server = socket.socket(socket.AF_INET, socket.AF_STREAM)
server.bind(('localhost', 12345))

server.listen(1)
print("Le serveur est en écoute sur le port 12345...")

try:
    client_socket, client_address = server.accept()
except KeyboardInterrupt:
    print("Le serveur est terminé")