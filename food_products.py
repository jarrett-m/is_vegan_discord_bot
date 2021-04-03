import pandas as pd
import time
import re
import requests
from concurrent.futures import ThreadPoolExecutor as TPE

foods = pd.read_csv('foods.csv')
foods['description'] = foods['description'].str.lower()

def find_id(name):
    '''Input name of product to find the ID.'''
    items = []
    '''for index, row in foods.iterrows():
        if name in str(row['description']).lower():
            items.append((index, row['description']))
        if index == 10000:
            print(10000)
    '''
    inds = foods['description'].str.contains(name, na=False).astype(bool)
    return foods[inds]['description'].to_dict()



def get_ingredents(product_id):
    '''Get the ingredents of a product by product_id.'''
    ingredents = re.split('[\\[\\]\\{\\}?.,&()]', foods.iloc[product_id]['ingredients'])
    return [i.strip().lower() for i in ingredents if len(i) > 0]
    
print(get_ingredents(1394))