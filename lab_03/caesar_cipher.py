import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from caesar import Ui_MainWindow


class CaesarCipherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.api_base = "http://127.0.0.1:5000/api/caesar"

        # Connect buttons
        self.ui.encryptBtn.clicked.connect(self.encrypt)
        self.ui.decryptBtn.clicked.connect(self.decrypt)

    def encrypt(self):
        plain_text = self.ui.encryptPlainText.text()
        key = self.ui.encryptKey.text()
        if not plain_text or not key:
            QMessageBox.warning(self, "Warning", "Please enter plain text and key!")
            return
        try:
            response = requests.post(f"{self.api_base}/encrypt",
                                     json={"plain_text": plain_text, "key": int(key)})
            if response.status_code == 200:
                self.ui.encryptResult.setText(response.json()["encrypted_message"])
            else:
                QMessageBox.critical(self, "Error", "API request failed!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Connection error: {str(e)}")

    def decrypt(self):
        cipher_text = self.ui.decryptCipherText.text()
        key = self.ui.decryptKey.text()
        if not cipher_text or not key:
            QMessageBox.warning(self, "Warning", "Please enter cipher text and key!")
            return
        try:
            response = requests.post(f"{self.api_base}/decrypt",
                                     json={"cipher_text": cipher_text, "key": int(key)})
            if response.status_code == 200:
                self.ui.decryptResult.setText(response.json()["decrypted_message"])
            else:
                QMessageBox.critical(self, "Error", "API request failed!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Connection error: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaesarCipherApp()
    window.show()
    sys.exit(app.exec_())
