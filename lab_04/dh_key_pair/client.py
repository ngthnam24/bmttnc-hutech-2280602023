import socket
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


class DHClient:
    def __init__(self, host="127.0.0.1", port=6666):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        print(f"[DH CLIENT] Connected to {self.host}:{self.port}")

        # Receive DH parameters
        param_len = int.from_bytes(self.socket.recv(4), "big")
        param_bytes = self.socket.recv(param_len)
        parameters = serialization.load_pem_parameters(param_bytes, backend=default_backend())

        # Receive server public key
        server_key_len = int.from_bytes(self.socket.recv(4), "big")
        server_public_bytes = self.socket.recv(server_key_len)
        server_public_key = serialization.load_pem_public_key(server_public_bytes, backend=default_backend())

        # Generate client key pair
        client_private_key = parameters.generate_private_key()
        client_public_key = client_private_key.public_key()

        # Send client public key
        client_public_bytes = client_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        self.socket.send(len(client_public_bytes).to_bytes(4, "big"))
        self.socket.send(client_public_bytes)

        # Derive shared secret
        shared_key = client_private_key.exchange(server_public_key)
        print(f"[DH CLIENT] Shared key established: {shared_key.hex()[:32]}...")

        # Send message
        message = "Hello from DH Client! Secure channel established via Diffie-Hellman."
        self.socket.send(len(message).to_bytes(4, "big"))
        self.socket.send(message.encode())

        # Receive response
        resp_len = int.from_bytes(self.socket.recv(4), "big")
        response = self.socket.recv(resp_len).decode()
        print(f"[DH SERVER] {response}")

        self.socket.close()


if __name__ == "__main__":
    client = DHClient()
    client.connect()
