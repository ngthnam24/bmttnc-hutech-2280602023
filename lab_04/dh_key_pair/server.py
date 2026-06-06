import socket
import os
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


class DHServer:
    def __init__(self, host="127.0.0.1", port=6666):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(1)

        # Generate DH parameters and keys
        self.parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
        self.private_key = self.parameters.generate_private_key()
        self.public_key = self.private_key.public_key()

        # Save server public key
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open("server_public_key.pem", "wb") as f:
            f.write(public_pem)
        print("[DH SERVER] Public key saved to server_public_key.pem")

    def start(self):
        print(f"[DH SERVER] Listening on {self.host}:{self.port}")
        client_socket, address = self.server.accept()
        print(f"[DH SERVER] Client connected: {address}")

        # Send parameters and server public key
        param_bytes = self.parameters.parameter_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.ParameterFormat.PKCS3
        )
        client_socket.send(len(param_bytes).to_bytes(4, "big"))
        client_socket.send(param_bytes)

        server_public_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        client_socket.send(len(server_public_bytes).to_bytes(4, "big"))
        client_socket.send(server_public_bytes)

        # Receive client public key
        client_key_len = int.from_bytes(client_socket.recv(4), "big")
        client_public_bytes = client_socket.recv(client_key_len)
        client_public_key = serialization.load_pem_public_key(client_public_bytes, backend=default_backend())

        # Derive shared secret
        shared_key = self.private_key.exchange(client_public_key)
        print(f"[DH SERVER] Shared key established: {shared_key.hex()[:32]}...")

        # Receive encrypted message
        msg_len = int.from_bytes(client_socket.recv(4), "big")
        message = client_socket.recv(msg_len).decode()
        print(f"[DH SERVER] Received message: {message}")

        # Send response
        response = "Hello from DH Server! Shared secret established."
        client_socket.send(len(response).to_bytes(4, "big"))
        client_socket.send(response.encode())

        client_socket.close()
        self.server.close()


if __name__ == "__main__":
    server = DHServer()
    server.start()
