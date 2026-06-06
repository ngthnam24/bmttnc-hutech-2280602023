import socket
import os
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class Client:
    def __init__(self, host="127.0.0.1", port=5555):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        print(f"[CLIENT] Connected to {self.host}:{self.port}")

        # Receive server public key
        public_pem = self.socket.recv(1024)
        server_public_key = serialization.load_pem_public_key(public_pem, backend=default_backend())

        # Generate AES key (256-bit)
        aes_key = os.urandom(32)

        # Encrypt AES key with server's RSA public key
        encrypted_aes_key = server_public_key.encrypt(
            aes_key,
            padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        self.socket.send(len(encrypted_aes_key).to_bytes(4, "big"))
        self.socket.send(encrypted_aes_key)

        print("[CLIENT] Secure channel established. Type messages (type 'quit' to exit):")

        while True:
            message = input("> ")
            if message.lower() == "quit":
                break

            # Encrypt with AES
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            msg_bytes = message.encode()
            # Add PKCS7 padding
            pad_len = 16 - (len(msg_bytes) % 16)
            msg_bytes += bytes([pad_len] * pad_len)
            encrypted_msg = encryptor.update(msg_bytes) + encryptor.finalize()

            self.socket.send(iv)
            self.socket.send(len(encrypted_msg).to_bytes(4, "big"))
            self.socket.send(encrypted_msg)

            # Receive response
            resp_iv = self.socket.recv(16)
            resp_len = int.from_bytes(self.socket.recv(4), "big")
            encrypted_resp = self.socket.recv(resp_len)

            cipher = Cipher(algorithms.AES(aes_key), modes.CBC(resp_iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted = decryptor.update(encrypted_resp) + decryptor.finalize()
            pad_len = decrypted[-1]
            response = decrypted[:-pad_len].decode()
            print(f"[SERVER] {response}")

        self.socket.close()


if __name__ == "__main__":
    client = Client()
    client.connect()
