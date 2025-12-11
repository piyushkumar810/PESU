import inventory
import billing
import customer
import utility

# inventory operations
inventory.add_product(101,"shampoo", 120,50)
inventory.add_product(102,"soap", 40,100)

inventory.show_inventory()

# customer operations
customer.add_customer(1,"piyush","8102356837")

# billing
items=[(120,2), (40,3)]
bill_amount=billing.calculate_bill(items,discount=10)
print("final bill: ", bill_amount)

# utilities
utility.log("billing done on "+str(utility.current_data()))