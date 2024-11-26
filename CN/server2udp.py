import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to localhost and port 8080
server_socket.bind(('127.0.0.1', 8080))
print("UDP server is up and listening on port 8080...")

# Infinite loop to listen for incoming messages
while True:
    # Buffer size is 1024 bytes
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received message from client: {data.decode()}")
    
    # Echo the message back to the client
    server_socket.sendto(data, client_address)
    print(f"Echoed back to {client_address}")
