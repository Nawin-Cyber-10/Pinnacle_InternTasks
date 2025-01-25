from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def generate_key():
    """Generate a random 32-byte key for AES-256 encryption."""
    return os.urandom(32)

def encrypt_image(input_path, output_path):
    """Encrypt an image file and save the encrypted file."""
    key = generate_key()
    iv = os.urandom(16)
    with open(input_path, "rb") as file:
        data = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(output_path, "wb") as enc_file:
        enc_file.write(iv + encrypted_data)

    # Save key to a separate file
    with open(output_path + ".key", "wb") as key_file:
        key_file.write(key)

    return key

def decrypt_image(input_path, key_path, output_path):
    """Decrypt an encrypted image file."""
    with open(input_path, "rb") as enc_file:
        data = enc_file.read()
    with open(key_path, "rb") as key_file:
        key = key_file.read()

    iv, encrypted_data = data[:16], data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    try:
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        with open(output_path, "wb") as dec_file:
            dec_file.write(decrypted_data)
        return True
    except Exception as e:
        print(f"Decryption failed: {e}")
        return False
