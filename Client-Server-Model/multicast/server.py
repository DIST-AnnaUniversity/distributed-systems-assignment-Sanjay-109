
import socket
import threading
import subprocess

def handle_client(client_socket, address):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received from {address}: {data}")

def get_client_info():
    result = subprocess.run(['netstat', '-ant'], capture_output=True, text=True)
    return result.stdout

def server():
    host = socket.gethostname()
    port = 21042
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    print(f"Server is listening on {host}:{port}")
    while True:
        client_socket, address = s.accept()
        print(f"Accepted connection from {address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

        # Use a system call to get information about connected clients
        client_info = get_client_info()
        print(f"Connected clients:\n{client_info}")
server()