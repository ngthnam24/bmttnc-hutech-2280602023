from flask import Flask, jsonify, request

from cipher.rsa.rsa_cipher import RSACipher
from cipher.ecc.ecc_cipher import ECCCipher

app = Flask(__name__)

rsa_cipher = RSACipher()
ecc_cipher = ECCCipher()

# ==================== RSA ====================

@app.route("/api/rsa/generate_keys", methods=["POST"])
def rsa_generate_keys():
    result = rsa_cipher.generate_keys()
    return jsonify({"message": result["message"] if isinstance(result, dict) else result})


@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    encrypted_text = rsa_cipher.encrypt(plain_text)
    return jsonify({"encrypted_text": encrypted_text})


@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    decrypted_text = rsa_cipher.decrypt(cipher_text)
    return jsonify({"decrypted_text": decrypted_text})


@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign():
    data = request.json
    message = data["message"]
    signature = rsa_cipher.sign(message)
    return jsonify({"signature": signature})


@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify():
    data = request.json
    message = data["message"]
    signature = data["signature"]
    is_valid = rsa_cipher.verify(message, signature)
    return jsonify({"is_valid": is_valid})


# ==================== ECC ====================

@app.route("/api/ecc/generate_keys", methods=["POST"])
def ecc_generate_keys():
    result = ecc_cipher.generate_keys()
    return jsonify({"message": result["message"] if isinstance(result, dict) else result})


@app.route("/api/ecc/sign", methods=["POST"])
def ecc_sign():
    data = request.json
    message = data["message"]
    signature = ecc_cipher.sign(message)
    return jsonify({"signature": signature})


@app.route("/api/ecc/verify", methods=["POST"])
def ecc_verify():
    data = request.json
    message = data["message"]
    signature = data["signature"]
    is_valid = ecc_cipher.verify(message, signature)
    return jsonify({"is_valid": is_valid})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
