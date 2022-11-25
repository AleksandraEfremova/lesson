def format_price(price):
    price=int(price)
    price=str(int(price))
    return 'Цена ' + (price) + " руб."


print(format_price(56.24))