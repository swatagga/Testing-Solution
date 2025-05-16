from common.logging_helper import BaseLogger

from common.logging_helper import PostgresStorage

class AILogger(BaseLogger):
    """Logs AI model inference results and performance metrics."""

    def __init__(self):
        self.storage = PostgresStorage(self, "db_uri")
            
    def log(self, ai_data: dict):
        self.logger.info("AI inference logged", ai_data)
        self.storage.save_ai_log(self, ai_data)
   
