
import discord
from discord import default_permissions
from discord.ext import commands , tasks
from discord.commands import Option
from data.beta_data import token  ,weapon , attachment
from itertools import cycle
guild = 1069174895893827604
intents=discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='R!', intents=discord.Intents.all())
status = cycle(["scpsl database rework bot", "made bt hanbin#0939", "SCP : Secreat Laboratory"])

@bot.event
async def on_ready():
    print("logined succesfully\n")
    print(f"{len(bot.guilds)} server joined\n") 
    change_status.start()

@tasks.loop(seconds=5)    # n초마다 다음 메시지 출력
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.slash_command(name="weponary",guild_ids=[guild])
@commands.has_role("BETA TESTING")
async def ping(ctx):
    await ctx.respond(view=weapon())


@ping.error
async def error(ctx,error):
    await ctx.respond(error)

@bot.slash_command(guild_ids=[1069174895893827604])
async def add_beta_testing(ctx):
    guild = bot.get_guild(1069174895893827604)
    role = guild.get_role(1088477030661763183)
    user = ctx.author
    await user.add_roles(role)
    await ctx.respond("이제 베타 태스팅에 참여할수 있습니다!")

bot.run(token)