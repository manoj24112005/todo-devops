from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "Todo App Backend is Running!"

@app.route("/health")
def health():
    return "OK"

@app.route("/db-test")
def db_test():
    try:
        conn = psycopg2.connect(
            host="database",
            database="todo_db",
            user="todo_user",
            password="todo_password"
        )
        conn.close()
        return "Database Connected Successfully!"
    except Exception as e:
        return f"Database Connection Failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)