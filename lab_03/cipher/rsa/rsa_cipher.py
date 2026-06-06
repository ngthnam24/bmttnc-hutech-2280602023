import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend


class RSACipher:
    def __init__(self):
        self.keys_dir = os.path.join(os.path.dirname(__file__), "keys")
        os.makedirs(self.keys_dir, exist_ok=True)

    def generate_keys(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # Save private key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(os.path.join(self.keys_dir, "privateKey.pem"), "wb") as f:
            f.write(private_pem)

        # Save public key
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(os.path.join(self.keys_dir, "publicKey.pem"), "wb") as f:
            f.write(public_pem)

        return {"message": "Keys generated successfully!"}

    def encrypt(self, plain_text: str) -> str:
        with open(os.path.join(self.keys_dir, "publicKey.pem"), "rb") as f:
            public_key = serialization.load_pem_public_key(
                f.read(), backend=default_backend()
            )
        cipher_text = public_key.encrypt(
            plain_text.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return cipher_text.hex()

    def decrypt(self, cipher_text_hex: str) -> str:
        cipher_text = bytes.fromhex(cipher_text_hex)
        with open(os.path.join(self.keys_dir, "privateKey.pem"), "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(), password=None, backend=default_backend()
            )
        plain_text = private_key.decrypt(
            cipher_text,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plain_text.decode()

    def sign(self, message: str) -> str:
        with open(os.path.join(self.keys_dir, "privateKey.pem"), "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(), password=None, backend=default_backend()
            )
        signature = private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature.hex()

    def verify(self, message: str, signature_hex: str) -> bool:
        signature = bytes.fromhex(signature_hex)
        with open(os.path.join(self.keys_dir, "publicKey.pem"), "rb") as f:
            public_key = serialization.load_pem_public_key(
                f.read(), backend=default_backend()
            )
        try:
            public_key.verify(
                signature,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
