import discord
from discord.ext import commands
from data.url import Server_Link

class Ad(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @discord.slash_command(name="scpsl_서버_광고")
    async def scpsl_ad(self,ctx):
        await ctx.respond(view=Server_Link())

def setup(bot):
    bot.add_cog(Ad(bot))
