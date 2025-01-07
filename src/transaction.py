def add_transaction(product_id, transaction_type, quantity):
    query = """
    INSERT INTO transactions (product_id, transaction_type, quantity, transaction_date)
    VALUES (%s, %s, %s, CURRENT_TIMESTAMP);
    """
    execute_query(query, (product_id, transaction_type, quantity))
