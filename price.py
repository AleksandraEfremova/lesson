def discounted(price, discount):
    price = abs(price)
    discount = abs(discount)
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount
price_disconted = discounted(100,50)
product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
product['price_discounted'] = discounted(product['price'], product['discount'])
print(product)