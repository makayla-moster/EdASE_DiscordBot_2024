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
ANNOUNCEMENTS = os.getenv("BOT_ANNOUNCEMENTS")
TEAM1_GEN = os.getenv("TEAM1")
TEAM2_GEN = os.getenv("TEAM2")
TEAM3_GEN = os.getenv("TEAM3")
TEAM4_GEN = os.getenv("TEAM4")
TEAM5_GEN = os.getenv("TEAM5")
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
    weekdays = [0, 1, 2, 3, 4]
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

@tasks.loop(time=datetime.time(hour=16, minute=30))
async def teamchannel_loop():
    t1 = bot.get_channel(int(TEAM1_GEN))
    t2 = bot.get_channel(int(TEAM2_GEN))
    t3 = bot.get_channel(int(TEAM3_GEN))
    t4 = bot.get_channel(int(TEAM4_GEN))
    t5 = bot.get_channel(int(TEAM5_GEN))
    weekday = datetime.datetime.now().weekday()
    weekdays = [0, 1, 2, 3, 4]
    if weekday in weekdays:
        checkinMsg = "What does everyone plan to work on for their project today?"
        team1 = "Hey <@&1262500319816843314>!"
        team2 = "Hey <@&1262500462054342757>!"
        team3 = "Hey <@&1262500478273458257>!"
        team4 = "Hey <@&1262500501363101789>!"
        team5 = "Hey <@&1262500529792225361>!"

        await t1.send(team1)
        await t1.send(checkinMsg)

        await t2.send(team2)
        await t2.send(checkinMsg)

        await t3.send(team3)
        await t3.send(checkinMsg)

        await t4.send(team4)
        await t4.send(checkinMsg)

        await t5.send(team5)
        await t5.send(checkinMsg)


@tasks.loop(time=datetime.time(hour=16, minute=40)) #12:40 EST
async def announcement_loop():
    weekday = datetime.datetime.now().weekday()
    weekdays = [0, 1, 2, 3, 4]
    if weekday in weekdays: # monday = 0, sunday = 6
        channel = bot.get_channel(int(ANNOUNCEMENTS))
        response = "Hey <@&1250861795329966140>! Just a reminder that our last day of camp starts in 20 minutes! We'll see you soon! :)"
        msg = await channel.send(response)


@bot.event
async def on_ready():
    game = discord.Game("with Scratch blocks")
    await bot.change_presence(activity=game)
    await load_cogs()
    # print(datetime.date.today().strftime("%A %B %d"))
    if not backchannel_loop.is_running():
        backchannel_loop.start()
        print("backchannel_loop started")
    if not announcement_loop.is_running():
        announcement_loop.start()
        print("announcement_loop started")
    # if not teamchannel_loop.is_running():
    #     teamchannel_loop.start()
    #     print("teamchannel_loop started")

bot.run(TOKEN)
