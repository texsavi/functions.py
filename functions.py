def calculate_discount(price,discount_percent):
    final_price = price * discount_percent/100
    if discount_percent > 20:
        return final_price
    else:
        return price
    
print(calculate_discount(50088,25))
