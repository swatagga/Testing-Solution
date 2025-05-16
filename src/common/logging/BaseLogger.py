from abc import ABC, abstractmethod
from common.logging_helper import EmailNotifier
import structlog
import smtplib
from email.mime.text import MIMEText

class BaseLogger(ABC):
    """Abstract class for structured logging."""

    def __init__(self):
        self.logger = structlog.get_logger()

    @abstractmethod
    def log(self, data: dict):
        pass

    @staticmethod
    def send_email_alert(subject, message):
        smtp_server = "smtp.example.com"        
        notifier = EmailNotifier(smtp_server, "port", "username", "password", "to_email")
        notifier.notify(subject, message)
        
