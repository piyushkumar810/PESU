# billing: function for calculation bills and appling discount

def calculate_bill(items,discount=0):

    total=sum(price*qty for price,qty in items)
    final_total=total-(total*discount/100)

    return final_total