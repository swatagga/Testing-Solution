from common.logging_helper import BaseLogger

from common.logging_helper import PostgresStorage

class AuditLogger(BaseLogger):
    """Logs user actions and compliance-related events."""

    def __init__(self):
        self.storage = PostgresStorage(self, "db_uri")
            
    def log(self, audit_data: dict):
        self.logger.info("Audit event recorded", audit_data)
        self.storage.save_error_log(self, audit_data)