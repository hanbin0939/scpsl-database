
import discord
from discord.ext import commands , tasks
from discord.commands import Option
from config.data import *
from data.weaponary import *
from data.scp import scp_classes
from itertools import cycle
from data.music_file import *
from data.human import MyView
from data.item import itemlist
from data.scp_item import scp_items
from data.url import *
from data.list import *
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
@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.event
async def on_message(message):
    if "안녕하세요" in message.content:
        await message.channel.send(f"{message.author.mention}님 만나서 반가워요! 소통해요 :)")
    if "ㅗㅗ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} shut the f*ck up")
    if "좆" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 누가 욕 하랬냐?!?!?!?")
    if "느금마" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 누가 패드립 하랬냐?!?!?!?")

@bot.slash_command()
async def scp_item(ctx):
    await ctx.respond(view=scp_items())
    
@bot.slash_command(name="weponary")
async def ping(ctx):
    await ctx.respond(view=weapon())

@bot.slash_command(name="scp_class")
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

@bot.slash_command(guild_ids=[879204407496028201],name="scpsl_server_advertistment")
async def ad(ctx):
    await ctx.respond("현제 이기능은 WG 제단에만 지원합니다!",view=Server_Link())

@bot.slash_command()
@commands.is_owner
async def view(ctx):
    await ctx.respond("choose a class!",view=Class_list())

bot.run(token_beta)