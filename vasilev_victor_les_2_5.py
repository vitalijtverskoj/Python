price = [98.98, 99.09, 55, 76.8, 45.50, 67.34, 86.66, 33.33, 22.75, 13.86, 7.51]


for n in price:
    price_1 = f'{n:.2f}'.split('.')
    rub = price_1[0]
    kop = price_1[1]
    print(f'{rub} руб {kop} коп', end=', ')
print(price)

print(f'ID {id(price)} - {price}')
price.sort()
print(f'ID sort {id(price)} - {price}')

price_high_to_low = list(reversed(price))
print(price_high_to_low)
_list = price_high_to_low[:5]
print(_list[::-1])
