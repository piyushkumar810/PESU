'''
Read Item(code, qty, price); compute bill total and print items where qty*price > threshold.
'''

user_input=int(input("enter number of items: "))

items=[]

for i in range(user_input):
    code=input(f"enter code for items {i+1}: ")
    qty=int(input(f"enter quantity for the items{i+1}: "))
    price=float(input(f"enter price for items {i+1}: "))
    items.append({'code': code, 
         'qty': qty,
         'price':price
    })
    
threshold=float(input("enter threshold amount :"))

total_bill=0

print("\n items excedding threshold:")
for item in items:
    total=item['qty']*item['price']
    total_bill +=total
    if total>threshold:
        print(f"code: {item['code']}, qty: {item['qty']}, price: {item['price']}, total: {total}")
        
print(f"\n Total bill amount: {total_bill}")
        