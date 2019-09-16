stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'recomended': ['Samsung Galaxy S10', 'iPhone Xs']}, 
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000}, 
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5},
]
print(stock)

stock[2]['price'] += 8000
print(stock[2])

print(type(stock))
print(type(stock[0]))