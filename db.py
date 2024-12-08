import psycopg2
from psycopg2.extras import DictCursor

def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname="MyProject",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise
