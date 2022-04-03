def avg(data):
    sum_of_price = 0
    for i in range(len(data['products'])):
        sum_of_price += data['products'][i]['price']
    return round(sum_of_price/len(data['products']),3)

print(avg({"products": [{"name": "Product 1", "price": 100},{"name": "Product 2","price": 700},{"name": "Product 3","price": 300}]}))
