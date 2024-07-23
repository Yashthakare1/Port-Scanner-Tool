import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return port
        sock.close()
    except Exception as e:
        pass
    return None

# Function to scan multiple ports
def scan_ports(ip, start_port, end_port):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port+1)]
        for future in futures:
            result = future.result()
            if result is not None:
                open_ports.append(result)
    return open_ports

# Main function to scan a network
def network_scan(target_ip, start_port, end_port):
    print(f"Scanning target {target_ip}")
    print(f"Time started: {str(datetime.now())}")
    
    open_ports = scan_ports(target_ip, start_port, end_port)
    
    print(f"Open ports on {target_ip}:")
    for port in open_ports:
        print(f"Port {port} is open")
    
    print(f"Time finished: {str(datetime.now())}")

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    network_scan(target_ip, start_port, end_port)
