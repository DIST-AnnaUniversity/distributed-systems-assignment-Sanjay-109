import socket
import threading

def send_messages(client_socket):
    while True:
        message = input("Enter your message: ")
        client_socket.sendall(message.encode('utf-8'))

def receive_messages(client_socket):
    while True:
        response = client_socket.recv(1024).decode('utf-8')
        print("Server:", response)

def start_chat_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall('chat'.encode('utf-8'))

    print("Connected to the chat server")

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))

    send_thread.start()
    receive_thread.start()

    send_thread.join()
    receive_thread.join()

    print("Closing the connection to the chat server")
    client_socket.close()

def start_calculator_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall('calculator'.encode('utf-8'))

    print("Connected to the calculator server")

    while True:
        expression = input("Enter an arithmetic expression (or 'exit' to quit): ")

        if expression.lower() == 'exit':
            break

        client_socket.sendall(expression.encode('utf-8'))

        result = client_socket.recv(1024).decode('utf-8')
        print(f"Result: {result}")

    print("Closing the connection to the calculator server")
    client_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT_CHAT = 12345
    PORT_CALCULATOR = 12345

    print("Choose an option:")
    print("1. Chat Server")
    print("2. Calculator Server")

    option = input("Enter your choice: ")

    if option == '1':
        start_chat_client(HOST, PORT_CHAT)
    elif option == '2':
        start_calculator_client(HOST, PORT_CALCULATOR)
    else:
        print("Invalid option")
