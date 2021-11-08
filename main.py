import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

from scout import get_scout_quote
from heavy import get_heavy_quote

#client = discord.Client()

load_dotenv()

client = commands.Bot(command_prefix = "!")

@client.event                               
async def on_ready():
    """Prints a message when bot is logged on"""
    print("Yeah. Yeah, yeah, yeah! Let's go!")


@client.command()
async def scout(ctx):
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_scout_quote())

@client.command()
async def heavy(ctx):
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_heavy_quote())


    

client.run(os.getenv('TOKEN'))
