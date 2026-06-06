import os
from ecdsa import SigningKey, NIST256p, VerifyingKey


class ECCCipher:
    def __init__(self):
        self.keys_dir = os.path.join(os.path.dirname(__file__), "keys")
        os.makedirs(self.keys_dir, exist_ok=True)

    def generate_keys(self):
        signing_key = SigningKey.generate(curve=NIST256p)
        verifying_key = signing_key.verifying_key

        # Save private key
        with open(os.path.join(self.keys_dir, "ecc_privateKey.pem"), "wb") as f:
            f.write(signing_key.to_pem())

        # Save public key
        with open(os.path.join(self.keys_dir, "ecc_publicKey.pem"), "wb") as f:
            f.write(verifying_key.to_pem())

        return {"message": "ECC Keys generated successfully!"}

    def sign(self, message: str) -> str:
        with open(os.path.join(self.keys_dir, "ecc_privateKey.pem"), "rb") as f:
            signing_key = SigningKey.from_pem(f.read())
        signature = signing_key.sign(message.encode())
        return signature.hex()

    def verify(self, message: str, signature_hex: str) -> bool:
        signature = bytes.fromhex(signature_hex)
        with open(os.path.join(self.keys_dir, "ecc_publicKey.pem"), "rb") as f:
            verifying_key = VerifyingKey.from_pem(f.read())
        try:
            verifying_key.verify(signature, message.encode())
            return True
        except Exception:
            return False
