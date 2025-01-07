def add_product(name, description, quantity, price):
    query = """
    INSERT INTO products (name, description, quantity, price)
    VALUES (%s, %s, %s, %s);
    """
    execute_query(query, (name, description, quantity, price))

def get_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
