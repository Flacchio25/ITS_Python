def total_price(**kwargs):
    total:float = 0
    for product, price in kwargs.items():
        print(f"{product}: {price}€")
        total += price
    return round(total, 2)
print(total_price(coffee=2.99, cake=4.55, juice=2.99))