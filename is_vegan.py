from ingredients_list_provider import get_non_vegan_list

def is_vegan_ingredient(ingredient_to_check):
    '''
    This functions takes the given ingredient.
    and checks it against the non-vegan list of ingredients.
    '''
    if(ingredient_to_check == ''):
        return True
    ingredient_to_check = ingredient_to_check.strip().lower().replace(" ", "")
    non_vegan_list = [i.lower().strip().replace(" ","") for i in get_non_vegan_list()]

    if (ingredient_to_check in non_vegan_list):
        return False
    return True

def contains_non_vegan_ingredients(ingredients_to_check):
    '''
    This functions takes a given list of ingredients
    and checks them against the non-vegan list of ingredients.
    '''
    ingredients_to_check = [i.strip().lower() for i in ingredients_to_check]
    return_list = []

    for ingredent in ingredients_to_check:
        for non_veg in get_non_vegan_list():
            if non_veg in ingredent: #REPLACE WITH REGEX
                return_list.append(ingredent)
                break

    return return_list
    #return [i for i in ingredients_to_check if i in non_vegan_list]

def is_vegan_ingredient_list(ingredients_to_check):
    '''
    This functions takes a given list of ingredients.
    and checks them against the non-vegan list of ingredients.
    '''
    for ingredents in ingredients_to_check:
        for non_vegan_list in get_non_vegan_list():
            if non_vegan_list == ingredents.lower(): #REPLACE WITH REGEX
                return False
    
    return True


    #return not bool([i.lower().strip() for i in ingredients_to_check if i in get_non_vegan_list()])
