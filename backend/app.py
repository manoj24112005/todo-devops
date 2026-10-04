from flask import Flask
import psycopg2
import redis

app = Flask(__name__)

# Redis connection
r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)


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


@app.route("/redis-test")
def redis_test():
    try:
        r.set("test", "Redis is working!")
        value = r.get("test")
        return value
    except Exception as e:
        return f"Redis Connection Failed: {e}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)