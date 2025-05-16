import smtplib
from email.mime.text import MIMEText

class EmailNotifier():
    def __init__(self, smtp_server, port, username, password, to_email):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password
        self.to_email = to_email

    def notify(self, subject: str, message: str):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = self.to_email

        with smtplib.SMTP_SSL(self.smtp_server, self.port) as server:
            server.login(self.username, self.password)
            server.sendmail(self.username, [self.to_email], msg.as_string())