import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
# OH1 = int(os.getenv("OFFICE_HOURS_1"))
# OH2 = int(os.getenv("OFFICE_HOURS_2"))
# TEAMTEST = int(os.getenv("TEST_TEAM_CHANNEL"))
# TEAMONE = int(os.getenv("TEAM_ONE"))
# TEAMTWO = int(os.getenv("TEAM_TWO"))
# TEAMTHREE = int(os.getenv("TEAM_THREE"))
# TEAMFOUR = int(os.getenv("TEAM_FOUR"))
# TEAMFIVE = int(os.getenv("TEAM_FIVE"))
# InstructorLink = os.getenv("INSTRUCTOR_LINK")
# CamperLink = os.getenv("CAMPER_LINK")
# TeamLink = os.getenv("CAMPER_MEETING_LINK")
# botTesting = int(os.getenv("BOT_TESTING_CHANNEL"))
botDMs = int(os.getenv("BOT_DM_CHANNEL"))
botID = int(os.getenv("BOT_USER_ID"))
botImportant = int(os.getenv("BOT_IMPORTANT"))
# TEAM_INSTRUCTOR = os.getenv("TEAM_INSTRUCTOR_LINK")
# TEAM_CAMPER = os.getenv("TEAM_CAMPER_LINK")

class DirectMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Removed for the 2024 iteration of the bot
    # # Checks to see if specific member roles are in specific voice channels and
    # # when they leave, shoots them a DM
    # @commands.Cog.listener()
    # async def on_voice_state_update(self, member, before, after):
    #     channel = before.channel or after.channel
    #     instructRole = discord.utils.get(member.roles, name="Instructor")
    #     campRole = discord.utils.get(member.roles, name="Camper")

    #     # If the member has the `Instructor` role
    #     if instructRole is not None and instructRole.name == "Instructor":
    #         if channel.id == OH1:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished an Office Hours session in the #office-hours-1 channel.")
    #                 await member.send(f"Please fill out this form to record your session: {InstructorLink}")
    #                 await member.send("Thank you!")
    #         elif channel.id == OH2:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished an Office Hours session in the #office-hours-2 channel.")
    #                 await member.send(f"Please fill out this form to record your session: {InstructorLink}")
    #                 await member.send("Thank you!")
    #         elif channel.id == TEAMONE:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished a team meeting with Team 1.")
    #                 await member.send(f"Please fill out this form to record your session: {TEAM_INSTRUCTOR}")
    #                 await member.send("Thank you!")
    #         elif channel.id == TEAMTWO:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished a team meeting with Team 2.")
    #                 await member.send(f"Please fill out this form to record your session: {TEAM_INSTRUCTOR}")
    #                 await member.send("Thank you!")
    #         elif channel.id == TEAMTHREE:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished a team meeting with Team 3.")
    #                 await member.send(f"Please fill out this form to record your session: {TEAM_INSTRUCTOR}")
    #                 await member.send("Thank you!")
    #         elif channel.id == TEAMFOUR:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished a team meeting with Team 4.")
    #                 await member.send(f"Please fill out this form to record your session: {TEAM_INSTRUCTOR}")
    #                 await member.send("Thank you!")
    #         elif channel.id == TEAMFIVE:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished a team meeting with Team 5.")
    #                 await member.send(f"Please fill out this form to record your session: {TEAM_INSTRUCTOR}")
    #                 await member.send("Thank you!")

    #     # If the member has the `Camper` role
    #     if campRole is not None and campRole.name == "Camper":
    #         if channel.id == OH1:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished getting help from the instructors in the #office-hours-1 channel.")
    #                 await member.send(f"Please fill out this form so we know how well we helped you: {CamperLink}")
    #                 await member.send("Thank you!")
    #         elif channel.id == OH2:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished getting help from the instructors in the #office-hours-2 channel.")
    #                 await member.send(f"Please fill out this form so we know how well we helped you: {CamperLink}")
    #                 await member.send("Thank you!")
    #         elif channel.id == TEAMONE:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished a team meeting.")
    #                 await member.send(f"Please fill out this form so we know how it went: {TEAM_CAMPER}")
    #                 await member.send("Thank you!")
    #         elif channel.id == TEAMTWO:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished a team meeting.")
    #                 await member.send(f"Please fill out this form so we know how it went: {TEAM_CAMPER}")
    #                 await member.send("Thank you!")
    #         elif channel.id == TEAMTHREE:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished a team meeting.")
    #                 await member.send(f"Please fill out this form so we know how it went: {TEAM_CAMPER}")
    #                 await member.send("Thank you!")
    #         elif channel.id == TEAMFOUR:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished a team meeting.")
    #                 await member.send(f"Please fill out this form so we know how it went: {TEAM_CAMPER}")
    #                 await member.send("Thank you!")
    #         elif channel.id == TEAMFIVE:
    #             if before.channel is not None and after.channel is None: # after leaving the voice channel
    #                 await member.send("Hi there, it looks like you just finished a team meeting.")
    #                 await member.send(f"Please fill out this form so we know how it went: {TEAM_CAMPER}")
    #                 await member.send("Thank you!")


    # Checks to see if someone DMs the bot
    # If so, it forwards the message to a specific channel and replies to the
    # person who sent the message
    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel): # if the message is a DM
            channel = self.bot.get_channel(botDMs) # get channel to forward message to
            if message.author.id != botID: # make sure we're not forwarding/sending messages when the bot messages
                newMessage = discord.Embed(title=f"New bot DM from `{message.author}`", description=f"{message.content}", timestamp=message.created_at)
                await channel.send(embed=newMessage) # forwards message to channel
                await message.author.send("I am a bot and cannot respond, but I have forwarded your message to the EdASE instructor team.")
            await self.bot.process_commands(message)
        elif isinstance(message.channel, discord.TextChannel):
            if message.channel.id == botImportant:
                if message.author.id != botID:
                    channel = self.bot.get_channel(int(botImportant))
                    msg = message.channel 
                    thread = await channel.create_thread(name=f"{message.author.display_name}'s Thread", message=message)
                    reminder = "Please use this thread to continue the conversation."
                    await thread.send(reminder)

async def setup(bot: commands.Bot):
    await bot.add_cog(DirectMessage(bot))
