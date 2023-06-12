import discord
from discord.ext import commands
from discord.commands import Option
from data_rework.weapon_rework import weapon_view
from data.weaponary import weapon

class weaponary(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @discord.slash_command(name="weaponary_rework")
    async def weapon(self,ctx,
        text: Option(str,"옵션을 소르세요",choices=["button","select"])):
        if text == "select":
            await ctx.respond(view=weapon_view())
        if text == "button":
            await ctx.respond(view=weapon())
            
def setup(bot):
    bot.add_cog(weaponary(bot))
    
