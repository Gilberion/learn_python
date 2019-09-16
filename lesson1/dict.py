product = {'name': 'iPhone Xs', 'stock':5, 'price': '65000'}
print(product)
print(len(product))
product['stock'] = 10
print(product)
product['memory'] = 64
print(product)
print(product['name'])
print(product.get('name'))
print(product.get('color', 'we havent'))
del product['stock']
print(product)
phones = ["iPhone Xs", "Samsung Galaxy S10", "Xiaomi Mi8"]
product['recomend'] = phones
print(product)