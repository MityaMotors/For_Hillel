"""map function to reassign all products in one table"""
from functools import reduce
from operator import itemgetter

products = [
    {"id": "001", "name": "Watermelon", "table": 23, "price": 11, "type": "fruit"},
    {"id": "002", "name": "Onion", "table": 50, "price": 11, "type": "vegetable"},
    {"id": "003", "name": "Cake", "table": 48, "price": 50, "type": "sweet"},
    {"id": "004", "name": "Apple", "table": 22, "price": 11, "type": "fruit"},
    {"id": "005", "name": "Kiwi", "table": 67, "price": 11, "type": "fruit"}
]

print("Map function -> Assign products to the 32nd table")


def assign_to_table(products, new_table_number) -> map:
    def apply(x):
        x["table"] = new_table_number
        return x

    return map(apply, products)


assign_table = assign_to_table(products, 32)
print(list(assign_table))

"""Filter by low price"""
print("---------------------------------------------------------------")
print("Filter by low price")

prices = {'Watermelon': 11, 'Onion': 5, 'Cake': 50, "Cucumber": 32, "Cabage": 7}


def has_low_price(price) -> int:
    return prices[price] <= 11


def has_high_price(price) -> int:
    return prices[price] > 12


low_price = list(filter(has_low_price, prices.keys()))
high_price = list(filter(has_high_price, prices.keys()))
print(f"The products with price less or equal 11:{low_price}")
print(f"The products with price more then 12:{high_price}")

"""Reduce the dict by same price"""
print("---------------------------------------------------------------")
print("Reduce the dict by same price")


def func(new_products, product):
    same_price = set([_['price'] for _ in new_products])
    if product['price'] in same_price:
        return new_products
    return new_products + [product]


products_reduce_by_same_price = reduce(func, [[]] + products)
print(products_reduce_by_same_price)

"""Sorted function to products_02 by table"""
print("---------------------------------------------------------------")
print("Sorted function to products_02 by table")
products_02 = [
    {"id": "001", "name": "Watermelon", "table": 23, "price": 11, "type": "fruit"},
    {"id": "002", "name": "Onion", "table": 50, "price": 11, "type": "vegetable"},
    {"id": "003", "name": "Cake", "table": 48, "price": 50, "type": "sweet"},
    {"id": "004", "name": "Apple", "table": 22, "price": 11, "type": "fruit"},
    {"id": "005", "name": "Kiwi", "table": 67, "price": 11, "type": "fruit"}
]

sort_product_02_by_table = sorted(products_02, key=itemgetter('table'))
print(sort_product_02_by_table)
