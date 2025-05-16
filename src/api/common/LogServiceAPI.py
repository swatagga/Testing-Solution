from urllib.request import Request
from common.logging import PostgresStorage
from common.logging.EmailNotifier import SMTPNotifier
from flask import Flask, jsonify, request

app = Flask(__name__)
storage = PostgresStorage("postgresql://user:pass@localhost:5432/logsdb")
notifier = SMTPNotifier("smtp.example.com", 465, "sender@example.com", "password", "alert@example.com")

class LogService:
    """API Endpoint for Fetching Logs"""
    
    @staticmethod
    def fetch_logs(log_type, limit=100):
        conn = psycopg2.connect("dbname=mydb user=myuser password=mypassword host=localhost")
        cursor = conn.cursor()
        
        query_map = {
            "error": "SELECT * FROM error_logs ORDER BY timestamp DESC LIMIT %s",
            "audit": "SELECT * FROM audit_logs ORDER BY timestamp DESC LIMIT %s",
            "ai": "SELECT * FROM ai_logs ORDER BY timestamp DESC LIMIT %s"
        }
        
        if log_type not in query_map:
            return {"error": "Invalid log type"}

        cursor.execute(query_map[log_type], (limit,))
        logs = cursor.fetchall()
        cursor.close()
        conn.close()

        return logs

@app.route("/logs/<log_type>", methods=["GET"])
def get_logs(log_type):
    """API Endpoint to Get Logs"""
    limit = request.args.get("limit", 100)
    logs = LogService.fetch_logs(log_type, limit)
    return jsonify(logs)

@app.route("/log/error")
async def log_error(request: Request):
    payload = request.json()
    try:
        storage.save_log("error", payload)
    except Exception as e:
        notifier.notify("Logging Error", str(e))
    return {"status": "logged"}

@app.route("/log/audit")
def log_audit(request: Request):
    payload = request.json()
    storage.save_log("audit", payload)
    return {"status": "logged"}

@app.route("/log/ai")
def log_ai(request: Request):
    payload = request.json()
    storage.save_log("ai", payload)
    return {"status": "logged"}

if __name__ == "__main__":
    app.run(port=5000)
