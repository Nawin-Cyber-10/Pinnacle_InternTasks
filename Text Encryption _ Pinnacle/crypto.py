from Crypto.Cipher import AES, DES, PKCS1_OAEP  # Import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

class CryptoTools:
    @staticmethod
    def aes_encrypt(plain_text, key):
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv, ct

    @staticmethod
    def aes_decrypt(iv, ct, key):
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')

    @staticmethod
    def des_encrypt(plain_text, key):
        cipher = DES.new(key, DES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), DES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv, ct

    @staticmethod
    def des_decrypt(iv, ct, key):
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = DES.new(key, DES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), DES.block_size)
        return pt.decode('utf-8')

    @staticmethod
    def rsa_generate_keys():
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key

    @staticmethod
    def rsa_encrypt(public_key, plain_text):
        rsa_key = RSA.import_key(public_key)
        cipher_rsa = PKCS1_OAEP.new(rsa_key)  # Use PKCS1_OAEP here
        ct = cipher_rsa.encrypt(plain_text.encode('utf-8'))
        return base64.b64encode(ct).decode('utf-8')

    @staticmethod
    def rsa_decrypt(private_key, ct):
        rsa_key = RSA.import_key(private_key)
        cipher_rsa = PKCS1_OAEP.new(rsa_key)  # Use PKCS1_OAEP here
        pt = cipher_rsa.decrypt(base64.b64decode(ct))
        return pt.decode('utf-8')