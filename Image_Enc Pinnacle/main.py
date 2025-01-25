from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QProgressBar
)
from PySide6.QtGui import QIcon
from encryption import encrypt_image, decrypt_image
import os

class ImageEncryptionTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Encryption Tool")
        self.setGeometry(200, 200, 600, 400)
        self.setWindowIcon(QIcon("assets/lock_icon.png"))  # Add a custom icon

        # Layout
        layout = QVBoxLayout()

        # Title Label
        self.title_label = QLabel("<h1>🔒 Image Encryption Tool</h1>")
        self.title_label.setStyleSheet("text-align: center; color: #333;")
        layout.addWidget(self.title_label)

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)

        # Buttons Layout
        button_layout = QHBoxLayout()

        # Encrypt Button
        self.encrypt_button = QPushButton("Encrypt Image")
        self.encrypt_button.setStyleSheet("padding: 10px; background-color: #4CAF50; color: white;")
        self.encrypt_button.clicked.connect(self.encrypt_image)
        button_layout.addWidget(self.encrypt_button)

        # Decrypt Button
        self.decrypt_button = QPushButton("Decrypt Image")
        self.decrypt_button.setStyleSheet("padding: 10px; background-color: #2196F3; color: white;")
        self.decrypt_button.clicked.connect(self.decrypt_image)
        button_layout.addWidget(self.decrypt_button)

        layout.addLayout(button_layout)

        # Status Label
        self.status_label = QLabel("Welcome! Secure your images with encryption.")
        self.status_label.setStyleSheet("color: #555; padding-top: 10px;")
        layout.addWidget(self.status_label)

        # Set Layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def encrypt_image(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Select Image to Encrypt", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if filepath:
            output_path = os.path.join("output", os.path.basename(filepath) + ".enc")
            self.progress_bar.setVisible(True)
            self.progress_bar.setValue(50)  # Simulate progress
            
            key = encrypt_image(filepath, output_path)
            self.progress_bar.setValue(100)

            self.status_label.setText(f"✅ Image encrypted successfully!\nKey: {key.hex()}\nSaved to: {output_path}")
            self.progress_bar.setVisible(False)

    def decrypt_image(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Select Encrypted File", "", "Encrypted Files (*.enc)")
        if filepath:
            key_path, _ = QFileDialog.getOpenFileName(self, "Select Key File", "", "Key Files (*.key)")
            if key_path:
                output_path = os.path.join("output", os.path.basename(filepath).replace(".enc", "_decrypted.png"))
                self.progress_bar.setVisible(True)
                self.progress_bar.setValue(50)  # Simulate progress
                
                success = decrypt_image(filepath, key_path, output_path)
                self.progress_bar.setValue(100)

                if success:
                    self.status_label.setText(f"✅ Image decrypted successfully!\nSaved to: {output_path}")
                else:
                    self.status_label.setText("❌ Decryption failed. Please check the key and file.")
                self.progress_bar.setVisible(False)

if __name__ == "__main__":
    app = QApplication([])
    window = ImageEncryptionTool()
    window.show()
    app.exec()
