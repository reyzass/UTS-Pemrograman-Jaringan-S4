# UTS-Pemrograman-Jaringan-S4

NAMA  : REYZA SYAIFULLAH SULLY
-
NIM   : 1203220045
-
KELAS : IF 02-01
-

Berikut Cara Program Dijalankan :
-
Pertama buat 2 terminal terlebih dahulu seperti dibawah, yang kiri untuk Server & kanan untuk Client. Pada bagian server ketik **python server.py** & pada bagian Client ketik **python client.py**, lalu tekan **Enter**.

![image](https://github.com/reyzass/UTS-Pemrograman-Jaringan-S4/assets/162030249/1c69f4ee-a51d-45f7-a095-a3bc27486fe1)

Penjelasan How Code Works
-
Program ini adalah server sederhana yang menggunakan protokol UDP untuk berkomunikasi dengan beberapa klien. Berikut adalah langkah-langkah bagaimana program ini bekerja:

1. **Inisialisasi Server**: Program pertama kali membuat sebuah socket menggunakan `socket.socket()` dengan alamat IPv4 (`socket.AF_INET`) dan tipe socket datagram (`socket.SOCK_DGRAM`). Socket ini digunakan untuk menerima koneksi dari klien. Kemudian, server melakukan binding ke alamat dan port tertentu menggunakan `server_socket.bind()`.

2. **Loop Utama**: Server memasuki loop utama yang terus berjalan selama program berjalan. Pada tahap ini, server akan terus menunggu untuk menerima data dari klien.

3. **Menerima Permintaan Koneksi**: Ketika server menerima data dari klien, ia akan memeriksa data tersebut. Jika data yang diterima adalah string "connect", maka server akan membuat sebuah socket baru untuk klien tersebut menggunakan `socket.socket()` dengan alamat IPv4 (`socket.AF_INET`) dan tipe socket datagram (`socket.SOCK_DGRAM`). Socket baru ini akan digunakan untuk berkomunikasi dengan klien.

4. **Menjalankan Thread**: Server membuat thread baru menggunakan `threading.Thread()` untuk menangani klien yang terhubung. Thread ini akan menjalankan fungsi `client_handler` yang memiliki dua parameter, yaitu socket klien dan alamat klien. Fungsi `client_handler` akan menjalankan proses mengirim data ke klien.

5. **Mengirim Data ke Klien**: Di dalam fungsi `client_handler`, server akan terus mengirimkan data berupa warna yang dihasilkan secara acak ke klien. Data dikirim menggunakan `client_socket.sendto()`.

6. **Loop Klien**: Klien juga akan memasuki loop yang terus berjalan selama program berjalan. Pada setiap iterasi loop, klien akan menerima data dari server menggunakan `client_socket.recvfrom()`.

7. **Menerima Data dari Server**: Ketika klien menerima data dari server, ia akan mencetak pesan yang berisi warna yang diterima.

8. **Menunggu**: Setelah menerima data dari server, klien akan menunggu untuk menerima data berikutnya.

Dengan cara ini, server dapat melayani banyak klien secara bersamaan dan mengirimkan data ke setiap klien yang terhubung. Klien juga dapat menerima data dari server dan merespons jika diperlukan.

TEST CASE 1 SERVER 10 CLIENTS
-
![hasil uts](https://github.com/reyzass/UTS-Pemrograman-Jaringan-S4/assets/162030249/fb860177-9256-4714-be54-2c232d87b031)
