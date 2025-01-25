# Image Encryption Tool

Secure your image files with encryption to protect visual data from unauthorized access and tampering. This tool allows you to easily encrypt and decrypt image files with a user-friendly GUI.

---

## Features

- **AES-256 Encryption**: Ensures high-level security for your image files.
- **User-Friendly GUI**: Simple interface for encryption and decryption.
- **Progress Indicator**: Visual feedback during encryption and decryption processes.
- **Custom Icons**: Modern design with a polished look.
- **Output Directory**: Automatically saves encrypted and decrypted files.

---

## Project Structure

```
image_encryption_tool/
├── main.py             # Main application (GUI and event handling)
├── encryption.py       # Encryption and decryption logic
├── utils.py            # Helper functions (e.g., key management)
├── assets/             # GUI resources like icons (optional)
│   └── lock_icon.png   # Lock icon for the app
└── output/             # Stores encrypted and decrypted files
```

---

## Prerequisites

- Python 3.8 or higher
- Kali Linux or any Linux distribution with Python support

### Install Required Libraries
Run the following command to install the required dependencies:
```bash
pip install PySide6 cryptography
```

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Nawin-Cyber-10/Pinnacle_InternTasks
   cd < Project Name >
   ```

2. Run the tool:
   ```bash
   python3 main.py
   ```

3. Use the GUI to:
   - Encrypt an image file: Select an image, and the tool will encrypt it and save it with a `.enc` extension.
   - Decrypt an image file: Select the encrypted file and its corresponding key to decrypt it.

---

## Screenshots

### Main Interface:
![Main Interface](assets/sample_ui.png)

### Encryption Progress:
![Encryption Progress](assets/encryption_progress.png)

---

## How It Works

1. **Encryption**:
   - Uses AES-256 with a randomly generated key and initialization vector (IV).
   - Saves the encrypted file and key in the `output/` directory.

2. **Decryption**:
   - Takes the encrypted file and key as input to restore the original image.
   - Saves the decrypted image in the `output/` directory.

---

## Output Directory
All encrypted and decrypted files are stored in the `output/` directory. Ensure this directory exists or let the tool create it automatically.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributions

Contributions are welcome! Feel free to fork this repository and submit pull requests.

---

## Contact

For any inquiries or issues, reach out to me at [heyitsmenawin010@gmail.com].

