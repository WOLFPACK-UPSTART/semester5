
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080)) # Connect to server
client_socket.sendall(b"Hello, Server form !")
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")
client_socket.close()
