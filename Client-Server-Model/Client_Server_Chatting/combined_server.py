import socket
import threading

def handle_chat_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    def receive_messages(client_socket):
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Client ({client_address}): {data}")

    def send_messages(client_socket):
        while True:
            try:
                response = input("Enter your response: ")
                client_socket.sendall(response.encode('utf-8'))
            except Exception as e:
                print(f"Error: {e}")
                break

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    print(f"Connection from {client_address} closed.")
    client_socket.close()

def handle_calculator_client(client_socket, client_address):
    print(f"Accepted connection from {client_address} (calculator)")

    while True:
        expression = client_socket.recv(1024).decode('utf-8')
        if not expression:
            break
        print(f"Client ({client_address}) expression: {expression}")
        
        try:
            result = eval(expression)
            client_socket.sendall(str(result).encode('utf-8'))
        except Exception as e:
            print(f"Calculation error: {e}")
            client_socket.sendall("Error".encode('utf-8'))

    print(f"Client ({client_address}) closed (calculator).")
    client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_type = client_socket.recv(1024).decode('utf-8')
        
        if client_type.lower() == 'chat':
            threading.Thread(target=handle_chat_client, args=(client_socket, client_address)).start()
        elif client_type.lower() == 'calculator':
            threading.Thread(target=handle_calculator_client, args=(client_socket, client_address)).start()
        else:
            print(f"Unknown client type from {client_address}: {client_type}")

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345

    start_server(HOST, PORT)
