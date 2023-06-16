import discord
from discord.ext import commands
from discord.commands import Option
from data_rework.scp_rework import SCP_select
from data.scp import scp_classes

class SCP(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @discord.slash_command(name="scp_view")
    async def scp_view(self,ctx,
        text: Option(str,"옵션을 소르세요",choices=["button","select"])):
        if text == "select":
            await ctx.respond(view=SCP_select())
        if text == "button":
            await ctx.respond(view=scp_classes())
            
def setup(bot):
    bot.add_cog(SCP(bot))
    
