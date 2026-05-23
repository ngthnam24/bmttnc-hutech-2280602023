from flask import Flask, render_template, request

from cipher.caesar import CaesarCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()


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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
