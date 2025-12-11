

customers={}

def add_customer(cid,name,phone):
    customers[cid]={"name":name, "phone":phone}
    print("customer added : ", name)

def get_customer(cid):
    return customers.get(cid, "customer not found")