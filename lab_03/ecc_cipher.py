import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ecc import Ui_MainWindow


class ECCCipherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.api_base = "http://127.0.0.1:5001/api/ecc"

        # Connect buttons
        self.ui.generateKeysBtn.clicked.connect(self.generate_keys)
        self.ui.signBtn.clicked.connect(self.sign)
        self.ui.verifyBtn.clicked.connect(self.verify)

    def _api_call(self, endpoint, data):
        try:
            response = requests.post(f"{self.api_base}/{endpoint}", json=data)
            return response.json()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Connection error: {str(e)}\nMake sure the ECC API server is running!")
            return None

    def generate_keys(self):
        result = self._api_call("generate_keys", {})
        if result:
            self.ui.keyStatus.setText(result.get("message", "Done!"))

    def sign(self):
        message = self.ui.signMessage.text()
        if not message:
            QMessageBox.warning(self, "Warning", "Please enter message!")
            return
        result = self._api_call("sign", {"message": message})
        if result:
            self.ui.signResult.setText(result["signature"])

    def verify(self):
        message = self.ui.verifyMessage.text()
        signature = self.ui.verifySignature.text()
        if not message or not signature:
            QMessageBox.warning(self, "Warning", "Please enter message and signature!")
            return
        result = self._api_call("verify", {"message": message, "signature": signature})
        if result:
            self.ui.verifyResult.setText("Valid ✓" if result["is_valid"] else "Invalid ✗")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ECCCipherApp()
    window.show()
    sys.exit(app.exec_())
