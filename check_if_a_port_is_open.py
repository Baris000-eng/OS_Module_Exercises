import socket

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open.")
    else:
        print(f"Port {port} is closed.")
    sock.close()

check_port('127.0.0.1', 80)
