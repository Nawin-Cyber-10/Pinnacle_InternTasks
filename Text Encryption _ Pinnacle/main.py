import sys
from PyQt5.QtWidgets import QApplication
from gui import EncryptionApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EncryptionApp()
    sys.exit(app.exec_())