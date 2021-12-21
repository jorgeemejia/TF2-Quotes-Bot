import discord
from discord.channel import VoiceChannel
from discord.errors import ClientException
from discord.ext import commands

import os
from dotenv import load_dotenv

import youtube_dl

from scout import get_scout_quote_url, get_scout_quote, print_half_scout_list, print_other_half_scout_list
from heavy import get_heavy_quote_url, get_heavy_quote, print_half_heavy_list, print_other_half_heavy_list
from demo_man import get_demo_man_quote, get_demo_man_quote_url, print_half_demo_man_list, print_other_half_demo_man_list
from engineer import get_engineer_quote_url, get_engineer_quote, print_engineer_list
from medic import get_medic_quote_url, get_medic_quote, print_medic_list
from pyro import get_pyro_quote_url, get_pyro_quote, print_pyro_list
from sniper import get_sniper_quote_url, get_sniper_quote, print_half_sniper_list, print_other_half_sniper_list
from soldier import get_soldier_quote_url, get_soldier_quote, print_half_soldier_list, print_other_half_soldier_list, print_last_half_soldier_list
from spy import get_spy_quote_url, get_spy_quote, print_half_spy_list, print_other_half_spy_list

#client = discord.Client()

load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "!", intents=intents)

@client.event                               
async def on_ready():
    """Prints a message when bot is logged on"""
    print("Yeah. Yeah, yeah, yeah! Let's go!")


@client.command()
async def scout(ctx, *arg: int):
    """Prints a random scout quote"""
    if ctx.author == client.user:
        return
    else:
        if arg:
            num = arg[0]
            quote = get_scout_quote(num)
        else:
            quote = get_scout_quote()
        url = get_scout_quote_url(quote)
        song_there = os.path.isfile("audio.mp3")
        try:
            if song_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing audio to end!")
            return
        await ctx.channel.send(quote)
       #user_id = discord.utils.get(ctx.memberid)
       #voiceChannel = discord.utils.get(ctx.) 
        user = ctx.author
        server = ctx.guild
        for vc in server.voice_channels:
            if user in vc.members:
                vc_name = vc.name
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = vc_name)
        try:
            await voiceChannel.connect()
        except ClientException:
            pass
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild )
        
      
        
        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "audio.mp3")
        voice.play(discord.FFmpegPCMAudio("audio.mp3"))

@client.command()
async def heavy(ctx, *arg: int ):
    """Prints a random heavy quote"""
    if ctx.author == client.user:
        return
    else:
        if arg:
            num = arg[0]
            quote = get_heavy_quote(num)
        else:
            quote = get_heavy_quote()
        url = get_heavy_quote_url(quote)
        song_there = os.path.isfile("audio.mp3")
        try:
            if song_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing audio to end!")
            return
        await ctx.channel.send(quote)
        user = ctx.author
        server = ctx.guild
        for vc in server.voice_channels:
            if user in vc.members:
                vc_name = vc.name
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = vc_name)
        try:
            await voiceChannel.connect()
        except ClientException:
            pass
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild )
        
      
        
        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "audio.mp3")
        voice.play(discord.FFmpegPCMAudio("audio.mp3"))

@client.command()
async def demo_man(ctx, *arg: int):
    """Prints a random demo_man quote"""
    if ctx.author == client.user:
        return
    else:
        # print(f"%%%%%%%%%%%%%%{arg}%%%%%%%%%")
        # print(f"%%%%%%%%%%%%%%{arg[0]}%%%%%%%%%")
        # print(f"%%%%%%%%%%%%%%{type(arg[0])}%%%%%%%%%")
        # print(f"%%%%%%%%%%%%%%{num}%%%%%%%%%")
        if arg:
            num = arg[0]
            quote = get_demo_man_quote(num)
        else:
            quote = get_demo_man_quote()
        url = get_demo_man_quote_url(quote)
        song_there = os.path.isfile("audio.mp3")
        try:
            if song_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing audio to end!")
            return
        await ctx.channel.send(quote)
        user = ctx.author
        server = ctx.guild
        for vc in server.voice_channels:
            if user in vc.members:
                vc_name = vc.name
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = vc_name)
        try:
            await voiceChannel.connect()
        except ClientException:
            pass
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild )
        
      
        
        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "audio.mp3")
        voice.play(discord.FFmpegPCMAudio("audio.mp3"))

