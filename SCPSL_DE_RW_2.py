import discord
from dotenv import load_dotenv
from discord.ext import commands
from config.data import *
load_dotenv()

bot = commands.Bot(command_prefix="!",intents=discord.Intents.default(),owner_ids=[759072684461391893])

cogs_path = 'cogs'
cogs_list = ['weapon',
             'music',
             'mp3'
             ]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print("ready!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Warning : this bot is test version"))


bot.run(token_beta)