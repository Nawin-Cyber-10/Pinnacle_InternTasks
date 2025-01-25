```markdown
# 🛡️ Text Encryption Project 🛡️

Welcome to the **Text Encryption Project**! This project provides a simple graphical user interface (GUI) to encrypt text using various cryptographic algorithms such as AES, DES, and RSA. The project runs on Kali Linux and uses Python along with PyQt5 for the GUI.

## 📦 Features

- **AES Encryption**: Advanced Encryption Standard (AES) for strong data protection.
- **DES Encryption**: Data Encryption Standard (DES) for legacy systems.
- **RSA Encryption**: Asymmetric encryption for secure key exchange.
- **User-Friendly GUI**: Easy-to-use interface built with PyQt5.
- **Key Management**: Simple key input for symmetric algorithms and automatic key generation for RSA.

## 🚀 Installation

### Prerequisites

- **Kali Linux**: Ensure you have Kali Linux installed.
- **Python 3**: Make sure Python 3 is installed (`python3 --version`).
- **PyQt5**: For creating the GUI.
- **pycryptodome**: For cryptographic functions.

Install the required packages:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Nawin-Cyber-10/Pinnacle_InternTasks
cd < Name of Project >
```

## 💻 Usage

1. **Run the Application**:

   Open a terminal and navigate to the project directory, then run the following command:

   ```bash
   python3 main.py
   ```

2. **Select Algorithm**:

   Choose the encryption algorithm from the dropdown menu:
   - **AES**
   - **DES**
   - **RSA**

3. **Enter Plain Text**:

   Input the text you want to encrypt in the "Enter Plain Text" field.

4. **Enter Key**:

   For AES and DES, enter a key of appropriate length:
   - **AES**: 16 characters (will be automatically adjusted)
   - **DES**: 8 characters (will be automatically adjusted)

   For RSA, keys will be generated automatically.

5. **Encrypt**:

   Click the "Encrypt" button to perform the encryption. The result will be displayed in the "Result" section.

## 🔒 Security Considerations

- **Key Management**: Always store your keys securely and never hard-code them within the application.
- **Error Handling**: The application includes basic error handling, but further enhancements are recommended for production use.
- **Encryption Strength**: Use AES for stronger security compared to DES, which is considered outdated.

## 🛠️ Extending Functionality

You can extend this project by adding features like:

- **File Encryption**: Encrypt entire files instead of just text.
- **Additional Algorithms**: Implement more encryption algorithms.
- **Decryption**: Add functionality to decrypt encrypted text.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

Happy Encrypting! 🔐😊
```

### Updated `requirements.txt`

Ensure your `requirements.txt` file looks like this:

```txt
pycryptodome==3.14.1
PyQt5==5.15.6
```

### Project Structure

Your project structure should now look something like this:

```
text-encryption-project/
│
├── main.py
├── gui.py
├── crypto.py
├── requirements.txt
├── README.md
└── LICENSE
```
#### `LICENSE`
```
MIT License

Copyright (c) 2023 Nawin-Cyber-10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```