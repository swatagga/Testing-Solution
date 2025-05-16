from persistence.connection.db_connection import get_db_connection

def create_index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE INDEX idx_test_case_id ON Test_Cases(test_case_id);")
    conn.commit()
    conn.close()
