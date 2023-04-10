
import discord
from discord import default_permissions
from discord.ext import commands , tasks
from discord.commands import Option
from config.beta_data import token , attachment
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
    class weapon(discord.ui.View):
        @discord.ui.button(label="com-15", style=discord.ButtonStyle.success)
        async def com_15(self, button, interaction):
            embed = discord.Embed(title="com-15", description="기본적인 호신용권총", color=0xadadad)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/22/COM-15Icon.png/375px-COM-15Icon.png")
            embed.set_image(url='https://hub.scpslgame.com/images/e/e8/COM-15_Inspect_Animation.gif')
            embed.set_footer(text='| 기본대미지=25\n| 해드샷대미지=50')
            await interaction.response.edit_message(embed=embed,view=attachment())

        @discord.ui.button(label="com-18", style=discord.ButtonStyle.success)
        async def com_18(self, button, interaction):
            await interaction.response.edit_message(view=attachment())



    await ctx.respond(view=weapon())
            
@ping.error
async def error(ctx,error):
    await ctx.respond(error)


bot.run(token)