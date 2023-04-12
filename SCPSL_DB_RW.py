
import discord
from discord import default_permissions
from discord.ext import commands , tasks
from discord.commands import Option
from config.data import token_beta
from data.beta_data import weapon
from data.scp_data import scp_classes
from itertools import cycle
guild = 1069174895893827604
intents=discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='R!', intents=discord.Intents.all(),owner_ids=[759072684461391893,1042790192307781642,842224641871577088])
#status = cycle(["scpsl database rework bot", "made bt hanbin#0939", "SCP : Secreat Laboratory"])

@bot.event
async def on_ready():
    print("logined succesfully\n")
    print(f"{len(bot.guilds)} server joined\n")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="private beta..."))
    #change_status.start()

#@tasks.loop(seconds=5)    # n초마다 다음 메시지 출력
#async def change_status():
#    await bot.change_presence(activity=discord.Game(next(status)))

@bot.slash_command(name="weponary")
@commands.has_role("BETA TESTING")
async def ping(ctx):
    await ctx.respond(view=weapon())

@bot.slash_command(name='scp-item',description="this commands is public!")
async def candy(ctx,
            item:Option(str,"SCP list",choices=["scp500","scp207","scp244","scp268","scp2176","scp1576","scp1853"])):
    if item == "scp500":
        embed = discord.Embed(title='SCP500',url="https://en.scpslgame.com/index.php?title=SCP-500",description='만병통치약')
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/a/ac/SCP500Icon.png/180px-SCP500Icon.png')
        embed.set_image(url='https://hub.scpslgame.com/images/7/78/500_Use.gif')
        embed.add_field(name='option 1',value='~사용자를 완전히 치유됩니다.',inline=False)
        embed.add_field(name='option 2',value='~10초동안 사용자는 최대 200hp 를 회복합니다.',inline=False)
        await ctx.respond(embed=embed)
    if item == "scp207":
        embed = discord.Embed(title="SCP207",url="https://en.scpslgame.com/index.php?title=SCP-207",color=0xff0000)
        embed.set_author(name='SCPitem',icon_url='https://hub.scpslgame.com/images/thumb/8/8b/CATEFFECT.png/61px-CATEFFECT.png')
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/d/dd/UpdatedSCP207Icon.png/300px-UpdatedSCP207Icon.png')
        embed.set_image(url='https://hub.scpslgame.com/images/4/45/207_Use_New.gif')
        embed.add_field(name='LV1',value='>>>207 X1 : 6.48m/sec ,-1HP.s',inline=False)
        embed.add_field(name='LV2',value='>>>207 X2 : 7.45m/sec , -1.5hp.s',inline=True)
        embed.add_field(name='LV3',value='>>>207 X3 : 8.1m/sec ,-2.5HP.s',inline=False)
        embed.add_field(name='LV4',value='>>>207 X4 : 8.42m/sec -4HP.s',inline=True)
        embed.set_footer(icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png')
        await ctx.respond(embed=embed)
    if item == "scp244":
        embed = discord.Embed(title='SCP244',url="https://en.scpslgame.com/index.php?title=SCP-244",description='An ancient vase, freezing to the touch.\nCreates a large cloud of icy fog when placed',color=0x85c2de)
        embed.set_author(name='SCP ITEM',icon_url="https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png")
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/3/30/SCP244BIcon.png/300px-SCP244BIcon.png')
        embed.set_image(url='https://hub.scpslgame.com/images/7/7e/244B_Equip_Animation.gif')
        embed.set_footer(text='SCP item',icon_url='https://hub.scpslgame.com/images/thumb/3/32/SCP244AIcon.png/300px-SCP244AIcon.png')
        embed.add_field(name="SCP-049-2",value='''**공격속도 쿨다운 + 2** & 공격속도 감소 & 스팩 감소''',inline=True)
        embed.add_field(name="SCP-096",value='''얼굴 못봄 & **공격속도 감소**''',inline=True)
        embed.add_field(name="SCP-106",value="""공격 쿨다온 속도 증가""",inline=True)
        await ctx.respond(embed=embed)

    if item == "scp268":
        embed = discord.Embed(title="SCP-268",color=0xFFD500)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/e8/UpdatedSCP268Icon.png/375px-UpdatedSCP268Icon.png")
        embed.set_footer(text="상호작용이 없을경우 최대 15초동안 투명상태를 유지할수 있습니다!")
        await ctx.respond(embed=embed)

    if item == "scp2176":
        embed = discord.Embed(title="SCP2176",description="ghost light",color=0x008000)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/5/52/Updated2176Icon.png")
        embed.add_field(name="기능1.",value="SCP079의 전력을 0으로 만들고 몇초간 전력을 무력화합니다.")
        embed.add_field(name="기능2.",value="해당 방은 일시적으로 문을 럭다운및 정전됩니다.")
        await ctx.respond(embed=embed)

    if item == "scp1576":
        embed = discord.Embed(title="SCP1576",description="마법의 소라고동",url="https://en.scpslgame.com/index.php?title=SCP-1576")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/24/SCP1576Icon.png/200px-SCP1576Icon.png")
        embed.set_footer(text="이 아이탬을 사용시 30초간 죽은 사람과 대화를 할수 있습니다.")
        embed.set_footer(text="회득 방법 : SCP item locker")
        await ctx.respond(embed=embed)

    if item == "scp1853":
        embed = discord.Embed(title="scp1853",url="https://en.scpslgame.com/index.php?title=SCP-1853",color=0x2e8d36)
        embed.set_author(name='Prometheus Labs Inc',icon_url="https://hub.scpslgame.com/images/f/ff/PromLabsLogo.png")
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/d/d8/SCP1853Icon.png/300px-SCP1853Icon.png')
        embed.set_image(url='https://hub.scpslgame.com/images/8/88/1853_Use_Animation.gif')
        embed.set_footer(text='상호작용 속도 +60%.\n조준속도 +30%\n[25%] 반동감소\n[25%] 재장전 시간\nEntering/Exiting ADS is faster by 20%.\n20% reducation in draw & usage time for certain items')
        await ctx.respond(embed=embed)
        
@bot.slash_command(name="scp_class")
@commands.has_role("BETA TESTING")
async def scp_list(ctx):
    await ctx.respond(view=scp_classes())

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


bot.run(token_beta)