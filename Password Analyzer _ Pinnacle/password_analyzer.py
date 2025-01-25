from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QLabel, QLineEdit, QPushButton, QMessageBox
)
from PySide6.QtGui import QIcon
import re
from passlib.utils import generate_password
import os

class PasswordAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Analyzer")
        self.setGeometry(100, 100, 400, 300)

        # Set window icon (use any .ico or .png file)
        icon_path = "icon.png"  # Replace with the path to your icon file
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file '{icon_path}' not found. Proceeding without icon.")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Input field
        self.password_label = QLabel("Enter Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Check button
        self.check_button = QPushButton("Check Password")
        self.check_button.clicked.connect(self.analyze_password)
        layout.addWidget(self.check_button)

        # Result labels
        self.strength_label = QLabel("")
        self.recommendation_label = QLabel("")
        layout.addWidget(self.strength_label)
        layout.addWidget(self.recommendation_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def analyze_password(self):
        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "Error", "Password cannot be empty!")
            return

        # Analyze password
        strength, recommendations = self.check_strength(password)

        # Update GUI
        self.strength_label.setText(f"Strength: {strength}")
        self.recommendation_label.setText(f"Recommendations: {recommendations}")

        # Congratulate if strong
        if strength == "Strong":
            QMessageBox.information(
                self, 
                "Congratulations 🎉", 
                "Your password is strong! 🛡️\nGreat job ensuring your security!"
            )

    def check_strength(self, password):
        score = 0
        recommendations = []

        # Length check
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            recommendations.append("Increase password length to at least 12 characters.")

        # Character variety
        if re.search(r"[A-Z]", password):  # Uppercase
            score += 1
        else:
            recommendations.append("Add uppercase letters.")
        if re.search(r"[a-z]", password):  # Lowercase
            score += 1
        else:
            recommendations.append("Add lowercase letters.")
        if re.search(r"\d", password):  # Numbers
            score += 1
        else:
            recommendations.append("Add numbers.")
        if re.search(r"[@$!%*?&#]", password):  # Special characters
            score += 1
        else:
            recommendations.append("Add special characters (e.g., @, $, !).")

        # Common patterns
        if re.search(r"(.)\1\1", password):  # Repeated characters
            recommendations.append("Avoid repeated characters.")
        if password.lower() in generate_password(1000):  # Simulated breach database
            recommendations.append("Avoid common or breached passwords.")

        # Score to strength
        if score >= 5:
            strength = "Strong"
        elif score >= 3:
            strength = "Moderate"
        else:
            strength = "Weak"

        return strength, " | ".join(recommendations)


if __name__ == "__main__":
    app = QApplication([])
    window = PasswordAnalyzer()
    window.show()
    app.exec()