@client.command()
async def engineer(ctx, *arg: int):
    """Prints a random engineer quote"""
    if ctx.author == client.user:
        return
    else:
        if arg:
            num = arg[0]
            quote = get_engineer_quote(num)
        else:
            quote = get_engineer_quote()
        url = get_engineer_quote_url(quote)
        song_there = os.path.isfile("audio.mp3")
        try:
            if song_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing audio to end!")
            return
        await ctx.channel.send(quote)
        user = ctx.author
        server = ctx.guild
        for vc in server.voice_channels:
            if user in vc.members:
                vc_name = vc.name
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = vc_name)
        try:
            await voiceChannel.connect()
        except ClientException:
            pass
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild )
        
      
        
        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "audio.mp3")
        voice.play(discord.FFmpegPCMAudio("audio.mp3"))

@client.command()
async def medic(ctx, *arg: int):
    """Prints a random medic quote"""
    if ctx.author == client.user:
        return
    else:
        if arg:
            num = arg[0]
            quote = get_medic_quote(num)
        else:
            quote = get_medic_quote()
        url = get_medic_quote_url(quote)
        song_there = os.path.isfile("audio.mp3")
        try:
            if song_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing audio to end!")
            return
        await ctx.channel.send(quote)
        user = ctx.author
        server = ctx.guild
        for vc in server.voice_channels:
            if user in vc.members:
                vc_name = vc.name
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = vc_name)
        try:
            await voiceChannel.connect()
        except ClientException:
            pass
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild )
        
      
        
        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "audio.mp3")
        voice.play(discord.FFmpegPCMAudio("audio.mp3"))

@client.command()
async def pyro(ctx, *arg: int):
    """Prints a random pyro quote"""
    if ctx.author == client.user:
        return
    else:
        if arg:
            num = arg[0]
            quote = get_pyro_quote(num)
        else:
            quote = get_pyro_quote()
        url = get_pyro_quote_url(quote)
        song_there = os.path.isfile("audio.mp3")
        try:
            if song_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing audio to end!")
            return
        await ctx.channel.send(quote)
        user = ctx.author
        server = ctx.guild
        for vc in server.voice_channels:
            if user in vc.members:
                vc_name = vc.name
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = vc_name)
        try:
            await voiceChannel.connect()
        except ClientException:
            pass
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild )
        
      
        
        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "audio.mp3")
        voice.play(discord.FFmpegPCMAudio("audio.mp3"))

@client.command()
async def sniper(ctx, *arg: int):
    """Prints a random sniper quote"""
    if ctx.author == client.user:
        return
    else:
        if arg:
            num = arg[0]
            quote = get_sniper_quote(num)
        else:
            quote = get_sniper_quote()
        url = get_sniper_quote_url(quote)
        song_there = os.path.isfile("audio.mp3")
        try:
            if song_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing audio to end!")
            return
        await ctx.channel.send(quote)
        user = ctx.author
        server = ctx.guild
        for vc in server.voice_channels:
            if user in vc.members:
                vc_name = vc.name
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = vc_name)
        try:
            await voiceChannel.connect()
        except ClientException:
            pass
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild )
        
      
        
        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "audio.mp3")
        voice.play(discord.FFmpegPCMAudio("audio.mp3"))

