def discounted(price, discount):
    if discount >= 100:
        price_with_discount =  price
    else:
        price_with_discount = price - price * discount /100
    print(price_with_discount)

try:
    discounted(100, 20)
    discounted(80, '20')
except(TypeError):
    print('введены неверные значения')