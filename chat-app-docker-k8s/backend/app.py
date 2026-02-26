from flask import Flask, request, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

# fetching details from Environment variables (Best Practice)
DB_HOST = os.getenv("DB_HOST", "postgres-service")
DB_NAME = os.getenv("DB_NAME", "chatdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "admin123")

def get_db_connection():
    """Postgres connect function with retry logic"""
    conn = None
    for i in range(5):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            break
        except Exception as e:
            print(f"Waiting for database... retry {i+1}")
            time.sleep(3)
    return conn

def init_db():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                username TEXT,
                message TEXT
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Database initialized successfully!")

@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    username = data["username"]
    message = data["message"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (username, message) VALUES (%s, %s)", (username, message))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"status": "Message saved in Postgres"})

@app.route("/messages", methods=["GET"])
def get_messages():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, message FROM messages")
    messages = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(messages)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
