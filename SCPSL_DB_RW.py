
import discord
from discord import default_permissions
from discord.ext import commands , tasks
from discord.commands import Option
from config.data import token , token_beta
from data.weaponary import weapon , special_weapon
from data.scp import scp_classes
from itertools import cycle
from data.music_file import SL_music , Parabellum , SCPSL_retro , The_Final_Flash , The_wating_game
from data.human import MyView
from data.item import itemlist
from data.scp_item import scp_items
from data.url import *
guild = 1069174895893827604
intents=discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(),owner_ids=[759072684461391893,1042790192307781642,842224641871577088])
status = cycle(["scpsl database rework bot", "made bt hanbin#0939", "SCP : Secreat Laboratory"])

@bot.event
async def on_ready():
    print("logined succesfully\n")
    print(f"{len(bot.guilds)} server joined\n")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="public beta"))
    change_status.start()

@tasks.loop(seconds=5)    # n초마다 다음 메시지 출력
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_message(message):
    if "안녕하세요" in message.content:
        await message.channel.send(f"{message.author.mention}안녕하세요 소통해요 :)")

@bot.slash_command()
async def scp_item(ctx):
    await ctx.respond(view=scp_items())
    
@bot.slash_command(name="weponary")
#@commands.has_role("BETA TESTING")
async def ping(ctx):
    await ctx.respond(view=weapon())

@bot.slash_command(name="scp_class")
#@commands.has_role("BETA TESTING")
async def scp_list(ctx):
    await ctx.respond(view=scp_classes())

@bot.slash_command(name="special_weapon")
async def special(ctx):
    await ctx.respond(view=special_weapon())

@scp_list.error
async def error(ctx,error):
    await ctx.respond(error)

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

@bot.slash_command(name="scpsl_ost")
async def scpsl_ost(ctx):
    await ctx.respond(view=SL_music())

@bot.slash_command(name='scpsl-theme',description="choose scpsl ost")
async def scp_item(ctx,
            ost:Option(str,"SCP list",choices=["parabllum","The Final Flash of Existence(oc)","SCPSL_retro","The_wating_game","scp2176","scp1576","scp1853"])):
    if ost == "parabllum":
        await ctx.respond(file=Parabellum)
    if ost == "The Final Flash of Existence(oc)":
        await ctx.respond(file=The_Final_Flash)
    if ost == "SCPSL_retro":
        await ctx.respond(file=SCPSL_retro)
    if ost == "The_wating_game":
        await ctx.respond(file=The_wating_game)

@bot.slash_command()
async def class_human(ctx):
    await ctx.respond("Choose a class!", view=MyView())

@bot.slash_command()
async def youtuber(ctx):
    await ctx.respond(view=SimpleView())

@bot.slash_command()
@commands.is_owner()
async def eas(ctx):
    await ctx.respond("""```ansi\n[2;34m[2;32m[2;33m[2;31m[1;31mEMERGENCY ALERT SYSTEM\n현제 [1;40m디도스[0;31m [0m[1;31m[1;40m[0m[1;31m공격이 감지되었습니다!\n봇이 비활성화 되어있을수 있으니 이점 양자 바랍니다.\n[1;34mserver : bot-hosting.net[0m[1;31m[1;34m[0m[1;31m[0m[2;31m[0m[2;33m[2;31m[0m[2;33m[0m[2;32m[0m[2;34m[0m\n```""")

bot.run(token_beta)