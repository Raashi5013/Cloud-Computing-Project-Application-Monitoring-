import psycopg2
import time

while True:
    try:
        print("Trying to connect to PostgreSQL...")
        conn = psycopg2.connect(
            host="postgres",
            database="logdb",
            user="admin",
            password="admin"
        )
        break
    except psycopg2.OperationalError:
        print(" Postgres not ready, retrying in 2 seconds...")
        time.sleep(2)

print("Connected to PostgreSQL!")

cur = conn.cursor()
with open("schema.sql", "r") as f:
    print(" Executing schema.sql...")
    cur.execute(f.read())
conn.commit()
cur.close()
conn.close()
print("DB Initialized successfully.")
