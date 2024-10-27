import socket
import sys
from datetime import datetime

def port_scanner(remote_host, start_port=1, end_port=1024):
    """
    A simple port scanner tool to check open ports on a target host.
    
    Args:
        remote_host (str): The hostname or IP address to scan.
        start_port (int): The starting port in the range (default is 1).
        end_port (int): The ending port in the range (default is 1024).
    """
    # Resolving host IP address
    try:
        remote_host_ip = socket.gethostbyname(remote_host)
    except socket.gaierror:
        print("Error: Hostname could not be resolved.")
        sys.exit()

    print(f"\nScanning {remote_host_ip} from port {start_port} to {end_port}...")
    start_time = datetime.now()

    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set timeout for socket connection
            result = sock.connect_ex((remote_host_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
            sock.close()
    except KeyboardInterrupt:
        print("Scan interrupted by user.")
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

    print(f"\nScan completed in: {datetime.now() - start_time}")

if __name__ == "__main__":
    target = input("Enter a remote host to scan: ")
    port_scanner(target)
