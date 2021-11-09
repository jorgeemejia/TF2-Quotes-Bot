import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

from scout import get_scout_quote
from heavy import get_heavy_quote
from demo_man import get_demo_man_quote
from engineer import get_engineer_quote
from medic import get_medic_quote
from pyro import get_pyro_quote
from sniper import get_sniper_quote
from soldier import get_soldier_quote
from spy import get_spy_quote

#client = discord.Client()

load_dotenv()

client = commands.Bot(command_prefix = "!")

@client.event                               
async def on_ready():
    """Prints a message when bot is logged on"""
    print("Yeah. Yeah, yeah, yeah! Let's go!")


@client.command()
async def scout(ctx):
    """Prints a random scout quote"""
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_scout_quote())

@client.command()
async def heavy(ctx):
    """Prints a random heavy quote"""
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_heavy_quote())

@client.command()
async def demo_man(ctx):
    """Prints a random heavy quote"""
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_demo_man_quote())

@client.command()
async def engineer(ctx):
    """Prints a random heavy quote"""
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_engineer_quote())

@client.command()
async def medic(ctx):
    """Prints a random heavy quote"""
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_medic_quote())

@client.command()
async def pyro(ctx):
    """Prints a random heavy quote"""
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_pyro_quote())

@client.command()
async def sniper(ctx):
    """Prints a random heavy quote"""
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_sniper_quote())  

@client.command()
async def soldier(ctx):
    """Prints a random heavy quote"""
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_soldier_quote()) 

@client.command()
async def spy(ctx):
    """Prints a random heavy quote"""
    if ctx.author == client.user:
        return
    else:
        await ctx.channel.send(get_spy_quote())   




    

client.run(os.getenv('TOKEN'))
