# Password Analyzer

## Overview
The Password Analyzer is a Python-based tool with a graphical user interface (GUI) for analyzing password strength. It detects weaknesses in passwords, provides strength scores, and offers recommendations for improving security. Designed to run on Kali Linux, this tool is ideal for users looking to enhance their cybersecurity practices.

## Features
- **Password Strength Analysis**: Evaluates passwords based on length, character variety, and patterns.
- **Recommendations**: Offers actionable advice to improve password security.
- **Congratulatory Message**: Displays a pop-up with an emoji if the password is strong.
- **GUI Interface**: User-friendly interface built with PySide6.
- **Window Icon**: Includes a custom icon for the application window.

## Requirements
- Python 3.x
- Libraries:
  - PySide6
  - Passlib

## Installation
1. **Update the System**:
   ```bash
   sudo apt update
   ```

2. **Install Python and Pip**:
   ```bash
   sudo apt install python3 python3-pip
   ```

3. **Install Required Libraries**:
   ```bash
   pip3 install PySide6 passlib
   ```

4. **Download the Project**:
   Clone or download the project files to your local system.
   ```bash
   git clone https://github.com/Nawin-Cyber-10/Pinnacle_InternTasks
   cd < Project Name >
   ```

5. **Run the Application**:
   ```bash
   python3 password_analyzer.py
   ```

## Usage
1. Launch the application by running the script.
2. Enter a password in the input field.
3. Click the **Check Password** button.
4. View the strength analysis and recommendations.
   - If the password is strong, a congratulatory message with an emoji will appear.

## File Structure
```
password-analyzer/
|— password_analyzer.py     # Main application script
|— icon.png                # Custom icon for the application window
```

## Customization
### Changing the Icon
1. Replace the `icon.png` file in the project directory with your own icon file.
2. Ensure the file name remains `icon.png` or update the path in the script.

## Future Enhancements
- Integration with the "Have I Been Pwned" API to check for breached passwords.
- Secure password generation feature.
- Dark mode toggle for improved usability.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.
