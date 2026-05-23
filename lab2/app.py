from flask import Flask, jsonify, request

try:
    from .cipher.caesar import CaesarCipher
    from .cipher.playfair import PlayfairCipher
    from .cipher.rail_fence import RailFenceCipher
    from .cipher.transposition import TranspositionCipher
    from .cipher.vigenere import VigenereCipher
except ImportError:
    from cipher.caesar import CaesarCipher
    from cipher.playfair import PlayfairCipher
    from cipher.rail_fence import RailFenceCipher
    from cipher.transposition import TranspositionCipher
    from cipher.vigenere import VigenereCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
rail_fence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()


def parse_json(required_fields: list[str]) -> dict:
    data = request.get_json(silent=True)
    if not data:
        raise ValueError("Request body must be valid JSON.")

    missing = [field for field in required_fields if field not in data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    return data


@app.errorhandler(ValueError)
def handle_value_error(error: ValueError):
    return jsonify({"error": str(error)}), 400


@app.get("/")
def index():
    return jsonify(
        {
            "message": "Lab 2 Flask API is running.",
            "endpoints": [
                "/api/caesar/encrypt",
                "/api/caesar/decrypt",
                "/api/vigenere/encrypt",
                "/api/vigenere/decrypt",
                "/api/railfence/encrypt",
                "/api/railfence/decrypt",
                "/api/playfair/encrypt",
                "/api/playfair/decrypt",
                "/api/transposition/encrypt",
                "/api/transposition/decrypt",
            ],
        }
    )


@app.post("/api/caesar/encrypt")
def caesar_encrypt():
    data = parse_json(["plain_text", "key"])
    encrypted_text = caesar_cipher.encrypt(data["plain_text"], int(data["key"]))
    return jsonify({"encrypted_text": encrypted_text})


@app.post("/api/caesar/decrypt")
def caesar_decrypt():
    data = parse_json(["cipher_text", "key"])
    decrypted_text = caesar_cipher.decrypt(data["cipher_text"], int(data["key"]))
    return jsonify({"decrypted_text": decrypted_text})


@app.post("/api/vigenere/encrypt")
def vigenere_encrypt():
    data = parse_json(["plain_text", "key"])
    encrypted_text = vigenere_cipher.encrypt(data["plain_text"], data["key"])
    return jsonify({"encrypted_text": encrypted_text})


@app.post("/api/vigenere/decrypt")
def vigenere_decrypt():
    data = parse_json(["cipher_text", "key"])
    decrypted_text = vigenere_cipher.decrypt(data["cipher_text"], data["key"])
    return jsonify({"decrypted_text": decrypted_text})


@app.post("/api/railfence/encrypt")
def rail_fence_encrypt():
    data = parse_json(["plain_text", "key"])
    encrypted_text = rail_fence_cipher.encrypt(data["plain_text"], int(data["key"]))
    return jsonify({"encrypted_text": encrypted_text})


@app.post("/api/railfence/decrypt")
def rail_fence_decrypt():
    data = parse_json(["cipher_text", "key"])
    decrypted_text = rail_fence_cipher.decrypt(data["cipher_text"], int(data["key"]))
    return jsonify({"decrypted_text": decrypted_text})


@app.post("/api/playfair/encrypt")
def playfair_encrypt():
    data = parse_json(["plain_text", "key"])
    encrypted_text = playfair_cipher.encrypt(data["plain_text"], data["key"])
    return jsonify({"encrypted_text": encrypted_text})


@app.post("/api/playfair/decrypt")
def playfair_decrypt():
    data = parse_json(["cipher_text", "key"])
    decrypted_text = playfair_cipher.decrypt(data["cipher_text"], data["key"])
    return jsonify({"decrypted_text": decrypted_text})


@app.post("/api/transposition/encrypt")
def transposition_encrypt():
    data = parse_json(["plain_text", "key"])
    encrypted_text = transposition_cipher.encrypt(data["plain_text"], int(data["key"]))
    return jsonify({"encrypted_text": encrypted_text})


@app.post("/api/transposition/decrypt")
def transposition_decrypt():
    data = parse_json(["cipher_text", "key"])
    decrypted_text = transposition_cipher.decrypt(data["cipher_text"], int(data["key"]))
    return jsonify({"decrypted_text": decrypted_text})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
