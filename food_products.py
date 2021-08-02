import pandas as pd
import re
from concurrent.futures import ThreadPoolExecutor as TPE

foods = pd.read_csv('foods.csv')
foods['name'] = foods['name'].str.lower()

def find_id(name):
    '''Input name of product to find the ID.'''

    '''for index, row in foods.iterrows():
        if name in str(row['description']).lower():
            items.append((index, row['description']))
        if index == 10000:
            print(10000)
    '''
    inds = foods['name'].str.contains(name, na=False).astype(bool)
    return foods[inds]['name'].to_dict()



def get_ingredents(product_id):
    '''Get the ingredents of a product by product_id.'''
    ingredents = re.split('[\\[\\]\\{\\}?.,&()]', foods.iloc[product_id]['features.value'])
    return [i.strip().lower() for i in ingredents if len(i) > 0]
    
print(get_ingredents(4608))