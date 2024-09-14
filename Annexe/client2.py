import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 1234))

pseudo = input("Entrez votre pseudo: ")

while True:
    message = input("Entrez votre message: ")
    if message.lower() == "exit":
        break
    
    client_socket.sendall('{pseudo}: {message}'.format(pseudo=pseudo, message=message).encode())
    data = client_socket.recv(1024)
    print('Received', data.decode())

client_socket.close()