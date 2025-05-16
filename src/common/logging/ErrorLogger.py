from common.logging_helper import BaseLogger

from common.logging_helper import PostgresStorage

class ErrorLogger(BaseLogger):
    """Logs system errors and exceptions."""
    def __init__(self):
        self.storage = PostgresStorage(self, "db_uri")

    def log(self, error_data: dict, logType):
        self.logger.error("Exception occurred", error_data)
        self.storage.save_error_log(self, error_data)
        if error_data.get("level") == "CRITICAL":
            self.send_email_alert("Critical Exception Alert", str(error_data))

    