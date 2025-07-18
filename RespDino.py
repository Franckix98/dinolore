#!/usr/bin/env python3

import sys
import os
import random
import discord
from env import DISCORD_TOKEN, DISCORD_GUILD
from clist2 import citlist
from discord.ext import commands
"from dotenv import load_dotenv"
project_folder = os.path.expanduser('~C:\\Users\\franc\\Documents\\DinoBot')
"load_dotenv(os.path.join(project_folder, '.env'))"

"load_dotenv()"
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

os.chdir("C:\\Users\\franc\\Documents\\DinoBot")
sys.path.insert(1, 'C:\\Users\\franc\\Documents\\DinoBot')

TOKEN = DISCORD_TOKEN
GUILD = DISCORD_GUILD

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


nv = len(citlist)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

   # citation = (f"Voilà une citation de Dinosaure : {citlist[random.randint(0, nv)]}")

    if message.content == "!cit":
        #response = citation
        await message.channel.send(f"Voici le lore de Dinosaure : {citlist[random.randint(0, nv-1)]}")
    #print("test")

bot.run(TOKEN)