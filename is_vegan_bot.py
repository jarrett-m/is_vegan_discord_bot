import discord
from IsVegan import *
from discord.ext import commands

bot = commands.Bot(command_prefix='??')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def vegan(ctx, ing):
    is_it_vegan = isVeganIngredient(str(ing))
    if is_it_vegan:
        await ctx.send(f"{ing}: Vegan! :white_check_mark:")
    else:
        await ctx.send(f"{ing}: Not vegan. :x:")
    

bot.run('ODI1MjUwMTg5ODgyNDI1Mzc1.YF7MIQ.XXCDR487df3jQSU1W-EhCIHj8CA')
