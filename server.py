import socket

def calculate_equation(equation):
    try:
        result = eval(equation)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def start_server():
    host = '127.0.0.1'
    port = 4444

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on port {port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        equation_result = calculate_equation(data)
        print(f"Received equation: {data}")
        print(f"Sending result: {equation_result}")

        client_socket.send(equation_result.encode('utf-8'))

        client_socket.close()

if __name__ == "__main__":
    start_server()
