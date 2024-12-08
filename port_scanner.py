import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} for open ports between {start_port} and {end_port}...")
    
    # Iterate through the specified range of ports
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        
        sock.close()

if __name__ == "__main__":
    target_host = "127.0.0.1"  # Can also use "scanme.nmap.org" for testing
    start_port = 20
    end_port = 443
    
    scan_ports(target_host, start_port, end_port)
