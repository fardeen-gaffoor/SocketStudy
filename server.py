import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8000))
server_socket.listen(1)

print("Server listening on port 8000...")

conn, addr = server_socket.accept()
print("Connected by", addr)

message = "Hello from server"
conn.send(message.encode())

data = conn.recv(1024).decode()
print("Received from client:", data)

conn.close()
server_socket.close()