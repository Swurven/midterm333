import socket

def start_server(host='127.0.0.1', port=12345):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")
    
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")
        
        # Receive data from client
        data = client_socket.recv(1024).decode()
        print(f"Received from client: {data}")
        
        # Send a response to client
        client_socket.send("Message received!".encode())
        
        # Close the client socket after communication
        client_socket.close()

if __name__ == "__main__":
    start_server()
