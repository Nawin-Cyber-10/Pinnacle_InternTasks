# Keylogger Software

This project implements a Python-based keylogger that captures keystrokes, encrypts logs, and sends them via email. It also includes features to detect other keyloggers and monitor network activity for suspicious connections.

## Features:
- Capture keystrokes and log them.
- Encrypt the logs for security.
- Send logs via email at regular intervals.
- Detect suspicious processes and network activity.
- Check file integrity and monitor for keylogger tampering.

## Requirements:
- Python 3.x
- Libraries: `pynput`, `psutil`, `cryptography`, `schedule`, `smtplib`

## Setup:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
