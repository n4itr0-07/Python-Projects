import sys
import socket
from datetime import datetime
import threading

# Function to scan a port
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect((target, port))
        print(f"Port {port} is open")
        s.close()
    except socket.timeout:
        pass  # Ignore timeout errors; port is closed
    except socket.error:
        pass  # Ignore other socket errors
    except Exception as e:
        print(f"Unexpected error on port {port}: {e}")
    finally:
        s.close()

# Main function - argument validation and target definition
def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("Invalid number of arguments")
        print("Usage: python.exe scanner.py <target>")
        sys.exit(1)

    # Resolve the target hostname to an IP address
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        sys.exit(1)

    # Add a pretty banner
    print("-" * 50)
    print(f"Scanning target {target_ip}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    # Use threading to scan ports concurrently
    try:
        threads = []
        for port in range(1, 65536):
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nExiting the program...")
        sys.exit(0)
    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit(1)

    print("\nScan completed successfully!")

if __name__ == "__main__":
    main()
