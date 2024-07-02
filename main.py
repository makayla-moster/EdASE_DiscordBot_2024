import asyncio
import logging
import os
import random
import datetime

import aiohttp
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
BACKCHANNEL = os.getenv("BOT_BACKCHANNEL")
intents=discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="!")
logging.basicConfig(level=logging.INFO)

async def load_cogs():
    for folder in os.listdir("cog_modules"):
        if os.path.exists(os.path.join("cog_modules", folder, "cog.py")):
            await bot.load_extension(f"cog_modules.{folder}.cog")
            print(f"{folder} cog loaded!")
        else:
            print(f"{folder} cog NOT loaded!")

@tasks.loop(time=datetime.time(hour=11, minute=30)) #7:30 EST
async def backchannel_loop():
    weekday = datetime.datetime.now().weekday()
    weekdays = [0, 1, 2, 3, 4, 5]
    if weekday in weekdays: # monday = 0, sunday = 6
        channel = bot.get_channel(int(BACKCHANNEL))
        response = "Please use the following thread for today's backchannel discussions."
        msg = await channel.send(response)
        thread = await channel.create_thread(name=f"{datetime.date.today().strftime('%A %B %d')} Thread", message=msg)
        reminder = "Remember to use the #important channel for any important messages and tag the necessary instructor or role (Camp Director, Leader, Instructor, TA)."
        await thread.send(reminder)
        # with open("dict.json", 'r') as filename:
        #     channelDict = json.load(filename)
        # for guild in channelDict: 
        #     channel = channelDict[guild]
        #     c = bot.get_channel(channel)
        #     response = "Hey @everyone! Just checking in for the week. Use the thread below to discuss your plans for this week."
        #     msg = await c.send(response)
        #     response2 = "What is everyone planning to work on this week? Are there any anticipated blockers/problems?"
        #     thread = await c.create_thread(name="Weekly Check-In", message=msg)
        #     await thread.send(response2)

@bot.event
async def on_ready():
    game = discord.Game("with Scratch blocks")
    await bot.change_presence(activity=game)
    await load_cogs()
    # print(datetime.date.today().strftime("%A %B %d"))
    if not backchannel_loop.is_running():
        backchannel_loop.start()
        print("backchannel_loop started")

bot.run(TOKEN)
