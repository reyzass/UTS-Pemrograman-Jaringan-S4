import socket
import random
import threading
import time

def generate_random_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    return random.choice(colors)

def client_handler(client_socket, client_address):
    while True:
        color = generate_random_color()
        print(f"Sending color '{color}' to {client_address}")
        client_socket.sendto(color.encode(), client_address)
        time.sleep(10)

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    print("Server is running...")

    while True:
        client_data, client_address = server_socket.recvfrom(1024)
        client_data = client_data.decode()

        if client_data == "connect":
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            threading.Thread(target=client_handler, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    main()
