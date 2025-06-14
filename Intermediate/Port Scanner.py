"""
Python Network Port Scanner (User Driven) - Educational Tool

This script scans a range of TCP ports on a specified target host to check which ports are open.
It allows interactive user input for target host and port range to enhance usability.

Usage:
    Run the script and follow the prompts to enter target host and port range.

Notes:
- Use this tool only on networks and systems you own or have permission to scan.
- Scanning unauthorized systems is illegal and unethical.

Author: Ethical Security Research Assistant
License: MIT License
"""

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(host: str, port: int, timeout=1.0) -> bool:
    """
    Attempts to connect to the specified host and port.
    Returns True if connection succeeds (port is open), False otherwise.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            return result == 0
    except Exception:
        return False

def scan_ports(host: str, start_port: int, end_port: int, max_workers=100):
    print(f"Scanning {host} ports {start_port} to {end_port}...")
    open_ports = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(scan_port, host, port): port for port in range(start_port, end_port + 1)}
        for future in as_completed(futures):
            port = futures[future]
            if future.result():
                print(f"Port {port}: OPEN")
                open_ports.append(port)
    print(f"Scan complete. Open ports: {open_ports if open_ports else 'None'}")
    return open_ports

def get_user_input():
    while True:
        target_host = input("Enter target host (IP address or domain name): ").strip()
        if target_host:
            break
        print("Target host cannot be empty. Please enter a valid host.")

    while True:
        try:
            start_port = int(input("Enter start port (default 1): ") or 1)
            end_port = int(input("Enter end port (default 1024): ") or 1024)
            if 1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port:
                break
            else:
                print("Invalid port range. Ports must be between 1 and 65535, and start port must be less than or equal to end port.")
        except ValueError:
            print("Please enter valid integer port numbers.")
    return target_host, start_port, end_port

def main():
    print("Python Network Port Scanner - User Driven")
    print("-----------------------------------------")
    target_host, start_port, end_port = get_user_input()
    scan_ports(target_host, start_port, end_port)

if __name__ == "__main__":
    main()

