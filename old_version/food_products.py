'''Find and get ingredents from database.'''
import pandas as pd
import time
import re
import requests
from concurrent.futures import ThreadPoolExecutor as TPE

foods = pd.read_csv('foods.csv')
foods['description'] = foods['description'].str.lower()

def find_id(name):
    '''
       Input name of product to find the ID.
       Returns all products in foods.csv that contain
       the name.
    '''
    items = []
    inds = foods['description'].str.contains(name, na=False).astype(bool)
    return foods[inds]['description'].to_dict()



def get_ingredents(product_id):
    '''Get the ingredents of a product by product_id.'''
    ingredents = re.split('[\\[\\]\\{\\}?.,&()]', foods.iloc[product_id]['ingredients'])
    return [i.strip().lower() for i in ingredents if len(i) > 0]
