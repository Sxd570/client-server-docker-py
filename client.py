import socket
import sys

def send_equation(equation):
    host = 'equation-server'
    port = 4444

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(equation.encode('utf-8'))

    result = client_socket.recv(1024).decode('utf-8')
    print(f"Result received from server: {result}")

    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <equation>")
        sys.exit(1)

    equation = sys.argv[1]
    send_equation(equation)
