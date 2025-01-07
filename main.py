def main():
    add_product("Laptop", "A high-performance laptop", 10, 1500) # an example

    add_transaction(1, "purchase", 5)

    products = get_products()
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[3]}, Price: {product[4]}")

if __name__ == "__main__":
    main()
