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
        '''if len(ingredent.split(" ")) > 1:
            for split_ingredent in ingredent.split(" "):
                for non_veg in get_non_vegan_list():
                    if split_ingredent in non_veg:
                        return_list.append(split_ingredent)
                        break
        else:'''
        for non_veg in get_non_vegan_list():
            if ingredent.lower().strip() == non_veg:
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
        '''if len(ingredents.split(" ")) > 1:
            for split_ingredents in ingredents.split(" "):
                for non_vegan_list in get_non_vegan_list():
                    if split_ingredents in non_vegan_list:
                        return False
        else:'''
        for non_vegan_list in get_non_vegan_list():
            if ingredents.lower() in non_vegan_list:
                return False
    
    return True


    #return not bool([i.lower().strip() for i in ingredients_to_check if i in get_non_vegan_list()])