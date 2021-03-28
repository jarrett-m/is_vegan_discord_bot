import discord
from is_vegan import *
from can_be_vegan import *
from discord.ext import commands

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(
    command_prefix='v?',
    description='100% vegan bot, powered by plants!',
    help_command= help_command
)

@bot.command()
async def vegan(ctx, *ingredient):
    '''
    Check if an ingredent is vegan
    '''
    is_it_maybe_vegan = is_flagged_ingredient(' '.join(ingredient))
    is_it_vegan = is_vegan_ingredient(' '.join(ingredient))
    if is_it_maybe_vegan:
        await ctx.send(f"{' '.join(ingredient)}: can be vegan... :question:")
    else:
        if is_it_vegan:
            await ctx.send(f"{' '.join(ingredient)}: vegan! :white_check_mark:")
        else:
            await ctx.send(f"{' '.join(ingredient)}: not vegan. :x:")

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




bot.run('ODI1MjUwMTg5ODgyNDI1Mzc1.YF7MIQ.XXCDR487df3jQSU1W-EhCIHj8CA')
