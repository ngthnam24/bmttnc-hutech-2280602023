import socket
import threading
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class Server:
    def __init__(self, host="127.0.0.1", port=5555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        # Generate RSA keys
        self.private_key = rsa.generate_private_key(65537, 2048, default_backend())
        self.public_key = self.private_key.public_key()
        print(f"[SERVER] Listening on {self.host}:{self.port}")

    def handle_client(self, client_socket, address):
        print(f"[SERVER] New connection from {address}")

        # Send public key to client
        public_pem = self.public_key.public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo
        )
        client_socket.send(public_pem)

        # Receive encrypted AES key from client
        encrypted_aes_key_len = int.from_bytes(client_socket.recv(4), "big")
        encrypted_aes_key = client_socket.recv(encrypted_aes_key_len)

        # Decrypt AES key with RSA private key
        aes_key = self.private_key.decrypt(
            encrypted_aes_key,
            padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )

        while True:
            try:
                # Receive IV
                iv = client_socket.recv(16)
                if not iv:
                    break

                # Receive encrypted message length
                msg_len = int.from_bytes(client_socket.recv(4), "big")
                encrypted_msg = client_socket.recv(msg_len)
                if not encrypted_msg:
                    break

                # Decrypt with AES
                cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
                decryptor = cipher.decryptor()
                decrypted = decryptor.update(encrypted_msg) + decryptor.finalize()
                # Remove PKCS7 padding
                pad_len = decrypted[-1]
                plain_text = decrypted[:-pad_len].decode()
                print(f"[CLIENT {address}] {plain_text}")

                # Send response
                response = f"Server received: {plain_text}"
                resp_iv = os.urandom(16)
                cipher = Cipher(algorithms.AES(aes_key), modes.CBC(resp_iv), backend=default_backend())
                encryptor = cipher.encryptor()
                # Add PKCS7 padding
                resp_bytes = response.encode()
                pad_len = 16 - (len(resp_bytes) % 16)
                resp_bytes += bytes([pad_len] * pad_len)
                encrypted_resp = encryptor.update(resp_bytes) + encryptor.finalize()
                client_socket.send(resp_iv)
                client_socket.send(len(encrypted_resp).to_bytes(4, "big"))
                client_socket.send(encrypted_resp)

            except Exception as e:
                print(f"[SERVER] Error: {e}")
                break

        client_socket.close()
        print(f"[SERVER] Connection closed: {address}")

    def start(self):
        while True:
            client_socket, address = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
            thread.daemon = True
            thread.start()


if __name__ == "__main__":
    server = Server()
    server.start()
