import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        dbname="ai_data",
        user="postgres",
        password="secure_password",
        host="localhost",
        port="5432"
    )
    return conn
