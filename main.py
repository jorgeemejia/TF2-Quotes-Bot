import discord
from discord.channel import VoiceChannel
from discord.errors import ClientException
from discord.ext import commands

import os
from dotenv import load_dotenv

import youtube_dl

from scout import get_scout_quote_url, get_scout_quote
from heavy import get_heavy_quote_url, get_heavy_quote
from demo_man import get_demo_man_quote, get_demo_man_quote_url
from engineer import get_engineer_quote_url, get_engineer_quote
from medic import get_medic_quote_url, get_medic_quote
from pyro import get_pyro_quote_url, get_pyro_quote
from sniper import get_sniper_quote_url, get_sniper_quote
from soldier import get_soldier_quote_url, get_soldier_quote
from spy import get_spy_quote_url, get_spy_quote

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
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
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
async def heavy(ctx):
    """Prints a random heavy quote"""
    if ctx.author == client.user:
        return
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
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
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
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
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
async def engineer(ctx):
    """Prints a random engineer quote"""
    if ctx.author == client.user:
        return
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
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
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
async def medic(ctx):
    """Prints a random medic quote"""
    if ctx.author == client.user:
        return
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
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
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
async def pyro(ctx):
    """Prints a random pyro quote"""
    if ctx.author == client.user:
        return
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
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
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
async def sniper(ctx):
    """Prints a random sniper quote"""
    if ctx.author == client.user:
        return
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
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
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
async def soldier(ctx):
    """Prints a random soldier quote"""
    if ctx.author == client.user:
        return
    else:
        quote = get_soldier_quote()
        await ctx.channel.send(quote) 
        url = get_soldier_quote_url(quote)
        song_there = os.path.isfile("audio.mp3")
        try:
            if song_there:
                os.remove("audio.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing audio to end")
            return

        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
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
async def spy(ctx):
    """Prints a random spy quote"""
    if ctx.author == client.user:
        return
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
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
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




    

client.run(os.getenv('TOKEN'))
