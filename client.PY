import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8000))
print("Client connected from:", client_socket.getsockname())
server_message = client_socket.recv(1024).decode()
print("Received from server:", server_message)
client_socket.send("Acknowledgement received by client".encode())

client_socket.close()