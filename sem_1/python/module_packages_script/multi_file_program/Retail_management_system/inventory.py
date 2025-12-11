# inventory management: function for adding and removing product

# inventory.py/product.py file

products = {}  # dictionary to store product_name: quantity


def add_product(pid,name,price, qty):
    products[pid]={"name": name,"price":price, "qty":qty}
    print(f"product {name} added successfully")


def remove_product(pid):
    if pid in products:
        del products[pid]
        print("product removed successfully")
    else:
        print("product not found")


def show_inventory():
    print("\n--- Current Inventory ---")
    print("current inventory :", products)