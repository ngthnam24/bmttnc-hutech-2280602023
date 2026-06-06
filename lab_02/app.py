from flask import Flask, render_template, request

from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    encrypted_text = ""
    decrypted_text = ""
    plain_text = ""
    cipher_text = ""
    key = ""

    if request.method == "POST":
        action = request.form.get("action")
        key = request.form.get("key", "")
        if action == "encrypt":
            plain_text = request.form.get("plain_text", "")
            encrypted_text = caesar_cipher.encrypt_text(plain_text, int(key))
        elif action == "decrypt":
            cipher_text = request.form.get("cipher_text", "")
            decrypted_text = caesar_cipher.decrypt_text(cipher_text, int(key))

    return render_template(
        "caesar.html",
        encrypted_text=encrypted_text,
        decrypted_text=decrypted_text,
        plain_text=plain_text,
        cipher_text=cipher_text,
        key=key,
    )


@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    encrypted_text = ""
    decrypted_text = ""
    plain_text = ""
    cipher_text = ""
    key = ""

    if request.method == "POST":
        action = request.form.get("action")
        key = request.form.get("key", "")
        if action == "encrypt":
            plain_text = request.form.get("plain_text", "")
            encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        elif action == "decrypt":
            cipher_text = request.form.get("cipher_text", "")
            decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)

    return render_template(
        "vigenere.html",
        encrypted_text=encrypted_text,
        decrypted_text=decrypted_text,
        plain_text=plain_text,
        cipher_text=cipher_text,
        key=key,
    )


@app.route("/railfence", methods=["GET", "POST"])
def railfence():
    encrypted_text = ""
    decrypted_text = ""
    plain_text = ""
    cipher_text = ""
    key = ""

    if request.method == "POST":
        action = request.form.get("action")
        key = request.form.get("key", "")
        if action == "encrypt":
            plain_text = request.form.get("plain_text", "")
            encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, int(key))
        elif action == "decrypt":
            cipher_text = request.form.get("cipher_text", "")
            decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, int(key))

    return render_template(
        "railfence.html",
        encrypted_text=encrypted_text,
        decrypted_text=decrypted_text,
        plain_text=plain_text,
        cipher_text=cipher_text,
        key=key,
    )


@app.route("/playfair", methods=["GET", "POST"])
def playfair():
    encrypted_text = ""
    decrypted_text = ""
    plain_text = ""
    cipher_text = ""
    key = ""
    matrix = ""

    if request.method == "POST":
        action = request.form.get("action")
        key = request.form.get("key", "")
        if key:
            playfair_matrix = playfair_cipher.create_playfair_matrix(key)
            matrix = str(playfair_matrix)
            if action == "encrypt":
                plain_text = request.form.get("plain_text", "")
                encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
            elif action == "decrypt":
                cipher_text = request.form.get("cipher_text", "")
                decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)

    return render_template(
        "playfair.html",
        encrypted_text=encrypted_text,
        decrypted_text=decrypted_text,
        plain_text=plain_text,
        cipher_text=cipher_text,
        key=key,
        matrix=matrix,
    )


@app.route("/transposition", methods=["GET", "POST"])
def transposition():
    encrypted_text = ""
    decrypted_text = ""
    plain_text = ""
    cipher_text = ""
    key = ""

    if request.method == "POST":
        action = request.form.get("action")
        key = request.form.get("key", "")
        if action == "encrypt":
            plain_text = request.form.get("plain_text", "")
            encrypted_text = transposition_cipher.encrypt(plain_text, int(key))
        elif action == "decrypt":
            cipher_text = request.form.get("cipher_text", "")
            decrypted_text = transposition_cipher.decrypt(cipher_text, int(key))

    return render_template(
        "transposition.html",
        encrypted_text=encrypted_text,
        decrypted_text=decrypted_text,
        plain_text=plain_text,
        cipher_text=cipher_text,
        key=key,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
