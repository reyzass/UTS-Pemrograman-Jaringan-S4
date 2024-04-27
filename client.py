import socket

COLORS_ENGLISH_TO_INDONESIAN = {
    "red": "merah",
    "green": "hijau",
    "blue": "biru",
    "yellow": "kuning",
    "purple": "ungu",
    "orange": "oranye"
}

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b"connect", (server_ip, server_port))

    while True:
        received_color, _ = client_socket.recvfrom(1024)
        received_color = received_color.decode()

        print(f"Received color: {received_color}")

        user_response = input("Masukkan warna dalam bahasa Indonesia: ")

        # Mengecek apakah jawaban klien sama dengan warna yang diterima dalam bahasa Indonesia
        if user_response.lower() == COLORS_ENGLISH_TO_INDONESIAN.get(received_color.lower(), ""):
            print("Jawaban benar! Nilai: 100")
        else:
            print("Jawaban salah. Nilai: 0")

if __name__ == "__main__":
    main()
