Certainly! Below is the updated version of the project that includes a 32-byte key generation option. The code and README have been revised to reflect these changes.

### Prerequisites

1. **Kali Linux Installation**: Ensure you have Kali Linux installed.
2. **Python3**: Make sure Python 3 is installed.
3. **Install Required Libraries**:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install pillow cryptography
   sudo apt-get install python3-tk
   ```

### Project Structure

```
image_encryption/
│
├── main.py
└── README.md
```

### Step-by-Step Guide

#### 1. Create `main.py`

This script will handle both encryption and decryption functionalities, provide a GUI using `tkinter`, and include a 32-byte key generation option.

```python
import os
import base64
from tkinter import Tk, Label, Button, filedialog, messagebox, Entry, StringVar, Toplevel
from PIL import Image
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_data = img.tobytes()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(img_data) + padder.finalize()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    with open(output_path, 'wb') as f:
        f.write(iv + encrypted_data)

def decrypt_image(input_path, output_path, key, width, height):
    with open(input_path, 'rb') as f:
        data = f.read()
    iv = data[:16]
    encrypted_data = data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    img_data = unpadder.update(padded_data) + unpadder.finalize()
    img = Image.frombytes('RGBA', (width, height), img_data)
    img.save(output_path)

def select_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        file_var.set(filepath)

def generate_new_key():
    password = key_var.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password for key generation.")
        return
    salt = os.urandom(16)
    key = generate_key(password, salt)
    new_window = Toplevel(root)
    new_window.title("Generated Key")
    Label(new_window, text="Generated Key:", font=("Arial", 12)).pack(pady=10)
    Label(new_window, text=key.decode(), font=("Courier", 10)).pack(pady=10)
    Label(new_window, text="Note: Save this key securely.", font=("Arial", 10)).pack(pady=10)

def encrypt():
    input_path = file_var.get()
    if not input_path:
        messagebox.showerror("Error", "Please select an image to encrypt.")
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".bin")
    if not output_path:
        return
    key = key_var.get().encode('utf-8')
    if len(key) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long for key derivation.")
        return
    try:
        salt = os.urandom(16)
        key = generate_key(key_var.get(), salt)
        encrypt_image(input_path, output_path, key)
        messagebox.showinfo("Success", "Image encrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt():
    input_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.bin")])
    if not input_path:
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".png")
    if not output_path:
        return
    key = key_var.get().encode('utf-8')
    if len(key) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long for key derivation.")
        return
    width = int(width_var.get())
    height = int(height_var.get())
    try:
        salt = os.urandom(16)
        key = generate_key(key_var.get(), salt)
        decrypt_image(input_path, output_path, key, width, height)
        messagebox.showinfo("Success", "Image decrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = Tk()
root.title("Image Encryption Tool")

Label(root, text="Select Image:").grid(row=0, column=0, padx=10, pady=5)
file_var = StringVar()
Entry(root, textvariable=file_var, width=50).grid(row=0, column=1, padx=10, pady=5)
Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=5)

Label(root, text="Encryption Password (min 8 chars):").grid(row=1, column=0, padx=10, pady=5)
key_var = StringVar()
Entry(root, textvariable=key_var, width=50).grid(row=1, column=1, padx=10, pady=5)
Button(root, text="Generate Key", command=generate_new_key).grid(row=1, column=2, padx=10, pady=5)

Label(root, text="Width:").grid(row=2, column=0, padx=10, pady=5)
width_var = StringVar(value="1920")
Entry(root, textvariable=width_var, width=50).grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Height:").grid(row=3, column=0, padx=10, pady=5)
height_var = StringVar(value="1080")
Entry(root, textvariable=height_var, width=50).grid(row=3, column=1, padx=10, pady=5)

Button(root, text="Encrypt", command=encrypt).grid(row=4, column=0, columnspan=3, pady=10)
Button(root, text="Decrypt", command=decrypt).grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
```

#### 2. Create `README.md`

Document your project so others can understand how to use it.

```markdown
# 🛡️ Image Encryption Tool with GUI and Key Generation

## Overview 📸🔒

This tool provides basic image encryption and decryption functionality using AES encryption. It includes a graphical user interface (GUI) for ease of use and a 32-byte key generation option. Designed to run on Kali Linux, it helps secure visual data from unauthorized access and tampering.

---

## Requirements 💻

Before you start, ensure you have the following installed:

- **Python 3** 🐍: The scripting language used.
- **Pillow** 🎨: For image manipulation (`pip3 install pillow`).
- **Cryptography** 🔐: For encryption functions (`pip3 install cryptography`).
- **Tkinter** 🖼️: For the GUI (`sudo apt-get install python3-tk`).

---

## Installation ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/Nawin-Cyber-10/Pinnacle_InternTasks
   cd < Project Name >
   ```

2. Install the required libraries:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install pillow cryptography
   sudo apt-get install python3-tk
   ```

---

## Usage 🚀

### Encrypting an Image 🔒

1. Open the application by running:
   ```bash
   python3 main.py
   ```

2. Click on "Browse" to select the image you want to encrypt.

3. Enter a password for key generation (minimum 8 characters).

4. Click "Generate Key" to see the generated 32-byte key.

5. Click "Encrypt" to save the encrypted image.

### Decrypting an Image 🔓

1. Open the application by running:
   ```bash
   python3 main.py
   ```

2. Click on "Browse" to select the encrypted image file.

3. Enter the same password used during encryption.

4. Enter the original image dimensions (width and height).

5. Click "Decrypt" to save the decrypted image.

---

## Important Considerations 🛑

1. **Key Management**: In this example, the key is derived from a password. Ensure you store the generated key securely.
2. **Error Handling**: Basic error handling is included. Consider adding more robust checks for production use.
3. **Performance**: For large images, consider optimizing the code for performance.

---

## Contributing 🤝

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy Coding! 🎉
```

This enhanced version of the project now includes a 32-byte key generation option, making it easier for users to manage their encryption keys while providing a clear and user-friendly interface to encrypt and decrypt images securely on Kali Linux.