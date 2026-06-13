import socket
import ssl
import threading
import os

# Đường dẫn đến chứng chỉ và khóa
CERT_DIR = os.path.join(os.path.dirname(__file__), "certificates")
CERTFILE = os.path.join(CERT_DIR, "server-cert.crt")
KEYFILE = os.path.join(CERT_DIR, "server-key.key")

HOST = "localhost"
PORT = 65432


def handle_client(conn, addr):
    """Xử lý kết nối từ client"""
    print(f"[+] Kết nối từ {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode("utf-8")
            print(f"[Client {addr}] {message}")

            # Phản hồi lại client
            response = f"Server đã nhận: {message}"
            conn.sendall(response.encode("utf-8"))
    except Exception as e:
        print(f"[-] Lỗi: {e}")
    finally:
        conn.close()
        print(f"[-] Đã ngắt kết nối từ {addr}")


def start_server():
    """Khởi động SSL Server"""
    # Tạo SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

    # Tạo socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    # Bọc socket bằng SSL
    ssl_socket = context.wrap_socket(server_socket, server_side=True)

    print(f"[*] SSL Server đang chạy tại {HOST}:{PORT}")

    try:
        while True:
            conn, addr = ssl_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
    except KeyboardInterrupt:
        print("\n[*] Server đã dừng.")
    finally:
        ssl_socket.close()


if __name__ == "__main__":
    start_server()
