from cryptography.fernet import Fernet
import os

class FileStorage:
    def __init__(self, key_file='key.key', log_file='logs/keystrokes.log'):
        self.key_file = key_file
        self.log_file = log_file
        self.key = self.load_key()

    def load_key(self):
        # Generate a new key or load the existing key
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
        else:
            with open(self.key_file, 'rb') as key_file:
                key = key_file.read()
        return key

    def encrypt_log(self):
        with open(self.log_file, 'rb') as file:
            data = file.read()

        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data)

        with open(self.log_file, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_log(self):
        with open(self.log_file, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(self.key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(self.log_file, 'wb') as file:
            file.write(decrypted_data)
