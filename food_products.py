import pandas as pd

foods = pd.read_csv('food.csv')

def find_id(name):
    '''Input name of product to find the ID.'''
    items = []
    for index, row in foods.iterrows():
        if name in str(row['name']).lower():
            items.append((index, row['name']))
    return items

def get_ingredents(product_id):
    '''Get the ingredents of a product by product_id.'''
    ingredents = []
    for index, row in foods.iterrows():
        if index == product_id: 
            ingredents = row['features.value'].split(",")
    return ingredents

print(get_ingredents(1279))