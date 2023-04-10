
import discord
from discord import default_permissions
from discord.ext import commands , tasks
from discord.commands import Option
from config.beta_data import token
from itertools import cycle
guild = 1069174895893827604
intents=discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='R!', intents=discord.Intents.all())
status = cycle(["SCPSL information bot", "made bt hanbin#0939", "SCP : Secreat Laboratory"])

@bot.event
async def on_ready():
    print("logined succesfully\n")
    print(f"{len(bot.guilds)} server joined\n") 
    change_status.start()

@tasks.loop(seconds=5)    # n초마다 다음 메시지 출력
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
@bot.slash_command(name="weponary",guild_ids=[guild])
async def ping(ctx):
    class weapon(discord.ui.View):
        @discord.ui.button(label="com-15", style=discord.ButtonStyle.success)
        async def com_15(self, button, interaction):
            embed = discord.Embed(title="com-15")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/22/COM-15Icon.png/375px-COM-15Icon.png")
            embed.set_image(url='https://hub.scpslgame.com/images/e/e8/COM-15_Inspect_Animation.gif')
            embed.set_footer(text='| 기본대미지=25\n| 해드샷대미지=50')
            class attachment(discord.ui.View):
                @discord.ui.button(label='소음기', style=discord.ButtonStyle.gray)
                async def sp(self, button: discord.ui.Button, interaction: discord.Interaction):
                    embed = discord.Embed(title="Suppressor",description=str('''총알 정확도:+25%\n총소리:-60%\n준비시간:+0.17/s\n길이:+94\n무게:+46%'''))
                    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/c/cd/COM-15Suppressor.png/180px-COM-15Suppressor.png')
                    await interaction.response.edit_message(embed=embed)
                @discord.ui.button(label='17발 탄창', style=discord.ButtonStyle.gray)
                async def big_mag(self, button: discord.ui.Button, interaction: discord.Interaction):
                    embed = discord.Embed(title='Extended MAG',description='''ammo + 5\n준비시간:+0.06/s\n무게:+46%''')
                    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/5/54/COM-15ExtendedMag.png/90px-COM-15ExtendedMag.png')
                    await interaction.response.edit_message(embed=embed)
                @discord.ui.button(label='go back', style=discord.ButtonStyle.gray)
                async def go_back(self, button: discord.ui.Button, interaction: discord.Interaction):
                    embed = discord.Embed(title="COM-15", description="기본적인 호신용권총", color=0xadadad)
                    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/22/COM-15Icon.png/375px-COM-15Icon.png')
                    embed.set_image(url='https://hub.scpslgame.com/images/e/e8/COM-15_Inspect_Animation.gif')
                    embed.set_author(name='weapon')
                    embed.set_footer(text='| 기본대미지=25\n| 해드샷대미지=50',icon_url='https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png')
                    await interaction.response.edit_message(embed=embed,view=attachment())
                @discord.ui.button(label='go home', style=discord.ButtonStyle.gray)
                async def go_home(self, button: discord.ui.Button, interaction: discord.Interaction):
                    await interaction.response.edit_message(embed=embed,view=weapon())


            await interaction.response.edit_message(embed=embed,view=attachment())


    await ctx.respond(view=weapon())
            



bot.run(token)