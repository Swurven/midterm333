import socket

def connect_to_server(host='127.0.0.1', port=12345):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        
        # Send a message to the server
        message = "Hello, Server!"
        client_socket.send(message.encode())
        
        # Receive server's response
        response = client_socket.recv(1024).decode()
        print(f"Received from server: {response}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        client_socket.close()
        print("Disconnected from server.")

if __name__ == "__main__":
    connect_to_server()