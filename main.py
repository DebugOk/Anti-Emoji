#Imports 
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions,when_mentioned_or
from discord.utils import get

from datetime import datetime
import time
import os
import shutil

#Important
Prefix = '$' #Change the prefix here

client = commands.Bot(command_prefix=when_mentioned_or(Prefix))
client.remove_command("help")

version = 1
#Ready message
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if len(message.stickers) != 0:
        await message.delete(message)

#Ensure we have a /temp directory, and if it exists we clear it
if not os.path.exists('temp'):
	os.makedirs('temp')
else:
    shutil.rmtree('temp')
    time.sleep(.6)
    os.makedirs('temp')

#Ping command
@client.command()
async def ping(ctx):
    embedVar = discord.Embed(title="Pong!", description="Got a reply in {0}".format(round(client.latency, 1)), color=0x4287f5,timestamp=datetime.now())
    await ctx.send(embed=embedVar)

#Help command
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="Current prefix: {0}\n\nCurrent version: {1}".format(Prefix,version), color=0x08ffa0, timestamp=datetime.now())
    embed.add_field(name="ping",value="This will check how fast the bot can reach Discord. It doesn't do anything special.\n\n**Required permissions:** *None*",inline=True)
    embed.add_field(name="help",value="I wonder what this does...\n\n**Required permissions:** *None*",inline=True)
    embed.set_footer(text="Bot created by DebugOk#6605", icon_url="https://cdn.discordapp.com/avatars/282227463642415104/f6d632f4fa73a7ff947ebba43277cf11.webp")
    await ctx.send(embed=embed)

#Main error thing
@client.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found\n```{0}```".format(error))
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to do that!\n```{0}```".format(error))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You are missing a required argument!\n```{0}```".format(error))
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Invalid argument!\n```{0}```".format(error))
    elif isinstance(error, commands.CommandError) or isinstance(error,commands.CommandInvokeError):
        await ctx.message.add_reaction('❌')
        try:
            await ctx.send("An error has occured!\n```{0}```".format(error)) #This error can possibly go past Discord's character limit. Better safe then sorry.
        except:
            await ctx.send("An error has occured!")
    else: 
        await ctx.send("An unknown error has occured!")

#Sign in
client.run('')