@client.command()
async def soldier(ctx, *arg: int):
    """Prints a random soldier quote"""
    if ctx.author == client.user:
        return
    else:
        if arg:
            num = arg[0]
            quote = get_soldier_quote(num)
        else:
            quote = get_soldier_quote() 
        url = get_soldier_quote_url(quote)
        song_there = os.path.isfile("audio.mp3")
        try:
            if song_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing audio to end")
            return
        await ctx.channel.send(quote)
        user = ctx.author
        server = ctx.guild
        for vc in server.voice_channels:
            if user in vc.members:
                vc_name = vc.name
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = vc_name)
        try:
            await voiceChannel.connect()
        except ClientException:
            pass
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild )
        
      
        
        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "audio.mp3")
        voice.play(discord.FFmpegPCMAudio("audio.mp3"))

@client.command()
async def spy(ctx, *arg: int):
    """Prints a random spy quote"""
    if ctx.author == client.user:
        return
    else:
        if arg:
            num = arg[0]
            quote = get_spy_quote(num)
        else:
            quote = get_spy_quote()
        url = get_spy_quote_url(quote)
        song_there = os.path.isfile("audio.mp3")
        try:
            if song_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing audio to end!")
            return
        await ctx.channel.send(quote)
        user = ctx.author
        server = ctx.guild
        for vc in server.voice_channels:
            if user in vc.members:
                vc_name = vc.name
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = vc_name)
        try:
            await voiceChannel.connect()
        except ClientException:
            pass
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild )
        
      
        
        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "audio.mp3")
        voice.play(discord.FFmpegPCMAudio("audio.mp3"))   

@client.command()
async def list (ctx, arg):
    if arg == 'demo_man':
        first_half = print_half_demo_man_list()
        second_half = print_other_half_demo_man_list()
        await ctx.channel.send(first_half)
        await ctx.channel.send(second_half)

    elif arg == 'engineer':
        txt = print_engineer_list()
        await ctx.channel.send(txt)


    elif arg == 'heavy':
        first_half = print_half_heavy_list()
        second_half = print_other_half_heavy_list()
        await ctx.channel.send(first_half)
        await ctx.channel.send(second_half)

    elif arg == 'medic':
        txt = print_medic_list()
        await ctx.channel.send(txt)


    elif arg == 'pyro':
        txt = print_pyro_list()
        await ctx.channel.send(txt)

    elif arg == 'scout':
        first_half = print_half_scout_list()
        second_half = print_other_half_scout_list()
        await ctx.channel.send(first_half)
        await ctx.channel.send(second_half)

    elif arg == 'sniper':
        first_half = print_half_sniper_list()
        second_half = print_other_half_sniper_list()
        await ctx.channel.send(first_half)
        await ctx.channel.send(second_half)

    elif arg == 'soldier':
        first_half = print_half_soldier_list()
        second_half = print_other_half_soldier_list()
        third_half = print_last_half_soldier_list()
        await ctx.channel.send(first_half)
        await ctx.channel.send(second_half)
        await ctx.channel.send(third_half)

    elif arg == 'spy':
        first_half = print_half_spy_list()
        second_half = print_other_half_spy_list()
        await ctx.channel.send(first_half)
        await ctx.channel.send(second_half)

    else:
        pass

# @client.command()
# async def voice(ctx):
#     user = ctx.author
#     print(user) #ChoccyMiltank (he/him)#9107
#     server = ctx.guild
#     print(server) #ChoccyMiltank (he/him)'s server
#     #channel = ctx.channel
#     #print(channel) #general-too
#     # for voice_channel in server.voice_channels:
#     #     print(voice_channel)
#     #     #General
#     #     #Audio
#     for vc in server.voice_channels:
#         if user in vc.members:
#             print(vc.name)
#     #store the vc.name
#     #make that the name of the chanell it'll enter 
#     # for vc in server.voice_channels:
#     #     print(vc.members)
    
# @client.command()
# async def join(ctx):
#     user = ctx.author
#     server = ctx.guild

client.run(os.getenv('TOKEN'))
