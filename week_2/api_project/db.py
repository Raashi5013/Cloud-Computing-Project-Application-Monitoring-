import psycopg2
import os
import json

def get_connection():
    return psycopg2.connect(
        dbname="logdb",
        user="admin",
        password="admin",
        host="postgres",  # Docker hostname
        port="5432"
    )

def insert_log(table, data):
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                if table == "logs":
                    cur.execute("""
                        INSERT INTO logs (timestamp, log_type, method, endpoint, status, response_time_ms, message)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (
                        data["timestamp"], 
                        data.get("log_type", "unknown"),  # Default to 'unknown' if missing
                        data.get("method", "unknown"),  # Default to 'unknown' if missing
                        data.get("endpoint", "unknown"),  # Default to 'unknown' if missing
                        data.get("status", 0),  # Default to 0 if missing
                        data.get("response_time_ms", 0),  # Default to 0 if missing
                        data.get("message", "")  # Default to empty string if missing
                    ))
                elif table == "requests":
                    cur.execute("""
                        INSERT INTO requests (timestamp,log_type, method, endpoint, response_time_ms, query, data, message)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        data["timestamp"],
                        data.get("log_type", "unknown"),  # Default to 'unknown' if missing 
                        data.get("method", "unknown"),  # Default to 'unknown'
                        data.get("endpoint", "unknown"),  # Default to 'unknown'
                        data.get("response_time_ms", 0),  # Default to 0
                        data.get("query", ""),  # Default to empty string
                        json.dumps(data.get("data", {})),  # Default to empty dict if no data
                        data.get("message", "")  # Default to empty string
                    ))
                elif table == "errors":
                    cur.execute("""
                        INSERT INTO errors (timestamp,log_type, method, endpoint, error_type, response_time_ms, message)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (
                        data["timestamp"],
                        data.get("log_type", "unknown"),  # Default to 'unknown' if missing  
                        data.get("method", "unknown"),  # Default to 'unknown'
                        data.get("endpoint", "unknown"),  # Default to 'unknown'
                        data.get("error_type", "unknown"),  # Default to 'unknown'
                        data.get("response_time_ms", 0),  # Default to 0
                        data.get("message", "")  # Default to empty string
                    ))
                conn.commit()  # Commit the transaction after each insert
            except Exception as e:
                print(f"Error inserting log into table {table}: {e}")
                conn.rollback()  # Rollback if there's any error
