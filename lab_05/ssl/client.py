import socket
import ssl
import os

# Đường dẫn đến chứng chỉ
CERT_DIR = os.path.join(os.path.dirname(__file__), "certificates")
CERTFILE = os.path.join(CERT_DIR, "server-cert.crt")

HOST = "localhost"
PORT = 65432


def start_client():
    """Khởi động SSL Client"""
    # Tạo SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(CERTFILE)

    # Tạo socket và kết nối
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_socket = context.wrap_socket(client_socket, server_hostname=HOST)

    try:
        ssl_socket.connect((HOST, PORT))
        print(f"[*] Đã kết nối đến SSL Server {HOST}:{PORT}")

        while True:
            message = input("Nhập tin nhắn (hoặc 'quit' để thoát): ")
            if message.lower() == "quit":
                break

            # Gửi tin nhắn đến server
            ssl_socket.sendall(message.encode("utf-8"))

            # Nhận phản hồi từ server
            data = ssl_socket.recv(1024)
            print(f"[Server] {data.decode('utf-8')}")

    except Exception as e:
        print(f"[-] Lỗi: {e}")
    finally:
        ssl_socket.close()
        print("[*] Đã ngắt kết nối.")


if __name__ == "__main__":
    start_client()
