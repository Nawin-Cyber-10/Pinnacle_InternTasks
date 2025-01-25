from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox
import sys
from crypto import CryptoTools

class EncryptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.algorithm_selector = QComboBox()
        self.algorithm_selector.addItems(['AES', 'DES', 'RSA'])
        layout.addWidget(QLabel("Select Algorithm"))
        layout.addWidget(self.algorithm_selector)

        self.plain_text = QLineEdit()
        layout.addWidget(QLabel("Enter Plain Text"))
        layout.addWidget(self.plain_text)

        self.key_input = QLineEdit()
        layout.addWidget(QLabel("Enter Key"))
        layout.addWidget(self.key_input)

        self.encrypt_button = QPushButton('Encrypt')
        self.encrypt_button.clicked.connect(self.encrypt_text)
        layout.addWidget(self.encrypt_button)

        self.result_display = QTextEdit()
        layout.addWidget(QLabel("Result"))
        layout.addWidget(self.result_display)

        self.setLayout(layout)
        self.setWindowTitle('Text Encryption App')
        self.show()

    def encrypt_text(self):
        algorithm = self.algorithm_selector.currentText()
        plain_text = self.plain_text.text()
        key = self.key_input.text()

        if algorithm == 'AES':
            key = key.ljust(16)[:16].encode('utf-8')  # Ensure key length is 16 bytes
            iv, ct = CryptoTools.aes_encrypt(plain_text, key)
            result = f"IV: {iv}\nCipher Text: {ct}"
        elif algorithm == 'DES':
            key = key.ljust(8)[:8].encode('utf-8')  # Ensure key length is 8 bytes
            iv, ct = CryptoTools.des_encrypt(plain_text, key)
            result = f"IV: {iv}\nCipher Text: {ct}"
        elif algorithm == 'RSA':
            private_key, public_key = CryptoTools.rsa_generate_keys()
            ct = CryptoTools.rsa_encrypt(public_key, plain_text)
            result = f"Public Key: {public_key.decode('utf-8')}\nCipher Text: {ct}"

        self.result_display.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EncryptionApp()
    sys.exit(app.exec_())