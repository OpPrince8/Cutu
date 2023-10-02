import discord
from discord.ext import commands
import os
from webserver import keep_alive

client = commands.Bot(command_prefix = '??', intents = discord.Intents.all())


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="'Op Prince' ??hello"))
    print("Bot is Ready and Online")

@client.command()
async def hello(ctx):
  await ctx.send("Hello! I am Cutu. Made by Op prince I am under development right now will soon be done.")

my_secret = os.environ['TOKEN']

keep_alive() 
client.run(os.getenv("TOKEN"))
test
