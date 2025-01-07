import psycopg2
from psycopg2 import sql

def create_connection():
    return psycopg2.connect(
        dbname="inventory",  # database name
        user="postgres",     # username
        password="mysecretpassword",  # password
        host="localhost",    # host (local)
        port="5432"          # default postgresql port
    )

def execute_query(query, params=None):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()