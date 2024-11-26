import socket
# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Specify the server address and port
server_address = ('127.0.0.1', 8080)
# Message to be sent to the server
message = "Hello, UDP Server!"
client_socket.sendto(message.encode(), server_address)
print(f"Sent message to server: {message}")
# Receive the echoed message from the server
data, _ = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")
# Close the client socket
client_socket.close()