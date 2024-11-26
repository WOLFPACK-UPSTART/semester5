import socket
# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to localhost and port 8080
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(1)
print("Server is listening on port 8080...")

# Accept a connection from the client
conn, addr = server_socket.accept()
print(f"Connected to client at {addr}")

# Handle client communication
while True:
    data = conn.recv(1024)  # Receive 1024 bytes of data
    if not data:
        break
    print(f"Received: {data.decode()}")
    conn.sendall(data)  # Echo the data back to the client
    
# Close the connection and socket
conn.close()
server_socket.close()
