import discord
from is_vegan import *
from can_be_vegan import *
from discord.ext import commands
from food_products import *
from discord.ext import menus

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

activity = discord.Game("Type v?help to start!")

bot = commands.Bot(
    command_prefix='v?',
    description='100% vegan bot, powered by plants!',
    help_command= help_command,
    activity = activity
)

class MySource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=8)

    async def format_page(self, menu, entries):
        offset = menu.current_page * self.per_page
        send_str = '```' + '\n'.join(f'{i}. {v}' for i, v in enumerate(entries, start=offset)) + '```'

        if send_str == '``````':
            return 'no items found...'
        
        return send_str

def combine_words(arg):
    if len(arg) > 1:
        return ' '.join(arg).lower()
    return str(arg[0]).lower()


@bot.command()
async def vegan(ctx, *ingredient):
    '''
    Check if an ingredent is vegan
    '''

    ingredient = combine_words(ingredient)
    is_it_maybe_vegan = is_flagged_ingredient(ingredient)
    is_it_vegan = is_vegan_ingredient(ingredient)

    if is_it_maybe_vegan:
        await ctx.send(f"{ingredient}: can be vegan... :question:")
    else:
        if is_it_vegan:
            await ctx.send(f"{ingredient}: vegan! :white_check_mark:")
        else:
            await ctx.send(f"{ingredient}: not vegan. :x:")

@bot.command()
async def happycow(ctx, *location):
    '''
    Type a zip code or city to see near by vegan restaurants
    '''
    
    if len(location) > 1:
        link_location = '+'.join(location)
    else:
        link_location = ''.join(location)
    
    happy_cow_link = f"https://www.happycow.net/searchmap/?s=3&location={link_location}&filters=vegan"
    await ctx.send(f"Here are some vegan restaurants near {' '.join(location)}:")
    await ctx.send(happy_cow_link)

@bot.command()
async def suggest(ctx, *ingredent):
    '''
    Suggest a non-vegan ingredent!
    '''
    
    ingredent = combine_words(ingredent)

    if is_flagged_ingredient(ingredent) or is_vegan_ingredient(ingredent):
        await ctx.send("Thank you for your suggestion!")
        with open('suggest.txt', 'a') as suggest_file:
            await suggest_file.write(ingredent + '\n')

    else:
        await ctx.send("Thank you for your suggestion, but we already have that in the data base!")

@bot.command()
async def find(ctx, *name_of_product):
    '''
    Find ID of a food product
    '''

    name_of_product = combine_words(name_of_product)
    dict_of_ids = find_id(name_of_product)
    formatted = []

    for key, value in dict_of_ids.items():
        formatted.append(f"ID:{key} | Product: {value}")

    pages = menus.MenuPages(source=MySource(formatted), clear_reactions_after=True)
    await pages.start(ctx)

    

@bot.command()
async def product(ctx, p_id):
    '''Enter product ID to see if it is vegan'''
    ingredent = get_ingredents(int(p_id))
    is_it_vegan = is_vegan_ingredient_list(ingredent)
    flagged = contains_flagged_ingredients(ingredent)

    if is_it_vegan == True and not len(flagged) > 0:
        await ctx.send(f'Totally plant powered!')
    else:
        non_vegan_foods = contains_non_vegan_ingredients(ingredent)
        non_vegan_foods = mylist = list(dict.fromkeys(non_vegan_foods))
        if len(flagged) > 0 and len(non_vegan_foods)  == 0:
            flagged_foods = ''
            for i in flagged:
                flagged_foods += f'{i}, '
            flagged_foods = flagged_foods[:-2]

            await ctx.send(f'May be vegan:\nHere are the possible non-vegan ingredents: {flagged_foods}')
        else:
            send_str = ''

            for i in non_vegan_foods:
                send_str += f'{i}, '
            send_str = send_str[:-2]
            
            await ctx.send(f'Not vegan...\nHere are the non-vegan ingredents: {send_str}')

bot.run('ODI1MjUwMTg5ODgyNDI1Mzc1.YF7MIQ.XXCDR487df3jQSU1W-EhCIHj8CA')